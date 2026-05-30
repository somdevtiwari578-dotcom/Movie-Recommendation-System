# Movie Recommendation System

## 📌 Summary
The Movie Recommendation System is a machine learning-based application designed to suggest movies to users based on their interests, preferences, and viewing patterns.  
It combines **content-based filtering** and **collaborative filtering** into a **hybrid recommendation model**, deployed with an interactive **Streamlit UI**.

---

## 🎯 Problem Statement
With thousands of movies available across streaming platforms, users often find it difficult to discover content that matches their interests.  
Traditional browsing methods are time-consuming and may not provide personalized suggestions, leading to poor user experience and content discovery challenges.

---

## 🎯 Objective
- Develop a Movie Recommendation System using machine learning techniques.  
- Recommend relevant movies to users based on similarity analysis and recommendation algorithms.  
- Include dataset preprocessing, movie search functionality, recommendation generation, and result display through a user-friendly interface.  
- Support advanced functionalities such as collaborative filtering, user rating systems, and web-based deployment for real-world usability.  

---

## ⚙️ Features
- **Content-Based Filtering** → Suggests movies based on genre similarity.  
- **Collaborative Filtering** → Suggests movies based on user rating patterns.  
- **Hybrid Model** → Combines both approaches for better accuracy.  
- **Interactive UI** → Built with Streamlit for easy movie search and recommendations.  
- **Fallback Handling** → Works even if external APIs (TMDb) are unavailable.  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Streamlit, Requests  
- **Dataset:** MovieLens (movies.csv, ratings.csv)  
- **Deployment:** Streamlit Cloud / Localhost  

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
Install dependencies:

bash
pip install -r requirements.txt
Run the app:

bash
streamlit run app.py
Open in browser:
👉 http://localhost:8501 (localhost in Bing)

📸 Screenshots
<img width="1118" height="930" alt="Screenshot 2026-05-30 095708" src="https://github.com/user-attachments/assets/9e9070ce-6ab3-4c4d-b6f3-bf7e4afc1b1b" />



🔮 Future Enhancements
Advanced collaborative filtering (SVD/Surprise/LightFM).

User rating input system.

Deployment with live demo link.

Poster caching/local dataset integration.

👨‍💻 Author
Somdev Tiwari  
MCA Student | Frontend Development Intern | Aspiring Software Engineer
