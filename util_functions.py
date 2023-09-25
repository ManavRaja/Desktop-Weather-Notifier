from notifypy import Notify


def get_wind_direction(degrees):
    """
    Takes in degrees and returns the cardinal direction for that degree
    """
    if (0 <= degrees <= 23) or (337 <= degrees <= 360):
        return "North"
    elif 24 <= degrees <= 68:
        return "Northeast"
    elif 69 <= degrees <= 113:
        return "East"
    elif 114 <= degrees <= 158:
        return "Southeast"
    elif 159 <= degrees <= 203:
        return "South"
    elif 204 <= degrees <= 248:
        return "Southwest"
    elif 249 <= degrees <= 293:
        return "West"
    elif 294 <= degrees <= 336:
        return "Northwest"


def send_weather_notification(current_temp, current_feels_like_temp, current_humidity, current_wind_speed,
                              current_wind_direction):
    """
    Takes in weather data and sends a desktop notification with it
    """
    notification = Notify()
    notification.application_name = "Python Weather Notification"
    notification.title = "Current Weather Information"
    notification.icon = "./weather-icon.png"
    notification.message = f"""
    Temperature: {current_temp}°F
    Feels Like: {current_feels_like_temp}°F
    Humidity: {current_humidity}%
    Wind: {current_wind_speed} mph {current_wind_direction}
    """
    notification.send()
