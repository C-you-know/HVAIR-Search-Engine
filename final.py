import pandas as pd
import numpy as np
from fuzzywuzzy import process # type: ignore
import json, sys

def FormatRow(Row):
    FormattedParts = [f'{Col}:{Row[Col]}' for Col in StringColumns if Row[Col]]
    return ' '.join(FormattedParts)

def FindSimilarStrings(Query, Choices, Ids, Threshold=95):
    Results = process.extract(Query, Choices, limit=3, scorer=process.fuzz.partial_ratio)
    MatchedIds = [Ids[Idx] for Idx, Score in enumerate(Choices) if process.fuzz.partial_ratio(Query, Score) >= Threshold]
    return MatchedIds

def FilterNonEmptyColumns(Row):
    return {Key: Value for Key, Value in Row.items() if pd.notna(Value) and Value != ""}

print("Loading and Initializing Data. Please Wait...\n")

Data1 = pd.DataFrame(pd.read_json("data-set.json"))
Data2 = Data1.drop_duplicates(subset=Data1.columns.difference(['id']), keep='first').copy()
Data1["NumofRelevant"] = 3249 - Data1.isna().sum(axis=1)
Data1.sort_values(by="NumofRelevant", ascending=False)
print("Dataset Loaded. Processing Data. Please wait: 1 Min...\n")

StringColumns = Data2.select_dtypes(include='object').columns
Data2.loc[:, StringColumns] = Data2[StringColumns].fillna('')
Data2.loc[:, 'Combined'] = Data2.apply(lambda Row: FormatRow(Row), axis=1)
Data2.loc[:, 'Combined'] = Data2['Combined'].str.replace(r'\s+', ' ', regex=True).str.strip()



print("Thank you for waiting. Search Ready.\n")

Exit = False

while not Exit:
    Query = input("\nEnter the Product you're looking for: \n")
    if Query == "0":
        print("Bye. Bye.")
        sys.exit(0)

    print("Querying...")
    Texts = Data2['Combined'].tolist()
    MatchedIds = Data2['id'].tolist()  
    Words = Query.split()

    for Word in Words:
        MatchedIds = FindSimilarStrings(Word, Texts, MatchedIds)
        Texts = Data2[Data2["id"].isin(MatchedIds)]["Combined"].tolist()

    

    if len(MatchedIds) == 0:
        print("No Products. Retry with Different Name or Specifications\n")
    else:
        MatchedData = Data1[Data1['id'].isin(MatchedIds)].sort_values(by="NumofRelevant")
        FilteredMatchedData = MatchedData.apply(FilterNonEmptyColumns, axis=1).tolist()
        MatchedJSON = json.dumps(FilteredMatchedData, indent=4)
        print(MatchedJSON)

    print("Enter 0 to Exit.")
