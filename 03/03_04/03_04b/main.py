user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}


def update_preferences(user_pref):
    new_preference = {}
    for key, value in user_pref.items():
        print(value)
        if(value is not None):
            new_preference[key] = value
    return new_preference


print(update_preferences(user_preferences))
