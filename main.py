from purpleair.sensor import Sensor
channel = Sensor(102160).parent

c = f"{round(channel.current_temp_c, 1)}\u00b0C"
f = f"{channel.current_temp_f}\u00b0F"
h = f"{channel.current_humidity}%"

print(f"It's {f} ({c}) with {h} humidity.")
