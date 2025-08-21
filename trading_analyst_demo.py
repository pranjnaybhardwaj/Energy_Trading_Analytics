# trading_analyst_demo.py
"""
A demo project showcasing energy demand forecasting, portfolio trading simulation,
and risk management  in the renewable energy domain.

Features:
1. Synthetic data generation for electricity and gas demand.
2. ETL pipeline: CSV ingestion, cleaning, and SQLite storage.
3. Short- and long-term forecasting using ARIMA.
4. Portfolio simulation of renewable generation vs. demand positions.
5. Risk metrics: VaR calculation.
6. Inline results and summary export (CSV, plots).

Dependencies:
- pandas, numpy, sqlalchemy, statsmodels, matplotlib

To run:
$ pip install pandas numpy sqlalchemy statsmodels matplotlib
$ python trading_analyst_demo.py
"""
import os
import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# 1. Synthetic Data Generation
def generate_synthetic_demand(start_date='2024-01-01', days=365*2):
    date_range = pd.date_range(start=start_date, periods=days, freq='D')
    # seasonal + trend + noise
    seasonal = 100 + 20 * np.sin(2 * np.pi * date_range.dayofyear / 365)
    trend = np.linspace(0, 5, days)
    noise = np.random.normal(0, 5, days)
    demand = seasonal + trend + noise
    return pd.DataFrame({'date': date_range, 'demand_mw': demand})

# 2. ETL Pipeline
DB_FILE = 'energy_trading.db'

def etl_load(df, table_name='demand'):  # loads into SQLite
    conn = sqlite3.connect(DB_FILE)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def etl_extract(table_name='demand'):
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql(f'SELECT * FROM {table_name}', conn, parse_dates=['date'])
    conn.close()
    return df

# 3. Forecasting
def forecast_arima(series, steps=30, order=(5,1,0)):
    model = ARIMA(series, order=order)
    fit = model.fit()
    forecast = fit.forecast(steps=steps)
    return forecast

# 4. Trading Simulation & Risk
def simulate_portfolio(demand_forecast, generation_mw=120):
    # Long: generation asset, Short: customer demand
    pnl = (generation_mw - demand_forecast) * 50  # price per MWh
    return pnl

def calculate_var(pnl, confidence=0.95):
    return np.percentile(pnl, (1-confidence)*100)

# 5. Visualization
def plot_series(df, column='demand_mw'):
    plt.figure()
    plt.plot(df['date'], df[column])
    plt.title(f'{column} over time')
    plt.xlabel('Date')
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig('demand_timeseries.png')

def plot_forecast(history, forecast):
    plt.figure()
    plt.plot(history.index, history, label='History')
    future_idx = pd.date_range(start=history.index[-1] + timedelta(days=1), periods=len(forecast), freq='D')
    plt.plot(future_idx, forecast, label='Forecast')
    plt.legend()
    plt.title('Demand Forecast')
    plt.savefig('demand_forecast.png')

# 6. Main Execution
if __name__ == '__main__':
    # Clean previous DB
    if os.path.exists(DB_FILE): os.remove(DB_FILE)

    # Generate & load data
    demand_df = generate_synthetic_demand()
    etl_load(demand_df)

    # Extract & visualize
    stored_df = etl_extract()
    plot_series(stored_df)

    # Forecast
    history = stored_df.set_index('date')['demand_mw']
    forecast = forecast_arima(history, steps=90)
    plot_forecast(history, forecast)

    # Simulate trading
    pnl = simulate_portfolio(forecast, generation_mw=120)
    var_95 = calculate_var(pnl)
    print(f"95% VaR on PnL over forecast horizon: €{var_95:.2f}")

    # Export PnL and forecast
    out = pd.DataFrame({'forecast_date': forecast.index, 'forecast_mw': forecast.values, 'pnl_eur': pnl.values})
    out.to_csv('forecast_and_pnl.csv', index=False)
    print("Exported forecast_and_pnl.csv and charts to working directory.")
