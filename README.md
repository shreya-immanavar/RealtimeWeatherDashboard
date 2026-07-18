# Real-Time Weather Analytics Dashboard

## Project Overview
This project is a professional-grade Data Analytics Dashboard built to monitor, process, and visualize real-time weather data. It is designed to demonstrate full-stack data analytics capabilities, from API data extraction and rigorous cleaning to advanced visualization and smart business insights. 

## Features
- **Real-Time Data Streaming:** Fetches live weather conditions via the OpenWeatherMap API with a 60-second auto-refresh.
- **Robust Data Processing:** Implements strict data cleaning, missing value handling, and type coercion.
- **Data Quality Tracking:** Monitors and displays total records, missing values prevented, and duplicates removed.
- **Smart Business Insights:** Automatically generates text-based insights (e.g., averages, extreme conditions) based on the dataset.
- **Advanced Filtering:** Interactively filter data by City, Date Range, and Weather Condition.
- **Professional Analytics:** Calculates and displays KPI metrics such as Min/Max/Avg for Temperature, Humidity, and Wind Speed.
- **Data Export:** Download the fully processed dataset in both `.csv` and Excel `.xlsx` formats.

## Technologies Used
- **Python:** Core programming language.
- **Streamlit:** Framework for building the interactive web application.
- **Pandas:** Used for robust data manipulation, cleaning, and structuring.
- **Requests:** Used for fetching JSON data from external APIs.
- **OpenWeatherMap API:** The real-time data source.

## Installation Steps
1. Clone this repository to your local machine.
2. Ensure you have Python 3 installed.
3. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

## API Information
This project utilizes the [OpenWeatherMap API](https://openweathermap.org/api). 
To use your own API key:
1. Sign up on the OpenWeatherMap website to get a free API key.
2. Open `app.py` and replace the `API_KEY` variable with your unique key.

## How to Run
After installing the dependencies, start the Streamlit server by running the following command in your terminal:
```bash
streamlit run app.py
```
The dashboard will automatically open in your default web browser.

## Folder Structure
```text
RealTimeWeatherDashboard/
│
├── app.py                 # Main Streamlit application script
├── requirements.txt       # List of Python dependencies
├── README.md              # Project documentation
├── weather_data.csv       # Automatically generated local database
└── screenshots/           # Folder for dashboard UI screenshots
```

## Screenshots Section
*(Drop screenshots of the live dashboard, data quality section, and analytics charts here before submitting your internship project)*

## Future Improvements
- **Database Integration:** Migrate from CSV storage to a robust SQL database (e.g., PostgreSQL or SQLite) for handling massive datasets.
- **Predictive Analytics:** Integrate Scikit-Learn to forecast temperature trends based on historical data.
- **Multi-City Comparison:** Allow users to search and compare multiple cities side-by-side simultaneously.
