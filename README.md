📊 Mutual Fund Analysis & Recommendation Tool

Python • Statistics • Financial Data Science

An end-to-end automated system for large-scale mutual fund data analysis and intelligent fund recommendation using statistical models and risk-adjusted performance metrics.

This project builds a data pipeline, ranking engine, and recommendation system for identifying top-performing mutual funds based on investor risk profiles.

🚀 Key Features

🔄 Automated Data Pipeline

Fetches real-time data for 30,000+ mutual funds

Uses public APIs to build a clean, structured dataset

Handles missing values, data normalization, and filtering

📈 Performance Analytics Engine

Daily NAV return calculations

Risk & volatility modeling using Standard Deviation

Annualized return and risk conversion

Outlier detection and filtering

Efficient frontier style risk-return analysis

🧮 Statistical Ranking System

Fund ranking using:

Z-Scores

Standard Deviation

Risk-adjusted returns

Probability modeling using Normal Distribution (CDF)

🤖 Intelligent Recommendation Engine

Investor-profile based recommendations:

🛡️ Conservative

⚖️ Moderate

🚀 Aggressive

Probability-based success scoring

Risk-filtered fund selection

Growth-fund focused filtering

🧠 Recommendation Logic
Risk-Adjusted Scoring Model

Each fund is scored using:

Z-Score = (Fund Return − Target Return) / Fund Risk


This ensures:

Higher returns ✅

Lower risk ✅

Better risk-return efficiency ✅

👤 Investor Profiles
Profile	Target Return	Risk Level
🛡️ Conservative	8%	Low Risk
⚖️ Moderate	12–15%	Medium Risk
🚀 Aggressive	15–20%+	High Risk
📐 Core Metrics Used

Daily Return

Annualized Return

Daily Volatility

Annualized Risk

Z-Score Ranking

Probability of Target Achievement

Risk-adjusted performance score

Standard deviation modeling

Statistical normalization

🛠️ Tech Stack

Python

Pandas

NumPy

Requests

SciPy

Matplotlib

Seaborn

Jupyter Notebook

Statistical Modeling

API Integration

📁 Project Structure
Mutual-fund-performance-tracking/
│
├── mf.py
├── mf.ipynb
├── data/                 # ignored (large datasets)
├── .gitignore
├── requirements.txt
└── README.md

📊 Data Pipeline Flow
API Fetch → Data Cleaning → NAV Processing → 
Daily Returns → Risk Modeling → Annualization → 
Z-Score Ranking → Probability Modeling → 
Investor Profile Filtering → Fund Recommendation

⚙️ Setup Instructions
Clone Repository
git clone https://github.com/shreyask890/Mutual-fund-performance-tracking.git
cd Mutual-fund-performance-tracking

Create Virtual Environment
python3 -m venv venv
source venv/bin/activate

Install Dependencies
pip install -r requirements.txt

▶️ Run Project
Python Script
python mf.py

Jupyter Notebook
jupyter notebook mf.ipynb

📈 Output

Ranked mutual fund lists

Risk-return scatter analysis

Distribution analysis

Conservative portfolio suggestions

Moderate portfolio suggestions

Aggressive portfolio suggestions

Probability-based recommendation confidence

Statistical performance reports

📌 Future Enhancements

Live NAV streaming API

Real-time recommendation system

Portfolio optimization engine

Streamlit web dashboard

User risk-profile input system

ML-based performance prediction

Reinforcement learning for portfolio balancing

API-based investment advisory system

Cloud deployment

Financial microservices architecture

🧑‍💻 Author

Shreyas Kadam
Data Science | Financial Analytics | AI Systems
GitHub: https://github.com/shreyask890