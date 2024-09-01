# third task for the final project
#! /usr/bin/env python3
import os
import requests

file_list = [f for f in os.listdir("supplier-data/descriptions") if ".txt" in f]

dict = {"name":[],"weight":[],"description":[],"image_name":[]}
for y in file_list:
    with open("supplier-data/descriptions/" + y) as x:
        lines = [line.rstrip('\n') for line in x]
    dict["name"] = lines[0]
    weight = lines[1]
    dict["weight"] = int(weight[:-4])
    dict["description"] = lines[2]
    dict["image_name"] = y[:-3] + "jpeg"
    try:
        response = requests.post("http://your_link_data/fruits/", data=dict)
        response.request.url
        response.request.body
        print(response.status_code)
    except:
        print("error")
