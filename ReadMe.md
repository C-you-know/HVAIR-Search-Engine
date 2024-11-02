# High Variance Attributed Item Retrival And Search Engine  -- HVAIR Search Engine 🔎👀

The name might seem like a word salad, but it works as named: It parses through items which don't have a definite set of attributes and return relevant searched item. It can efficiently retrieve relevant items depending on the characteristics specified by the user. 

It currently searches through the ```"data-set.json"``` file included in the repository. The dataset contains e-commerce products avaliable on famous e-commerce sites. It includes product name and some other attributes/characteristics the seller has listed. 

Note: It doesn't contain any images.

Libraries used: numpy, pandas, fuzzywuzzy, json, and sys

## Working

This section gives an brief explanation of the design decisions and methods implemented in the code. It also explores possible steps that can be taken to make the program more efficient and quick. 

The goals of the system are:
 - Fast and Efficient Retrival
 - Accurate and Relevant Item Retrival
 - High Specificity of Results
 - A certain degree of spelling errors is accepted
 - Accept multiple types of dataset formats

 ## Dataset

 The dataset has 21176 ecommerce products and these items together have a subset of 3249 attributes. In the dataset, there are 16083 unique items all having different features. The primary key of the dataset is the ```id```. If an item doesn't have a value for an attribute, it is populated with a ```NULL``` value. About 95% of all atrributes for any particular item has ```NULL``` value.    

### Load the dataset

The data is loaded using the ```"pd.read_json()"``` and immediately converted into a pandas dataframe. I have used pandas dataframe because it underscores the high dissimilarity between the attributes of the dataset -- meaning, these items don't share similar attributes.

We copy the dataset into another dataframe and remove all duplicate entries present in it.(There are x duplicates present in the dataset.)

### Preprocessing the data

We calculate the attribute `NumofRelevant`. This attribute stores the number of relevant predictions present in the dataset. Then we sort the dataset with respect to this attribute.

The more official and popular the product it is, the more likely it is to have more documentation. There this automatically acts as a relevance predicting attribute.

We, then, create another attribute called `combined`. This column's funtionality is to combined all the attributes into a single column for effcient and accurate text matching. Only relevant attributes are included into this `combined` column in the form of `{key:value}` pair.

On my machine(Apple MacBook Air M2) it takes about 1 min to perform preprocessing. This code doesn't store the preprocessed results. For very large datasets storing will reduce a lot of time. The attributes ```Data1``` ```Data2``` once computed, need not be computed again until new data is added to the dataset. This new subset of data could be directly appended to the end of file.

### Querying

The input query is first split into its component words. The program checks for the occurance of ```query[0]``` in the ```combined``` attribute of the ```Data2``` dataframe.

Then ```query[1],query[2]...query[n]```, where ```n``` is the number of unique items present in the dataset.

This specific search algorithm was designed to search and retrive items with very specific characteristics. This algorithm focus on more specificity.

The more descriptive the query the more refined the output shall be. But, the word used in the query matters quite a lot. If its spelling is not accruate or the user doesn't know the exact word to describe it, it will hard to search for it.But,for a certain degree of error in the query text, the system will still give satisfactory results to a user. 

if no items are founded, the program effcitively handles the output with an error message.

If it finds somne products, it sorts the products by ```NumofRelevant``` attribute and prints them on the screen.

At the moment, it doesn't store user profiles or learns from user's needs/requests. Adding that may make the results more accrate and curated, but I don't know.

### Display Output


All the items that fit the user's description are printed on the screen. It's a terminal program at the moment, you won't find beatuiful graphics or fonts. The output is printed in the JSON form as present in the ```data-set.json``` file.