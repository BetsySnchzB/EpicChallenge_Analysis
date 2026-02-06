# MetroExpress BRT Synthetic Dataset Documentation

## Overview
This synthetic dataset extends the original 11-day MetroExpress BRT launch data (Oct 27 - Nov 7, 2025) to a full 6-month period (Oct 27, 2025 - Apr 27, 2026). The data was generated to simulate realistic transit patterns, payment behavior evolution, and external factors affecting ridership.

**Total Records:** 87,875 transactions  
**Date Range:** October 27, 2025 - April 27, 2026 (183 days)  
**File:** `synthetic_brt_data_6months.csv`

---

## Data Generation Methodology

### 1. Station Data (14 BRT Stations)
All 14 MetroExpress BRT stations along the South Dade TransitWay:

| Station Name | Latitude | Longitude | Volume Weight | Digital Affinity |
|--------------|----------|-----------|---------------|------------------|
| 312th/CAMPBELL | 25.4713 | -80.4454 | 1.30 | 1.20 |
| 296th/AVACADO | 25.4867 | -80.4589 | 1.10 | 0.80 |
| 264th/BAUER | 25.5213 | -80.4178 | 1.15 | 0.85 |
| 244th | 25.5456 | -80.3989 | 0.90 | 0.90 |
| 200th/CARIBBEAN | 25.5815 | -80.3568 | 1.25 | 1.15 |
| 184th/EUREKA | 25.5967 | -80.3412 | 0.85 | 0.95 |
| 177th/KROME | 25.6045 | -80.3345 | 0.80 | 0.90 |
| 168th/RICHMOND | 25.6123 | -80.3267 | 0.75 | 0.85 |
| 152th/CORAL REEF | 25.6278 | -80.3145 | 0.95 | 0.90 |
| 136th/HOWARD | 25.6456 | -80.3089 | 0.85 | 0.85 |
| 112th/ALLAPATTAH | 25.6734 | -80.2978 | 1.20 | 1.10 |
| 104TH | 25.6823 | -80.2912 | 0.70 | 0.95 |
| CIVIC | 25.7617 | -80.1918 | 1.20 | 1.25 |
| MARLIN | 25.7534 | -80.2156 | 0.80 | 1.00 |

**Volume Weight:** Relative ridership volume compared to average station (higher = more riders)  
**Digital Affinity:** Station's propensity to adopt digital payments (higher = faster digital adoption)

### 2. Payment Type Evolution
Digital payment adoption increases gradually over the 6-month period:

| Month | Digital Adoption % | Notes |
|-------|-------------------|-------|
| Oct 2025 | 29.0% | Launch baseline |
| Nov 2025 | 32.7% | Early adoption |
| Dec 2025 | 34.1% | Art Basel boost |
| Jan 2026 | 37.4% | Post-holiday normalization |
| Feb 2026 | 39.5% | Steady growth |
| Mar 2026 | 42.7% | Ultra Music Festival boost |
| Apr 2026 | 44.1% | Reaching target |

**Payment Type Distribution:**
- **Cash:** 61.7% (declining over time)
- **Visa:** 27.2% (most popular digital)
- **Mastercard:** 8.9%
- **American Express:** 1.2%
- **Discover:** 1.1%

### 3. Temporal Patterns

**Hourly Distribution:**
Peak hours follow typical commuter patterns:
- **Morning Peak:** 6-8 AM (highest volume at 7 AM)
- **Midday:** 11 AM - 1 PM (moderate activity)
- **Evening Peak:** 4-6 PM (highest volume at 5 PM)
- **Off-Peak:** After 7 PM and overnight (minimal activity)

**Weekly Patterns:**
- **Weekday:** 79.9% of transactions (high commuter volume)
- **Weekend:** 20.1% of transactions (reduced service utilization)

### 4. Miami Events Calendar
Specific events that impacted ridership volume:

| Date | Event | Impact Factor |
|------|-------|---------------|
| Oct 31, 2025 | Halloween | 1.1x |
| Nov 28, 2025 | Thanksgiving | 0.6x |
| Nov 29, 2025 | Black Friday | 0.8x |
| Dec 5-8, 2025 | Art Basel | 1.4-1.5x |
| Dec 24-25, 2025 | Christmas | 0.4-0.7x |
| Dec 31, 2025 | New Year's Eve | 1.2x |
| Jan 1, 2026 | New Year's Day | 0.5x |
| Mar 15, 2026 | Spring Break | 1.2x |
| Mar 19-30, 2026 | Miami Open Tennis | 1.3x |
| Mar 28-30, 2026 | Ultra Music Festival | 1.6-1.7x |

### 5. External Factors

**Weather Impact:**
- Rainy season months (Oct): 30% probability of 15% ridership reduction on random days
- Cooler months (Nov-Feb): Generally higher ridership
- Warmer months (Mar-Apr): Moderate ridership

