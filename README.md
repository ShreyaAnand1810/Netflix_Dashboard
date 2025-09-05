🎬 Netflix Shows & Movies Analytics Dashboard

An interactive Streamlit dashboard for exploring and analyzing Netflix titles (Movies + TV Shows).
Users can filter by year, type, country, genre, and search by title — with dynamic visualizations and links that redirect directly to Netflix.

🚀 Live Demo

👉 Open the App

📊 Features

Interactive Filters

Year range slider

Movie vs TV Show toggle

Multi-select for countries and genres

Title search box

Dynamic Visualizations

Releases per year (line chart)

Content type distribution (pie chart)

Top countries producing Netflix content (bar chart)

Heatmap of top genres across years

Filtered Table

Shows title, type, year, country, genre, description

Direct link to Netflix search page for each title

🛠️ Tech Stack

Python 3.x

Streamlit
 – interactive dashboard

Pandas
 – data handling

Plotly
 – interactive charts

📂 Project Structure
├── app.py              # Streamlit app (UI & dashboard)
├── data.py             # Data loading & preprocessing
├── netflix_titles.csv  # Dataset (from Kaggle)
├── 01_EDA.ipynb        # Exploratory Data Analysis notebook
├── 02_EDA.ipynb        # Additional EDA
├── 02_Preprocessing.ipynb # Preprocessing notebook
├── requirements.txt    # Dependencies
└── README.md           # Project documentation

📦 Installation & Local Run

Clone the repository

git clone https://github.com/your-username/netflix-dashboard.git
cd netflix-dashboard


Create virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py


Open the link from the terminal (default: http://localhost:8501
)

📊 Dataset

The dataset comes from Kaggle - Netflix Movies and TV Shows
.
It contains:

Title, type (Movie/TV Show), director, cast

Country, release year, rating, duration

Listed genres, description, and date added to Netflix

✨ Future Improvements

Recommendation system for similar titles

Advanced search (multi-genre, multi-country matching)

Deploy on multiple platforms (Render, Railway, AWS)

User authentication (e.g., Streamlit Authenticator)

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature-new-idea)

Commit changes & push

Open a Pull Request

📜 License

This project is licensed under the MIT License – free to use and modify.

👩‍💻 Author: Shreya Anand
🔗 LinkedIn
 | GitHub
