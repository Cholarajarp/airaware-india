# 🌬️ AirAware India

AirAware India provides real-time AQI data, safe time recommendations, and shareable alerts via a single-file, mobile-first web interface powered by a Python Flask backend.

## Features
* **Single-File Frontend:** Optimized performance with all HTML, CSS, and JS contained in one `index.html`.
* **Python Flask Backend:** Simple, RESTful API endpoints for data handling and logic.
* **Multi-Language Support:** Instant switching between English and Hindi.
* **PWA Ready:** Installable on mobile and desktop, with offline functionality via Service Worker.
* **Safe Time Logic:** Provides explicit recommendations (e.g., "Best time: After 6 PM") based on AQI.
* **Community Reporting:** Allows users to submit local air quality reports.
* **Offline Fallback:** Uses static JSON data if external APIs are unavailable.

## Quick Start: Local Run Instructions

This project uses a standard Python/Flask structure.

### 1. Setup Environment
```powershell
# Create the project directory (if needed)
cd C:\Users\cchol\Downloads\AirQuality\airaware-india\backend

# Create virtual environment
python -m venv venv

# Install dependencies (no activation required)
.\venv\Scripts\pip.exe install -r requirements.txt
```

### 2. Configure Optional AQI API
The application is designed to work fully offline using `data/sample_aqi.json`. To enable live data fetching, create a file named `.env` inside the `backend/` directory and add your API credentials:

```text
# .env file inside backend/
AQI_API_KEY=your_live_api_key_here
AQI_API_URL=https://api.example.com/v1/latest/
```

### 3. Run the Application
```powershell
.\venv\Scripts\python.exe app.py
```

Open your browser to: http://localhost:5000

Project File Layout
```
airaware-india/
├── backend/
│  ├─ app.py
│  ├─ requirements.txt
│  ├─ .env (optional)
│  ├─ data/
│  │  ├─ cities.json
│  │  ├─ sample_aqi.json
│  │  ├─ reports.json  (generated on first run)
│  │  └─ subscribers.json (generated on first run)
│  ├─ templates/
│  │  └─ index.html
│  └─ static/
│     ├─ sw.js
│     └─ manifest.json
└── README.md
```

Deployment to Free Tiers (Render / Railway)
Both Render and Railway support Python Flask apps easily.

Host on GitHub: Push this entire airaware-india directory to a GitHub repository.

Choose a Platform: Select Render or Railway.

Connect Repository: Create a new Web Service and link it to your GitHub repo.

Configure:

Root Directory: Set the root directory to `backend/` (where `app.py` and `requirements.txt` are).

Build Command: `pip install -r requirements.txt`

Start Command: `python app.py` (or `gunicorn app:app` for production).

Environment Variables: Add `AQI_API_KEY` and `AQI_API_URL` to the platform's environment settings if you use a live API.

Contributing
Contributions are highly encouraged to make this tool a robust public resource!

Adding More Cities
Edit the `backend/data/cities.json` file. The city id should be lowercase and hyphenated (e.g., guwahati).

Implementing Live API
If you implement a specific live API (like OpenAQ, AccuWeather, etc.), update the logic inside the `api_aqi()` function in `backend/app.py` and ensure the `normalize_aqi_data()` helper converts the response to the required application format.

Privacy Notice
No Third-Party Tracking: This application does not use external analytics or tracking tools.

Local Data Storage: Subscriber and report data is stored locally in JSON files (`subscribers.json`, `reports.json`). This data is not shared, but it is viewable by anyone with server access. For true public use, a database should replace these files.

WhatsApp Share: The share function uses the native `wa.me` URL scheme and does not track user activity.
