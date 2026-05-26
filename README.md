# sds210-project
Course project in SDS 210 FS26 at GIUZ UZH, about wildfire monitoring in South America.

# Project Title & Description:
In this project, we aim to answer the question of whether wildfires detected in
close spatial proximity are connected through a common origin or represent an expansion during
periods in which no sensor data was acquired. In a second step, the system should be able to identify
and visualize which wildfires expanded the most within a given timeframe.

# Data Sources:
Data source: https://firms.modaps.eosdis.nasa.gov/api/area/ Documentation: https://firms.modaps.eosdis.nasa.gov/active_fire/

# Setup Instructions:
 To run the code, use either the virtual environment (sds-env.yml) or install all required libraries according to requirements.txt.

Before running the code, make sure you have a data folder (with the subfolders raw and processed) and an output folder.

Your project setup should be organized as follows:

 sds210-project/
│── data/
│   ├── raw/
│   └── processed/
│
│── output/ 
│
│── notebooks/
│   ├── API-script.ipynb
│   └── Cleaning-script.ipynb
│   └── Analysis-script.ipynb
│
│── README.md
│── requirements.txt
│── sds-env.yml
│── .gitignore

# Execution Order:
 
 0. Make sure data folders raw & processed are empty!
 1. Decide about adjustable parameter time_window (in API-script.ipynb)
 2. Run API-script.ipynb
 3. Run Cleaning-script.ipynb
 4. Decide about adjustable parameters MAX_DISTANCE_KM & TIME_THRESHOLD (in Analysis-script.ipynb)
 5. Run Analysis-script.ipynb