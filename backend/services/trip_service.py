def get_trip_category(budget):
    if budget < 1000:
        return "Backpacker"
    elif budget <= 3000:
        return "Standard"
    else:
        return "Luxury"


def get_travel_season(month):
    if month == "December":
        return "Peak Season"
    elif month == "June":
        return "Holiday Season"
    else:
        return "Regular Season"


def calculate_daily_budget(budget, days):
    return budget / days


def get_recommended_places(destination):
    places_by_destination = {
        "Japan": ["Tokyo Tower", "Shibuya", "Mount Fuji"],
        "Bali": ["Ubud", "Kuta Beach", "Tanah Lot"],
        "Paris": ["Eiffel Tower", "Louvre Museum", "Montmartre"],
    }

    return places_by_destination.get(destination, ["No recommendation available"])


def print_recommended_places(destination):
    places = get_recommended_places(destination)

    print("Recommended Places")
    for place in places:
        print(f"- {place}")


def get_transportations():
    return ["Bus", "Train", "Flight"]


def get_default_recommendations():
    return ["Tokyo Tower", "Mount Fuji", "Shibuya"]