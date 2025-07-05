#Imports libraries and functions from utils files
import pandas as pd
import numpy as np
import os
from datetime import datetime
import json
from dotenv import load_dotenv
load_dotenv('.env')
import sys
# The check_maintenance_due function will determine which maintenance tasks are due based on the current mileage and the maintenance log.
# The send_email function will send an email with the list of due tasks.
from Utils import send_email, check_maintenance_due

#This dictionary sets the frequency standards for maintenance
car_maintenance_tasks_frequency_dict = {
    "Oil/Oil filter change": 5000,
    "Tire Alignment": 12000,
    "Tire rotation": 5000,
    "Check windshield wiper condition": 5000,
    "Top off fluids (washer, brake, coolant, etc.)": 5000,
    "Check all exterior lights": 5000,
    "Oil & oil filter change (synthetic oil)": 7500,
    "Inspect air filter": 7500,
    "Inspect brakes": 7500,
    "Clean battery terminals": 7500,
    "Replace cabin air filter": 15000,
    "Replace engine air filter": 15000,
    "Inspect belts and hoses": 15000,
    "Replace transmission fluid (if required)": 30000,
    "Inspect suspension and steering components": 30000,
    "Replace spark plugs": 50000,
    "Replace brake fluid": 50000,
    "Replace timing belt (if applicable)": 75000,
    "Replace coolant/antifreeze": 75000}

# This creates a dictioary from the JSON file that contains the maintenance log for the vehicle.
#Be sure to update this file whenver matience is performed on the vehicle.
# The JSON file should be in the format of {"task_name": last_mileage_performed}
with open('Maintenance_Logs_JSONS\\2017_Toyota_Corolla_MLog.json', 'r') as f:
    maintenance_log_dictionary = json.load(f)
for task in maintenance_log_dictionary:
    maintenance_log_dictionary[task] = int(maintenance_log_dictionary[task])

#The current milage of the vehicle will be compared to the last performed mileage of each task in the maintenance log.
try:
    vehicle_mileage = int(input("Enter the current mileage of the vehicle: "))
except ValueError:
    print("Invalid input. Please enter a valid integer for mileage.")
    sys.exit(1)


tasks_due = check_maintenance_due(vehicle_mileage, maintenance_log_dictionary, car_maintenance_tasks_frequency_dict)


# This defines the arguments of the send email function if the script errors out here check that the .env file is set up correctly, 
# and check that your gmail has an active app password token.
subject = 'Report of Car Maintenance Tracker 2017 Toyota Corolla'
body = f'The Following maintenance task are due on the 2017 Toyota Corolla {tasks_due}.'
sender_email = os.getenv('email')
receiver_email = os.getenv('email')
password = os.getenv('python_email_connector_token')

if tasks_due:
    print("Sending email with due tasks...")
    print(f"Tasks due: {tasks_due}")
    send_email(subject, body, sender_email, receiver_email, password)
else:
    print("No maintenance tasks are due at this time.")
    sys.exit(0)