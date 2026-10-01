# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib

# # Load model & scaler
# model = joblib.load("flood_model.pkl")
# scaler = joblib.load("scaler.pkl")

# st.set_page_config(page_title="Flood Prediction", page_icon="🌊")

# st.title("🌊 Flood Prediction System")
# st.write("Enter all environmental details to predict flood risk")

# # ---------------- INPUT FIELDS ---------------- #

# Station_Names = st.text_input("Station Name")
# Year = st.number_input("Year", value=2023)
# Month = st.number_input("Month", min_value=1, max_value=12, value=7)

# Max_Temp = st.number_input("Max Temperature")
# Min_Temp = st.number_input("Min Temperature")
# Rainfall = st.number_input("Rainfall")
# Relative_Humidity = st.number_input("Relative Humidity")
# Wind_Speed = st.number_input("Wind Speed")
# Cloud_Coverage = st.number_input("Cloud Coverage")
# Bright_Sunshine = st.number_input("Bright Sunshine")

# Station_Number = st.number_input("Station Number")
# X_COR = st.number_input("X Coordinate")
# Y_COR = st.number_input("Y Coordinate")
# LATITUDE = st.number_input("Latitude")
# LONGITUDE = st.number_input("Longitude")
# ALT = st.number_input("Altitude")

# Period = st.text_input("Period (e.g., 2023.07)")

# # ---------------- PREDICTION ---------------- #

# if st.button("Predict Flood"):

#     # Create dataframe
#     input_data = pd.DataFrame([{
#         'Station_Names': Station_Names,
#         'Year': Year,
#         'Month': Month,
#         'Max_Temp': Max_Temp,
#         'Min_Temp': Min_Temp,
#         'Rainfall': Rainfall,
#         'Relative_Humidity': Relative_Humidity,
#         'Wind_Speed': Wind_Speed,
#         'Cloud_Coverage': Cloud_Coverage,
#         'Bright_Sunshine': Bright_Sunshine,
#         'Station_Number': Station_Number,
#         'X_COR': X_COR,
#         'Y_COR': Y_COR,
#         'LATITUDE': LATITUDE,
#         'LONGITUDE': LONGITUDE,
#         'ALT': ALT,
#         'Period': Period
#     }])

#     # Encode categorical columns SAME AS TRAINING
#     cat_cols = ['Station_Names', 'Period']
#     for col in cat_cols:
#         input_data[col] = pd.Categorical(input_data[col]).codes

#     # Ensure same column order
#     model_features = model.feature_names_in_
#     input_data = input_data[model_features]

#     # Scale input
#     input_scaled = scaler.transform(input_data)

#     # Predict
#     prediction = model.predict(input_scaled)
#     probability = model.predict_proba(input_scaled)[0][1]

#     # Output
#     st.subheader("Result")

#     if prediction[0] == 1:
#         st.error(f"🚨 Flood Likely\nProbability: {probability:.2%}")
#     else:
#         st.success(f"✅ No Flood\nProbability: {probability:.2%}")





# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Load model
# model = joblib.load("flood_model.pkl")
# scaler = joblib.load("scaler.pkl")
# encoders = joblib.load("encoders.pkl")

# st.title("🌊 Flood Prediction System")

# # Inputs
# Station_Names = st.text_input("Station Name", "Barisal")
# Year = st.number_input("Year", value=2023)
# Month = st.number_input("Month", 1, 12, 7)

# Max_Temp = st.number_input("Max Temperature", value=33.5)
# Min_Temp = st.number_input("Min Temperature", value=25.1)
# Rainfall = st.number_input("Rainfall", value=5.0)
# Relative_Humidity = st.number_input("Humidity", value=85.0)
# Wind_Speed = st.number_input("Wind Speed", value=1.2)
# Cloud_Coverage = st.number_input("Cloud Coverage", value=1.8)
# Bright_Sunshine = st.number_input("Sunshine", value=4.5)

# Station_Number = st.number_input("Station Number", value=41950)
# X_COR = st.number_input("X Coordinate", value=536809)
# Y_COR = st.number_input("Y Coordinate", value=510151)
# LATITUDE = st.number_input("Latitude", value=22.0)
# LONGITUDE = st.number_input("Longitude", value=90.0)
# ALT = st.number_input("Altitude", value=4.0)

# Period = st.text_input("Period", "2023.07")

# # Predict
# if st.button("Predict Flood"):

#     input_data = pd.DataFrame([{
#         'Station_Names': Station_Names,
#         'Year': Year,
#         'Month': Month,
#         'Max_Temp': Max_Temp,
#         'Min_Temp': Min_Temp,
#         'Rainfall': Rainfall,
#         'Relative_Humidity': Relative_Humidity,
#         'Wind_Speed': Wind_Speed,
#         'Cloud_Coverage': Cloud_Coverage,
#         'Bright_Sunshine': Bright_Sunshine,
#         'Station_Number': Station_Number,
#         'X_COR': X_COR,
#         'Y_COR': Y_COR,
#         'LATITUDE': LATITUDE,
#         'LONGITUDE': LONGITUDE,
#         'ALT': ALT,
#         'Period': Period
#     }])

