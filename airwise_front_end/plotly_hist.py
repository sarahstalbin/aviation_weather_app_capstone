#!/usr/bin/env python3
import plotly.graph_objects as go
import plotly.io as pio
from hist_data import specific_data


def plotting():
    # Sample weather data dictionary (simplified for example)
    
    weather_data = specific_data()
    # weather_data = {
    #     "location": "London,UK",
    #     "days": [
    #         {"datetime": "2024-05-27", "tempmax": 62.9, "tempmin": 52.8, "temp": 56.7, "humidity": 69.6, "windspeed": 14.5},
    #         {"datetime": "2024-05-28", "tempmax": 64.0, "tempmin": 53.0, "temp": 57.5, "humidity": 70.0, "windspeed": 13.0},
    #         # Add more days as needed
    #     ]
    # }
    # print(weather_data)
    # print("hello")

    # Extracting data for plotting
    dates = [day["datetime"] for day in weather_data]
    temps = [day["temp"] for day in weather_data]
    humidity = [day["humidity"] for day in weather_data]
    windspeed = [day["precip"] for day in weather_data]

    # Create a line chart for temperature
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=temps, mode='lines+markers', name='Temperature'))
    fig.add_trace(go.Scatter(x=dates, y=humidity, mode='lines+markers', name='Humidity'))
    fig.add_trace(go.Scatter(x=dates, y=windspeed, mode='lines+markers', name='precipitaion'))

    # Customize layout
    fig.update_layout(
        title='Weather Data for London, UK',
        xaxis_title='Date',
        yaxis_title='Values',
        legend_title='Legend'
    )

    graph_html = pio.to_html(fig, full_html=False)

    return graph_html 
    #render_template('plot.html', plot=fig)
    # Show the plot
    # fig.show()

if __name__ == '__main__':
    plotting()
