# 📊 Mutual Fund Analysis & Recommendation Tool  
**Python • Statistics • Financial Data Science**

An end-to-end automated system for large-scale mutual fund data analysis and intelligent fund recommendation using statistical models and risk-adjusted performance metrics.

This project builds a **data pipeline, ranking engine, and recommendation system** for identifying top-performing mutual funds based on investor risk profiles.

---

## 🚀 Key Features

### 🔄 Automated Data Pipeline
- Fetches real-time data for **30,000+ mutual funds**
- Uses public APIs to build a clean, structured dataset
- Handles missing values, data normalization, and filtering

### 📈 Performance Analytics Engine
- Daily NAV return calculations  
- Risk & volatility modeling using **Standard Deviation**  
- Annualized return and risk conversion  
- Outlier detection and filtering  
- Efficient frontier style risk-return analysis  

### 🧮 Statistical Ranking System
Fund ranking using:
- Z-Scores  
- Standard Deviation  
- Risk-adjusted returns  
- Probability modeling using **Normal Distribution (CDF)**  

### 🤖 Intelligent Recommendation Engine
Investor-profile based recommendations:
- 🛡️ Conservative  
- ⚖️ Moderate  
- 🚀 Aggressive  

Features:
- Probability-based success scoring  
- Risk-filtered fund selection  
- Growth-fund focused filtering  

---

## 🧠 Recommendation Logic

### Risk-Adjusted Scoring Model

Each fund is scored using:

```text
Z-Score = (Fund Return − Target Return) / Fund Risk
