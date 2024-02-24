user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

user_preferences["language"] = "Spanish"
user_preferences["volume_level"] = 100
user_preferences["highlight_color"] = "yellow"

removed_item = user_preferences.pop("date_format", "N/A")
print(removed_item)
