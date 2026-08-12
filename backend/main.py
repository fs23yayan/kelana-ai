def print_trip_summary(destination, country, days, budget, currency, travel_month):
    print("========================")
    print("KelanaAI")
    print("========================")
    print(f"Destination : {destination}")
    print(f"Country     : {country}")
    print(f"Days        : {days}")
    print(f"Budget      : {budget} {currency}")
    print(f"Currency    : {currency}")
    print(f"Travel Month: {travel_month}")


def main():
    destination = input("Masukkan destinasi: ")
    country = input("Masukkan negara: ")
    days = int(input("Masukkan jumlah hari: "))
    budget = float(input("Masukkan budget: "))
    currency = input("Masukkan mata uang: ")
    travel_month = input("Masukkan bulan perjalanan: ")

    print_trip_summary(destination, country, days, budget, currency, travel_month)


if __name__ == "__main__":
    main()