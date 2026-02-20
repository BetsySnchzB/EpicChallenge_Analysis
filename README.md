# EpicChallenge_Analysis

# MetroExpress BRT Launch Analytics

**Featured in [Miami-Dade County Employee Newsletter](https://secure.miamidade.gov/employee/ithrive/archive/dtpw-interns.page)**

> Exploratory, predictive, and strategic modeling for Miami-Dade County's first Bus Rapid Transit system

[![View Live Case Study](https://img.shields.io/badge/View-Live_Case_Study-0f766e?style=for-the-badge)](https://betsysnchzb.github.io/EpicChallenge_Analysis/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/betsy.sanchez5833/vizzes)


## Project Overview

This project analyzes launch data from **MetroExpress**, Miami-Dade County's first Bus Rapid Transit system, the longest all-electric BRT corridor in the United States.

**What began as a 6-week team internship analyzing 11 days of real launch data evolved into a comprehensive analytical framework demonstrating:**

- **Descriptive analytics** → Exploratory insights from launch period
- **Predictive modeling** → Time-series forecasting, classification, clustering
- **Prescriptive strategy** → Resource allocation and ROI modeling

## Business Objective

Support Miami-Dade DTPW's modernization goals:

- Increase ridership
- Reduce cash dependency (69% cash at launch)
- Accelerate digital payment adoption
- Prepare for Phase 2 (1,000-bus fleet integration)

## My Contributions

### During EPIC Challenge Internship (Team Phase)

**Oct-Nov 2025** | *Collaborative analysis with Miami-Dade County DTPW*

- Analyzed **3,596 transactions** from the first 11 days of operations
- Identified 69% cash dominance and station concentration patterns
- Contributed to executive presentation delivered to DTPW leadership
- **Featured in county employee newsletter** alongside team members Sally Posey and Anabel Ferreiro Perez

### Independent Extension (Solo Phase)

**Dec 2025-Jan 2026** | *Advanced analytics framework development*

- Built **3 interactive Tableau dashboards** for executive stakeholders
- Generated synthetic 6-month dataset (**87,875 transactions**) preserving statistical characteristics
- Developed **3 production-ready ML models** in Python:
  - Time-series forecasting (Facebook Prophet)
  - Payment type classification (Random Forest, 62.7% accuracy)
  - Station segmentation (K-Means clustering)
- Designed ROI modeling framework projecting **320% ROI** on targeted digital adoption campaigns
- Built and deployed full case study website (HTML/CSS + Tableau Public + GitHub pages)

## Key Findings (Real Launch Data)

**Payment Behavior:**
- **69% cash** vs. 31% digital during launch
- Industry leaders show 70-95% digital adoption (NYC: 70%, London: 95%, Singapore: 98%)

**Station Performance:**
- Top 4 stations generated **44% of all transactions**
- Clear geographic concentration patterns

**Temporal Patterns:**
- Morning peak: 6-8 AM
- Evening peak: 4-6 PM
- Consistent commuter-driven demand

## Machine Learning Extension

> **Note:** To enable advanced modeling, I generated a statistically consistent 6-month synthetic dataset preserving real-world patterns, distributions, and correlations.

### 1. Time-Series Forecasting (Prophet)

**Objective:** Forecast 30-day ridership trends for proactive resource planning

- **Performance:** MAE = 47 transactions/day, RMSE = 64
- **Insight:** Sustained growth trajectory with maintained weekday/weekend patterns
- **Business application:** Capacity planning, staffing optimization, Phase 2 preparation

### 2. Payment Classification (Random Forest)

**Objective:** Predict cash vs. digital payment likelihood based on context

- **Accuracy:** 62.7%
- **Top predictors:**
  1. Days since launch (44% importance)
  2. Station location (28% importance)
  3. Hour of day (25% importance)
- **Strategic insight:** Location-based interventions > time-based campaigns

### 3. Station Segmentation (K-Means)

**Objective:** Identify station clusters for targeted resource allocation

**3 Behavioral Clusters Identified:**

| Cluster | Stations | Digital Adoption | Strategy |
|---------|----------|------------------|----------|
| Digital Leaders | 4 stations | 45.3% | Document best practices |
| Balanced Adopters | 8 stations | 35.3% | Maintain steady growth |
| High-Opportunity | 2 stations | 31.7% | Intensive intervention |

## Resource Allocation & ROI Simulation

**Scenario:** $10,000 digital adoption campaign

**Optimized Budget Allocation:**
- **70% ($7,000)** → 2 high-opportunity stations (264th/BAUER, 296th/AVACADO)
- **20% ($2,000)** → 8 mid-tier stations
- **10% ($1,000)** → Best practice documentation from leaders

**Projected Impact:**
- **320% ROI** (3-month payback)
- **$29,436** annual operational savings
- **1,933** additional digital transactions/month from targeted stations

*ROI modeling uses synthetic data and operational assumptions for methodology demonstration*

## 🛠️ Tools & Technologies

**Data Analysis & ML:**
- Python (Pandas, NumPy, Scikit-learn)
- Facebook Prophet (time-series)
- Matplotlib, Seaborn (visualization)

**Dashboards & Deployment:**
- Tableau Public
- HTML/CSS
- GitHub Pages

**Modeling Techniques:**
- Time-series forecasting
- Classification (Random Forest)
- Unsupervised clustering (K-Means)
- Synthetic data generation

---

## Repository Structure

MetroExpress-BRT-Analytics/
├── data/               # Launch data (anonymized)
├── notebooks/          # Google colab notebooks for EDA & ML
├── images/             # Charts, plots, model outputs
├── dashboards/         # Tableau workbooks
├── website/            # HTML/CSS case study files
├── README.md           # This file
└── requirements.txt    # Python dependencies

## What This Project Demonstrates

**End-to-end analytical ownership** (data → insights → deployment)  
**Applied machine learning** in operational transit context  
**Executive communication** of technical work  
**Strategic resource modeling** with ROI analysis  
**Stakeholder-focused deliverables** (dashboards, case study site)  
**Honest data practices** (transparent about synthetic data use)


## Future Extensions

**Technical:**
- Real-time API integration with DTPW fare systems
- Anomaly detection for equipment failures/fraud
- Automated reporting workflows
- Predictive maintenance for TVMs

**Strategic:**
- A/B testing framework for digital adoption pilots
- Cross-system integration (Metrobus + Metrorail)
- Natural language insight summaries (LLM-powered)
- Network-wide optimization modeling

## Links & Recognition

- [**Live Case Study Website**](https://betsysnchzb.github.io/EpicChallenge_Analysis/)
- [**Featured in Miami-Dade County Newsletter**](https://secure.miamidade.gov/employee/ithrive/archive/dtpw-interns.page)
- [**Tableau Dashboards**]([https://public.tableau.com/app/profile/betsysnchzb)](https://public.tableau.com/app/profile/betsy.sanchez5833/vizzes))


## Acknowledgments

**Team Members (EPIC Internship Phase):**
- Sally Posey
- Anabel Ferreiro Perez

**Client:**
- Miami-Dade County Department of Transportation & Public Works (DTPW)

**Program:**
- EPIC Challenge Micro-Internship (Oct-Nov 2025)


## Contact

**Betsy Sanchez**  
Data Science & Analytics | Machine Learning & Business Intelligence

- Email: BetsySnchzB@gmail.com
- LinkedIn: [linkedin.com/in/betsy-sanchez](https://www.linkedin.com/in/betsy-sanchez-b63780192/)
- GitHub: [github.com/BetsySnchzB](https://github.com/BetsySnchzB)

<div align="center">

** If this project was helpful, please consider giving it a star!**

Made with 💙 by Betsy Sanchez | © 2026

</div>
