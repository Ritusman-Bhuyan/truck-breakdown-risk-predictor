import streamlit as st
import numpy as np
import joblib
import os

st.set_page_config(page_title="Tire Risk Predictor", page_icon="🚛")

st.title("🚛 Tire Breakdown Risk Predictor")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))   

PROJECT_ROOT = os.path.dirname(BASE_DIR)                 

# Model & Scaler Paths
model_paths = {
    "Surface": os.path.join(PROJECT_ROOT, "model/Surface_Roads/surface_model.pkl"),
    "Dump": os.path.join(PROJECT_ROOT, "model/Dump_Roads/dump_model.pkl"),
    "Inpit": os.path.join(PROJECT_ROOT, "model/Inpit_Roads/inpit_model.pkl"),
    "Lift": os.path.join(PROJECT_ROOT, "model/Lift_Roads/lift_model.pkl")
}

scaler_paths = {
    "Surface": os.path.join(PROJECT_ROOT, "model/Surface_Roads/scaler_surface.pkl"),
    "Dump": os.path.join(PROJECT_ROOT, "model/Dump_Roads/scaler_dump.pkl"),
    "Inpit": os.path.join(PROJECT_ROOT, "model/Inpit_Roads/scaler_inpit.pkl"),
    "Lift": os.path.join(PROJECT_ROOT, "model/Lift_Roads/scaler_lift.pkl")
}

@st.cache_resource
def load_model_and_scaler(model_path, scaler_path):
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler

# Road Selection
road_type = st.selectbox(
    "Select Road Category",
    ["Surface", "Dump", "Inpit", "Lift"]
)

# Load selected model + scaler
model, scaler = load_model_and_scaler(
    model_paths[road_type],
    scaler_paths[road_type]
)

# User Inputs
st.subheader("Enter Operating Conditions")

tonnage = st.slider("Tonnage Percentage", 0.0, 150.0, 50.0)
speed = st.slider("Speed (km/h)", 0.0, 120.0, 40.0)
gradient = st.slider("Road Gradient", -10.0, 10.0, 0.0)

# Model Prediction
if st.button("Predict Risk"):

    with st.spinner("Analyzing risk..."):

        # Prepare input
        input_data = np.array([[tonnage, speed, gradient]])
        input_scaled = scaler.transform(input_data)

        # Prediction (Probability)
        prob = model.predict(input_scaled)[0][0]
        risk_percent = prob * 100

    # Output After Prediction
    st.subheader(f"📊 Risk Probability: {risk_percent:.2f}%")

    # Risk Levels
    if risk_percent < 30:
        st.success("✅ Low Risk: Safe operating conditions")

    elif 30 <= risk_percent < 70:
        st.warning("⚠️ Medium Risk: Monitor conditions carefully")

    else:
        st.error("🚨 High Risk: Potential tire failure likely! Take preventive action")

    # Smart Insights
    st.subheader("🔍 Insights")

    if tonnage > 100:
        st.warning("⚠️ High load detected — may increase tire stress")

    if speed > 80:
        st.warning("⚠️ High speed — increases failure probability")

    if abs(gradient) > 5:
        st.warning("⚠️ Steep gradient — risky condition for tires")