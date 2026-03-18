import random

class GreenScoringEngine:
    def __init__(self):
        # Baseline multipliers by industry
        self.industry_baselines = {
            'textile': {'carbon_weight': 0.3, 'water_weight': 0.6, 'waste_weight': 0.1},
            'steel': {'carbon_weight': 0.7, 'water_weight': 0.1, 'waste_weight': 0.2},
            'default': {'carbon_weight': 0.4, 'water_weight': 0.3, 'waste_weight': 0.3}
        }

    def compute_financial_health_score(self, finance_data):
        # Dummy normalization, high profit, low debt, good credit score = 100
        score = (finance_data.profit / (finance_data.revenue + 1)) * 100
        if finance_data.debt < finance_data.profit:
            score += 20
        score += finance_data.credit_score * 0.1
        return min(max(score, 0), 100)

    def compute_energy_efficiency_score(self, energy_data):
        # High renewable share and low peak demand = 100
        score = energy_data.renewable_share * 100  # Assume 0.0 to 1.0
        return min(max(score, 0), 100)

    def compute_water_efficiency_score(self, water_data):
        # Normal pH and low heavy metals = good
        score = 100
        if water_data.ph < 6 or water_data.ph > 8:
            score -= 30
        if water_data.heavy_metals > 0.5:
            score -= 50
        return min(max(score, 0), 100)

    def compute_waste_recycling_score(self, waste_data):
        return waste_data.recycling_percentage

    def calculate_green_credit_score(self, finance_data, energy_data, water_data, waste_data):
        """
        GCS = 0.40 Financial Health + 0.30 Energy Efficiency + 0.15 Water Efficiency + 
              0.10 Waste Recycling + 0.05 Supply Chain Sustainability
        """
        fin_score = self.compute_financial_health_score(finance_data)
        energy_score = self.compute_energy_efficiency_score(energy_data)
        water_score = self.compute_water_efficiency_score(water_data)
        waste_score = self.compute_waste_recycling_score(waste_data)
        supply_chain_score = 80 # Placeholder logic for supply chain
        
        gcs = (0.40 * fin_score) + (0.30 * energy_score) + \
              (0.15 * water_score) + (0.10 * waste_score) + (0.05 * supply_chain_score)
        
        return round(min(max(gcs, 0), 100), 2)

    def calculate_green_impact_score(self, factory_industry, carbon_saved, water_saved, waste_diverted, total_waste):
        """
        GIS = (Carbon Reduction/Industry Baseline)*weight + 
              (Water Saved/Industry Baseline)*weight + 
              (Waste Diverted/Total Waste)*weight
        """
        weights = self.industry_baselines.get(factory_industry.lower(), self.industry_baselines['default'])
        
        carbon_factor = min(carbon_saved / 1000, 1) # Assumed baseline 1000 tons
        water_factor = min(water_saved / 5000, 1) # Assumed baseline 5000 liters
        waste_factor = (waste_diverted / max(total_waste, 1))

        gis = (carbon_factor * weights['carbon_weight']) + \
              (water_factor * weights['water_weight']) + \
              (waste_factor * weights['waste_weight'])
              
        return round(gis * 100, 2) # Return as 0-100 score

    def calculate_interest_discount(self, gcs):
        """
        Score above 90: interest reduction 0.50%
        Score above 80: interest reduction 0.30%
        Score above 70: interest reduction 0.10%
        """
        if gcs > 90:
            return 0.50
        elif gcs > 80:
            return 0.30
        elif gcs > 70:
            return 0.10
        return 0.0

class CarbonAccountingEngine:
    """Implement GHG protocol calculations (Scopes 1, 2, 3)"""
    def compute_emissions(self, fuel_used, grid_electricity, transportation_miles):
        # Conversion factors (simplified for POC)
        scope1 = fuel_used * 2.3  # kg CO2 per liter diesel
        scope2 = grid_electricity * 0.5  # kg CO2 per kWh (depends on grid mix)
        scope3 = transportation_miles * 0.15 # kg CO2 per mile

        total = scope1 + scope2 + scope3
        return round(scope1, 2), round(scope2, 2), round(scope3, 2), round(total, 2)

class AIAnalyticsEngine:
    """Predictive models for the platform"""
    def predict_emissions_trend(self, historical_emissions):
        # Simple moving average / linear regression placeholder
        if not historical_emissions: return 0
        trend = sum(historical_emissions[-5:]) / 5
        return trend * 1.05 # Forecast 5% increase if business as usual

    def detect_anomalies(self, sensor_reading):
        """Detect pollution spikes"""
        anomalies = []
        if sensor_reading.get('pm25', 0) > 50:
            anomalies.append("High PM2.5 Alert")
        if sensor_reading.get('voc', 0) > 100:
            anomalies.append("High VOC Level Detected")
        return anomalies
