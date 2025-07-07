import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Data Points')

    # Create first line of best fit
    slope, intercept, *args = linregress(x, y)
    x_fit1 = pd.Series(range(1880, 2051))
    y_fit1 = intercept + slope * x_fit1
    plt.plot(x_fit1, y_fit1, color='red', label='Best Fit Line (1880-2050)')

    # Create second line of best fit
    x = df[df['Year'] >= 2000]['Year']
    y = df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    
    slope, intercept, *args = linregress(x, y)
    x_fit2 = pd.Series(range(2000, 2051))
    y_fit2 = intercept + slope * x_fit2
    plt.plot(x_fit2, y_fit2, color='green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()