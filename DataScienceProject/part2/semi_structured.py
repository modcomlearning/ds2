
# Semi Structured is data that has some tags, ids,  keys to identify
# Ex. JSON/XML
# Needs a bit of processing to make it structured.
import pandas
dataframe = pandas.read_json("https://jsonplaceholder.typicode.com/posts")
print(dataframe)

# XML Reader.
# https://www.geeksforgeeks.org/xml-parsing-python/






