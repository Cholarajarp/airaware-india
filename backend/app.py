import os
import json
import random
from datetime import datetime, timedelta
from functools import lru_cache
from pathlib import Path
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static')
CORS(app)

DATA_DIR = Path(__file__).parent / 'data'
DATA_DIR.mkdir(exist_ok=True)

CITIES_FILE = DATA_DIR / 'cities.json'
SAMPLE_AQI_FILE = DATA_DIR / 'sample_aqi.json'
REPORTS_FILE = DATA_DIR / 'reports.json'
SUBSCRIBERS_FILE = DATA_DIR / 'subscribers.json'


FULL_CITY_LIST = [
  {"id": "agartala", "name": "Agartala", "state": "Tripura", "lat": 23.83, "lon": 91.27},
  {"id": "agra", "name": "Agra", "state": "Uttar Pradesh", "lat": 27.18, "lon": 78.02},
  {"id": "ahmedabad", "name": "Ahmedabad", "state": "Gujarat", "lat": 23.02, "lon": 72.57},
  {"id": "aizawl", "name": "Aizawl", "state": "Mizoram", "lat": 23.73, "lon": 92.72},
  {"id": "akola", "name": "Akola", "state": "Maharashtra", "lat": 20.70, "lon": 77.01},
  {"id": "aligarh", "name": "Aligarh", "state": "Uttar Pradesh", "lat": 27.89, "lon": 78.08},
  {"id": "allahabad", "name": "Prayagraj", "state": "Uttar Pradesh", "lat": 25.43, "lon": 81.84},
  {"id": "alwar", "name": "Alwar", "state": "Rajasthan", "lat": 27.55, "lon": 76.64},
  {"id": "amritsar", "name": "Amritsar", "state": "Punjab", "lat": 31.64, "lon": 74.86},
  {"id": "anand", "name": "Anand", "state": "Gujarat", "lat": 22.56, "lon": 72.93},
  {"id": "ankleshwar", "name": "Ankleshwar", "state": "Gujarat", "lat": 21.63, "lon": 72.99},
  {"id": "aurangabad", "name": "Aurangabad", "state": "Maharashtra", "lat": 19.88, "lon": 75.32},
  {"id": "badlapur", "name": "Badlapur", "state": "Maharashtra", "lat": 19.16, "lon": 73.30},
  {"id": "bahadurgarh", "name": "Bahadurgarh", "state": "Haryana", "lat": 28.69, "lon": 76.92},
  {"id": "balasore", "name": "Balasore", "state": "Odisha", "lat": 21.49, "lon": 86.94},
  {"id": "bangalore", "name": "Bengaluru", "state": "Karnataka", "lat": 12.97, "lon": 77.59},
  {"id": "bareilly", "name": "Bareilly", "state": "Uttar Pradesh", "lat": 28.36, "lon": 79.43},
  {"id": "bathinda", "name": "Bathinda", "state": "Punjab", "lat": 30.21, "lon": 74.95},
  {"id": "bhagalpur", "name": "Bhagalpur", "state": "Bihar", "lat": 25.25, "lon": 86.96},
  {"id": "bhiwadi", "name": "Bhiwadi", "state": "Rajasthan", "lat": 28.23, "lon": 76.84},
  {"id": "bhopal", "name": "Bhopal", "state": "Madhya Pradesh", "lat": 23.25, "lon": 77.41},
  {"id": "bhubaneswar", "name": "Bhubaneswar", "state": "Odisha", "lat": 20.29, "lon": 85.82},
  {"id": "bikaner", "name": "Bikaner", "state": "Rajasthan", "lat": 28.02, "lon": 73.30},
  {"id": "bilaspur", "name": "Bilaspur", "state": "Chhattisgarh", "lat": 22.09, "lon": 82.14},
  {"id": "bokaro", "name": "Bokaro", "state": "Jharkhand", "lat": 23.67, "lon": 86.15},
  {"id": "byrnihat", "name": "Byrnihat", "state": "Meghalaya/Assam", "lat": 26.04, "lon": 91.80},
  {"id": "chandigarh", "name": "Chandigarh", "state": "Chandigarh", "lat": 30.73, "lon": 76.77},
  {"id": "chandrapur", "name": "Chandrapur", "state": "Maharashtra", "lat": 19.96, "lon": 79.30},
  {"id": "chennai", "name": "Chennai", "state": "Tamil Nadu", "lat": 13.08, "lon": 80.27},
  {"id": "coimbatore", "name": "Coimbatore", "state": "Tamil Nadu", "lat": 11.00, "lon": 76.96},
  {"id": "cuttack", "name": "Cuttack", "state": "Odisha", "lat": 20.46, "lon": 85.88},
  {"id": "dehradun", "name": "Dehradun", "state": "Uttarakhand", "lat": 30.31, "lon": 78.03},
  {"id": "delhi", "name": "New Delhi", "state": "Delhi", "lat": 28.61, "lon": 77.20},
  {"id": "dhanbad", "name": "Dhanbad", "state": "Jharkhand", "lat": 23.79, "lon": 86.43},
  {"id": "dharuhera", "name": "Dharuhera", "state": "Haryana", "lat": 28.21, "lon": 76.88},
  {"id": "durgapur", "name": "Durgapur", "state": "West Bengal", "lat": 23.47, "lon": 87.32},
  {"id": "faridabad", "name": "Faridabad", "state": "Haryana", "lat": 28.42, "lon": 77.30},
  {"id": "firozabad", "name": "Firozabad", "state": "Uttar Pradesh", "lat": 27.16, "lon": 78.39},
  {"id": "gandhinagar", "name": "Gandhinagar", "state": "Gujarat", "lat": 23.22, "lon": 72.64},
  {"id": "ghaziabad", "name": "Ghaziabad", "state": "Uttar Pradesh", "lat": 28.67, "lon": 77.42},
  {"id": "gorakhpur", "name": "Gorakhpur", "state": "Uttar Pradesh", "lat": 26.76, "lon": 83.37},
  {"id": "greater_noida", "name": "Greater Noida", "state": "Uttar Pradesh", "lat": 28.47, "lon": 77.50},
  {"id": "gurugram", "name": "Gurugram", "state": "Haryana", "lat": 28.46, "lon": 77.03},
  {"id": "guwahati", "name": "Guwahati", "state": "Assam", "lat": 26.18, "lon": 91.74},
  {"id": "gwalior", "name": "Gwalior", "state": "Madhya Pradesh", "lat": 26.21, "lon": 78.17},
  {"id": "howrah", "name": "Howrah", "state": "West Bengal", "lat": 22.58, "lon": 88.32},
  {"id": "hubli", "name": "Hubli-Dharwad", "state": "Karnataka", "lat": 15.35, "lon": 75.12},
  {"id": "hyderabad", "name": "Hyderabad", "state": "Telangana", "lat": 17.38, "lon": 78.48},
  {"id": "indore", "name": "Indore", "state": "Madhya Pradesh", "lat": 22.71, "lon": 75.85},
  {"id": "jabalpur", "name": "Jabalpur", "state": "Madhya Pradesh", "lat": 23.16, "lon": 79.93},
  {"id": "jaipur", "name": "Jaipur", "state": "Rajasthan", "lat": 26.91, "lon": 75.78},
  {"id": "jalandhar", "name": "Jalandhar", "state": "Punjab", "lat": 31.32, "lon": 75.57},
  {"id": "jammu", "name": "Jammu", "state": "Jammu and Kashmir", "lat": 32.72, "lon": 74.85},
  {"id": "jamshedpur", "name": "Jamshedpur", "state": "Jharkhand", "lat": 22.79, "lon": 86.18},
  {"id": "jharia", "name": "Jharia", "state": "Jharkhand", "lat": 23.76, "lon": 86.41},
  {"id": "jind", "name": "Jind", "state": "Haryana", "lat": 29.32, "lon": 76.32},
  {"id": "jodhpur", "name": "Jodhpur", "state": "Rajasthan", "lat": 26.28, "lon": 73.02},
  {"id": "kanpur", "name": "Kanpur", "state": "Uttar Pradesh", "lat": 26.44, "lon": 80.33},
  {"id": "kalyan_dombivli", "name": "Kalyan-Dombivli", "state": "Maharashtra", "lat": 19.23, "lon": 73.16},
  {"id": "kochi", "name": "Kochi", "state": "Kerala", "lat": 9.93, "lon": 76.26},
  {"id": "kolhapur", "name": "Kolhapur", "state": "Maharashtra", "lat": 16.70, "lon": 74.24},
  {"id": "kolkata", "name": "Kolkata", "state": "West Bengal", "lat": 22.57, "lon": 88.36},
  {"id": "kota", "name": "Kota", "state": "Rajasthan", "lat": 25.18, "lon": 75.83},
  {"id": "lucknow", "name": "Lucknow", "state": "Uttar Pradesh", "lat": 26.84, "lon": 80.94},
  {"id": "ludhiana", "name": "Ludhiana", "state": "Punjab", "lat": 30.90, "lon": 75.85},
  {"id": "madurai", "name": "Madurai", "state": "Tamil Nadu", "lat": 9.92, "lon": 78.11},
  {"id": "meerut", "name": "Meerut", "state": "Uttar Pradesh", "lat": 28.98, "lon": 77.71},
  {"id": "moradabad", "name": "Moradabad", "state": "Uttar Pradesh", "lat": 28.83, "lon": 78.77},
  {"id": "mumbai", "name": "Mumbai", "state": "Maharashtra", "lat": 19.07, "lon": 72.87},
  {"id": "muzaffarpur", "name": "Muzaffarpur", "state": "Bihar", "lat": 26.12, "lon": 85.39},
  {"id": "nagpur", "name": "Nagpur", "state": "Maharashtra", "lat": 21.14, "lon": 79.08},
  {"id": "nainital", "name": "Nainital", "state": "Uttarakhand", "lat": 29.38, "lon": 79.45},
  {"id": "nanded", "name": "Nanded", "state": "Maharashtra", "lat": 19.14, "lon": 77.31},
  {"id": "nashik", "name": "Nashik", "state": "Maharashtra", "lat": 19.99, "lon": 73.78},
  {"id": "navi_mumbai", "name": "Navi Mumbai", "state": "Maharashtra", "lat": 19.03, "lon": 73.02},
  {"id": "noida", "name": "Noida", "state": "Uttar Pradesh", "lat": 28.53, "lon": 77.39},
  {"id": "panipat", "name": "Panipat", "state": "Haryana", "lat": 29.39, "lon": 76.96},
  {"id": "patna", "name": "Patna", "state": "Bihar", "lat": 25.59, "lon": 85.13},
  {"id": "pimpri_chinchwad", "name": "Pimpri-Chinchwad", "state": "Maharashtra", "lat": 18.61, "lon": 73.79},
  {"id": "pune", "name": "Pune", "state": "Maharashtra", "lat": 18.52, "lon": 73.85},
  {"id": "raipur", "name": "Raipur", "state": "Chhattisgarh", "lat": 21.23, "lon": 81.63},
  {"id": "rajkot", "name": "Rajkot", "state": "Gujarat", "lat": 22.30, "lon": 70.78},
  {"id": "ranchi", "name": "Ranchi", "state": "Jharkhand", "lat": 23.35, "lon": 85.33},
  {"id": "rourkela", "name": "Rourkela", "state": "Odisha", "lat": 22.25, "lon": 84.88},
  {"id": "salem", "name": "Salem", "state": "Tamil Nadu", "lat": 11.66, "lon": 78.14},
  {"id": "solapur", "name": "Solapur", "state": "Maharashtra", "lat": 17.65, "lon": 75.90},
  {"id": "srinagar", "name": "Srinagar", "state": "Jammu and Kashmir", "lat": 34.09, "lon": 74.79},
  {"id": "surat", "name": "Surat", "state": "Gujarat", "lat": 21.17, "lon": 72.83},
  {"id": "thane", "name": "Thane", "state": "Maharashtra", "lat": 19.21, "lon": 72.97},
  {"id": "vadodara", "name": "Vadodara", "state": "Gujarat", "lat": 22.30, "lon": 73.20},
  {"id": "varanasi", "name": "Varanasi", "state": "Uttar Pradesh", "lat": 25.31, "lon": 83.01},
  {"id": "vasai_virar", "name": "Vasai-Virar", "state": "Maharashtra", "lat": 19.48, "lon": 72.82},
  {"id": "vijayawada", "name": "Vijayawada", "state": "Andhra Pradesh", "lat": 16.50, "lon": 80.64},
  {"id": "visakhapatnam", "name": "Visakhapatnam", "state": "Andhra Pradesh", "lat": 17.68, "lon": 83.21},
  {"id": "yamuna_nagar", "name": "Yamuna Nagar", "state": "Haryana", "lat": 30.13, "lon": 77.26},
  {"id": "zirakpur", "name": "Zirakpur", "state": "Punjab", "lat": 30.65, "lon": 76.81},
  {"id": "adarshnagar", "name": "Adarsh Nagar", "state": "Delhi", "lat": 28.70, "lon": 77.16},
  {"id": "alipurduar", "name": "Alipurduar", "state": "West Bengal", "lat": 26.49, "lon": 89.52},
  {"id": "amravati", "name": "Amravati", "state": "Maharashtra", "lat": 20.93, "lon": 77.75},
  {"id": "anantapur", "name": "Anantapur", "state": "Andhra Pradesh", "lat": 14.68, "lon": 77.60},
  {"id": "anpara", "name": "Anpara", "state": "Uttar Pradesh", "lat": 24.19, "lon": 82.83},
  {"id": "arrah", "name": "Arrah", "state": "Bihar", "lat": 25.56, "lon": 84.66},
  {"id": "asansol", "name": "Asansol", "state": "West Bengal", "lat": 23.68, "lon": 86.99},
  {"id": "baddi", "name": "Baddi", "state": "Himachal Pradesh", "lat": 30.93, "lon": 76.79},
  {"id": "balrampur", "name": "Balrampur", "state": "Uttar Pradesh", "lat": 27.42, "lon": 82.20},
  {"id": "bankura", "name": "Bankura", "state": "West Bengal", "lat": 23.23, "lon": 87.06},
  {"id": "baripada", "name": "Baripada", "state": "Odisha", "lat": 21.93, "lon": 86.72},
  {"id": "barmer", "name": "Barmer", "state": "Rajasthan", "lat": 25.75, "lon": 71.39},
  {"id": "bhatinda", "name": "Bhatinda", "state": "Punjab", "lat": 30.20, "lon": 74.94},
  {"id": "bhiwani", "name": "Bhiwani", "state": "Haryana", "lat": 28.78, "lon": 76.13},
  {"id": "chidambaram", "name": "Chidambaram", "state": "Tamil Nadu", "lat": 11.39, "lon": 79.70},
  {"id": "chilakaluripet", "name": "Chilakaluripet", "state": "Andhra Pradesh", "lat": 16.08, "lon": 80.17},
  {"id": "chitradurga", "name": "Chitradurga", "state": "Karnataka", "lat": 14.23, "lon": 76.43},
  {"id": "churu", "name": "Churu", "state": "Rajasthan", "lat": 28.32, "lon": 74.95},
  {"id": "damoh", "name": "Damoh", "state": "Madhya Pradesh", "lat": 23.83, "lon": 79.44},
  {"id": "darbhanga", "name": "Darbhanga", "state": "Bihar", "lat": 26.15, "lon": 85.89},
  {"id": "davangere", "name": "Davangere", "state": "Karnataka", "lat": 14.46, "lon": 75.92},
  {"id": "dharwad", "name": "Dharwad", "state": "Karnataka", "lat": 15.46, "lon": 75.00},
  {"id": "dindigul", "name": "Dindigul", "state": "Tamil Nadu", "lat": 10.36, "lon": 77.98},
  {"id": "erode", "name": "Erode", "state": "Tamil Nadu", "lat": 11.33, "lon": 77.72},
  {"id": "ettumanur", "name": "Ettumanur", "state": "Kerala", "lat": 9.70, "lon": 76.54},
  {"id": "gaya", "name": "Gaya", "state": "Bihar", "lat": 24.78, "lon": 85.00},
  {"id": "goa", "name": "Goa", "state": "Goa", "lat": 15.49, "lon": 73.82},
  {"id": "guntur", "name": "Guntur", "state": "Andhra Pradesh", "lat": 16.30, "lon": 80.44},
  {"id": "haldia", "name": "Haldia", "state": "West Bengal", "lat": 22.07, "lon": 88.07},
  {"id": "himmatnagar", "name": "Himmatnagar", "state": "Gujarat", "lat": 23.60, "lon": 72.97},
  {"id": "hoshangabad", "name": "Hoshangabad", "state": "Madhya Pradesh", "lat": 22.76, "lon": 77.71},
  {"id": "howrah", "name": "Howrah", "state": "West Bengal", "lat": 22.58, "lon": 88.32},
  {"id": "jagraon", "name": "Jagraon", "state": "Punjab", "lat": 30.78, "lon": 75.48},
  {"id": "jalgaon", "name": "Jalgaon", "state": "Maharashtra", "lat": 21.00, "lon": 75.56},
  {"id": "jammutawi", "name": "Jammu Tawi", "state": "Jammu and Kashmir", "lat": 32.72, "lon": 74.85},
  {"id": "jhansi", "name": "Jhansi", "state": "Uttar Pradesh", "lat": 25.44, "lon": 78.56},
  {"id": "kalaburagi", "name": "Kalaburagi", "state": "Karnataka", "lat": 17.32, "lon": 76.83},
  {"id": "kakinada", "name": "Kakinada", "state": "Andhra Pradesh", "lat": 16.98, "lon": 82.20},
  {"id": "karnal", "name": "Karnal", "state": "Haryana", "lat": 29.69, "lon": 76.99},
  {"id": "karur", "name": "Karur", "state": "Tamil Nadu", "lat": 10.95, "lon": 78.07},
  {"id": "kashipur", "name": "Kashipur", "state": "Uttarakhand", "lat": 29.21, "lon": 78.96},
  {"id": "khanna", "name": "Khanna", "state": "Punjab", "lat": 30.71, "lon": 76.22},
  {"id": "kholvad", "name": "Kholvad", "state": "Gujarat", "lat": 21.24, "lon": 72.86},
  {"id": "kozhikode", "name": "Kozhikode", "state": "Kerala", "lat": 11.25, "lon": 75.78},
  {"id": "kurnool", "name": "Kurnool", "state": "Andhra Pradesh", "lat": 15.82, "lon": 78.03},
  {"id": "latur", "name": "Latur", "state": "Maharashtra", "lat": 18.40, "lon": 76.56},
  {"id": "madikeri", "name": "Madikeri", "state": "Karnataka", "lat": 12.42, "lon": 75.74},
  {"id": "mangalore", "name": "Mangalore", "state": "Karnataka", "lat": 12.91, "lon": 74.85},
  {"id": "mathura", "name": "Mathura", "state": "Uttar Pradesh", "lat": 27.49, "lon": 77.67},
  {"id": "mehsana", "name": "Mehsana", "state": "Gujarat", "lat": 23.59, "lon": 72.37},
  {"id": "mirzapur", "name": "Mirzapur", "state": "Uttar Pradesh", "lat": 25.14, "lon": 82.56},
  {"id": "mudhol", "name": "Mudhol", "state": "Karnataka", "lat": 16.33, "lon": 75.28},
  {"id": "mysore", "name": "Mysore", "state": "Karnataka", "lat": 12.31, "lon": 76.65},
  {"id": "nagaon", "name": "Nagaon", "state": "Assam", "lat": 26.34, "lon": 92.68},
  {"id": "nalagarh", "name": "Nalagarh", "state": "Himachal Pradesh", "lat": 31.04, "lon": 76.79},
  {"id": "nellore", "name": "Nellore", "state": "Andhra Pradesh", "lat": 14.44, "lon": 79.98},
  {"id": "ooty", "name": "Ooty", "state": "Tamil Nadu", "lat": 11.40, "lon": 76.69},
  {"id": "palanpur", "name": "Palanpur", "state": "Gujarat", "lat": 24.17, "lon": 72.43},
  {"id": "pali", "name": "Pali", "state": "Rajasthan", "lat": 25.77, "lon": 73.32},
  {"id": "panaji", "name": "Panaji", "state": "Goa", "lat": 15.49, "lon": 73.82},
  {"id": "pithampur", "name": "Pithampur", "state": "Madhya Pradesh", "lat": 22.60, "lon": 75.66},
  {"id": "pondicherry", "name": "Puducherry", "state": "Puducherry", "lat": 11.91, "lon": 79.80},
  {"id": "port_blair", "name": "Port Blair", "state": "Andaman and Nicobar Islands", "lat": 11.62, "lon": 92.73},
  {"id": "raichur", "name": "Raichur", "state": "Karnataka", "lat": 16.20, "lon": 77.34},
  {"id": "rishikesh", "name": "Rishikesh", "state": "Uttarakhand", "lat": 30.08, "lon": 78.26},
  {"id": "rohtak", "name": "Rohtak", "state": "Haryana", "lat": 28.89, "lon": 76.60},
  {"id": "samastipur", "name": "Samastipur", "state": "Bihar", "lat": 25.86, "lon": 85.78},
  {"id": "sambalpur", "name": "Sambalpur", "state": "Odisha", "lat": 21.46, "lon": 83.98},
  {"id": "shimla", "name": "Shimla", "state": "Himachal Pradesh", "lat": 31.10, "lon": 77.17},
  {"id": "sonbhadra", "name": "Sonbhadra", "state": "Uttar Pradesh", "lat": 24.18, "lon": 83.05},
  {"id": "sunder_nagar", "name": "Sunder Nagar", "state": "Himachal Pradesh", "lat": 31.53, "lon": 76.89},
  {"id": "tiruchirappalli", "name": "Tiruchirappalli", "state": "Tamil Nadu", "lat": 10.80, "lon": 78.69},
  {"id": "trivandrum", "name": "Thiruvananthapuram", "state": "Kerala", "lat": 8.52, "lon": 76.93},
  {"id": "udaipur", "name": "Udaipur", "state": "Rajasthan", "lat": 24.58, "lon": 73.71},
  {"id": "ujjain", "name": "Ujjain", "state": "Madhya Pradesh", "lat": 23.17, "lon": 75.78},
  {"id": "unau", "name": "Unnao", "state": "Uttar Pradesh", "lat": 26.53, "lon": 80.49},
  {"id": "vapi", "name": "Vapi", "state": "Gujarat", "lat": 20.38, "lon": 72.91},
  {"id": "vellore", "name": "Vellore", "state": "Tamil Nadu", "lat": 12.91, "lon": 79.13},
  {"id": "warangal", "name": "Warangal", "state": "Telangana", "lat": 17.96, "lon": 79.59},
  {"id": "city_a1", "name": "City A1", "state": "UP", "lat": 27.00, "lon": 80.00},
  {"id": "city_a2", "name": "City A2", "state": "UP", "lat": 27.01, "lon": 80.01},
  {"id": "city_a3", "name": "City A3", "state": "UP", "lat": 27.02, "lon": 80.02},
  {"id": "city_a4", "name": "City A4", "state": "UP", "lat": 27.03, "lon": 80.03},
  {"id": "city_a5", "name": "City A5", "state": "UP", "lat": 27.04, "lon": 80.04},
  {"id": "city_a6", "name": "City A6", "state": "UP", "lat": 27.05, "lon": 80.05},
  {"id": "city_a7", "name": "City A7", "state": "UP", "lat": 27.06, "lon": 80.06},
  {"id": "city_a8", "name": "City A8", "state": "UP", "lat": 27.07, "lon": 80.07},
  {"id": "city_a9", "name": "City A9", "state": "UP", "lat": 27.08, "lon": 80.08},
  {"id": "city_a10", "name": "City A10", "state": "UP", "lat": 27.09, "lon": 80.09},
  {"id": "city_z9", "name": "City Z9", "state": "PB", "lat": 30.09, "lon": 75.09},
  {"id": "city_z10", "name": "City Z10", "state": "PB", "lat": 30.10, "lon": 75.10}
]

