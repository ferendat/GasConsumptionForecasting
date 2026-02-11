Natural Gas Consumption Forecast Model

Forecasts national natural gas consumption using a smoothing-based accumulation model with least squares parameter estimation. Generates predicted values, calculates RMSE, and visualizes observed vs forecasted data.

Features

Smoothing-based accumulation modeling
Least squares parameter estimation (alpha, beta)
Consumption restoration using exponential response function
RMSE performance evaluation
Matplotlib visualization of observed vs predicted data
Interactive country selection

Requirements

numpy
matplotlib

Usage
python gas_forecast.py


The script will:

Prompt user to select a country

Fit the forecasting model

Output observed values

Output predicted values

Compute RMSE

Display consumption forecast plot

Technical Details

Model: Accumulation-based exponential forecasting
Parameter estimation: Linear least squares (NumPy)
Smoothing factor: Configurable (default 0.59)
Dataset length: 9 annual observations per country
Evaluation metric: Root Mean Squared Error (RMSE)
Visualization: Matplotlib line plot

Dataset

Countries included:

Brazil, Bolivia, Denmark, Netherlands, Qatar, Nigeria,
Turkmenistan, Brunei, Italy, India, UAE

Units: Billion cubic meters (bcm)

Time range: Starting from 2008 (9 consecutive years)

Model Workflow

Accumulate raw time-series data using smoothing

Estimate parameters (alpha, beta) via regression

Restore predicted values

Evaluate accuracy with RMSE

Plot results

Output

Console: Observed data, predicted data, RMSE

Graph: Observed vs forecasted consumption
