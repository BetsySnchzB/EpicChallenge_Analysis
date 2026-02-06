"""
MetroExpress BRT Data Analysis - Starter Script
------------------------------------------------
Quick starter code for analyzing the synthetic 6-month dataset

Author: Betsy Sanchez
Date: January 2026
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set display options
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
sns.set_style('whitegrid')

# Load the data
df = pd.read_csv('synthetic_brt_data_6months.csv')

# Convert date columns to datetime
df['date'] = pd.to_datetime(df['date'])
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create additional useful columns
df['month'] = df['date'].dt.to_period('M')
df['week'] = df['date'].dt.isocalendar().week
df['day_of_week'] = df['date'].dt.day_name()
df['is_weekend'] = df['date'].dt.dayofweek.isin([5, 6])
df['is_digital'] = df['payment_type'] != 'Cash'

print("=" * 70)
print("DATA LOADED SUCCESSFULLY")
print("=" * 70)
print(f"Shape: {df.shape}")
print(f"Date Range: {df['date'].min()} to {df['date'].max()}")
print(f"Total Transactions: {len(df):,}")
print("\n")

# ============================================================================
# EXAMPLE 1: Digital Adoption Trend Over Time
# ============================================================================
print("📈 EXAMPLE 1: Digital Adoption Trend Over Time")
print("-" * 70)

digital_trend = df.groupby('month').agg({
    'is_digital': ['sum', 'count']
}).round(2)

digital_trend.columns = ['digital_count', 'total_count']
digital_trend['digital_pct'] = (digital_trend['digital_count'] / digital_trend['total_count'] * 100).round(1)

print(digital_trend)
print("\n")

# ============================================================================
# EXAMPLE 2: Station Performance Comparison
# ============================================================================
print("🏢 EXAMPLE 2: Top 10 Stations by Volume")
print("-" * 70)

station_performance = df.groupby('tvm_station').agg({
    'order_id': 'count',
    'is_digital': 'mean',
    'ridership': 'mean'
}).round(3)

station_performance.columns = ['total_transactions', 'digital_adoption_rate', 'validation_rate']
station_performance = station_performance.sort_values('total_transactions', ascending=False)

print(station_performance.head(10))
print("\n")

# ============================================================================
# EXAMPLE 3: Hourly Patterns
# ============================================================================
print("⏰ EXAMPLE 3: Peak Hours Analysis")
print("-" * 70)

hourly = df.groupby('hour').size().sort_values(ascending=False)
print("Top 5 Peak Hours:")
for hour, count in hourly.head().items():
    am_pm = 'AM' if hour < 12 else 'PM'
    hour_12 = hour if hour <= 12 else hour - 12
    if hour == 0:
        hour_12 = 12
    print(f"  {hour_12:2d} {am_pm}: {count:,} transactions")
print("\n")

# ============================================================================
# EXAMPLE 4: Weekday vs Weekend Comparison
# ============================================================================
print("📅 EXAMPLE 4: Weekday vs Weekend Analysis")
print("-" * 70)

day_comparison = df.groupby('is_weekend').agg({
    'order_id': 'count',
    'is_digital': 'mean',
    'total_sale': 'sum'
}).round(2)

day_comparison.columns = ['transactions', 'digital_rate', 'total_revenue']
day_comparison.index = ['Weekday', 'Weekend']
print(day_comparison)
print("\n")

# ============================================================================
# EXAMPLE 5: Monthly Growth Rate
# ============================================================================
print("📊 EXAMPLE 5: Month-over-Month Growth")
print("-" * 70)

monthly_transactions = df.groupby('month').size()
monthly_growth = monthly_transactions.pct_change() * 100

growth_df = pd.DataFrame({
    'Transactions': monthly_transactions,
    'MoM Growth %': monthly_growth.round(1)
})

print(growth_df)
print("\n")

# ============================================================================
# READY FOR ML MODELING
# ============================================================================
print("=" * 70)
print("✅ DATA READY FOR ML MODELS")
print("=" * 70)
print("\nSuggested Next Steps:")
print("1. Time Series Forecasting: Use ARIMA/Prophet on daily ridership")
print("2. Classification: Predict payment type based on time/station/weather")
print("3. Clustering: Group stations by behavior patterns")
print("4. Anomaly Detection: Identify unusual transaction patterns")
print("5. Impact Analysis: Measure event effects on ridership")
print("\nHappy modeling! 🚀")