**Ridership Growth:**
- Overall 15% growth trajectory over 6 months
- Launch period (Oct): Lower volume due to system newness
- Maturity period (Mar-Apr): Higher volume as system becomes established

**Validation Rate:**
- **85.1%** of tickets are validated (scanned at faregate)
- **14.9%** not scanned (purchased but not used, or used without scanning)

---

## Column Definitions

| Column Name | Type | Description |
|-------------|------|-------------|
| `order_id` | Integer | Unique transaction identifier (incremental) |
| `timestamp` | DateTime | Transaction timestamp (YYYY-MM-DD HH:MM:SS) |
| `hour` | Integer | Hour of day (0-23) |
| `am_pm` | String | AM or PM indicator |
| `ticket_id` | Integer | Unique ticket identifier (random 10-digit) |
| `unit_price` | Float | Price per ticket ($2.25) |
| `product_count` | Integer | Number of tickets in transaction (1-4) |
| `total_sale` | Float | Total transaction amount |
| `tvm` | String | Ticket vending machine ID (F011XXXX) |
| `tvm_name` | String | TVM identifier (TVMXX001/002) |
| `tvm_station_sort` | String | TVM sort code (TVMXX) |
| `tvm_station` | String | Station name where purchase occurred |
| `tvm_sort_name` | String | Combined TVM-Station identifier |
| `payment_type` | String | Cash, Visa, MASTERCARD, DISCOVER, or American Express |
| `cc_last_4` | Integer | Last 4 digits of card (0 for cash) |
| `faregate_name` | String | Faregate identifier (FGXX001/002) or "Not Scanned" |
| `gate_station` | String | Station where ticket was validated or "Not Scanned" |
| `scan_time` | DateTime | Validation timestamp or "Not Scanned" |
| `faregate` | String | Faregate device ID (U20150XXX) or "Not Scanned" |
| `ridership` | Integer | 1 if validated, 0 if not scanned |
| `date` | Date | Transaction date (YYYY-MM-DD) |

---

## Data Quality Notes

### Realistic Features
✅ Follows actual launch data patterns from Oct 27 - Nov 7, 2025  
✅ Station volume matches observed high-performers (312th/Campbell, 200th/Caribbean)  
✅ Peak hours align with actual commuter behavior  
✅ Digital adoption curve reflects realistic behavior change  
✅ Event impacts based on Miami's actual event calendar  
✅ Validation rate (~85%) matches transit industry standards  

### Synthetic Assumptions
⚠️ Weather impacts are simplified (not tied to actual Miami weather data)  
⚠️ Station-specific digital affinity is estimated based on location/demographics  
⚠️ Event impacts are estimates based on typical event effects on transit  
⚠️ TVM and faregate IDs are systematically generated  

---

## Use Cases for ML Models

This dataset is designed to support:

1. **Time Series Forecasting**
   - Predict daily/weekly ridership trends
   - Forecast payment type adoption rates
   - Models: ARIMA, Prophet, LSTM

2. **Predictive Maintenance**
   - Identify TVM failure patterns
   - Predict high-traffic periods for equipment stress
   - Models: Random Forest, XGBoost

3. **Anomaly Detection**
   - Flag unusual transaction patterns
   - Detect potential fraud or equipment malfunctions
   - Models: Isolation Forest, Autoencoders

4. **Customer Segmentation**
   - Cluster stations by behavior (cash-heavy vs digital-adopting)
   - Identify rider groups by usage patterns
   - Models: K-Means, DBSCAN

5. **Impact Analysis**
   - Measure effect of events on ridership
   - Simulate "what-if" scenarios for policy changes
   - Models: Monte Carlo Simulation, Causal Inference

---

## Data Integrity Checks

✓ No missing values in required fields  
✓ All timestamps are valid and sequential  
✓ All station names match the 14 official stations  
✓ Payment types are limited to valid options  
✓ Card numbers (last 4) are 0 for cash, 1000-9999 for card payments  
✓ Validation timestamps are after purchase timestamps  
✓ Total sale = unit_price × product_count  
✓ Date range is complete with no gaps  

---

## Version History

**Version 1.0** - January 9, 2026
- Initial 6-month synthetic dataset
- 87,875 transactions
- October 27, 2025 - April 27, 2026

---

## Contact & Attribution

**Created by:** Betsy Sanchez  
**Project:** MetroExpress BRT Launch Analytics  
**Client:** Miami-Dade County DTPW  
**Purpose:** Portfolio demonstration and ML model training  

**Note:** This is synthetic data generated for analysis and demonstration purposes. It extends real launch-period data with realistic patterns but should not be used for official reporting or decision-making without validation against actual data.
