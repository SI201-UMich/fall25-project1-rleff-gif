# Name: Reagan Leff
# Course: SI 201
# Project 1: Coffee Sales Data Analysis
# Date: October 9, 2025

# Collaborators: Jamie Kornblum and Claire Abbo

# Who wrote what functions: 
# Jamie: calculate_coffees_sold_per_type(), calculate_coffees_sold_per_time_of_day(), and their corresponding test functions
# Reagan: add_season_column() (including get_season() helper function), calculate_orders_per_season(), calculate_average_coffees_sold_per_day(), and their corresponding test functions  
# Claire: get_most_popular_coffee_per_season(), calculate_total_revenue(), write_results_to_txt(), and their corresponding test functions

# We used ChatGPT to help us debug our code and help us when we ran into errors. We also used it help us to generate test cases for some of our tests.

# Program Description:
# This program reads and analyzes coffee sales data from a CSV file, calculates sales statistics by type, time of day, and season, and outputs a summary report to a text file.

import csv
with open('data/Coffe_sales.csv', mode='r') as file: 
    #opening the csv file and reading the data
    reader = csv.DictReader(file) #reading the csv file as a dictionary
    data = [row for row in reader] #making the rows into a list of dictionaries
    for row in data:
        row['money'] = float(row['money'])
        row['Time_of_Day'] = row['Time_of_Day'].strip()
        row['Month_name'] = row['Month_name'].strip()
        row['coffee_name'] = row['coffee_name'].strip()

