# High Variance Attribute Item Retrival Search Engine  -- HVAIR Search Engine 🔎👀

The name might seem like a word salad, but it works as named: It searches through items which don't have a definite set of attributes. It can efficiently retrieve relevant items depending on the characteristics specified by the user. 

It currently searches through the ```"data-set.json"``` file included in the repository. The dataset contains e-commerce products avaliable on famous e-commerce sites. It includes product name and some attribute/characteristic the seller has listed. 

Note: It doesn't contain any images.

Libraries used: numpy, pandas, fuzzywuzzy, json, and sys

## Working

This section gives an brief explanation of the design decisions and methods used in the code. It also explores possible steps that can be taken to make the program more efficient and fast. 

The goals of the system are:
 - Fast and Efficient Retrival
 - Accurate and Relevant Item Retrival
 - High Specificity of Results
 - A certain degree of spelling errors is accepted

 ## The Dataset

### Load the dataset

The data is loaded using the ```"pd.read_json()"``` and immediately converted into a pandas dataframe. I have used pandas dataframe because it underscores the high dissimilarity between the attributes of the dataset.

We copy the dataset into another dataframe and remove all duplicate entries present in it.(There are x duplicates present in the dataset.)

### Preprocessing the data

We calculate the attribute `NumofRelevant`. This attribute stores the number of relevant predictions present in the dataset. Then we sort the dataset with respect to this attribute.

The more official and popular the product it is, the more likely it is to have more documentation. There this automatically acts as a relevance predicting attribute.

We, then, create another attribute called `Combined`. This column's funtionality is to combined all the attributes into a single column for effcient and accurate text matching. Only relevant attributes are included into this `Combined` column in the form of `{key:value}` pair. Any whitespaces are removed to decrease the memory usage.

### Querying

### Display Output
