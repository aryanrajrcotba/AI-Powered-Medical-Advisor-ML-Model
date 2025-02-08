import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Load dataset
df = pd.read_csv('C:/Users/aryan/OneDrive/Desktop/medical_advisor/disease_symptoms_solutions_dataset.csv', encoding='Windows-1252')


# Train the model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['symptoms'])
y = df['disease']
model = MultinomialNB()
model.fit(X, y)

def predict_disease(symptoms):
    symptoms_vectorized = vectorizer.transform([symptoms])
    prediction = model.predict(symptoms_vectorized)[0]
    solution = df[df['disease'] == prediction]['solution'].values[0]
    return prediction, solution