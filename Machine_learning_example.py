import pandas as pd
df=pd.read_csv('amazon_cells_labelled.txt', names=['review','sentiment'],sep='\t')
# try delimiter later
from sklearn.model_selection import train_test_split

#print(df)
reviews=df['review'].values
sentiments=df['sentiment'].values
reviews_train, reviews_test, sentiment_train, sentiment_test= train_test_split(reviews,sentiments,test_size=0.3,random_state=400)
print(reviews_train)


from sklearn.feature_extraction.text import CountVectorizer
#create a vectorizer object
vectorizer=CountVectorizer()
# build the vocabulary of tokens found in the reviews dataset
vectorizer.fit(reviews)
X_train=vectorizer.transform(reviews_train)
X_test=vectorizer.transform(reviews_test)

from sklearn.linear_model import LogisticRegression
# train Sklearn's LogisticRegression() classfier to predict the sentiment of a review
classifier=LogisticRegression()
# use fit method to train the model accoding to the given training data
classifier.fit(X_train, sentiment_train)

accuracy=classifier.score(X_test,sentiment_test)
print("Accuracy:", accuracy)

new_reviews=['Old Version of python useless', 'Very good effort, but not five stars', 'Clear and concise']
X_new=vectorizer.transform(new_reviews)
print(classifier.predict(X_new))
