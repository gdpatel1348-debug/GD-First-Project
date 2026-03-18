# EcoCredit India Platform

EcoCredit is a climate fintech intelligence platform that integrates industrial IoT environmental monitoring, financial data, and verified carbon accounting to generate sustainability-based credit scores. These scores are used by banks, regulators, and carbon markets to incentivize green practices.

## Overview
The platform generates two core scores for factories:
- **Green Credit Score (GCS)**: A sustainability-based credit score (0-100) combining financial health, energy efficiency, water efficiency, and waste recycling. Used for green loan decisions and interest rate discounts.
- **Green Impact Score (GIS)**: Measures the environmental benefit (carbon reduction, water saved, waste diverted) tailored to specific industry baselines.

## Architecture

1. **Frontend**: HTML5, CSS3, Vanilla JS with Chart.js. Uses a Stark Industries/futuristic climate command center dark theme.
2. **Backend**: Python with Flask serving web pages and APIs.
3. **Database**: SQLite (via SQLAlchemy) storing data across 9 distinct modules (Factories, Sensors, Energy, Water, Waste, Carbon, Financial, Scores, Users).
4. **Scoring & AI Engines**: Python classes implementing predictive AI analytics for anomaly detection, GCS/GIS calculation formulas, and Greenhouse Gas (GHG) Protocol carbon accounting.
5. **API Integrations**: Built-in integrations for fetching grid carbon intensity, real-time weather, emissions estimates, and satellite imagery.

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Deployment

1. **Clone/Navigate to the directory:**
   ```bash
   cd "d:\Project fintech\ecocredit_platform"
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv venv
   
   # Windows:
   .\venv\Scripts\activate
   
   # Mac/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```
   *Note: On the first run, the system will automatically seed the SQLite database `ecocredit.db` with sample factory data.*

5. **Access the Dashboards:**
   Open your browser and navigate to:
   - **Command Center:** http://127.0.0.1:5000/
   - **Banker Dashboard:** http://127.0.0.1:5000/bank
   - **Carbon Marketplace:** http://127.0.0.1:5000/marketplace

## External API Integrations & Keys

To use the external integrations in `apis.py`, you will need to obtain free API keys. Update your environment variables or the `apis.py` class initializers with the respective keys once obtained.

1. **ElectricityMap (Carbon Intensity)**
   - **Purpose:** Fetches the carbon intensity of the grid based on factory location.
   - **Get a Free Key:** Sign up at [https://api.electricitymap.org](https://api.electricitymap.org). Select the free tier for non-commercial use to obtain your token.

2. **CarbonInterface (GHG Estimates)**
   - **Purpose:** Provide accurate estimates for flight, shipping, and power emissions.
   - **Get a Free Key:** Register at [https://www.carboninterface.com/](https://www.carboninterface.com/). Extract the Bearer Token from your developer dashboard.

3. **OpenWeather (Real-time Weather Context)**
   - **Purpose:** Fetches current weather telemetry to correlate with environmental sensors (e.g. relating wind/rain to PM2.5 dispersal).
   - **Get a Free Key:** Sign up at [https://openweathermap.org/api](https://openweathermap.org/api) and generate a free API key for the current weather data API.

4. **Sentinel Hub (Satellite Imagery for Reforestation/Deforestation)**
   - **Purpose:** Analyzes satellite data to verify land-use claims.
   - **Get a Free Key:** Create a free trial account at [https://www.sentinel-hub.com](https://www.sentinel-hub.com). Navigate to your dashboard to create an OAuth Client ID and Secret.
