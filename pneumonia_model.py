import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

# Trained Model for PNEUMONIA
def pneumonia_model(temperature, oxygen_saturation):
    X = pd.read_excel("DATASET4.xlsx", usecols=["PNEUMONIA"])
    Y = pd.read_excel("DATASET4.xlsx", usecols=["Temperature", "Oxygen Saturation"])

    X_train, X_test, y_train, y_test = train_test_split(Y, X, test_size=0.3, random_state=5)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)
    # y_pred = classifier.predict(X_test)

    arr = np.array([float(temperature), float(oxygen_saturation)])
    newarr = arr.reshape(-1, 2)
    # print(classifier.predict(newarr))
    return classifier.predict(newarr)

# pneumonia_model(101,0.90)