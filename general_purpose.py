import csv
import json

# 1/ single line completion 
listofvegetables = ["carrot", "cabbage", "broccoli", "potato"]
for i in listofvegetables:
    print(i)

listofdictsofawsregions = [
    {"name": "us-east-1", "region": "us-east-1"}, 
    {"name": "us-east-2", "region": "us-east-2"},
    {"name": "us-west-1", "region": "us-west-1"},
    {"name": "us-west-2", "region": "us-west-2"},
    {"name": "ca-central-1", "region": "ca-central-1"},
    {"name": "eu-central-1", "region": "eu-central-1"},
    {"name": "eu-west-1", "region": "eu-west-1"},
]

# 2/ multi line completion

# a function that reads a csv file and returns a panda dataframe
# remove the email collumn from the dataframe
import pandas as pd
def read_csv_file(filepath):
    df = pd.read_csv(filepath)
    return df.drop(columns=["email"])

# 3/ more complex patterns

# a function that does the bubble sort on a list of numbers
def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Smalest Multiple
# Create a function that returns the smallest positive number that is evenly divisible by all of the numbers from 1 to n.
def smallest_positive_number(n):
    for i in range(1, n + 1):
        if n % i == 0:
            return i
        
# 10001st prime number
# Create a function to find the 10001st prime number
        

# Write code to convert numbers to Roman numerals
def convert_to_roman(number):
    roman_numerals = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    roman_numeral = ""
    for key, value in roman_numerals.items():
        while number >= key:
            roman_numeral += value
            number -= key
    return roman_numeral


convert_to_roman(199)


# 4/ Common API calls

# a function that calls the tomtom api to get a route between two locations


# 5/ Show a Code Reference log



# 6/ Other examples

# define torch nn.module with 1 input layer, 3 hidden layers, and 1 output layer  
# define function to train model


## in this example, we will see how additional code in our project affects the responses. Open the file python/prompts/example6a.py.
# function to verify email address
import re
def verify_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False

#create a function to get user age and name  and print happy birthday
def get_user_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    return name, age

# Create a function to make an api call to the joke.com api and return a joke
import requests
def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any")
    if response.status_code == 200:
        joke = response.json()
        if joke["type"] == "single":
            return joke["joke"]
        else:
            return joke["setup"] + " " + joke["delivery"]
