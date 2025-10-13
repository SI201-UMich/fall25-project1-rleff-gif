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

def calculate_coffees_sold_per_type(data):
    #Counting how many coffees of each type were sold
    coffee_counts = {}
    for row in data:
        coffee = row['coffee_name']
        if coffee not in coffee_counts:
            coffee_counts[coffee] = 0
        coffee_counts[coffee] += 1

def add_season_column(data):
    # Add a season column to the data based on month name
    def get_season(month): #adding a season key based on month
        if month in ['Dec', 'Jan', 'Feb']:
            return 'Winter'
        elif month in ['Mar', 'Apr', 'May']:
            return 'Spring'
        elif month in ['Jun', 'Jul', 'Aug']:
            return 'Summer'
        elif month in ['Sep', 'Oct', 'Nov']:
            return 'Fall'
        else:
            return 'Unknown'
    
    # for each sale find its season and adding it as a new column
    for row in data:
        month = row['Month_name']
        row['Season'] = get_season(month)
    return data

def calculate_orders_per_season(data):
    season_counts = {}
    
    for row in data:
        season = row.get('Season')  
        if season:  
            if season not in season_counts:
                season_counts[season] = 0
            season_counts[season] += 1  
    
    return season_counts
    
    return season_counts

def get_most_popular_coffee_per_season(data):
    #Finds the most ordered coffee for each season.
    season_coffee_counts = {}
    
    # Count coffee orders for each season
    for row in data:
        season = row['Season']
        coffee = row['coffee_name']
        
        if season:
            if season not in season_coffee_counts:
                season_coffee_counts[season] = {}
            
            if coffee not in season_coffee_counts[season]:
                season_coffee_counts[season][coffee] = 0
                
            season_coffee_counts[season][coffee] += 1

 # Find most popular coffee for each season and stores its count
    most_popular_by_season = {}
    for season, coffee_counts in season_coffee_counts.items():
        if coffee_counts:  
            most_popular_coffee = max(coffee_counts, key=coffee_counts.get)
            order_count = coffee_counts[most_popular_coffee]
            most_popular_by_season[season] = {
                'coffee': most_popular_coffee,
                'count': order_count,
                'all_coffees': coffee_counts
            }
    
    return most_popular_by_season

def calculate_average_coffees_sold_per_day(data):
    #Calculates average daily sales
    daily_counts = {}
    
    # Count coffees sold each day
    for row in data:
        date = row['Date']
        
        if date not in daily_counts:
            daily_counts[date] = 0
        
        daily_counts[date] += 1  
    
    # Calculate average
    if daily_counts:
        total_coffees = sum(daily_counts.values())
        total_days = len(daily_counts)
        average_per_day = total_coffees / total_days
        
        return {
            'average_per_day': average_per_day,
            'total_coffees': total_coffees,
            'total_days': total_days,
            'daily_counts': daily_counts
        }
    else:
        return {
            'average_per_day': 0,
            'total_coffees': 0,
            'total_days': 0,
            'daily_counts': {}
        }

    

