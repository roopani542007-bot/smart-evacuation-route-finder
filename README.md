# 🚨 SafePath — Smart Evacuation Route Finder

A portfolio-friendly web application that demonstrates how a graph algorithm can find an evacuation route while avoiding hazardous or blocked areas.

## Highlights
- Interactive web interface
- Grid-based hazard map
- Breadth-First Search (BFS)
- Dynamic hazard simulation
- Route length and status display

## Tech Stack
- Python
- Flask
- HTML/CSS
- Data Structures & Algorithms

## Run
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## How to demonstrate
1. Run the project.
2. Explain S = start and A = assembly point.
3. Explain that red cells represent hazards.
4. Enter a row/column to simulate a new hazard.
5. Click **Recalculate Route** and show the changed route.

## Disclaimer
This is an educational simulation, not a real emergency-management system.
