# Trading Analyst Energy Forecasting Demo

A complete Python demo project simulating the responsibilities of a **Trading Analyst** in the renewable energy sector. This project combines forecasting, trading simulation, risk assessment, and data engineering to showcase practical knowledge.

## 🔧 Features

- Synthetic electricity demand data generation (2 years)
- ETL pipeline using SQLite (CSV ingestion, cleaning, storage)
- Forecasting with ARIMA (short- and long-term)
- Renewable energy trading simulation (simple PnL model)
- 95% Value-at-Risk (VaR) calculation
- Matplotlib visualizations and CSV output

## 📁 Files

- `trading_analyst_demo.py`: Main script (all-in-one)
- `demand_timeseries.png`: Time series plot of historical demand
- `demand_forecast.png`: 90-day demand forecast plot
- `forecast_and_pnl.csv`: Combined forecast and PnL data
- `energy_trading.db`: SQLite database storing raw demand data

## ▶️ How to Run

```bash
pip install pandas numpy sqlalchemy statsmodels matplotlib
python trading_analyst_demo.py
```

## 📈 Sample Output
- Time series of energy demand over 2 years
- 90-day forecast using ARIMA
- Simulated PnL for a fixed renewable asset (120 MW)
- Calculated 95% VaR: estimated downside risk in EUR

## 📌 Concepts Demonstrated

- Time-series forecasting in energy markets
- ETL pipelines using Python and SQLite
- Portfolio simulation (generation vs. customer demand)
- Risk quantification using historical simulations

## 📚 Technologies Used

- Python
- Pandas, NumPy, SQLite, Statsmodels, Matplotlib

## 💼 Use Case

This project is ideal for showcasing:
- Energy demand forecasting and risk modeling skills
- Data engineering and Python proficiency
- Alignment with Trading Analyst responsibilities in energy firms

## 📎 License

MIT License. 

---

**Author:** [Pranjnay Bhardwaj](https://www.linkedin.com/in/pranjnay-bhardwaj-716631192)  
**GitHub:** [pranjnaybhardwaj](https://github.com/pranjnaybhardwaj)
