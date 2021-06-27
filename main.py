from purpleair.sensor import Sensor
import aqi
import colored

SENSOR_ID = 102160


def main():
    channel = Sensor(SENSOR_ID).parent
    c = f"{round(channel.current_temp_c, 1)}\u00b0C"
    f = f"{channel.current_temp_f}\u00b0F"
    h = f"{channel.current_humidity}%"
    q = aqi.to_aqi([(aqi.POLLUTANT_PM25, channel.current_pm2_5)])
    d = aqi_to_category(q)

    print(f"It's {f} ({c}) with {h} humidity, with {d} AQI of {q}.")


def aqi_to_category(index):
    if index >= 0 and index <= 50:
        description = colored.stylize("a good", "green")
    elif index >= 51 and index <= 100:
        description = colored.stylize("a moderate", colored.bg("yellow"))
    elif index >= 101 and index <= 150:
        description = "an unhealthy for sensitive groups"
    elif index >= 151 and index <= 200:
        description = "an unhealthy"
    elif index >= 201 and index <= 300:
        description = "a very unhealthy"
    elif index >= 301 and index <= 500:
        description = "a hazardous"

    return description


if __name__ == "__main__":
    main()
