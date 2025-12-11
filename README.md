# 🚀 Crypto Full-Stack Analytics Project

A fully deployed **end-to-end full-stack data engineering project** that collects real-time Bitcoin prices, stores them in a database, exposes them via a FastAPI backend, and visualizes them through a deployed dashboard.

This project demonstrates:
- Data collection
- Database engineering
- API development
- Frontend web development
- Deployment of both backend and frontend

Perfect for data engineering, full-stack, and backend portfolio use cases.

---

## 📌 Live Demo

### 🔗 Frontend Dashboard (Vercel)
**https://crypto-fullstack-project.vercel.app**

### 🔗 Backend API (Render)
**https://crypto-fullstack-project.onrender.com**

---

## 🎯 Features

### 🧩 **Data Pipeline**
- Fetches real-time Bitcoin price from CoinGecko API
- Automated data collector script (`auto_collect.py`)
- Stores timestamped prices in SQLite database

### 🗄 **Database**
- SQLite database (`crypto.db`)
- SQLAlchemy ORM for clean model definitions
- Historical price retrieval
- Support for analytics (Moving averages, volatility, etc.)

### ⚙️ **Backend API (FastAPI)**
- `/current` – latest Bitcoin price  
- `/history` – recent historical prices  
- `/stats/moving_average` – simple moving average  
- CORS enabled for frontend integration  
- Hosted on Render as a public API

### 🖥 **Frontend Dashboard**
- Built with HTML, JavaScript, Chart.js
- Fetches data from backend API
- Displays:
  - Current BTC price  
  - Historical line chart  
- Deployed through Vercel

### ☁️ **Deployment**
- Backend: Render.com  
- Frontend: Vercel.com  
- GitHub version control integration

---

## 🧱 Project Architecture

