import joblib
import pandas as pd

# Load the trained model
model = joblib.load('trained_model.joblib')

def predict(input_data):
    # Assuming your model expects a DataFrame, convert input_data to DataFrame
    # Adjust the below line according to the format of your 'data.txt'
    data_df = pd.DataFrame(input_data, columns=None)
    
    # Here, add any preprocessing steps that your model requires

    # Making a prediction
    prediction = model.predict(data_df)
    return prediction