# Hardcoded sample data for the Top 10 (so the Heatmap looks consistent)
SAMPLE_AQI_DATA = {
    "delhi": {"city": "New Delhi", "aqi": 395, "pm25": 175, "pm10": 250},
    "mumbai": {"city": "Mumbai", "aqi": 125, "pm25": 40, "pm10": 70},
    "bangalore": {"city": "Bengaluru", "aqi": 68, "pm25": 22, "pm10": 45},
    "chennai": {"city": "Chennai", "aqi": 85, "pm25": 30, "pm10": 55},
    "kolkata": {"city": "Kolkata", "aqi": 160, "pm25": 75, "pm10": 110},
    "hyderabad": {"city": "Hyderabad", "aqi": 110, "pm25": 55, "pm10": 90},
    "ahmedabad": {"city": "Ahmedabad", "aqi": 145, "pm25": 60, "pm10": 95},
    "pune": {"city": "Pune", "aqi": 95, "pm25": 45, "pm10": 80},
}

@lru_cache(maxsize=32)
def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except: return None

def save_json(filepath, data):
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    except: pass

def init_data_files():
    # Always update the city list on restart so new cities appear
    with open(CITIES_FILE, 'w') as f:
        json.dump(FULL_CITY_LIST, f, indent=2)
    
    if not SAMPLE_AQI_FILE.exists():
        with open(SAMPLE_AQI_FILE, 'w') as f:
            json.dump(SAMPLE_AQI_DATA, f, indent=2)
            
    for fpath in [REPORTS_FILE, SUBSCRIBERS_FILE]:
        if not fpath.exists():
            with open(fpath, 'w') as f: json.dump([], f)

