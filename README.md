# ☀️ Solar Data Dashboard

A Streamlit-powered interactive dashboard for exploring solar radiation metrics (GHI, DNI, DHI) across selected West African countries.

## 📊 Project Overview

This dashboard visualizes solar energy data using intuitive charts and tables, making it easy to compare key solar radiation metrics across countries and regions. It is designed to help stakeholders identify high-potential areas for solar installations.

---

## 🧰 Features

- ✅ **Country selection** with multi-select widget
- ✅ **Metric selector** (GHI, DNI, DHI)
- ✅ **Interactive boxplot** by country and metric
- ✅ **Summary statistics table** (mean, median, std)
- ✅ **Top 5 regions** based on selected metric
- ✅ **Average GHI bar chart** by country
- ✅ **CSV download** of filtered data

---

## 🗂️ Folder Structure


├── app/
│ ├── init.py
│ ├── main.py # Main Streamlit dashboard
│ └── utils.py # Data loading and processing functions
├── scripts/
│ ├── init.py
│ └── README.md # You’re reading it!
├── data/
│ ├── benin.csv
│ ├── sierra_leone.csv
│ └── togo.csv
├── .gitignore
├── requirements.txt
└── README.md



---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https:/github.com/HanaTeshome721/-solar-challenge-week1


###2. Create a virtual environment & activate it
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
