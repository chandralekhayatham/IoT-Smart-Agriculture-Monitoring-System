def get_status(
    soil,
    temperature,
    pump
):

    if soil < 40:
        return "🌱 LOW SOIL MOISTURE"

    elif temperature > 35:
        return "🌡 HIGH TEMPERATURE"

    elif pump == "ON":
        return "💧 IRRIGATION ACTIVE"

    else:
        return "✅ FARM CONDITIONS NORMAL"