import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import numpy as np

# Load data from Excel file
data_frame = pd.read_excel("DATASET4.xlsx")

# Trained Model for FEVER
def fever_model(temperature):
    X = data_frame[["Temperature"]]
    Y = data_frame[["FEVER"]]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=5)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predict fever based on given parameters
    arr = np.array([float(temperature)])
    newarr = arr.reshape(-1, 1)
    return classifier.predict(newarr)

# Trained Model for STRESS
def stress_model(pulse):
    X = data_frame[["Pulse"]]
    Y = data_frame[["STRESS"]]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=5)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predict stress based on given parameters
    arr = np.array([float(pulse)])
    newarr = arr.reshape(-1, 1)
    return classifier.predict(newarr)

# Trained Model for HYPOXIA
def hypoxia_model(oxygen_saturation):
    X = data_frame[["Oxygen Saturation"]]
    Y = data_frame[["HYPOXIA"]]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=5)

    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predict hypoxia based on given parameters
    arr = np.array([float(oxygen_saturation)])
    newarr = arr.reshape(-1, 1)
    return classifier.predict(newarr)
