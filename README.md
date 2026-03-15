# ❤️ Heart Disease Prediction System

A machine learning-powered web application that predicts the likelihood of heart disease based on patient health parameters. This project combines **data preprocessing, feature scaling, model training, and interactive web deployment** to provide fast and user-friendly predictions.

---

## 📌 Project Overview

The **Heart Disease Prediction System** is designed to help identify whether a person is at risk of heart disease using clinical and lifestyle-related inputs such as age, blood pressure, cholesterol, chest pain type, heart rate, and more.

The project includes:
- **Data preprocessing & feature engineering**
- **Model training and evaluation**
- **Feature scaling**
- **Model serialization**
- **Interactive web interface for predictions**

This project demonstrates the end-to-end workflow of a real-world **machine learning application**, from data analysis to deployment-ready prediction.

---

## 🚀 Features

- Predicts heart disease risk based on user input
- Clean and interactive web-based UI
- Trained ML model with preprocessing pipeline
- Feature scaling using saved scaler
- Easy-to-use prediction interface
- Deployment-ready project structure
- Suitable for portfolio, resume, and ML showcase

---

## 🛠️ Tech Stack

### Programming & Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Pickle / Joblib

### Web Framework
- Flask / Streamlit *(Update based on what you used)*

### Development & Visualization
- Jupyter Notebook
- VS Code
- Matplotlib
- Seaborn

---

## 📂 Project Structure

```bash
Heart-Disease-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── heart_disease_prediction.ipynb
│
├── models/
│   ├── heart_model.pkl      # Download separately from Google Drive
│   └── scaler.pkl           # Optional (if used in your project)
│
├── templates/               # For Flask projects
│   └── index.html
│
├── static/                  # CSS / JS / images
│
└── dataset/
    └── heart.csv            # Optional dataset/sample file


## 🔗 Download Model Files

Due to GitHub's file size limitations, the trained model file (`heart_model.pkl`) is not included directly in this repository.

To run this project successfully after cloning, please download the required model file from the link below and place it inside the `models/` folder.

### 📥 Model Download Link
[Download heart_model.pkl from Google Drive]("https://drive.google.com/file/d/1O4c8uSJeIihejbLu2BEp3QZHSUjYQWW6/view?usp=sharing")

### 📂 After Download
Move the downloaded file to:

```bash
models/heart_model.pkl

 🚀 How to Clone and Run the Project

Follow these steps to set up and run the **Heart Disease Prediction System** on your local machine.

---

 1️⃣ Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/Vivek-4142/Heart-Disease-Prediction.git

2️⃣ Navigate to the Project Folder
cd Heart-Disease-Prediction
3️⃣ (Optional) Create a Virtual Environment

Creating a virtual environment is recommended to keep project dependencies isolated.

python -m venv venv
4️⃣ Activate the Virtual Environment
For Windows:
venv\Scripts\activate
5️⃣ Install Required Dependencies

Install all the necessary Python libraries using:

pip install -r requirements.txt
6️⃣ Download the Trained Model File (Important)

Due to GitHub's file size limitations, the trained model file (heart_model.pkl) is not included directly in this repository.

Please download it from the Google Drive link below:

📥 Download Model File:
Download heart_model.pkl
7️⃣ Create the models Folder

Inside the project directory, create a folder named models if it does not already exist.

mkdir models
8️⃣ Place the Model File in the Correct Path

After downloading, move the file into the models folder so the final path looks like this:

models/heart_model.pkl
9️⃣ Run the Application
If your project uses Flask:
python app.py

Then open your browser and go to:

http://127.0.0.1:5000
If your project uses Streamlit:
streamlit run app.py
