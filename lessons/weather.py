# 240911 practice challenge question


def get_weather_report() -> str:
    weather: str = input(
        "What is the weather? "
    )  # Asks for user input (remember to specify data type!)
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


print(get_weather_report())  # Prints user input for weather
