from services.trip_service import (
    get_trip_category,
    get_travel_season,
    calculate_daily_budget,
    print_recommended_places,
)


def print_trip_summary(destination, days, budget, currency, travel_month):
    category = get_trip_category(budget)
    season = get_travel_season(travel_month)
    daily_budget = calculate_daily_budget(budget, days)

    print("==================================")
    print("KelanaAI")
    print("==================================")
    print(f"Destination : {destination}")
    print(f"Days        : {days}")
    print(f"Budget      : {budget} {currency}")
    print(f"Category    : {category}")
    print(f"Daily Budget: {daily_budget} {currency}/Day")
    print(f"Travel Month: {travel_month}")
    print(f"Season      : {season}")
    print()

    print_recommended_places(destination)


def main():
    destination = input("Masukkan destinasi: ")
    country = input("Masukkan negara: ")
    days = int(input("Masukkan jumlah hari: "))
    budget = float(input("Masukkan budget: "))
    currency = input("Masukkan mata uang: ")
    travel_month = input("Masukkan bulan perjalanan: ")

    print_trip_summary(destination, days, budget, currency, travel_month)


if __name__ == "__main__":
    main()