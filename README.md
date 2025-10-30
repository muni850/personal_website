# Muni Sundaram - Personal Portfolio

This is a Flask portfolio website built for Muni Sundaram.

## Run locally
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Place your profile image at `static/profile.svg` (or replace with your own).
3. Run:
   ```
   python app.py
   ```
4. Open `http://localhost:5000`

## Docker
```
docker build -t muni-portfolio .
docker run -p 5000:5000 muni-portfolio
```

## Deploy
Deploy from GitHub to Render (connect repo, choose Python, start command `python app.py`).
