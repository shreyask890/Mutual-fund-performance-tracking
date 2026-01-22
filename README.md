# 📊 Mutual Fund Analysis & Recommendation Tool
### Python • Statistics • Financial Data Science

An end-to-end automated system for large-scale mutual fund data analysis and intelligent fund recommendation using statistical models and risk-adjusted performance metrics.

---

## 📖 Overview
This project builds a robust data pipeline, ranking engine, and recommendation system designed to identify top-performing mutual funds. By leveraging statistical modeling, the tool categorizes funds based on investor risk profiles, ensuring data-driven investment decisions.



## 🚀 Key Features

### 🔄 Automated Data Pipeline
* **Scale:** Fetches real-time data for **30,000+** mutual funds.
* **Integrity:** Uses public APIs to build a clean, structured dataset.
* **Preprocessing:** Handles missing values, data normalization, and filtering automatically.

### 📈 Performance Analytics Engine
* **Returns:** Daily NAV return calculations and annualized return conversion.
* **Risk:** Volatility modeling using Standard Deviation and outlier detection.
* **Analysis:** Efficient frontier-style risk-return analysis.

### 🧮 Statistical Ranking System
Funds are ranked using a combination of:
* **Z-Scores** for performance benchmarking.
* **Standard Deviation** for volatility assessment.
* **Probability Modeling** using Normal Distribution (CDF) to estimate target achievement.

### 🤖 Intelligent Recommendation Engine
Tailored fund selection based on three distinct investor profiles:
* 🛡️ **Conservative:** Focus on low-risk, steady growth.
* ⚖️ **Moderate:** Balanced risk-reward ratio.
* 🚀 **Aggressive:** High-growth potential with higher volatility.

### 👤 Investor Profiles
| Profile | Target Return | Risk Level |
| :--- | :--- | :--- |
| 🛡️ **Conservative** | 8% | Low Risk |
| ⚖️ **Moderate** | 12–15% | Medium Risk |
| 🚀 **Aggressive** | 15–20%+ | High Risk |

---

## 🛠️ Tech Stack
* **Language:** Python
* **Data Handling:** Pandas, NumPy
* **Statistics:** SciPy
* **Visualization:** Matplotlib, Seaborn
* **Environment:** Jupyter Notebook
* **Data Source:** API Integration (Requests)

---

## 📁 Project Structure
```text
Mutual-fund-performance-tracking/
│
├── mf.py                 # Main execution script
├── mf.ipynb              # Interactive analysis notebook
├── data/                 # Local data storage (Git ignored)
├── .gitignore            # Files to exclude from Git
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
📊 Data Pipeline Flow
API Fetch: Retrieve raw NAV data.

Data Cleaning: Handle nulls and normalize formats.

NAV Processing: Calculate daily returns.

Risk Modeling: Compute annualized risk and volatility.

Statistical Ranking: Apply Z-Score and Probability modeling.

Filtering: Apply Investor Profile logic.

Recommendation: Generate final fund list.

⚙️ Setup & Installation
1. Clone Repository
Bash
git clone [https://github.com/shreyask890/Mutual-fund-performance-tracking.git](https://github.com/shreyask890/Mutual-fund-performance-tracking.git)
cd Mutual-fund-performance-tracking
2. Create Virtual Environment
Bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Run the Project
As a Script:

Bash
python mf.py
As a Notebook:

Bash
jupyter notebook mf.ipynb
🧑‍💻 Author
Shreyas Kadam Data Science | Financial Analytics | AI Systems
