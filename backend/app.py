import os
import json
import random
from datetime import datetime, timedelta
from functools import lru_cache
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_cors import CORS
from dotenv import load_dotenv

# --- Configuration and Initialization ---
load_dotenv()

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
CORS(app)

# Ensure data directory exists
DATA_DIR = Path(__file__).parent / 'data'
DATA_DIR.mkdir(exist_ok=True)

CITIES_FILE = DATA_DIR / 'cities.json'
SAMPLE_AQI_FILE = DATA_DIR / 'sample_aqi.json'
REPORTS_FILE = DATA_DIR / 'reports.json'
SUBSCRIBERS_FILE = DATA_DIR / 'subscribers.json'

# --- FIX 1: Top 15 Major Cities Defined Explicitly at the top ---
FULL_CITY_LIST = [
    {"id": "delhi", "name": "New Delhi", "state": "Delhi", "lat": 28.6139, "lon": 77.2090},
    {"id": "mumbai", "name": "Mumbai", "state": "Maharashtra", "lat": 19.0760, "lon": 72.8777},
    {"id": "bangalore", "name": "Bengaluru", "state": "Karnataka", "lat": 12.9716, "lon": 77.5946},
    {"id": "chennai", "name": "Chennai", "state": "Tamil Nadu", "lat": 13.0827, "lon": 80.2707},
    {"id": "kolkata", "name": "Kolkata", "state": "West Bengal", "lat": 22.5726, "lon": 88.3639},
    {"id": "hyderabad", "name": "Hyderabad", "state": "Telangana", "lat": 17.3850, "lon": 78.4867},
    {"id": "ahmedabad", "name": "Ahmedabad", "state": "Gujarat", "lat": 23.0225, "lon": 72.5714},
    {"id": "pune", "name": "Pune", "state": "Maharashtra", "lat": 18.5204, "lon": 73.8567},
    {"id": "jaipur", "name": "Jaipur", "state": "Rajasthan", "lat": 26.9124, "lon": 75.7873},
    {"id": "lucknow", "name": "Lucknow", "state": "Uttar Pradesh", "lat": 26.8467, "lon": 80.9462},
    {"id": "kanpur", "name": "Kanpur", "state": "Uttar Pradesh", "lat": 26.4499, "lon": 80.3319},
    {"id": "nagpur", "name": "Nagpur", "state": "Maharashtra", "lat": 21.1458, "lon": 79.0882},
    {"id": "indore", "name": "Indore", "state": "Madhya Pradesh", "lat": 22.7196, "lon": 75.8577},
    {"id": "thane", "name": "Thane", "state": "Maharashtra", "lat": 19.2183, "lon": 72.9781},
    {"id": "bhopal", "name": "Bhopal", "state": "Madhya Pradesh", "lat": 23.2599, "lon": 77.4126},
    # Add more cities here for the search functionality to find
    {"id": "patna", "name": "Patna", "state": "Bihar", "lat": 25.5941, "lon": 85.1376},
    {"id": "visakhapatnam", "name": "Visakhapatnam", "state": "Andhra Pradesh", "lat": 17.6868, "lon": 83.2185},
    {"id": "kochi", "name": "Kochi", "state": "Kerala", "lat": 9.9312, "lon": 76.2673},
]

# Corresponding Sample Data for the Top 15 (to ensure Heatmap isn't empty)
SAMPLE_AQI_DATA = {
    "delhi": {"city": "New Delhi", "aqi": 395, "pm25": 175, "pm10": 250, "o3": 60, "no2": 70},
    "mumbai": {"city": "Mumbai", "aqi": 125, "pm25": 40, "pm10": 70, "o3": 65, "no2": 30},
    "bangalore": {"city": "Bengaluru", "aqi": 68, "pm25": 22, "pm10": 45, "o3": 40, "no2": 25},
    "chennai": {"city": "Chennai", "aqi": 85, "pm25": 30, "pm10": 55, "o3": 45, "no2": 20},
    "kolkata": {"city": "Kolkata", "aqi": 160, "pm25": 75, "pm10": 110, "o3": 50, "no2": 40},
    "hyderabad": {"city": "Hyderabad", "aqi": 110, "pm25": 55, "pm10": 90, "o3": 42, "no2": 35},
    "ahmedabad": {"city": "Ahmedabad", "aqi": 145, "pm25": 60, "pm10": 95, "o3": 55, "no2": 45},
    "pune": {"city": "Pune", "aqi": 95, "pm25": 45, "pm10": 80, "o3": 48, "no2": 28},
    "jaipur": {"city": "Jaipur", "aqi": 180, "pm25": 85, "pm10": 130, "o3": 58, "no2": 50},
    "lucknow": {"city": "Lucknow", "aqi": 210, "pm25": 95, "pm10": 160, "o3": 62, "no2": 55},
    "kanpur": {"city": "Kanpur", "aqi": 220, "pm25": 100, "pm10": 170, "o3": 65, "no2": 60},
    "nagpur": {"city": "Nagpur", "aqi": 105, "pm25": 50, "pm10": 85, "o3": 45, "no2": 30},
    "indore": {"city": "Indore", "aqi": 130, "pm25": 58, "pm10": 92, "o3": 52, "no2": 38},
    "thane": {"city": "Thane", "aqi": 115, "pm25": 38, "pm10": 65, "o3": 60, "no2": 32},
    "bhopal": {"city": "Bhopal", "aqi": 140, "pm25": 62, "pm10": 98, "o3": 54, "no2": 42},
    "patna": {"city": "Patna", "aqi": 250, "pm25": 120, "pm10": 190, "o3": 70, "no2": 65},
    "visakhapatnam": {"city": "Visakhapatnam", "aqi": 75, "pm25": 28, "pm10": 50, "o3": 35, "no2": 18},
    "kochi": {"city": "Kochi", "aqi": 55, "pm25": 18, "pm10": 40, "o3": 30, "no2": 15},
}

