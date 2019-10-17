clothes_data = []

# temperature = int(weather.get('temperature'))

        # temperature_level = {
        #     0:  "It's scorching hot. Stay cool! Keep hydrated!",
        #     1:  "It's hot and sunny. Don't forget that sunscreen!",
        #     2:  "It's nice and warm today. Time to flex those flip-flops",
        #     3:  "A sweater would be nice in this cool weather",
        #     4:  "It's gonna be cold today. Treat yourself to a hot chocolate!",
        #     5:  "Winter is here! Wear your beanie and gloves!",
        #     6:  "It's Freezing Cold. Maybe don't leave the house."
        # }

        # if temperature >= 35:
        #     return temperature_level[0]
        # elif 27 <= temperature <= 34:
        #     return temperature_level[1]
        # elif 21 <= temperature <= 26:
        #     return temperature_level[2]
        # elif 15 <= temperature <= 20:
        #     return temperature_level[3]
        # elif 4 <= temperature <= 14:
        #     return temperature_level[4]
        # elif -4 <= temperature <= 4:
        #     return temperature_level[5]
        # elif temperature <= -3:
        #     return temperature_level[6]

        # clothes_data.append(temperature_level)

    return render_template('index.html', weather_data=weather_data, clothes_data=clothes_data)


# It is picking up London (first city in list) and displaying option [4]


<div class="col">
    {% for temperature_level in clothes_data %}
    <div class="card-body">
        <article class="media">
            <div class="media-content">
                <div class="content">
                    <p class="info"></p>
                        <span>{{ temperature_level }}</span>
                        <br>
                    </p>
                </div>
            </div>
        </article>
    </div>
    {% endfor %}
</div>