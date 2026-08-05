# InsiderGuard
<img width="1907" height="917" alt="insiderguard_dashboard" src="https://github.com/user-attachments/assets/4a650a62-4bc0-4289-b366-fab91fd40d73" />

## Overview

InsiderGuard is a User and Entity
Behavior Analytics system designed
to detect unusual user activity.

## Features

- User behavior profiling
- Anomaly detection
- Risk scoring
- Alert generation
- Security dashboard

## Technologies

Python
Pandas
Scikit-learn
Streamlit
SQLite

## Installation

pip install -r requirements.txt

## Run

python src/generate_logs.py

python src/detector.py

python src/risk_engine.py

streamlit run src/dashboard.py

## Screenshots

<img width="1908" height="916" alt="insiderguard_soc_dashboard" src="https://github.com/user-attachments/assets/ba9c7e55-192c-454b-8672-cd0bb6dc6886" />

## Future Improvements

- Real-time log collection
- Email alerts
- Splunk integration
- MITRE ATT&CK mapping
- User authentication
