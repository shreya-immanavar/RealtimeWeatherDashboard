# Real-Time Weather Analytics Dashboard

## Project Overview

The Real-Time Weather Analytics Dashboard is a data analytics application that collects, processes, analyzes, and visualizes live weather data using the OpenWeatherMap API.

The project demonstrates the complete data analytics workflow, including API integration, data cleaning, data validation, KPI generation, interactive visualization, filtering, and data export. It is built using Python, Streamlit, and Pandas to provide real-time weather monitoring through a user-friendly dashboard.

## Live Demo

https://realtime-weather-dashboard.streamlit.app/

## GitHub Repository

https://github.com/shreya-immanavar/RealtimeWeatherDashboard

## Features

- Fetches live weather data using the OpenWeatherMap API.
- Automatically refreshes weather information every 60 seconds.
- Cleans and validates incoming weather data.
- Prevents missing values and duplicate records.
- Displays real-time weather metrics including:
  - Temperature
  - Feels Like Temperature
  - Humidity
  - Wind Speed
  - Atmospheric Pressure
  - Visibility
- Provides weather alerts for extreme weather conditions.
- Generates analytical insights from collected weather data.
- Allows filtering by:
  - City
  - Date Range
  - Weather Condition
- Visualizes weather data through interactive charts.
- Maintains historical weather records.
- Supports CSV and Excel data export.

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- OpenWeatherMap API
- OpenPyXL

## Dashboard Components

### Current Weather Dashboard

Displays live weather information including:

- Temperature
- Feels Like Temperature
- Humidity
- Wind Speed
- Pressure
- Visibility
- Current Weather Condition

### Analytics Dashboard

Provides:

- Average Temperature
- Maximum Temperature
- Minimum Temperature
- Average Humidity
- Maximum Wind Speed
- Average Pressure
- Most Frequent Weather Condition

### Visualizations

The dashboard includes:

- Temperature Trend
- Wind Speed Trend
- Humidity Trend
- Weather Condition Distribution
- Daily Temperature Summary

### Smart Insights

Automatically generates insights based on collected weather data, including:

- Average weather statistics
- Humidity analysis
- Dominant weather condition
- Weather alerts

### Data Management

- Automatic data cleaning
- Missing value prevention
- Duplicate removal
- Historical data storage
- CSV Export
- Excel Export

## Project Structure

```
RealTimeWeatherDashboard/
│
├── app.py
├── requirements.txt
├── README.md
├── weather_data.csv
├── .gitignore
└── screenshots/
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/shreya-immanavar/RealtimeWeatherDashboard.git
```

### Navigate to the Project Directory

```bash
cd RealtimeWeatherDashboard
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

## API Configuration

This project uses the OpenWeatherMap API.

Create a free API key from:

https://openweathermap.org/api

Replace the API key in the application:

```python
API_KEY = "YOUR_API_KEY"
```

For deployment, it is recommended to store the API key securely using Streamlit Secrets instead of hardcoding it.

## Screenshots

Add screenshots of the following sections:

- Home Dashboard
- Current Weather Metrics
- Analytics Dashboard
- Weather Charts
- Historical Data Table
- Weather Alerts

Store the images inside the `screenshots` folder.

## Future Enhancements

- Database integration using SQLite or PostgreSQL
- Machine Learning-based weather prediction
- Multi-city weather comparison
- Interactive weather maps
- User authentication
- Weather notification system
- Cloud database integration
- Advanced analytics dashboard

## Author

Shreya Immanavar

GitHub:
https://github.com/shreya-immanavar

Live Application:
https://realtime-weather-dashboard.streamlit.app/
