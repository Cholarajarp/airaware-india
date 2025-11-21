import json
import random
from pathlib import Path
from datetime import datetime

DATA_DIR = Path(__file__).parent.parent / 'data'
CITIES_FILE = DATA_DIR / 'cities.json'
SAMPLE_AQI_FILE = DATA_DIR / 'sample_aqi.json'

def load_cities():
    {
  "agartala": {"city": "Agartala", "aqi": 75, "pm25": 28, "pm10": 50, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "agra": {"city": "Agra", "aqi": 215, "pm25": 105, "pm10": 170, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "ahmedabad": {"city": "Ahmedabad", "aqi": 165, "pm25": 75, "pm10": 110, "o3": 60, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "aizawl": {"city": "Aizawl", "aqi": 48, "pm25": 15, "pm10": 30, "o3": 25, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "akola": {"city": "Akola", "aqi": 125, "pm25": 50, "pm10": 80, "o3": 45, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "aligarh": {"city": "Aligarh", "aqi": 250, "pm25": 110, "pm10": 160, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "allahabad": {"city": "Prayagraj", "aqi": 290, "pm25": 125, "pm10": 180, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "alwar": {"city": "Alwar", "aqi": 310, "pm25": 135, "pm10": 190, "o3": 60, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "amritsar": {"city": "Amritsar", "aqi": 188, "pm25": 85, "pm10": 130, "o3": 52, "no2": 48, "last_updated": "2025-11-21 13:00:00"},
  "anand": {"city": "Anand", "aqi": 115, "pm25": 48, "pm10": 72, "o3": 44, "no2": 36, "last_updated": "2025-11-21 13:00:00"},
  "ankleshwar": {"city": "Ankleshwar", "aqi": 140, "pm25": 60, "pm10": 90, "o3": 45, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "aurangabad": {"city": "Aurangabad", "aqi": 90, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "badlapur": {"city": "Badlapur", "aqi": 105, "pm25": 40, "pm10": 65, "o3": 42, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "bahadurgarh": {"city": "Bahadurgarh", "aqi": 345, "pm25": 155, "pm10": 210, "o3": 62, "no2": 68, "last_updated": "2025-11-21 13:00:00"},
  "balasore": {"city": "Balasore", "aqi": 98, "pm25": 38, "pm10": 62, "o3": 41, "no2": 29, "last_updated": "2025-11-21 13:00:00"},
  "bangalore": {"city": "Bengaluru", "aqi": 68, "pm25": 22, "pm10": 45, "o3": 40, "no2": 25, "last_updated": "2025-11-21 13:00:00"},
  "bareilly": {"city": "Bareilly", "aqi": 220, "pm25": 100, "pm10": 150, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "bathinda": {"city": "Bathinda", "aqi": 260, "pm25": 115, "pm10": 170, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "bhagalpur": {"city": "Bhagalpur", "aqi": 195, "pm25": 90, "pm10": 140, "o3": 55, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "bhiwadi": {"city": "Bhiwadi", "aqi": 360, "pm25": 165, "pm10": 240, "o3": 60, "no2": 70, "last_updated": "2025-11-21 13:00:00"},
  "bhopal": {"city": "Bhopal", "aqi": 155, "pm25": 65, "pm10": 100, "o3": 50, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "bhubaneswar": {"city": "Bhubaneswar", "aqi": 75, "pm25": 28, "pm10": 50, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "bikaner": {"city": "Bikaner", "aqi": 195, "pm25": 90, "pm10": 140, "o3": 55, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "bilaspur": {"city": "Bilaspur", "aqi": 180, "pm25": 78, "pm10": 120, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "bokaro": {"city": "Bokaro", "aqi": 145, "pm25": 60, "pm10": 95, "o3": 48, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "byrnihat": {"city": "Byrnihat", "aqi": 450, "pm25": 200, "pm10": 300, "o3": 70, "no2": 80, "last_updated": "2025-11-21 13:00:00"},
  "chandigarh": {"city": "Chandigarh", "aqi": 140, "pm25": 60, "pm10": 90, "o3": 45, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "chandrapur": {"city": "Chandrapur", "aqi": 225, "pm25": 105, "pm10": 155, "o3": 58, "no2": 52, "last_updated": "2025-11-21 13:00:00"},
  "chennai": {"city": "Chennai", "aqi": 85, "pm25": 25, "pm10": 55, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "coimbatore": {"city": "Coimbatore", "aqi": 52, "pm25": 16, "pm10": 35, "o3": 30, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "cuttack": {"city": "Cuttack", "aqi": 122, "pm25": 48, "pm10": 78, "o3": 45, "no2": 33, "last_updated": "2025-11-21 13:00:00"},
  "dehradun": {"city": "Dehradun", "aqi": 102, "pm25": 40, "pm10": 65, "o3": 42, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "delhi": {"city": "New Delhi", "aqi": 395, "pm25": 175, "pm10": 250, "o3": 60, "no2": 70, "last_updated": "2025-11-21 13:00:00"},
  "dhanbad": {"city": "Dhanbad", "aqi": 305, "pm25": 130, "pm10": 185, "o3": 60, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "dharuhera": {"city": "Dharuhera", "aqi": 380, "pm25": 170, "pm10": 240, "o3": 65, "no2": 72, "last_updated": "2025-11-21 13:00:00"},
  "durgapur": {"city": "Durgapur", "aqi": 160, "pm25": 70, "pm10": 105, "o3": 50, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "faridabad": {"city": "Faridabad", "aqi": 340, "pm25": 160, "pm10": 220, "o3": 62, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "firozabad": {"city": "Firozabad", "aqi": 270, "pm25": 120, "pm10": 170, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "gandhinagar": {"city": "Gandhinagar", "aqi": 80, "pm25": 30, "pm10": 55, "o3": 40, "no2": 25, "last_updated": "2025-11-21 13:00:00"},
  "ghaziabad": {"city": "Ghaziabad", "aqi": 420, "pm25": 190, "pm10": 280, "o3": 65, "no2": 75, "last_updated": "2025-11-21 13:00:00"},
  "gorakhpur": {"city": "Gorakhpur", "aqi": 230, "pm25": 105, "pm10": 155, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "greater_noida": {"city": "Greater Noida", "aqi": 405, "pm25": 180, "pm10": 250, "o3": 68, "no2": 78, "last_updated": "2025-11-21 13:00:00"},
  "gurugram": {"city": "Gurugram", "aqi": 385, "pm25": 175, "pm10": 245, "o3": 65, "no2": 75, "last_updated": "2025-11-21 13:00:00"},
  "guwahati": {"city": "Guwahati", "aqi": 110, "pm25": 45, "pm10": 75, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "gwalior": {"city": "Gwalior", "aqi": 255, "pm25": 110, "pm10": 160, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "howrah": {"city": "Howrah", "aqi": 175, "pm25": 75, "pm10": 110, "o3": 52, "no2": 48, "last_updated": "2025-11-21 13:00:00"},
  "hubli": {"city": "Hubli-Dharwad", "aqi": 88, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "hyderabad": {"city": "Hyderabad", "aqi": 105, "pm25": 35, "pm10": 65, "o3": 45, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "indore": {"city": "Indore", "aqi": 130, "pm25": 55, "pm10": 85, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "jabalpur": {"city": "Jabalpur", "aqi": 98, "pm25": 38, "pm10": 62, "o3": 41, "no2": 29, "last_updated": "2025-11-21 13:00:00"},
  "jaipur": {"city": "Jaipur", "aqi": 280, "pm25": 100, "pm10": 160, "o3": 58, "no2": 52, "last_updated": "2025-11-21 13:00:00"},
  "jalandhar": {"city": "Jalandhar", "aqi": 205, "pm25": 95, "pm10": 145, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "jammu": {"city": "Jammu", "aqi": 165, "pm25": 70, "pm10": 110, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "jamshedpur": {"city": "Jamshedpur", "aqi": 115, "pm25": 48, "pm10": 72, "o3": 44, "no2": 36, "last_updated": "2025-11-21 13:00:00"},
  "jharia": {"city": "Jharia", "aqi": 460, "pm25": 210, "pm10": 320, "o3": 70, "no2": 85, "last_updated": "2025-11-21 13:00:00"},
  "jind": {"city": "Jind", "aqi": 370, "pm25": 165, "pm10": 230, "o3": 65, "no2": 70, "last_updated": "2025-11-21 13:00:00"},
  "jodhpur": {"city": "Jodhpur", "aqi": 180, "pm25": 78, "pm10": 120, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "kanpur": {"city": "Kanpur", "aqi": 310, "pm25": 135, "pm10": 190, "o3": 60, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "kalyan_dombivli": {"city": "Kalyan-Dombivli", "aqi": 145, "pm25": 60, "pm10": 95, "o3": 48, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "kochi": {"city": "Kochi", "aqi": 45, "pm25": 15, "pm10": 30, "o3": 30, "no2": 18, "last_updated": "2025-11-21 13:00:00"},
  "kolhapur": {"city": "Kolhapur", "aqi": 90, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "kolkata": {"city": "Kolkata", "aqi": 185, "pm25": 70, "pm10": 110, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "kota": {"city": "Kota", "aqi": 260, "pm25": 115, "pm10": 170, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "lucknow": {"city": "Lucknow", "aqi": 350, "pm25": 150, "pm10": 200, "o3": 65, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "ludhiana": {"city": "Ludhiana", "aqi": 240, "pm25": 105, "pm10": 155, "o3": 58, "no2": 52, "last_updated": "2025-11-21 13:00:00"},
  "madurai": {"city": "Madurai", "aqi": 60, "pm25": 20, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "meerut": {"city": "Meerut", "aqi": 360, "pm25": 165, "pm10": 240, "o3": 60, "no2": 70, "last_updated": "2025-11-21 13:00:00"},
  "moradabad": {"city": "Moradabad", "aqi": 305, "pm25": 130, "pm10": 185, "o3": 60, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "mumbai": {"city": "Mumbai", "aqi": 125, "pm25": 40, "pm10": 70, "o3": 65, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "muzaffarpur": {"city": "Muzaffarpur", "aqi": 285, "pm25": 120, "pm10": 175, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "nagpur": {"city": "Nagpur", "aqi": 108, "pm25": 42, "pm10": 70, "o3": 45, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "nainital": {"city": "Nainital", "aqi": 55, "pm25": 18, "pm10": 35, "o3": 32, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "nanded": {"city": "Nanded", "aqi": 95, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "nashik": {"city": "Nashik", "aqi": 88, "pm25": 30, "pm10": 55, "o3": 40, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "navi_mumbai": {"city": "Navi Mumbai", "aqi": 95, "pm25": 35, "pm10": 60, "o3": 42, "no2": 32, "last_updated": "2025-11-21 13:00:00"},
  "noida": {"city": "Noida", "aqi": 410, "pm25": 185, "pm10": 260, "o3": 64, "no2": 72, "last_updated": "2025-11-21 13:00:00"},
  "panipat": {"city": "Panipat", "aqi": 320, "pm25": 140, "pm10": 195, "o3": 60, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "patna": {"city": "Patna", "aqi": 312, "pm25": 130, "pm10": 190, "o3": 55, "no2": 58, "last_updated": "2025-11-21 13:00:00"},
  "pimpri_chinchwad": {"city": "Pimpri-Chinchwad", "aqi": 92, "pm25": 38, "pm10": 60, "o3": 41, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "pune": {"city": "Pune", "aqi": 95, "pm25": 30, "pm10": 60, "o3": 42, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "raipur": {"city": "Raipur", "aqi": 145, "pm25": 60, "pm10": 95, "o3": 48, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "rajkot": {"city": "Rajkot", "aqi": 120, "pm25": 45, "pm10": 75, "o3": 45, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "ranchi": {"city": "Ranchi", "aqi": 118, "pm25": 50, "pm10": 70, "o3": 42, "no2": 33, "last_updated": "2025-11-21 13:00:00"},
  "rourkela": {"city": "Rourkela", "aqi": 150, "pm25": 65, "pm10": 100, "o3": 50, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "salem": {"city": "Salem", "aqi": 62, "pm25": 20, "pm10": 45, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "solapur": {"city": "Solapur", "aqi": 112, "pm25": 45, "pm10": 75, "o3": 45, "no2": 32, "last_updated": "2025-11-21 13:00:00"},
  "srinagar": {"city": "Srinagar", "aqi": 78, "pm25": 28, "pm10": 55, "o3": 38, "no2": 25, "last_updated": "2025-11-21 13:00:00"},
  "surat": {"city": "Surat", "aqi": 135, "pm25": 55, "pm10": 85, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "thane": {"city": "Thane", "aqi": 140, "pm25": 60, "pm10": 90, "o3": 45, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "vadodara": {"city": "Vadodara", "aqi": 128, "pm25": 50, "pm10": 80, "o3": 45, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "varanasi": {"city": "Varanasi", "aqi": 330, "pm25": 140, "pm10": 195, "o3": 60, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "vasai_virar": {"city": "Vasai-Virar", "aqi": 118, "pm25": 48, "pm10": 75, "o3": 44, "no2": 36, "last_updated": "2025-11-21 13:00:00"},
  "vijayawada": {"city": "Vijayawada", "aqi": 98, "pm25": 38, "pm10": 62, "o3": 41, "no2": 29, "last_updated": "2025-11-21 13:00:00"},
  "visakhapatnam": {"city": "Visakhapatnam", "aqi": 55, "pm25": 18, "pm10": 35, "o3": 32, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "yamuna_nagar": {"city": "Yamuna Nagar", "aqi": 305, "pm25": 130, "pm10": 185, "o3": 60, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "zirakpur": {"city": "Zirakpur", "aqi": 170, "pm25": 75, "pm10": 110, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "adarshnagar": {"city": "Adarsh Nagar", "aqi": 380, "pm25": 170, "pm10": 240, "o3": 65, "no2": 72, "last_updated": "2025-11-21 13:00:00"},
  "alipurduar": {"city": "Alipurduar", "aqi": 85, "pm25": 30, "pm10": 55, "o3": 40, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "amravati": {"city": "Amravati", "aqi": 130, "pm25": 55, "pm10": 85, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "anantapur": {"city": "Anantapur", "aqi": 65, "pm25": 22, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "anpara": {"city": "Anpara", "aqi": 400, "pm25": 180, "pm10": 250, "o3": 68, "no2": 75, "last_updated": "2025-11-21 13:00:00"},
  "arrah": {"city": "Arrah", "aqi": 320, "pm25": 140, "pm10": 195, "o3": 60, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "asansol": {"city": "Asansol", "aqi": 185, "pm25": 80, "pm10": 120, "o3": 52, "no2": 48, "last_updated": "2025-11-21 13:00:00"},
  "baddi": {"city": "Baddi", "aqi": 190, "pm25": 85, "pm10": 130, "o3": 52, "no2": 48, "last_updated": "2025-11-21 13:00:00"},
  "balrampur": {"city": "Balrampur", "aqi": 270, "pm25": 120, "pm10": 170, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "bankura": {"city": "Bankura", "aqi": 155, "pm25": 65, "pm10": 100, "o3": 50, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "baripada": {"city": "Baripada", "aqi": 90, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "barmer": {"city": "Barmer", "aqi": 210, "pm25": 95, "pm10": 145, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "bhatinda": {"city": "Bhatinda", "aqi": 260, "pm25": 115, "pm10": 170, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "bhiwani": {"city": "Bhiwani", "aqi": 300, "pm25": 125, "pm10": 180, "o3": 60, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "chidambaram": {"city": "Chidambaram", "aqi": 50, "pm25": 15, "pm10": 30, "o3": 25, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "chilakaluripet": {"city": "Chilakaluripet", "aqi": 88, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "chitradurga": {"city": "Chitradurga", "aqi": 72, "pm25": 25, "pm10": 45, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "churu": {"city": "Churu", "aqi": 340, "pm25": 150, "pm10": 200, "o3": 65, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "damoh": {"city": "Damoh", "aqi": 110, "pm25": 45, "pm10": 75, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "darbhanga": {"city": "Darbhanga", "aqi": 295, "pm25": 125, "pm10": 180, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "davangere": {"city": "Davangere", "aqi": 85, "pm25": 30, "pm10": 55, "o3": 40, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "dharwad": {"city": "Dharwad", "aqi": 88, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "dindigul": {"city": "Dindigul", "aqi": 70, "pm25": 25, "pm10": 45, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "erode": {"city": "Erode", "aqi": 68, "pm25": 22, "pm10": 45, "o3": 40, "no2": 25, "last_updated": "2025-11-21 13:00:00"},
  "ettumanur": {"city": "Ettumanur", "aqi": 42, "pm25": 15, "pm10": 30, "o3": 25, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "gaya": {"city": "Gaya", "aqi": 305, "pm25": 130, "pm10": 185, "o3": 60, "no2": 60, "last_updated": "2025-11-21 13:00:00"},
  "goa": {"city": "Goa", "aqi": 50, "pm25": 15, "pm10": 30, "o3": 25, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "guntur": {"city": "Guntur", "aqi": 92, "pm25": 38, "pm10": 60, "o3": 41, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "haldia": {"city": "Haldia", "aqi": 160, "pm25": 70, "pm10": 105, "o3": 50, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "himmatnagar": {"city": "Himmatnagar", "aqi": 108, "pm25": 42, "pm10": 70, "o3": 45, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "hoshangabad": {"city": "Hoshangabad", "aqi": 115, "pm25": 48, "pm10": 72, "o3": 44, "no2": 36, "last_updated": "2025-11-21 13:00:00"},
  "howrah": {"city": "Howrah", "aqi": 175, "pm25": 75, "pm10": 110, "o3": 52, "no2": 48, "last_updated": "2025-11-21 13:00:00"},
  "jagraon": {"city": "Jagraon", "aqi": 210, "pm25": 95, "pm10": 145, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "jalgaon": {"city": "Jalgaon", "aqi": 135, "pm25": 55, "pm10": 85, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "jammutawi": {"city": "Jammu Tawi", "aqi": 165, "pm25": 70, "pm10": 110, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "jhansi": {"city": "Jhansi", "aqi": 200, "pm25": 90, "pm10": 140, "o3": 55, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "kalaburagi": {"city": "Kalaburagi", "aqi": 82, "pm25": 30, "pm10": 55, "o3": 40, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "kakinada": {"city": "Kakinada", "aqi": 75, "pm25": 28, "pm10": 50, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "karnal": {"city": "Karnal", "aqi": 365, "pm25": 170, "pm10": 240, "o3": 62, "no2": 70, "last_updated": "2025-11-21 13:00:00"},
  "karur": {"city": "Karur", "aqi": 60, "pm25": 20, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "kashipur": {"city": "Kashipur", "aqi": 120, "pm25": 45, "pm10": 75, "o3": 45, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "khanna": {"city": "Khanna", "aqi": 250, "pm25": 110, "pm10": 160, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "kholvad": {"city": "Kholvad", "aqi": 155, "pm25": 65, "pm10": 100, "o3": 50, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "kozhikode": {"city": "Kozhikode", "aqi": 58, "pm25": 20, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "kurnool": {"city": "Kurnool", "aqi": 85, "pm25": 30, "pm10": 55, "o3": 40, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "latur": {"city": "Latur", "aqi": 110, "pm25": 45, "pm10": 75, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "madikeri": {"city": "Madikeri", "aqi": 40, "pm25": 12, "pm10": 25, "o3": 20, "no2": 10, "last_updated": "2025-11-21 13:00:00"},
  "mangalore": {"city": "Mangalore", "aqi": 70, "pm25": 25, "pm10": 45, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "mathura": {"city": "Mathura", "aqi": 280, "pm25": 125, "pm10": 175, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "mehsana": {"city": "Mehsana", "aqi": 130, "pm25": 55, "pm10": 85, "o3": 48, "no2": 38, "last_updated": "2025-11-21 13:00:00"},
  "mirzapur": {"city": "Mirzapur", "aqi": 340, "pm25": 160, "pm10": 220, "o3": 62, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "mudhol": {"city": "Mudhol", "aqi": 92, "pm25": 38, "pm10": 60, "o3": 41, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "mysore": {"city": "Mysore", "aqi": 75, "pm25": 28, "pm10": 50, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "nagaon": {"city": "Nagaon", "aqi": 105, "pm25": 40, "pm10": 65, "o3": 42, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "nalagarh": {"city": "Nalagarh", "aqi": 180, "pm25": 78, "pm10": 120, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "nellore": {"city": "Nellore", "aqi": 90, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "ooty": {"city": "Ooty", "aqi": 35, "pm25": 10, "pm10": 20, "o3": 20, "no2": 10, "last_updated": "2025-11-21 13:00:00"},
  "palanpur": {"city": "Palanpur", "aqi": 118, "pm25": 48, "pm10": 75, "o3": 44, "no2": 36, "last_updated": "2025-11-21 13:00:00"},
  "pali": {"city": "Pali", "aqi": 265, "pm25": 115, "pm10": 170, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "panaji": {"city": "Panaji", "aqi": 60, "pm25": 20, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "pithampur": {"city": "Pithampur", "aqi": 140, "pm25": 60, "pm10": 90, "o3": 45, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "pondicherry": {"city": "Puducherry", "aqi": 65, "pm25": 22, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "port_blair": {"city": "Port Blair", "aqi": 38, "pm25": 10, "pm10": 20, "o3": 20, "no2": 10, "last_updated": "2025-11-21 13:00:00"},
  "raichur": {"city": "Raichur", "aqi": 95, "pm25": 35, "pm10": 60, "o3": 40, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "rishikesh": {"city": "Rishikesh", "aqi": 88, "pm25": 30, "pm10": 55, "o3": 40, "no2": 28, "last_updated": "2025-11-21 13:00:00"},
  "rohtak": {"city": "Rohtak", "aqi": 355, "pm25": 160, "pm10": 230, "o3": 62, "no2": 68, "last_updated": "2025-11-21 13:00:00"},
  "samastipur": {"city": "Samastipur", "aqi": 290, "pm25": 125, "pm10": 180, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "sambalpur": {"city": "Sambalpur", "aqi": 150, "pm25": 65, "pm10": 100, "o3": 50, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "shimla": {"city": "Shimla", "aqi": 45, "pm25": 15, "pm10": 30, "o3": 25, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "sonbhadra": {"city": "Sonbhadra", "aqi": 410, "pm25": 185, "pm10": 260, "o3": 64, "no2": 72, "last_updated": "2025-11-21 13:00:00"},
  "sunder_nagar": {"city": "Sunder Nagar", "aqi": 98, "pm25": 38, "pm10": 62, "o3": 41, "no2": 29, "last_updated": "2025-11-21 13:00:00"},
  "tiruchirappalli": {"city": "Tiruchirappalli", "aqi": 60, "pm25": 20, "pm10": 40, "o3": 35, "no2": 20, "last_updated": "2025-11-21 13:00:00"},
  "trivandrum": {"city": "Thiruvananthapuram", "aqi": 48, "pm25": 15, "pm10": 30, "o3": 25, "no2": 15, "last_updated": "2025-11-21 13:00:00"},
  "udaipur": {"city": "Udaipur", "aqi": 140, "pm25": 60, "pm10": 90, "o3": 45, "no2": 40, "last_updated": "2025-11-21 13:00:00"},
  "ujjain": {"city": "Ujjain", "aqi": 118, "pm25": 48, "pm10": 75, "o3": 44, "no2": 36, "last_updated": "2025-11-21 13:00:00"},
  "unau": {"city": "Unnao", "aqi": 325, "pm25": 140, "pm10": 195, "o3": 60, "no2": 65, "last_updated": "2025-11-21 13:00:00"},
  "vapi": {"city": "Vapi", "aqi": 170, "pm25": 75, "pm10": 110, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "vellore": {"city": "Vellore", "aqi": 75, "pm25": 28, "pm10": 50, "o3": 38, "no2": 22, "last_updated": "2025-11-21 13:00:00"},
  "warangal": {"city": "Warangal", "aqi": 105, "pm25": 40, "pm10": 65, "o3": 42, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "city_a1": {"city": "City A1", "aqi": 150, "pm25": 65, "pm10": 100, "o3": 50, "no2": 35, "last_updated": "2025-11-21 13:00:00"},
  "city_a2": {"city": "City A2", "aqi": 180, "pm25": 78, "pm10": 120, "o3": 50, "no2": 45, "last_updated": "2025-11-21 13:00:00"},
  "city_a3": {"city": "City A3", "aqi": 210, "pm25": 95, "pm10": 145, "o3": 55, "no2": 50, "last_updated": "2025-11-21 13:00:00"},
  "city_a4": {"city": "City A4", "aqi": 250, "pm25": 110, "pm10": 160, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "city_a5": {"city": "City A5", "aqi": 290, "pm25": 125, "pm10": 180, "o3": 58, "no2": 55, "last_updated": "2025-11-21 13:00:00"},
  "city_z9": {"city": "City Z9", "aqi": 120, "pm25": 45, "pm10": 75, "o3": 45, "no2": 30, "last_updated": "2025-11-21 13:00:00"},
  "city_z10": {"city": "City Z10", "aqi": 155, "pm25": 65, "pm10": 100, "o3": 50, "no2": 35, "last_updated": "2025-11-21 13:00:00"}
}
    try:
        with open(CITIES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"CRITICAL: {CITIES_FILE} not found. Run generate_cities.py first.")
        return []

def generate_sample_aqi(cities):
    """Generates synthetic AQI data for all cities."""
    sample_data = {}
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create_aqi_profile(city_name):
        # High Pollution Zones
        if any(keyword in city_name for keyword in ["Delhi", "Noida", "Ghaziabad", "Kanpur", "Lucknow", "Patna", "Meerut"]):
            aqi_base = random.randint(300, 450)
        elif any(keyword in city_name for keyword in ["Mumbai", "Kolkata", "Chennai", "Jaipur", "Ahmedabad"]):
            aqi_base = random.randint(120, 200)
        elif any(keyword in city_name for keyword in ["Kochi", "Ooty", "Shimla", "Aizawl", "Port Blair"]):
            aqi_base = random.randint(30, 80)
        else:
            aqi_base = random.randint(80, 280)
        pm25 = int(aqi_base * random.uniform(0.4, 0.5))
        pm10 = int(aqi_base * random.uniform(0.6, 0.7))
        o3 = random.randint(30, 70)
        no2 = random.randint(30, 70)
        return {
            "city": city_name,
            "aqi": aqi_base,
            "pm25": pm25,
            "pm10": pm10,
            "o3": o3,
            "no2": no2,
            "last_updated": now
        }
    for city in cities:
        sample_data[city['id']] = create_aqi_profile(city['name'])
    return sample_data

def save_aqi_file(sample_data):
    """Writes the generated AQI data to sample_aqi.json."""
    try:
        with open(SAMPLE_AQI_FILE, 'w', encoding='utf-8') as f:
            json.dump(sample_data, f, indent=2, ensure_ascii=False)
        print(f"✅ Successfully generated sample AQI for {len(sample_data)} cities in {SAMPLE_AQI_FILE}")
    except Exception as e:
        print(f"❌ Failed to write {SAMPLE_AQI_FILE}: {e}")

if __name__ == '__main__':
    cities = load_cities()
    if not cities:
        print("Cannot proceed. Please run 'python generate_cities.py' first.")
    else:
        sample_data = generate_sample_aqi(cities)
        save_aqi_file(sample_data)
