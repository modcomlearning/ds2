from flask import Flask, render_template, request, redirect
import pandas as pd
import sklearn


app =  Flask(__name__)

# routing
@app.route("/home")
def home():
    return render_template('home.html')

import pandas
import sklearn
@app.route("/recommender", methods = ['POST','GET'])
def recommender():
    if request.method =='POST':
        clean_review1 = pd.read_csv('Hotel_Reviews.csv')
        clean_review1 = clean_review1.groupby('Hotel_Name').agg({
            'Negative_Review': ', '.join, 'Positive_Review': ', '.join}).reset_index()

        print(clean_review1)

        # extracting new columne review_text by merging postitive and negative review column
        clean_review1['review_text'] = clean_review1['Positive_Review'].astype(str) + clean_review1[
            'Negative_Review'].astype(str)
        # findout similarity between the reviews of hotel using TF-IDF
        from sklearn.feature_extraction.text import TfidfVectorizer

        # Define a TF-IDF Vectorizer Object. Remove all english stop words such as 'the', 'a'
        tfidf = TfidfVectorizer(stop_words='english')

        # Replace NaN with an empty string
        clean_review1['review_text'] = clean_review1['review_text'].fillna('')

        # Construct the required TF-IDF matrix by fitting and transforming the data
        tfidf_matrix = tfidf.fit_transform(clean_review1['review_text'])


        # You see that over 80,000 different words were used to describe the 1492 hotels in dataset.
        # used linear_kernal method for calculating similarity between the hotels.
        from sklearn.metrics.pairwise import linear_kernel
        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

        # Construct a reverse map of indices and hotel names
        indices = pd.Series(clean_review1.index, index=clean_review1['Hotel_Name']).drop_duplicates()

        # Function that takes in hotel name as input and outputs most similar hotels
        def get_recommendations(title, cosine_sim=cosine_sim):
            # Get the index of the hotel that matches the hotel_name
            idx = indices[title]

            # Get the pairwsie similarity scores of all hotels with that hotel
            sim_scores = list(enumerate(cosine_sim[idx]))

            # Sort the hotels based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the 10 most similar hotels
            sim_scores = sim_scores[1:11]

            # Get the hotel indices
            hotel_indices = [i[0] for i in sim_scores]

            # Return the top 10 most similar hotel
            return clean_review1['Hotel_Name'].iloc[hotel_indices]

        # user input hotel name 11 cadogan garden and get top 10 similar hotel based on user review
        hotel_name = request.form['search']
        x = get_recommendations(hotel_name)
        print(x)

        return render_template('recommender.html', msg = x.tolist())
    else:
        return render_template('recommender.html')


import pymysql
# Application Layer - Logic
from flask import request
@app.route("/register", methods=['POST','GET'])
def blog():
   # Logic goes here
   # handle form data
   if request.method=='POST':  # check if user posted something
       firstname = request.form['firstname']
       secondname = request.form['secondname']
       password = request.form['password']
       password1 = request.form['password1']

       # validate fields
       if firstname=="":
           #flash("Email is Empty!")
           return render_template('regiter.html', msg1="Firstname is Empty!")

       elif secondname =="":
            #flash("Name is Empty!")
            return render_template('register.html', msg2="Second Name is Empty!")

       elif password=="":
           #flash("Message is Empty!")
           return render_template('register.html', msg3="Password is Empty!")

       elif len(password) < 8:
           #flash("Message too Short")
           return render_template('register.html', msg4="Password too short")

       elif password != password1:
           # flash("Message too Short")
           return render_template('register.html', msg4="Password do not match")

       else:
           con = pymysql.connect("localhost","root","","hotel_recommenderdb")
           cursor = con.cursor()
           sql  = "INSERT INTO `users`(`firstname`,`secondname`,`password`)VALUES(%s,%s,%s)"
           # %s protect from SQL injection
           try:
              cursor.execute(sql,(firstname,secondname,password))
              con.commit() # commit changes to db
              return render_template('register.html', msg="Uploaded!")
           except:
               con.rollback()
               return render_template('register.html', msg="Failed!")

   else:
       return render_template('register.html')
       # END




# Login  Route
@app.route('/', methods=['POST','GET'])
def login():
    if request.method =='POST':
        firstname = request.form['firstname']
        password = request.form['password']

        # validate fields
        if firstname == "":
            # flash("Email is Empty!")
            return render_template('login.html', msg1="Firstname is Empty!")

        elif password == "":
            # flash("Message is Empty!")
            return render_template('login.html', msg3="Password is Empty!")

        else:
            # connect to db
            con = pymysql.connect("localhost", "root", "", "hotel_recommenderdb")
            cursor = con.cursor()
            sql = "SELECT * FROM users WHERE firstname = %s AND password= %s"
            # execute SQL using the cursor
            cursor.execute(sql,(firstname,password))
            # check if a match was found/or not
            if cursor.rowcount==0:  # no user found
                return render_template('login.html', msg = "No Match. Wrong Input")
            elif cursor.rowcount==1: # 1 user found
               # create a session for the logged in
                return redirect('/home')
            elif cursor.rowcount > 1:  # more than 1 user found
                return render_template('login.html', msg="Try Again Later. Contact Admin")
            else:
                return render_template('login.html', msg="Contact Admin")
    else:  # shows login page,, after the route is visited
        return render_template('login.html')


@app.route("/about")
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run()






