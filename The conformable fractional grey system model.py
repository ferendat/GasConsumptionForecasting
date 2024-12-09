import numpy as np
import matplotlib.pyplot as plt

# Data representing natural gas consumption across different countries
country_data = {
    "Brazil": [14, 11.9, 14.6, 16.7, 19.3, 21.3, 22.7, 23.1, 23.5],
    "Bolivia": [14.3, 12.3, 14.2, 15.6, 17.8, 20.3, 21, 20.3, 19.7],
    "Denmark": [10, 8.4, 8.2, 6.6, 5.7, 4.8, 4.6, 4.6, 4.5],
    "Netherlands": [66.5, 62.7, 70.5, 64.1, 63.8, 68.6, 57.9, 43.3, 40.2],
    "Qatar": [77, 89.3, 131.2, 145.3, 157, 177.6, 174.1, 178.5, 181.2],
    "Nigeria": [36.2, 26, 37.3, 40.6, 43.3, 36.2, 45, 50.1, 44.9],
    "Turkmenistan": [66.1, 36.4, 42.4, 59.5, 62.3, 62.3, 67.1, 69.6, 66.8],
    "Brunei": [12.2, 11.4, 12.3, 12.8, 12.6, 12.2, 11.9, 11.6, 11.2],
    "Italy": [8.4, 7.3, 7.6, 7.7, 7.8, 7, 6.5, 6.2, 5.3],
    "India": [30.5, 37.6, 49.3, 44.5, 38.9, 32.1, 30.5, 29.3, 27.6],
    "UAE": [49.8, 50.3, 51.4, 52.9, 53.3, 53.6, 54.2, 55.1, 56.6]
}

class GasConsumptionModel:
    def __init__(self, data, smoothing_factor=0.5):
        self.data = np.array(data)
        self.smoothing_factor = smoothing_factor
        self.num_points = len(data)
        self.accumulated_series = None
        self.model_params = None
        self.predicted_values = None

    def accumulate_data(self):
        raw_data = self.data
        smoothing_factor = self.smoothing_factor
        num_points = self.num_points
        accumulated = np.zeros(num_points)
        accumulated[0] = raw_data[0]
        
        for i in range(1, num_points):
            accumulated[i] = (1 - smoothing_factor) * raw_data[i] + smoothing_factor * accumulated[i - 1]
        
        self.accumulated_series = accumulated
        return accumulated

    def fit_model(self):
        accumulated = self.accumulated_series
        raw_data = self.data[1:]
        
        design_matrix = np.vstack((-0.5 * (accumulated[:-1] + accumulated[1:]), np.ones(len(raw_data)))).T
        target_values = raw_data
        
        alpha, beta = np.linalg.lstsq(design_matrix, target_values, rcond=None)[0]
        self.model_params = alpha, beta
        return alpha, beta

    def restore_values(self):
        alpha, beta = self.model_params
        accumulated = self.accumulated_series
        num_points = self.num_points
        restored = np.zeros(num_points)
        restored[0] = accumulated[0]
        
        for i in range(1, num_points):
            restored[i] = (restored[i - 1] - beta / alpha) * np.exp(-alpha) + beta / alpha
        
        self.predicted_values = np.diff(restored, prepend=restored[0])
        return self.predicted_values

    def execute(self):
        self.accumulate_data()
        self.fit_model()
        return self.restore_values()

    def plot_consumption(self, country):
        years = range(2008, 2008 + len(self.data))
        plt.plot(years, self.data, label=f'Observed Data ({country})', marker='o')

        future_years = range(2008 + len(self.data), 2008 + len(self.data) + len(self.predicted_values))
        plt.plot(future_years, self.predicted_values, label=f'Forecasted Data ({country})', marker='x')

        plt.title(f'Natural Gas Consumption Forecast for {country}')
        plt.xlabel('Year')
        plt.ylabel('Consumption (bcm)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Ask the user to choose a country
selected_country = input("Choose a country from the list (Brazil, Bolivia, Denmark, Netherlands, Qatar, Nigeria, Turkmenistan, Brunei, Italy, India, UAE): ")

if selected_country in country_data:
    country_values = country_data[selected_country]
    model = GasConsumptionModel(country_values, smoothing_factor=0.59)
    predicted_values = model.execute()

    print(f"Observed Data for {selected_country}: {country_values}")
    print(f"Predicted Data for {selected_country}: {predicted_values}")
    
    # Calculate the Root Mean Squared Error (RMSE)
    rmse_value = np.sqrt(np.mean((country_values - predicted_values) ** 2))
    print(f"RMSE for {selected_country}: {rmse_value}")

    # Plot the results
    model.plot_consumption(selected_country)
else:
    print("Invalid country name. Please try again with a valid country.")
