# 🎯 Candidate Segmentation using Machine Learning

A **Candidate Segmentation system** built using **unsupervised machine learning (KMeans)** to group candidates based on skills, experience, projects, and GPA.  
The project also includes a **Streamlit web app** for interactive exploration and visualization.

---

## 📌 Project Overview

Recruiters often struggle to quickly understand and group candidates based on multiple attributes.

This project solves that by:
- Segmenting candidates into meaningful clusters
- Visualizing those clusters using **PCA**
- Allowing **real-time interaction** via a Streamlit app

This is a **pure ML + visualization project**, not a CRUD app.

---

## 🧠 Machine Learning Approach

- **Type:** Unsupervised Learning  
- **Algorithm:** KMeans Clustering  
- **Feature Scaling:** StandardScaler  
- **Dimensionality Reduction:** PCA (2D visualization)

### Features Used
- Number of skills  
- Years of experience  
- Number of projects  
- GPA  

---

## 🗂️ Project Structure
Candidate_Segmentation-project/
│
├── app.py
│ └── Streamlit web application
│
├── candidate_segmentation.py
│ └── Data preparation, scaling, KMeans model, PCA visualization
│
├── pycache/
│ └── Compiled Python files (auto-generated)
│
└── README.md
---

## ⚙️ What This Project Does

### 1️⃣ Data Preparation
- Generates or loads candidate feature data
- Cleans and structures it using Pandas

### 2️⃣ Feature Scaling
- Uses `StandardScaler` to normalize features
- Ensures fair clustering across attributes

### 3️⃣ Clustering
- Applies **KMeans** to segment candidates
- Identifies cluster centroids

### 4️⃣ Visualization
- Reduces dimensions using **PCA**
- Visualizes clusters and centroids using Matplotlib & Seaborn

### 5️⃣ Web App (Streamlit)
- Interactive sliders for:
  - Skills
  - Experience
  - Projects
  - GPA
- Predicts which cluster a candidate belongs to
- Displays cluster visualization dynamically

---

## 🖥️ Streamlit App Features

- Interactive UI using sliders
- Real-time cluster prediction
- PCA-based cluster visualization
- Clear labeling of centroids

To run the app:
```bash
streamlit run app.py

📦 Tech Stack

Python

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn

Streamlit
# Clone repository
git clone https://github.com/your-username/Candidate_Segmentation-project.git

# Navigate into project
cd Candidate_Segmentation-project

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
