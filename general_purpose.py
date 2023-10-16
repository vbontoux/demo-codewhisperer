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

# a fucntion that reads a csv file and returns a panda dataframe
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

# 4/ Common API calls

# a function that calls the tomtom api to get a route between two locations
def get_route(origin, destination):
    import tomtom
    client = tomtom.TomTomClient("YOUR_API_KEY")
    response = client.directions_between(origin, destination)
    return response


# 5/ Show a Code Reference log



# 6/ Other examples

# define torch nn.module with 1 input layer, 3 hidden layers, and 1 output layer  
# define function to train model
import torch
def train_model(model, train_loader, optimizer, criterion, epochs):
    for epoch in range(epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            # forward pass
            output = model(data)
            loss = criterion(output, target)
            # backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")
    return mode


## in this example, we will see how additional code in our project affects the responses. Open the file python/prompts/example6a.py.
# function to verify email address
import re
def verify_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    else:
        return False
    
import boto3
# Create SES client
ses = boto3.client('ses')
# function to verify email address
def verify_email(email):
    response = ses.verify_email_identity(EmailAddress=email)
    return response
    