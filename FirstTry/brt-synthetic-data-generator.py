"""
MetroExpress BRT Synthetic Data Generator
Generates 6 months of realistic transit data (Oct 27, 2025 - March 31, 2026)
Based on actual launch period patterns from Miami-Dade County DTPW internship
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# ============================================================================
# CONFIGURATION - Based on Real Launch Data
# ============================================================================

START_DATE = datetime(2025, 10, 27)
END_DATE = datetime(2026, 3, 31)
TOTAL_DAYS = (END_DATE - START_DATE).days + 1

# Station names (exactly as in real data)
STATIONS = [
    '312th/CAMPBELL',
    '200th/CARIBBEAN', 
    '112th/ALLAPATTAH',
    'CIVIC',
    'CORAL REEF',
    'CAMPBELL',
    'HOWARD',
    'AVOCADO',
    'DADELAND SOUTH',
    'FLORIDA CITY',
    'HOMESTEAD',
    'PRINCETON',
    'SOUTH MIAMI HEIGHTS',
    'NARANJA'
]

# Station weights based on launch data (approximate distribution)
STATION_WEIGHTS = [
    0.16,  # 312th/CAMPBELL (highest)
    0.14,  # 200th/CARIBBEAN
    0.12,  # 112th/ALLAPATTAH
    0.12,  # CIVIC
    0.10,  # CORAL REEF
    0.08,  # CAMPBELL
    0.06,  # HOWARD
    0.06,  # AVOCADO
    0.04,  # DADELAND SOUTH
    0.04,  # FLORIDA CITY
    0.03,  # HOMESTEAD
    0.02,  # PRINCETON
    0.02,  # SOUTH MIAMI HEIGHTS
    0.01   # NARANJA
]

# Payment types (exactly as in real data)
PAYMENT_TYPES = ['Cash', 'VISA', 'MASTERCARD', 'DISCOVER', 'American Express']

# Launch period payment distribution (from real data)
LAUNCH_PAYMENT_DIST = {
    'Cash': 0.724,
    'VISA': 0.202,
    'MASTERCARD': 0.070,
    'DISCOVER': 0.003,
    'American Express': 0.001
}

# Target distribution after 6 months (45% digital)
TARGET_PAYMENT_DIST = {
    'Cash': 0.550,
    'VISA': 0.315,
    'MASTERCARD': 0.110,
    'DISCOVER': 0.015,
    'American Express': 0.010
}

# Ticket prices
TICKET_PRICES = {
    'Single Ride': 2.25,
    '1-Day Pass': 5.65,
    '7-Day Pass': 29.25,
    'Monthly Pass': 112.50
}

# Product distribution (mostly single rides during launch)
PRODUCT_DIST = [0.85, 0.10, 0.04, 0.01]  # Single, Day, Week, Month

# Miami holidays and events
HOLIDAYS = [
    datetime(2025, 11, 28),  # Thanksgiving
    datetime(2025, 11, 29),  # Day after Thanksgiving
    datetime(2025, 12, 24),  # Christmas Eve
    datetime(2025, 12, 25),  # Christmas
    datetime(2025, 12, 31),  # New Year's Eve
    datetime(2026, 1, 1),    # New Year's Day
    datetime(2026, 1, 20),   # MLK Day
    datetime(2026, 2, 17)    # Presidents Day
]

# Special events (Miami-specific)
SPECIAL_EVENTS = [
    (datetime(2025, 12, 5), datetime(2025, 12, 8)),   # Art Basel
    (datetime(2026, 1, 19), datetime(2026, 2, 2)),    # Miami Open (Tennis)
    (datetime(2026, 3, 27), datetime(2026, 3, 29))    # Ultra Music Festival
]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def is_holiday(date):
    """Check if date is a holiday"""
    return date in HOLIDAYS

def is_special_event(date):
    """Check if date has a special event"""
    for start, end in SPECIAL_EVENTS:
        if start <= date <= end:
            return True
    return False

def get_daily_volume(date, base_volume=269):
    """Calculate daily ticket volume with growth over time"""
    # Days since start
    days_elapsed = (date - START_DATE).days
    
    # 15% growth over 6 months
    growth_factor = 1 + (0.15 * (days_elapsed / TOTAL_DAYS))
    
    # Day of week adjustment
    day_of_week = date.weekday()
    if day_of_week >= 5:  # Weekend
        weekday_factor = 0.75
    else:  # Weekday
        weekday_factor = 1.0
    
    # Holiday adjustment (lower ridership)
    holiday_factor = 0.6 if is_holiday(date) else 1.0
    
    # Special event adjustment (higher ridership)
    event_factor = 1.3 if is_special_event(date) else 1.0
    
    # Calculate volume with some random noise
    volume = base_volume * growth_factor * weekday_factor * holiday_factor * event_factor
    volume = int(volume * np.random.uniform(0.85, 1.15))
    
    return max(volume, 50)  # Minimum 50 tickets per day

def get_hourly_distribution():
    """Return probability distribution for hours of day"""
    # Based on launch data: peaks at 6-8 AM and 4-6 PM
    hourly_probs = np.array([
        0.005, 0.005, 0.005, 0.010,  # 0-3 AM
        0.025, 0.050, 0.090, 0.110,  # 4-7 AM (morning peak starts)
        0.080, 0.055, 0.040, 0.035,  # 8-11 AM
        0.040, 0.035, 0.030, 0.035,  # 12-3 PM
        0.070, 0.095, 0.080, 0.055,  # 4-7 PM (evening peak)
        0.035, 0.025, 0.015, 0.010   # 8-11 PM
    ])
    return hourly_probs / hourly_probs.sum()

def get_payment_distribution(date):
    """Get payment distribution that evolves over time"""
    days_elapsed = (date - START_DATE).days
    progress = days_elapsed / TOTAL_DAYS
    
    # Interpolate between launch and target distributions
    payment_dist = {}
    for payment_type in PAYMENT_TYPES:
        launch_prob = LAUNCH_PAYMENT_DIST[payment_type]
        target_prob = TARGET_PAYMENT_DIST[payment_type]
        payment_dist[payment_type] = launch_prob + (target_prob - launch_prob) * progress
    
    return payment_dist

def get_validation_rate(date):
    """Get validation rate (higher not-scanned during promo period)"""
    # Promotional period: Oct 27 - Nov 15 (first 3 weeks)
    promo_end = START_DATE + timedelta(days=20)
    
    if date <= promo_end:
        # Promo period: 85% validated (15% free promotional rides)
        return 0.85
    else:
        # Normal operations: 97-98% validated
        return np.random.uniform(0.97, 0.98)

def get_weather(date):
    """Generate realistic Miami weather"""
    # Month-based patterns
    month = date.month
    
    # Temperature (Miami ranges 70-90F, cooler Dec-Jan)
    if month in [12, 1, 2]:
        temp = np.random.uniform(70, 82)
    elif month in [6, 7, 8, 9]:
        temp = np.random.uniform(80, 92)
    else:
        temp = np.random.uniform(75, 88)
    
    # Weather condition (Miami is mostly sunny)
    weather_roll = np.random.random()
    if weather_roll < 0.80:
        condition = 'Sunny'
    elif weather_roll < 0.95:
        condition = 'Rainy'
    else:
        condition = 'Stormy'
    
    # Rain more common in summer
    if month in [6, 7, 8, 9] and condition == 'Sunny':
        if np.random.random() < 0.25:  # 25% chance to override to rainy
            condition = 'Rainy'
    
    return condition, round(temp, 1)

def generate_cc_last_4(payment_type):
    """Generate last 4 digits of card (0 for cash)"""
    if payment_type == 'Cash':
        return 0
    else:
        return np.random.randint(1000, 10000)

# ============================================================================
# MAIN GENERATION FUNCTION
# ============================================================================

def generate_synthetic_data():
    """Generate complete synthetic dataset"""
    
    print("Generating MetroExpress BRT Synthetic Data...")
    print(f"Period: {START_DATE.date()} to {END_DATE.date()}")
    print(f"Total days: {TOTAL_DAYS}")
    
    all_records = []
    order_id = 1
    ticket_id = 2025347950  # Start from realistic ID
    
    hourly_dist = get_hourly_distribution()
    
    # Generate data for each day
    for day_offset in range(TOTAL_DAYS):
        current_date = START_DATE + timedelta(days=day_offset)
        
        if day_offset % 30 == 0:
            print(f"Generating data for {current_date.date()}...")
        
        # Get daily volume
        daily_volume = get_daily_volume(current_date)
        
        # Get payment distribution for this date
        payment_dist = get_payment_distribution(current_date)
        
        # Get validation rate for this date
        validation_rate = get_validation_rate(current_date)
        
        # Get weather
        weather_condition, temperature = get_weather(current_date)
        
        # Generate transactions for this day
        for _ in range(daily_volume):
            # Select hour based on distribution
            hour = np.random.choice(24, p=hourly_dist)
            
            # Create timestamp
            minute = np.random.randint(0, 60)
            second = np.random.randint(0, 60)
            timestamp = current_date.replace(hour=hour, minute=minute, second=second)
            
            # Select station
            station = np.random.choice(STATIONS, p=STATION_WEIGHTS)
            
            # Select payment type
            payment_types = list(payment_dist.keys())
            payment_probs = list(payment_dist.values())
            payment_type = np.random.choice(payment_types, p=payment_probs)
            
            # Select product type
            product_types = list(TICKET_PRICES.keys())
            product = np.random.choice(product_types, p=PRODUCT_DIST)
            unit_price = TICKET_PRICES[product]
            
            # Product count (usually 1, occasionally 2-3)
            product_count = np.random.choice([1, 2, 3], p=[0.92, 0.06, 0.02])
            total_sale = unit_price * product_count
            
            # Validation (ridership)
            ridership = 1 if np.random.random() < validation_rate else 0
            
            # Scan time (if validated, a few minutes after purchase)
            if ridership == 1:
                scan_delay = np.random.randint(1, 15)  # 1-15 minutes
                scan_time = timestamp + timedelta(minutes=scan_delay)
                scan_time_str = scan_time.strftime('%Y-%m-%d %H:%M:%S')
            else:
                scan_time_str = '2025-10-27 0:02:15'  # Placeholder for not scanned
            
            # Generate TVM info
            tvm_number = np.random.randint(1, 3)  # 2 TVMs per station
            tvm = f'TVM{tvm_number:02d}'
            tvm_name = f'{station}-{tvm}'
            
            # Generate faregate info
            faregate_number = np.random.randint(1, 3)  # 2 faregates per station
            faregate = f'FG{faregate_number:02d}'
            faregate_name = f'{station}-{faregate}'
            
            # Create record
            record = {
                'order_id': order_id,
                'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'hour': hour,
                'am_pm': 'AM' if hour < 12 else 'PM',
                'ticket_id': ticket_id,
                'unit_price': unit_price,
                'product_count': product_count,
                'total_sale': round(total_sale, 2),
                'tvm': tvm,
                'tvm_name': tvm_name,
                'tvm_station_sort': station,
                'tvm_station': station,
                'tvm_sort_name': tvm_name,
                'payment_type': payment_type,
                'cc_last_4': generate_cc_last_4(payment_type),
                'faregate_name': faregate_name,
                'gate_station': station,
                'scan_time': scan_time_str,
                'faregate': faregate,
                'ridership': ridership,
                'date': current_date.strftime('%Y-%m-%d'),
                # New columns for ML
                'weather_condition': weather_condition,
                'temperature': temperature,
                'is_holiday': is_holiday(current_date),
                'is_event_day': is_special_event(current_date),
                'day_of_week': current_date.strftime('%A')
            }
            
            all_records.append(record)
            order_id += 1
            ticket_id += 1
    
    # Create DataFrame
    df = pd.DataFrame(all_records)
    
    print(f"\nGeneration complete!")
    print(f"Total records: {len(df):,}")
    print(f"\nPayment distribution at start:")
    start_df = df[df['date'] <= '2025-11-15']
    print(start_df['payment_type'].value_counts(normalize=True).round(3))
    print(f"\nPayment distribution at end:")
    end_df = df[df['date'] >= '2026-03-01']
    print(end_df['payment_type'].value_counts(normalize=True).round(3))
    print(f"\nValidation rate at start: {start_df['ridership'].mean():.1%}")
    print(f"Validation rate at end: {end_df['ridership'].mean():.1%}")
    
    return df

# ============================================================================
# RUN GENERATION AND SAVE
# ============================================================================

if __name__ == "__main__":
    # Generate data
    synthetic_data = generate_synthetic_data()
    
    # Save to CSV
    output_file = 'synthetic_brt_data_6months.csv'
    synthetic_data.to_csv(output_file, index=False)
    print(f"\nData saved to: {output_file}")
    
    # Display sample
    print("\nSample records:")
    print(synthetic_data.head(10))
    
    # Display summary statistics
    print("\nSummary Statistics:")
    print(f"Date range: {synthetic_data['date'].min()} to {synthetic_data['date'].max()}")
    print(f"Total transactions: {len(synthetic_data):,}")
    print(f"Total revenue: ${synthetic_data['total_sale'].sum():,.2f}")
    print(f"\nTop 5 stations by volume:")
    print(synthetic_data['tvm_station'].value_counts().head())
    print(f"\nWeather distribution:")
    print(synthetic_data['weather_condition'].value_counts())
