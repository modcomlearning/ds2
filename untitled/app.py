import pandas as pd
import sklearn
import flask

clean_review1 = pd.read_csv('Hotel_Reviews.csv')
clean_review1 = clean_review1.groupby('Hotel_Name').agg({
    'Negative_Review': ', '.join, 'Positive_Review': ', '.join}).reset_index()

print(clean_review1)


