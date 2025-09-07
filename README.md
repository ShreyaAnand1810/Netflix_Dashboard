# 🎬 Netflix Shows & Movies Analytics Dashboard

An interactive **Streamlit dashboard** for exploring and analyzing Netflix titles (Movies + TV Shows).  
Users can filter by year, type, country, genre, and search by title — with **dynamic visualizations** and links that redirect directly to Netflix.

---
## 🔎 Problem Statement:
“The project aims to analyze Netflix titles dataset to explore trends in content production across time, countries, and genres, providing users with an interactive dashboard for insights.”

### 🎯 Objectives:

- Understand how Netflix’s content has evolved over years.
- Compare distribution of Movies vs TV Shows.
- Identify popular genres and producing countries.
- Provide interactive exploration tools for deeper insights.

---

## 🚀 Live Demo
👉 [Open the App](https://netflixdashboard-qwjbcktrn9a4gc8eddeaqs.streamlit.app/)

---

## 📊 Features

### 🔍 Interactive Filters
- Year range slider  
- Movie vs TV Show toggle  
- Multi-select for countries and genres  
- Title search box  

### 📈 Dynamic Visualizations
- Releases per year (line chart)  
- Content type distribution (pie chart)  
- Top countries producing Netflix content (bar chart)  
- Heatmap of top genres across years  

### 📑 Filtered Table
- Shows title, type, year, country, genre, description  
- Direct link to **Netflix search page** for each title  

---

## 🛠️ Tech Stack
- [Python 3.x](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – interactive dashboard  
- [Pandas](https://pandas.pydata.org/) – data handling  
- [Plotly](https://plotly.com/python/) – interactive charts  

---

## 📂 Project Structure
 - ├── data/ # Folder containing dataset
 - ├── data.py # Data loading & preprocessing
 - ├── app.py # Streamlit app (UI & dashboard)
 - ├── requirements.txt # Dependencies
 - └── README.md # Project documentation

---

## 📦 Installation & Local Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/netflix-dashboard.git
   cd netflix-dashboard

2. **Create virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   source venv/bin/activate   # On Mac/Linux

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Run the app**
   ```bash
   streamlit run app.py

5.**Open the link from the terminal** (default: http://localhost:8501)

---

## 📊 Dataset

- Dataset name: Netflix Movies and TV Shows Dataset
- Source: Kaggle (https://www.kaggle.com/shivamb/netflix-shows)
- Size: “~8,800 rows × 12 columns.”
- It contains:
  - Title, type (Movie/TV Show), director, cast
  - Country, release year, rating, duration
  - Listed genres, description, and date added to Netflix

### 🧹 Data Cleaning & Preparation
- Handled missing values in 'country', 'director', and 'cast'.
- Converted 'date_added' to datetime format.
- Extracted 'year' column for temporal analysis.
- Removed duplicate rows.

### 🔎 Data Exploration & Summary
- Total Titles: 8,807
- Movies: 6,132 (≈70%), TV Shows: 2,675 (≈30%)
- Top Producing Countries: United States, India, United Kingdom
- Popular Genres: Dramas, Comedies, Documentaries
  
---
## 💡 Key Insights
- Netflix’s content library expanded rapidly after 2015, coinciding with global expansion.
- Movies dominate (~70%), but TV Shows have steadily increased in recent years.
- U.S. leads in content production, but India and the U.K. are strong contributors.
- Genres like Dramas and Comedies dominate, reflecting audience preferences.

---

## ✨ Future Improvements

- Recommendation system for similar titles
- Advanced search (multi-genre, multi-country matching)
- Deploy on multiple platforms (Render, Railway, AWS)
- User authentication (e.g., Streamlit Authenticator)

## 🤝 Contributing

Contributions are welcome!
- Fork the repo
- Create a new branch (feature-new-idea)
- Commit changes & push
- Open a Pull Request