@lru_cache(maxsize=32)
def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_json(filepath, data):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False

def init_data_files():
    """Initializes local JSON files with the explicit Top 15 data."""
    # Always overwrite cities.json to ensure the order is correct
    with open(CITIES_FILE, 'w') as f:
        json.dump(FULL_CITY_LIST, f, indent=2)

    if not SAMPLE_AQI_FILE.exists():
        with open(SAMPLE_AQI_FILE, 'w') as f:
            json.dump(SAMPLE_AQI_DATA, f, indent=2)
            
    for filename in [REPORTS_FILE, SUBSCRIBERS_FILE]:
        if not filename.exists():
            with open(filename, 'w') as f:
                json.dump([], f)

# Initialize files on startup
init_data_files()

# --- ROUTES ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cities', methods=['GET'])
def api_cities():
    cities = load_json(CITIES_FILE)
    return jsonify(cities or [])

@app.route('/api/aqi', methods=['GET'])
def api_aqi():
    city_id = request.args.get('city')
    if not city_id:
        return jsonify({"error": "Missing city parameter"}), 400

    # Fallback to Sample Data
    sample_data = load_json(SAMPLE_AQI_FILE)
    if sample_data and city_id in sample_data:
        aqi_data = sample_data[city_id]
        aqi_data['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return jsonify(aqi_data)
    
    return jsonify({"error": "AQI data not found"}), 404

@app.route('/api/predict', methods=['GET'])
def api_predict():
    """Generates a 24-hour forecast curve based on logic."""
    city_id = request.args.get('city')
    hours = int(request.args.get('hours', 24))
    
    # Get current AQI base
    aqi_resp = api_aqi().get_json()
    current_aqi = aqi_resp.get('aqi', 150) if 'error' not in aqi_resp else 150
    
    predictions = []
    current_trend = current_aqi
    
    for i in range(1, hours + 1):
        future_time = datetime.now() + timedelta(hours=i)
        hour_of_day = future_time.hour
        
        # Logic: Pollution spikes in morning (8-10am) and evening (6-9pm)
        shift = 0
        if 8 <= hour_of_day <= 10: shift = random.randint(10, 25)
        elif 18 <= hour_of_day <= 21: shift = random.randint(15, 30)
        elif 2 <= hour_of_day <= 5: shift = random.randint(-20, -5) # Clears up at night
        else: shift = random.randint(-5, 5)
        
        current_trend = (current_trend * 0.7) + ((current_aqi + shift) * 0.3)
        predictions.append({"hour": i, "predicted_aqi": int(current_trend)})
        
    return jsonify(predictions)

@app.route('/api/reports', methods=['POST'])
def api_reports():
    data = request.get_json()
    reports = load_json(REPORTS_FILE) or []
    reports.append({
        "timestamp": datetime.now().isoformat(),
        "city": data.get('city'),
        "location": data.get('location'),
        "message": data.get('message')
    })
    save_json(REPORTS_FILE, reports)
    return jsonify({"success": True})

@app.route('/api/subscribe', methods=['POST'])
def api_subscribe():
    data = request.get_json()
    subs = load_json(SUBSCRIBERS_FILE) or []
    subs.append({
        "timestamp": datetime.now().isoformat(),
        "name": data.get('name'),
        "phone": data.get('phone_or_whatsapp'),
        "city": data.get('city')
    })
    save_json(SUBSCRIBERS_FILE, subs)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)