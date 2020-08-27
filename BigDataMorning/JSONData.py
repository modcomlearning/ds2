
import pandas
dataframe = pandas.read_json("https://jsonplaceholder.typicode.com/users")
print(dataframe)

print(dataframe.shape)
print(dataframe['address'])
print(dataframe['address'])
print(dataframe['id'])

df = dataframe['address'].join(dataframe['id'])
print(df)

