# 🎬 Netflix Shows & Movies Analytics Dashboard

An interactive **Streamlit dashboard** for exploring and analyzing Netflix titles (Movies + TV Shows).  
Users can filter by year, type, country, genre, and search by title — with **dynamic visualizations** and links that redirect directly to Netflix.

---

## 🚀 Live Demo
👉 [Open the App](https://your-username-netflix-dashboard.streamlit.app)

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
├── app.py # Streamlit app (UI & dashboard)
├── data.py # Data loading & preprocessing
├── netflix_titles.csv # Dataset (from Kaggle)
├── 01_EDA.ipynb # Exploratory Data Analysis notebook
├── 02_EDA.ipynb # Additional EDA
├── 02_Preprocessing.ipynb # Preprocessing notebook
├── requirements.txt # Dependencies
└── README.md # Project documentation

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

## 📊 Dataset

The dataset comes from Kaggle - Netflix Movies and TV Shows.
It contains:
-Title, type (Movie/TV Show), director, cast
-Country, release year, rating, duration
-Listed genres, description, and date added to Netflix

## ✨ Future Improvements

-Recommendation system for similar titles
-Advanced search (multi-genre, multi-country matching)
-Deploy on multiple platforms (Render, Railway, AWS)
-User authentication (e.g., Streamlit Authenticator)

## 🤝 Contributing

Contributions are welcome!
1.Fork the repo
2.Create a new branch (feature-new-idea)
3.Commit changes & push
4.Open a Pull Request

## 👩‍💻 Author: Shreya Anand
🔗 LinkedIn
 | GitHub
