import streamlit as st
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# --- IBM Deployment Details ---
API_KEY = "xO377ovKfwiMUm9mEAIlBYePmV0OQ6DNbSgINIBJYLM5"
DEPLOYMENT_URL = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/d55602bf-f4d9-42cb-a82d-87d3d3234909/predictions?version=2021-05-01"

# --- Get access token from IBM ---
def get_token(api_key):
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = f"apikey={api_key}&grant_type=urn:ibm:params:oauth:grant-type:apikey"
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

# --- Make prediction using IBM AutoAI deployment ---
def predict(input_data, token):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "input_data": [ {
            "fields": [
                "STATE_NAME", "DISTRICT_NAME",
                "NO_OF_ROAD_WORK_SANCTIONED", "LENGTH_OF_ROAD_WORK_SANCTIONED",
                "NO_OF_BRIDGES_SANCTIONED", "COST_OF_WORKS_SANCTIONED",
                "NO_OF_ROAD_WORKS_COMPLETED", "LENGTH_OF_ROAD_WORK_COMPLETED",
                "NO_OF_BRIDGES_COMPLETED", "EXPENDITURE_OCCURED",
                "NO_OF_ROAD_WORKS_BALANCE", "LENGTH_OF_ROAD_WORK_BALANCE",
                "NO_OF_BRIDGES_BALANCE", "COLUMN15"
            ],
            "values": [input_data]
        }]
    }

     

    response = requests.post(DEPLOYMENT_URL, headers=headers, json=payload)
    st.text(response.text) 
    return response.json()

# --- Set page background ---
def add_background(url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        .block-container {{
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 10px;
    }}
        </style>
    """, unsafe_allow_html=True)

background_url = "https://get.pxhere.com/photo/tree-road-asphalt-travel-transport-lane-dromedary-infrastructure-india-rajasthan-rural-area-charette-677428.jpg"
add_background(background_url)

# --- Title ---
st.title("🛣️ PMGSY Scheme Classifier (Powered by IBM AutoAI)")
st.markdown("Enter the project details to predict the correct PMGSY scheme category.")


# --- Input fields ---
state = st.text_input("State Name", "Bihar")
district = st.text_input("District Name", "Patna")
f1 = st.number_input("No. of Road Works Sanctioned", min_value=0)
f2 = st.number_input("Length of Road Works Sanctioned (km)", min_value=0.0)
f3 = st.number_input("No. of Bridges Sanctioned", min_value=0)
f4 = st.number_input("Cost of Works Sanctioned (₹)", min_value=0.0)
f5 = st.number_input("No. of Road Works Completed", min_value=0)
f6 = st.number_input("Length of Road Works Completed (km)", min_value=0.0)
f7 = st.number_input("No. of Bridges Completed", min_value=0)
f8 = st.number_input("Expenditure Occurred (₹)", min_value=0.0)
f9 = st.number_input("No. of Road Works Remaining", min_value=0)
f10 = st.number_input("Length of Road Works Remaining (km)", min_value=0.0)
f11 = st.number_input("No. of Bridges Remaining", min_value=0)
f12 = st.number_input("Extra Column (COLUMN15)", min_value=0)

# --- Prediction ---
if st.button("🔍 Predict PMGSY Scheme"):
    input_features = [
        state, district,
        f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12
    ]

    try:
        token = get_token(API_KEY)
        result = predict(input_features, token)

        prediction = result["predictions"][0]["values"][0][0]
        probabilities = result["predictions"][0]["values"][0][1]

        st.success(f"🎯 Predicted Scheme Category: **{prediction}**")

        # --- Pie Chart: Class Probabilities ---
        st.subheader("📊 Class Probabilities")
        prob_labels = [f"Class {i}" for i in range(len(probabilities))]
        fig, ax = plt.subplots()
        ax.pie(probabilities, labels=prob_labels, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

        # --- Plotly Chart: Input Summary ---
        st.subheader("📈 Input Summary Visualization")
        labels = [
            "Road Sanctioned", "Length Sanctioned", "Bridges Sanctioned", "Cost",
            "Road Completed", "Length Completed", "Bridges Completed", "Expenditure",
            "Road Remaining", "Length Remaining", "Bridges Remaining", "Extra Col"
        ]
        values = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12]

        df = pd.DataFrame({"Feature": labels, "Value": values})
        fig2 = px.bar(df, x="Feature", y="Value", text="Value", template="plotly_dark", color="Feature")
        fig2.update_layout(xaxis_tickangle=-45, showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

    except Exception as e:
        st.error("❌ Prediction failed. Please check your input or try again.")
        st.exception(e)
