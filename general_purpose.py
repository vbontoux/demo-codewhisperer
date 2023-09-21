import csv
import json

# Take a look at the code exemple and various or code completion here :
# https://docs.aws.amazon.com/codewhisperer/latest/userguide/whisper-code-examples.html


# Here are few sample to see how code suggestions work

# USUAL EVERY DAY FUNCTIONS
# a function that does a bubble sort on a list of numbers
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]


# a function that converts a json file to a csv file
# json keys are converted to csv columns
def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        for key, value in data.items():
            writer.writerow([key, value])

# a function that converts a csv file to a json file
# csv columns are converted to json keys
def csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        data = dict(reader)
    with open(json_file, 'w') as f:
        json.dump(data, f)

# Auto complete (type enter at the end of the line of an item)
fake_users = [
    { "name": "User 1", "id": "user1", "city": "San Francisco", "state": "CA" },
    { "name": "User 2", "id": "user2", "city": "Tampa", "state": "FL" },
    { "name": "User 3", "id": "user3", "city": "New York", "state": "NY" },
]

# a function that displays an image
def display_image(image_file):
    from PIL import Image
    im = Image.open(image_file)
    im.show()

# Try
#a recursive function that sorts a list of numbers
def sort_list(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        return sort_list(numbers[1:]) + [numbers[0]]


# CALL EXTERNAL APIS 

# a function that calls the tomtom api to get a route between two locations
def get_route(origin, destination):
    import tomtom
    client = tomtom.TomTomClient("YOUR_API_KEY")
    response = client.directions_between(origin, destination)
    return response


# a function that calls weather forcast in paris at a past date using pyowm
def get_weather_forecast(date):
    import pyowm
    owm = pyowm.OWM("YOUR_API_KEY")
    observation = owm.weather_at_date(date)
    return observation


