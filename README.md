# 📊 Stock Market Performance Analysis (Python)

## 👋 Project Overview

This project analyzes stock market performance using Python.

The goal is to show how financial data can be:

- downloaded automatically
- cleaned and transformed
- analyzed using financial indicators
- compared across multiple stocks
- visualized with interactive charts
- saved in a reproducible way

The project is designed to demonstrate mid-level data analysis and engineering skills, not just plotting charts.


---

## 🎯 What This Project Tries to Show

This project demonstrates:

✔ Building a clean analytics pipeline  
✔ Working with real financial data  
✔ Using modular Python architecture  
✔ Creating reproducible experiment outputs  
✔ Calculating risk & performance metrics  

In short:

> Turning raw stock data into useful insights.


---

## 📈 What Analysis Is Performed

### 1️⃣ Data Download

Stock data is downloaded automatically from Yahoo Finance using:

- Open price
- High price
- Low price
- Close price
- Volume

Example stocks used:

| Company                 | Ticker | Sector              |
| ----------------------- | ------ | ------------------- |
| JPMorgan Chase & Co.    | JPM    | Banking / Finance   |
| Exxon Mobil Corporation | XOM    | Energy              |
| Johnson & Johnson       | JNJ    | Healthcare          |
| Tesla, Inc.             | TSLA   | Automotive / Growth |


---

### 2️⃣ Technical Indicators

The project calculates:

#### Moving Averages
- Smooth price movement
- Help identify trends

#### Daily Return
- Daily percentage change in price

#### Volatility
- Measures how unstable the stock price is
- Indicates risk level


---

### 3️⃣ Correlation Analysis

Shows how stocks move relative to each other.

Example insight:

- High correlation → stocks move together
- Low correlation → diversification opportunity


---

### 4️⃣ Risk Metric (Sharpe Ratio)

Sharpe Ratio measures:

> Return earned per unit of risk taken.

Higher Sharpe Ratio usually means better risk-adjusted performance.


---

### 5️⃣ Summary Report

The project automatically identifies:

- Best performing stock (Sharpe)
- Worst performer
- Most highly correlated stock pair

This simulates what an analyst would actually present.


---

## 🧱 Project Structure

