import eel
import pyowm

owm = pyowm.OWM('5efdfb0edbf028d2c03d79be12f39804')


@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temperature = w.temperature("celsius")["temp"]
    w_status = w.detailed_status
    wind = w.wind()["speed"]
    humidity = w.humidity

    total_weather = "Погода в " + place + ":"\
                    "\nСейчас " + str(temperature) + " градусов. " + w_status + \
                    "\nCкорость ветра: " + str(wind) + " м/с" + \
                    "\nВлажность воздуха: " + str(humidity) + "%"
    return total_weather


eel.init("web")
eel.start("main.html", mode="default", size=(700, 700))