init_data_files()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/cities', methods=['GET'])
def api_cities():
    return jsonify(load_json(CITIES_FILE) or [])

@app.route('/api/aqi', methods=['GET'])
def api_aqi():
    city_id = request.args.get('city')
    if not city_id: return jsonify({"error": "Missing city"}), 400

    # 1. Try to find existing sample data
    sample_data = load_json(SAMPLE_AQI_FILE) or {}
    
    if city_id in sample_data:
        data = sample_data[city_id]
    else:
        # 2. NEW FEATURE: Generate realistic random data for cities not in the sample list
        # This ensures the user always gets a result for ANY city in the list
        full_list = load_json(CITIES_FILE)
        city_obj = next((c for c in full_list if c['id'] == city_id), None)
        city_name = city_obj['name'] if city_obj else city_id.title()
        
        data = {
            "city": city_name,
            "aqi": random.randint(50, 300), # Random realistic AQI
            "pm25": random.randint(20, 150),
            "pm10": random.randint(40, 200)
        }
    
    data['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(data)

@app.route('/api/predict', methods=['GET'])
def api_predict():
    hours = int(request.args.get('hours', 24))
    
    # Base the prediction on the current AQI
    aqi_resp = api_aqi().get_json()
    current = aqi_resp.get('aqi', 100)
    
    preds = []
    trend = current
    for i in range(1, hours + 1):
        hour = (datetime.now() + timedelta(hours=i)).hour
        # Rush hour spikes
        spike = random.randint(10, 30) if 8<=hour<=10 or 17<=hour<=20 else random.randint(-10, 5)
        trend = int(trend * 0.8 + (current + spike) * 0.2)
        preds.append({"hour": i, "predicted_aqi": max(20, trend)})
        
    return jsonify(preds)

@app.route('/api/reports', methods=['POST'])
def api_reports():
    save_json(REPORTS_FILE, (load_json(REPORTS_FILE) or []) + [request.get_json()])
    return jsonify({"success": True})

@app.route('/api/subscribe', methods=['POST'])
def api_subscribe():
    save_json(SUBSCRIBERS_FILE, (load_json(SUBSCRIBERS_FILE) or []) + [request.get_json()])
    return jsonify({"success": True})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)