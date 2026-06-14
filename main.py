from src.sensor import get_soil_moisture
from src.sensor import get_temperature
from src.sensor import get_humidity
from src.sensor import get_light

from src.irrigation import pump_status
from src.alert import get_status

from src.dashboard import save_data

print("=" * 65)
print(" IOT ENABLED SMART AGRICULTURE MONITORING SYSTEM ")
print("=" * 65)

soil = get_soil_moisture()

temperature = get_temperature()

humidity = get_humidity()

light = get_light()

pump = pump_status(soil)

status = get_status(
    soil,
    temperature,
    pump
)

save_data(
    soil,
    temperature,
    humidity,
    light,
    pump,
    status
)

print("\nSoil Moisture :", soil, "%")
print("Temperature   :", temperature, "°C")
print("Humidity      :", humidity, "%")
print("Light Level   :", light)
print("Water Pump    :", pump)

print("\nStatus :", status)

print("\nData Logged Successfully")
print("Thank You for Using Smart Agriculture Monitoring System")