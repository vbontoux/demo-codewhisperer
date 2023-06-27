import csv
import json


# just typing the function name
def bubblesort(list):
    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

print(bubblesort([10,1,34,2,56,12,7,1,1,4,5,7,32]))

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


# a function that displays an image
def display_image(image_file):
    from PIL import Image
    im = Image.open(image_file)
    im.show()





    