#     # Encode
#     for col in encoders:
#         input_data[col] = encoders[col].transform(input_data[col])

#     # Match order
#     input_data = input_data[model.feature_names_in_]

#     # Scale
#     input_scaled = scaler.transform(input_data)

#     # Predict
#     prediction = model.predict(input_scaled)
#     probability = model.predict_proba(input_scaled)[0][1]

#     # Output
#     if prediction[0] == 1:
#         st.error(f"🚨 Flood Likely (Probability: {probability:.2%})")
#     else:
#         st.success(f"✅ No Flood (Probability: {probability:.2%})")
        
        
        
# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Load files
# model = joblib.load("flood_model.pkl")
# scaler = joblib.load("scaler.pkl")
# encoders = joblib.load("encoders.pkl")

# st.title("🌊 Flood Prediction System")

# # Inputs
# Station_Names = st.text_input("Station Name", "Barisal")
# Year = st.number_input("Year", value=2023)
# Month = st.number_input("Month", 1, 12, 7)

# Max_Temp = st.number_input("Max Temperature", value=33.5)
# Min_Temp = st.number_input("Min Temperature", value=25.1)
# Rainfall = st.number_input("Rainfall", value=5.0)
# Relative_Humidity = st.number_input("Humidity", value=85.0)
# Wind_Speed = st.number_input("Wind Speed", value=1.2)
# Cloud_Coverage = st.number_input("Cloud Coverage", value=1.8)
# Bright_Sunshine = st.number_input("Sunshine", value=4.5)

# Station_Number = st.number_input("Station Number", value=41950)
# X_COR = st.number_input("X Coordinate", value=536809)
# Y_COR = st.number_input("Y Coordinate", value=510151)
# LATITUDE = st.number_input("Latitude", value=22.0)
# LONGITUDE = st.number_input("Longitude", value=90.0)
# ALT = st.number_input("Altitude", value=4.0)

# Period = st.text_input("Period", "2023.07")

# if st.button("Predict Flood"):

#     input_data = pd.DataFrame([{
#         'Station_Names': Station_Names,
#         'Year': Year,
#         'Month': Month,
#         'Max_Temp': Max_Temp,
#         'Min_Temp': Min_Temp,
#         'Rainfall': Rainfall,
#         'Relative_Humidity': Relative_Humidity,
#         'Wind_Speed': Wind_Speed,
#         'Cloud_Coverage': Cloud_Coverage,
#         'Bright_Sunshine': Bright_Sunshine,
#         'Station_Number': Station_Number,
#         'X_COR': X_COR,
#         'Y_COR': Y_COR,
#         'LATITUDE': LATITUDE,
#         'LONGITUDE': LONGITUDE,
#         'ALT': ALT,
#         'Period': Period
#     }])

#     # Safe encoding
#     for col in encoders:
#         try:
#             input_data[col] = encoders[col].transform(input_data[col])
#         except:
#             input_data[col] = 0

#     # Match columns safely
#     for col in model.feature_names_in_:
#         if col not in input_data:
#             input_data[col] = 0

#     input_data = input_data[model.feature_names_in_]

#     # Scale
#     input_scaled = scaler.transform(input_data)

#     # Predict
#     prediction = model.predict(input_scaled)
#     probability = model.predict_proba(input_scaled)[0][1]

#     if prediction[0] == 1:
#         st.error(f"🚨 Flood Likely (Probability: {probability:.2%})")
#     else:
#         st.success(f"✅ No Flood (Probability: {probability:.2%})")




# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib

# # Load files
# model = joblib.load("flood_model.pkl")
# scaler = joblib.load("scaler.pkl")
# encoders = joblib.load("encoders.pkl")
# feature_names = joblib.load("features.pkl")  # ✅ NEW

# st.title("🌊 Flood Prediction System")

# # Inputs
# Station_Names = st.text_input("Station Name", "Barisal")
# Year = st.number_input("Year", value=2023)
# Month = st.number_input("Month", 1, 12, 7)

# Max_Temp = st.number_input("Max Temperature", value=33.5)
# Min_Temp = st.number_input("Min Temperature", value=25.1)
# Rainfall = st.number_input("Rainfall", value=5.0)
# Relative_Humidity = st.number_input("Humidity", value=85.0)
# Wind_Speed = st.number_input("Wind Speed", value=1.2)
# Cloud_Coverage = st.number_input("Cloud Coverage", value=1.8)
# Bright_Sunshine = st.number_input("Sunshine", value=4.5)

# Station_Number = st.number_input("Station Number", value=41950)
# X_COR = st.number_input("X Coordinate", value=536809)
# Y_COR = st.number_input("Y Coordinate", value=510151)
# LATITUDE = st.number_input("Latitude", value=22.0)
# LONGITUDE = st.number_input("Longitude", value=90.0)
# ALT = st.number_input("Altitude", value=4.0)

