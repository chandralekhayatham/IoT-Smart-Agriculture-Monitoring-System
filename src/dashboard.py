import pandas as pd
from datetime import datetime

def save_data(
    soil,
    temperature,
    humidity,
    light,
    pump,
    status
):

    data = {
        "Timestamp": [datetime.now()],
        "SoilMoisture": [soil],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Light": [light],
        "Pump": [pump],
        "Status": [status]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        "data/agriculture_data.csv",
        mode="a",
        index=False,
        header=False
    )