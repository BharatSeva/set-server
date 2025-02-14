import requests
import json

# Initializing variables
TOKEN = ""
HEALTHCAREID = ""
LICENSE = ""
PASSWORD = "12345"

# Step 1: Register Healthcare
url = "http://localhost:80/api/v1/healthcare/auth/register"
payload = {
    "name": "Guest Hospital",
    "availability": "Yes",
    "total_facilities": 200,
    "total_mbbs_doc": 58,
    "total_worker": 400,
    "no_of_beds": 200,
    "email": "Guest@gmail.com",
    "appointment_fee": 300,
    "about": "Regional",
    "password": PASSWORD,
    "address": {
        "country": "Indian",
        "landmark": "Francis Garden",
        "city": "Quincy",
        "state": "Syracuse"
    }
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, json=payload)

# Extracting healthcare ID and license from the response
if response.status_code == 201:  # Assuming 201 for successful creation
    response_data = response.json()
    HEALTHCAREID = response_data.get("Healthcare_details", "").get("healthcare_id")
    LICENSE = response_data.get("Healthcare_details", "").get("healthcare_license", "")
    # print("Healthcare registered successfully.")
    # print(response_data)
    print("HEALTHCAREID ", HEALTHCAREID)
    print("LICENSE ", LICENSE)
    print("Healthcare Has been Registered Successfully")
else:
    print(f"Healthcare Exists: {response.text}")
    exit()

# Step 2: Login Healthcare to get TOKEN
url = "http://localhost:80/api/v1/healthcare/auth/login"
payload = {
    "healthcare_id": HEALTHCAREID,
    "healthcare_license": LICENSE,
    "password": PASSWORD
}
response = requests.post(url, headers=headers, json=payload)

# Extracting token from the response
if response.status_code == 200:  # Assuming 200 for successful login
    response_data = response.json()
    TOKEN = response_data.get("token", "")
    # print(response_data)
    print("Successfully Fetched Token!!")
else:
    print(f"Failed to login healthcare: {response.text}")
    exit()

# Step 3: Create a user profile
url = "http://localhost:80/api/v1/healthcare/client/profile/create"
payload = {
    "fname": "Guest",
    "middlename": "kumar",
    "lname": "User",
    "sex": "Male",
    "dob": "2024-12-31T00:50:42",  # Corrected ISO-8601 datetime format
    "bloodgrp": "O+",
    "bmi": "22.5",
    "marriage_status": "Single",
    "weight": "70",  # Corrected to a valid number
    "email": "Guest@hotmail.com",
    "mobilenumber": "737-338-26931",
    "aadhar_number": "804-995-84117",
    "primary_location": "Delhi",
    "sibling": "no",
    "twin": "No",
    "fathername": "Dr. Jason Mueller",
    "mothername": "Lera Grimes",
    "emergencynumber": "646-658-4280",
    "address": {
        "country": "Honduras",
        "state": "Bayer Drive",
        "city": "West Jolie",
        "landmark": "4039 Ilene Village"
    }
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {TOKEN}'
}

response = requests.post(url, headers=headers, json=payload)

USER_EMAIL = ""
User_health_id = ""

# Output the result
if response.status_code == 201:  # Assuming 201 for successful profile creation
    response_data = response.json()
    USER_EMAIL = response_data.get("email", '')
    User_health_id = response_data.get("health_id", '')
    
    print("User_email ", USER_EMAIL)
    print("User_health_id ", User_health_id)
    # print("User profile created successfully:", response.json())
else:
    print(f"Failed to create user profile: {response.text}")

# Save the output to profile.txt
with open("profile.txt", "w") as file:
    file.write(f"HEALTHCAREID: {HEALTHCAREID}\n")
    file.write(f"LICENSE: {LICENSE}\n")
    file.write(f"TOKEN: {TOKEN}\n")
    file.write(f"USER_EMAIL: {USER_EMAIL}\n")
    file.write(f"User_health_id: {User_health_id}\n")
    file.write(f"PASSWORD: 12345\n")

url = "http://localhost:80/api/v1/user/auth/register"
payload = {
    "health_id": User_health_id,
    "email": USER_EMAIL,
    "password": "12345"
}
headers = {
    'Content-Type': 'application/json'
}
response = requests.post(url, headers=headers, json=payload)
if response.status_code == 201:
    print("User registered successfully:", response.json())
else:
    print(f"Failed to register user: {response.text}")
