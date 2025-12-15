import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from candidate_segmentation import df, scaler, kmeans, pca

st.title("Candidate Segmentation App")
st.write("This app groups candidates using unsupervised learning (KMeans).")


skills = st.slider("Number of Skills", 0, 20, 5)
experience = st.slider("Years of Experience", 0, 10, 1)
projects = st.slider("Number of Projects", 0, 10, 1)
gpa = st.slider("GPA", 0.0, 10.0, 7.0)

user_data = pd.DataFrame([{
    "skills": skills,
    "experience": experience,
    "projects": projects,
    "gpa": gpa
}])


user_scaled = scaler.transform(user_data)


user_cluster = kmeans.predict(user_scaled)[0]

cluster_labels = {
    0: "Low Potential",
    1: "High Potential (Experienced)",
    2: "High Potential (Skill-Focused)"
}

st.subheader("Result")
st.write(f"You belong to: **{cluster_labels[user_cluster]}**")


fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(
    x=df['pca1'],
    y=df['pca2'],
    hue=df['cluster'],
    palette='Set2',
    ax=ax
)

user_pca = pca.transform(user_scaled)
ax.scatter(
    user_pca[:, 0],
    user_pca[:, 1],
    color='black',
    s=200,
    marker='X',
    label='You'
)

ax.set_title("Your Position in Candidate Clusters")
ax.legend()

st.pyplot(fig)
