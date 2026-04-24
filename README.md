# 🚛 Tire Risk Prediction System

## 📌 Overview

This project is an AI-based predictive maintenance system designed to estimate the probability of tire failure in heavy vehicles based on real-time operating conditions.

It helps identify high-risk situations early and enables proactive decision-making to prevent failures, reduce downtime, and improve safety.

---

## ⚙️ Features

* Predicts tire failure risk using Deep Learning
* Supports multiple road types:

  * Surface Roads
  * Dump Roads
  * Inpit Roads
  * Lift Roads
* Real-time prediction through an interactive UI
* Risk categorization:

  * ✅ Low Risk
  * ⚠️ Medium Risk
  * 🚨 High Risk
* Rule-based insights for better decision-making

---

## 🧠 Model Details

* Separate models trained for each road category
* Input features:

  * Tonnage Percentage
  * Speed (km/h)
  * Road Gradient
* Data preprocessing using standard scaling
* Model outputs probability of tire failure

---

## 🖥️ Tech Stack

* Python
* Streamlit
* NumPy
* Scikit-learn
* Joblib
* TensorFlow (if ANN model is used)

---

## 📂 Project Structure

```
tire-risk-predictor/
│
├── app/
│   └── main.py
│
├── model/
│   ├── Surface_Roads/
│   ├── Dump_Roads/
│   ├── Inpit_Roads/
│   └── Lift_Roads/
│
├── notebooks/
|
├── screenshots/
│
├── requirements.txt
├── README.md
├── .gitignore
├── pyproject.toml
└── .python-version
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/your-username/tire-risk-predictor.git
cd tire-risk-predictor
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the application

```
streamlit run app/main.py
```

---

## 📊 Example Output

The system predicts a risk probability and categorizes it into:

* **Low Risk** → Safe operating conditions
* **Medium Risk** → Monitor conditions carefully
* **High Risk** → High chance of tire failure, preventive action recommended

---

## 🌐 Deployment

Live App: (Add your deployed link here after deployment)

---

## 👨‍💻 Author

Ritusman Bhuyan
GitHub: https://github.com/RitusmanBhuyan
