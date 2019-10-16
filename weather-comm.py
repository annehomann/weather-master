def weather_commentary(temperature):
    temperature = int(temperature)
    temperature_level = {
                0:  "it's scorching hot. Stay cool!",
                1:  "it's hot and sunny. Don't forget that sunscreen!",
                2:  "it's nice and warm today. Time to flex those flip-flops",
                3:  "a cup of hot cappucino would be nice on this cool weather",
                4:  "it's gonna be cold today. Make sure you keep yourself warm!",
                5:  "winter is here! Brrrrrrr",
                6:  "it's Freezing Cold."
    }

    if temperature >= 95:
        return temperature_level[0]
    elif 80 <= temperature <= 94:
        return temperature_level[1]
    elif 69 <= temperature <= 79:
        return temperature_level[2]
    elif 59 <= temperature <= 68:
        return temperature_level[3]
    elif 40 <= temperature <= 57:
        return temperature_level[4]
    elif 25 <= temperature <= 39:
        return temperature_level[5]
    elif temperature <= 24:
        return temperature_level[6]