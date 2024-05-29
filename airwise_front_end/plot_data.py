#!/usr/bin/env python3
import plotly.graph_objects as go
import plotly.io as pio
from future_data import specific_data


def plotting(location="Seattle",type='\'temp\''):
    # Sample weather data dictionary (simplified for example)
    
    weather_data = specific_data(location, type)
    type = type[1:-1]
    if location[0] == "'":
        location = location[1:-1]
    # Extracting data for plotting
    dates = [day["datetime"] for day in weather_data]
    type_data = [day[type] for day in weather_data]
    print(f"printing plot {type_data}")
    # humidity = [day["humidity"] for day in weather_data]
    # windspeed = [day["precip"] for day in weather_data]

    # Create a line chart for temperature
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=dates, y=type_data, mode='lines+markers', name=type))
    # fig.add_trace(go.Scatter(x=dates, y=humidity, mode='lines+markers', name='Humidity'))
    # fig.add_trace(go.Scatter(x=dates, y=windspeed, mode='lines+markers', name='precipitaion'))

    # Customize layout
    fig.update_layout(       
        title={
            'text': f'{type.capitalize()} Weather Data for {location}', 'font': {'size': 16},
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        xaxis_title='Date',
        yaxis_title='Values',
        legend_title='Legend'
    )

    graph_html = pio.to_html(fig, full_html=False)
    # graph_html = fig.to_html(full_html=False)
    

    return graph_html 
    #render_template('plot.html', plot=fig)
    # Show the plot
    # fig.show()

if __name__ == '__main__':
    plotting()