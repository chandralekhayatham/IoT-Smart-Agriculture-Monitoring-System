import random

def get_soil_moisture():
    return random.randint(10, 100)

def get_temperature():
    return round(random.uniform(20, 45), 1)

def get_humidity():
    return round(random.uniform(30, 90), 1)

def get_light():
    return random.randint(100, 1000)