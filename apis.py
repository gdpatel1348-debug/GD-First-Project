import requests
import json

class ElectricityMapAPI:
    """Fetch grid carbon intensity relying on https://api.electricitymap.org"""
    def __init__(self, api_key=None):
        self.api_url = "https://api-access.electricitymaps.com/free-tier/carbon-intensity/latest"
        self.api_key = api_key

    def get_carbon_intensity(self, lat, lon):
        if not self.api_key:
            return {"error": "API Key required. Sign up at https://api.electricitymap.org for a free tier key. Provide key via environment variable."}
        
        headers = {'auth-token': self.api_key}
        params = {'lat': lat, 'lon': lon}
        try:
            response = requests.get(self.api_url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

class CarbonInterfaceAPI:
    """Estimates emissions based on various activities relying on https://www.carboninterface.com"""
    def __init__(self, api_key=None):
        self.api_url = "https://www.carboninterface.com/api/v1/estimates"
        self.api_key = api_key

    def estimate_flight_emissions(self, passengers, legs):
        if not self.api_key:
           return {"error": "API Key required. Sign up at https://www.carboninterface.com/ for a free tier key. Extract the Bearer Token."} 
        
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            "type": "flight",
            "passengers": passengers,
            "legs": legs
        }
        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

class OpenWeatherAPI:
    """Fetches real-time weather using https://openweathermap.org/api"""
    def __init__(self, api_key=None):
        self.api_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = api_key

    def get_weather(self, lat, lon):
        if not self.api_key:
           return {"error": "API Key required. Get free key at https://openweathermap.org/api ."} 
        
        params = {'lat': lat, 'lon': lon, 'appid': self.api_key, 'units': 'metric'}
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

class SentinelHubAPI:
    """Satellite data for checking deforestation/environmental impact"""
    def __init__(self, client_id=None, client_secret=None):
        self.auth_url = "https://services.sentinel-hub.com/oauth/token"
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = None

    def authenticate(self):
        if not self.client_id or not self.client_secret:
            return {"error": "Client ID & Secret required. Register at https://www.sentinel-hub.com to get a free trial account."}

        data = {'grant_type': 'client_credentials'}
        try:
            response = requests.post(self.auth_url, data=data, auth=(self.client_id, self.client_secret))
            response.raise_for_status()
            self.token = response.json()['access_token']
            return True
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
            
    def get_satellite_data(self, bbox):
        if not self.token: return self.authenticate()
        return "Authenticated. Fetching specialized satellite tile..." 
