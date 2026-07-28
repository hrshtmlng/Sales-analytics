# 📊 Sales & Revenue Analytics Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sales-analytics-iftkvqq4jzqm8jnnyp5yqu.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Live Demo:** [sales-analytics-iftkvqq4jzqm8jnnyp5yqu.streamlit.app](https://sales-analytics-iftkvqq4jzqm8jnnyp5yqu.streamlit.app/)

---

## 🎯 Overview

An interactive **Sales & Revenue Analytics Dashboard** built with **Streamlit**, **Plotly**, and **SQLite** — analyzing **105,130+ transactional records** across 40,000 orders, 5,000 customers, and 500 products.

The dashboard provides real-time insights into:
- 📈 Revenue trends & growth patterns
- 🥧 Category contribution & performance
- 🏆 Top-performing products
- 👥 Customer segmentation analysis
- 🗓️ Seasonal demand & peak detection

---

## 🖼️ Dashboard Preview

![Dashboard Preview](dashboard_preview.png)

### Key Features

| Feature | Description |
|---------|-------------|
| **KPI Cards** | Total Revenue, Orders, AOV, Active Customers, Gross Margin |
| **Revenue Trend** | Monthly time-series with interactive zoom & hover |
| **Category Share** | Donut chart showing revenue distribution by category |
| **Top Products** | Horizontal bar chart of best-performing products |
| **Customer Segments** | Revenue breakdown by VIP, Regular, and New customers |
| **Seasonality** | Peak demand detection highlighting Nov-Dec surge |

---

## 🗂️ Data Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  customers  │────▶│   orders    │◀────│ order_items │
│  (5,000)    │     │  (40,000)   │     │ (105,130)   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                                │
                                         ┌──────┴──────┐
                                         │   products  │
                                         │    (500)    │
                                         └──────┬──────┘
                                                │
                                         ┌──────┴──────┐
                                         │  categories │
                                         │    (10)     │
                                         └─────────────┘
```

### Database Schema

| Table | Records | Description |
|-------|---------|-------------|
| `categories` | 10 | Product categories with profit margins |
| `products` | 500 | Product catalog with costs & pricing |
| `customers` | 5,000 | Customer profiles with segmentation |
| `orders` | 40,000 | Order headers with status & dates |
| `order_items` | 105,130 | Line-item transactions |

---

## 🚀 Live App

**No installation required!** View the live dashboard here:

👉 **[sales-analytics-iftkvqq4jzqm8jnnyp5yqu.streamlit.app](https://sales-analytics-iftkvqq4jzqm8jnnyp5yqu.streamlit.app/)**

---

## 🛠️ Local Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/hrshtmlng/Sales-analytics.git
cd Sales-analytics

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate (Linux/Mac)
source venv/bin/activate
#    Activate (Windows)
#    venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 📦 Project Structure

```
Sales-analytics/
├── app.py                      # Main Streamlit application
├── sales_analytics.db          # SQLite database (105K+ records)
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── analytics_queries.sql       # SQL analytics queries
├── powerbi_dax_measures.txt    # DAX measures for Power BI
├── powerbi_dashboard_guide.txt # Power BI layout guide
├── excel_dashboard_guide.txt   # Excel + Power Pivot guide
├── categories.csv              # Raw data exports
├── customers.csv
├── orders.csv
├── order_items.csv
├── products.csv
└── README.md                   # This file
```

---

## 🔍 Key Insights

| Metric | Value |
|--------|-------|
| **Total Revenue** | ~$22.8M |
| **Total Orders** | ~33,500 completed |
| **Avg Order Value** | ~$680 |
| **Active Customers** | ~4,800 |
| **Gross Margin** | ~38% |
| **Peak Season** | November–December |
| **Top Category** | Automotive (13.1%) |

### Business Actions Enabled

- **Inventory Optimization** — Identify peak demand months for stock planning
- **Product Strategy** — Focus on top-performing categories and products
- **Customer Targeting** — Segment-based marketing (VIP vs Regular vs New)
- **Revenue Forecasting** — Seasonal patterns for sales planning

---

## 🧮 SQL Analytics

The `analytics_queries.sql` file contains **8 sections** of production-ready queries:

1. **KPI Calculations** — Revenue, orders, AOV, margin
2. **Time Intelligence** — MoM growth, running totals, YoY comparison
3. **Category Analysis** — Revenue share, contribution, trends
4. **Product Performance** — Top products, ABC classification, monthly cohorts
5. **Customer Analytics** — Segments, CLV, cohort retention
6. **Seasonality** — Monthly patterns, day-of-week analysis
7. **Inventory Optimization** — Demand forecasting, safety stock, reorder points
8. **Executive Summary View** — Pre-built SQL view

Run any query in **DB Browser for SQLite** or connect via Python:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('sales_analytics.db')
df = pd.read_sql("SELECT * FROM v_executive_summary", conn)
print(df)
```

---

## 📊 Power BI & Excel

This project includes guides for building the same dashboard in:

- **Power BI** — `powerbi_dashboard_guide.txt` + `powerbi_dax_measures.txt`
- **Excel + Power Pivot** — `excel_dashboard_guide.txt`

Both use the same SQLite database or CSV exports.

---

## 🛡️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Streamlit** | Web application framework |
| **Plotly** | Interactive visualizations |
| **Pandas** | Data manipulation & analysis |
| **SQLite** | Lightweight database engine |
| **Python** | Core programming language |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new visualizations
- Improve query performance
- Add forecasting models
- Enhance the UI/UX

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualizations powered by [Plotly](https://plotly.com/)
- Data generated for demonstration purposes

---

> ⭐ **Star this repo** if you found it helpful!
