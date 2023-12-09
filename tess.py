import random
import string

# Function to generate a random fake username
def generate_username(first_name, last_name):
    username = first_name.lower() + last_name.lower() + str(random.randint(10, 99))
    return username

# Function to generate a random fake password
def generate_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(8))
    return password

# Function to generate a random fake address
def generate_address():
    street_names = ["Main", "Maple", "Cedar", "Elm", "Oak", "Pine"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
    address = str(random.randint(100, 999)) + ' ' + random.choice(street_names) + ' St, ' + random.choice(cities) + ', USA'
    zip_code = ''.join(random.choice(string.digits) for i in range(5))
    return address, zip_code

# Generate fake user information
first_names = ["John", "Emily", "Michael", "Sarah", "David", "Emma"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis"]

fake_first_name = random.choice(first_names)
fake_last_name = random.choice(last_names)
fake_username = generate_username(fake_first_name, fake_last_name)
fake_password = generate_password()
fake_address, zip_code = generate_address()

# Print the generated fake information
print("Generated Fake User Information:")
print("Name:", fake_first_name, fake_last_name)
print("Username:", fake_username)
print("Password:", fake_password)
print("Address:", fake_address)
print("Zip Code:", zip_code)
