# Natural Gas Consumption Forecasting Model

Forecasts natural gas consumption using a Grey Model (GM(1,1)) with exponential smoothing. Generates country-specific predictions from 9 years of historical data across 11 countries.

## Features
- Exponential smoothing accumulation for noise reduction
- Least squares parameter estimation (Grey GM(1,1) approach)
- RMSE evaluation against observed data
- Interactive country selection via CLI
- Line plot visualization of observed vs. forecasted values

## Countries Included
Brazil, Bolivia, Denmark, Netherlands, Qatar, Nigeria, Turkmenistan, Brunei, Italy, India, UAE

All values are in billion cubic meters (bcm), covering 2008–2016.

## Requirements
```
numpy
matplotlib
```

## Usage
```
python gas_forecast.py
```
The script will:
1. Prompt you to choose a country
2. Apply the Grey Model to historical consumption data
3. Print observed and predicted values with RMSE
4. Display a forecast plot

## Technical Details
- **Model:** Grey GM(1,1) with exponential smoothing pre-processing
- **Smoothing factor:** 0.59 (adjustable)
- **Parameter estimation:** Ordinary least squares via `numpy.linalg.lstsq`
- **Restoration:** Exponential response function using fitted α and β
- **Evaluation:** Root Mean Squared Error (RMSE)

## Output
The program displays:
- Observed consumption values (2008–2016)
- Model-fitted predictions over the same period
- RMSE score
- Plot comparing observed data (circles) vs. forecasted data (crosses)

## Adjustable Parameters
Modify the smoothing factor when initializing the model:
```python
model = GasConsumptionModel(country_values, smoothing_factor=0.59)
```
- `0` → no smoothing (raw data)
- `1` → maximum smoothing (heavy averaging)

## Limitations
- Short dataset (9 data points per country)
- Predictions fit the training period rather than extrapolating forward
- Assumes exponential growth/decay behavior
- No cross-validation or hyperparameter tuning

## License
MIT
