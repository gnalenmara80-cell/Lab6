"""
Program Name: Lab6_Gnalen-1.py
Author: Gnalen Mara
Purpose: This program verifies user login information using a dictionary
         and displays the correct security level.
Starter Code: No starter code used
Date: 2/19/2026
"""

# Create a dictionary to store user login information
users = {
    "guest": "guest",
    "Gnalen": "MySecurePass!",
    "Martin": "Sunshine12",
    "Kassian": "StrongPass9",
}

# Prompt the user for their username
username = input("Enter your username: ").strip()

# Check if the username exists in the dictionary
if username not in users:
    print("\nUser not found. Exiting.")
else:
    correct_password = users[username]
    attempts = 3

    while attempts > 0:
        password = input("Enter your password: ")

        if password == correct_password:
            # Assign the security level based on the username
            if username == "guest":
                level = "Guest"
            else:
                level = "Security Level 1"

            print(f"\nWelcome, {username}. You have {level}.")
            break

        else:
            attempts -= 1
            if attempts > 0:
                print(f"Access Denied. {attempts} attempt(s) remaining.\n")
            else:
                print("\nToo many failed attempts. Account locked.")