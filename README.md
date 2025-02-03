# ChurnShield-AI: Customer Churn Prediction App

![Demo](https://via.placeholder.com/800x400.png?text=Streamlit+App+Demo+Video/GIF)  

A machine learning-powered Streamlit application to predict customer churn probability for businesses. Built with TensorFlow, scikit-learn, and Streamlit.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Data Preprocessing](#data-preprocessing)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## 🌟 Overview
Customer churn prediction is critical for businesses to retain clients. This app predicts the likelihood of a customer leaving a service (churning) using a neural network trained on historical data. It provides:
- Real-time churn probability calculation
- Interactive user inputs via sliders, dropdowns, and number fields
- Clear visual output with actionable insights

---

## 🚀 Key Features
- **User-Friendly Interface**: Built with Streamlit for seamless interaction.
- **Real-Time Predictions**: Instant churn probability results.
- **Data Preprocessing**: Automated encoding (one-hot, label) and scaling.
- **Interpretable Output**: Clear "Churn" or "No Churn" classification with confidence percentage.
- **Scalable Architecture**: Modular code for easy updates and integration.

---

## 🔧 Tech Stack
- **ML Framework**: TensorFlow/Keras
- **Preprocessing**: scikit-learn (`OneHotEncoder`, `LabelEncoder`, `StandardScaler`)
- **Web App**: Streamlit
- **Data Handling**: pandas, NumPy
- **Serialization**: pickle

---

## 📥 Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ChurnShield-AI.git
   cd ChurnShield-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure the following files are in the root directory**:
   - `model.h5` (pre-trained TensorFlow model)
   - `one_hot_encoding_geo.pkl`, `label_gender.pkl`, `scaler.pkl` (preprocessing artifacts)

---

## 🖥️ Usage
1. Launch the app:
   ```bash
   streamlit run app.py
   ```

2. Fill in customer details:  
   ![Input Form](https://via.placeholder.com/600x300.png?text=Input+Form+Screenshot)

3. Get instant predictions:  
   - Churn probability percentage
   - Binary classification ("Likely to Churn" or "Not Likely")

---

## 🔍 Data Preprocessing
- **Categorical Features**:
  - `Geography`: One-hot encoded (France, Spain, Germany)
  - `Gender`: Label encoded (Male/Female → 0/1)
- **Numerical Features**: Standardized using `StandardScaler`
- **Input Pipeline**: Combines encoded and scaled features for model input.

---

## 🤖 Model Details
- **Architecture**: Neural network with TensorFlow/Keras.
- **Input Layer**: 12 features (post-preprocessing)
- **Output Layer**: Sigmoid activation for binary classification
- **Threshold**: Customers with >50% probability classified as "Likely to Churn"

---

## 👥 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for details.

---

## 🙏 Acknowledgments
- Dataset inspiration: [Kaggle Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Streamlit community for UI components
- TensorFlow/scikit-learn documentation

---

**⭐ Star this repo if you find it useful!**  
**🐛 Report issues in the [GitHub Issues](https://github.com/yourusername/ChurnShield-AI/issues) section.**

---

*Optimize customer retention strategies with AI-driven insights. Predict churn before it happens!*