# Period = st.text_input("Period", "2023.07")

# if st.button("Predict Flood"):

#     input_data = pd.DataFrame([{
#         'Station_Names': Station_Names,
#         'Year': Year,
#         'Month': Month,
#         'Max_Temp': Max_Temp,
#         'Min_Temp': Min_Temp,
#         'Rainfall': Rainfall,
#         'Relative_Humidity': Relative_Humidity,
#         'Wind_Speed': Wind_Speed,
#         'Cloud_Coverage': Cloud_Coverage,
#         'Bright_Sunshine': Bright_Sunshine,
#         'Station_Number': Station_Number,
#         'X_COR': X_COR,
#         'Y_COR': Y_COR,
#         'LATITUDE': LATITUDE,
#         'LONGITUDE': LONGITUDE,
#         'ALT': ALT,
#         'Period': Period
#     }])

#     # Encode
#     for col in encoders:
#         try:
#             input_data[col] = encoders[col].transform(input_data[col])
#         except:
#             input_data[col] = 0

#     # ✅ Use saved feature names
#     for col in feature_names:
#         if col not in input_data:
#             input_data[col] = 0

#     input_data = input_data[feature_names]

#     # Scale
#     input_scaled = scaler.transform(input_data)

#     # Predict
#     prediction = model.predict(input_scaled)
#     probability = model.predict_proba(input_scaled)[0][1]

#     if prediction[0] == 1:
#         st.error(f"🚨 Flood Likely (Probability: {probability:.2%})")
#     else:
#         st.success(f"✅ No Flood (Probability: {probability:.2%})")



import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pymongo import MongoClient


model = joblib.load("flood_model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")
feature_names = joblib.load("features.pkl")

client = MongoClient("mongodb://localhost:27017/")
db = client["flood_db"]
collection = db["predictions"]


st.title("🌊 Flood Prediction System")

# Inputs
Station_Names = st.text_input("Station Name", "Barisal")
Year = st.number_input("Year", value=2023)
Month = st.number_input("Month", 1, 12, 7)

Max_Temp = st.number_input("Max Temperature", value=33.5)
Min_Temp = st.number_input("Min Temperature", value=25.1)
Rainfall = st.number_input("Rainfall", value=5.0)
Relative_Humidity = st.number_input("Humidity", value=85.0)
Wind_Speed = st.number_input("Wind Speed", value=1.2)
Cloud_Coverage = st.number_input("Cloud Coverage", value=1.8)
Bright_Sunshine = st.number_input("Sunshine", value=4.5)

Station_Number = st.number_input("Station Number", value=41950)
X_COR = st.number_input("X Coordinate", value=536809)
Y_COR = st.number_input("Y Coordinate", value=510151)
LATITUDE = st.number_input("Latitude", value=22.0)
LONGITUDE = st.number_input("Longitude", value=90.0)
ALT = st.number_input("Altitude", value=4.0)

Period = st.text_input("Period", "2023.07")


if st.button("Predict Flood"):

    input_data = pd.DataFrame([{
        'Station_Names': Station_Names,
        'Year': Year,
        'Month': Month,
        'Max_Temp': Max_Temp,
        'Min_Temp': Min_Temp,
        'Rainfall': Rainfall,
        'Relative_Humidity': Relative_Humidity,
        'Wind_Speed': Wind_Speed,
        'Cloud_Coverage': Cloud_Coverage,
        'Bright_Sunshine': Bright_Sunshine,
        'Station_Number': Station_Number,
        'X_COR': X_COR,
        'Y_COR': Y_COR,
        'LATITUDE': LATITUDE,
        'LONGITUDE': LONGITUDE,
        'ALT': ALT,
        'Period': Period
    }])

    for col in encoders:
        try:
            input_data[col] = encoders[col].transform(input_data[col])
        except:
            input_data[col] = 0


    for col in feature_names:
        if col not in input_data:
            input_data[col] = 0

    input_data = input_data[feature_names]

    input_scaled = scaler.transform(input_data)

  
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

 
    if prediction[0] == 1:
        st.error(f"🚨 Flood Likely (Probability: {probability:.2%})")
    else:
        st.success(f"✅ No Flood (Probability: {probability:.2%})")

  
    data_to_store = {
        "Station_Names": Station_Names,
        "Year": int(Year),
        "Month": int(Month),
        "Rainfall": float(Rainfall),
        "Humidity": float(Relative_Humidity),
        "Prediction": int(prediction[0]),
        "Probability": float(probability)
    }

    collection.insert_one(data_to_store)

    st.info("📦 Prediction saved to MongoDB!")

if st.checkbox("📊 Show Prediction History"):
    data = list(collection.find({}, {"_id": 0}))
    if data:
        st.dataframe(pd.DataFrame(data))
    else:
        st.warning("No data found in database.")