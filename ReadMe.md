# High Variance Attribute Item Retrival Search Engine  -- HVAIR Search Engine 🔎👀

The name might seem like a word salad, but it works as named: It searches through items which don't have a definite set of attributes. It can efficiently retrieve relevant items depending on the characteristics specified by the user. 

It currently searches through the ```"data-set.json"``` file included in the repository. The dataset contains e-commerce products avaliable on famous e-commerce sites. It includes product name and some attribute/characteristic the seller has listed. 

Note: It doesn't contain any images.

Libraries used: numpy, pandas, fuzzywuzzy, json, and sys

# Working

This section gives an brief explanation of the design decisions and methods used in the code. It also explores possible steps that can be taken to make the program more efficient and fast. 

The goals of the system are:
 - Fast and Efficient Retrival
 - Accurate and Relevant Item Retrival
 - High Specificity of Results

### Load the dataset

The data is loaded using the ```"pd.read_json()"``` and immediately converted into a pandas dataframe. I have used pandas dataframe because it underscores the high dissimilarity between the attributes of the dataset.

### Preprocessing the data

### Querying

### Display Output
