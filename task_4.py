def main():
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]

    total_revenue = sum([day["revenue"] for day in days])
    print("Выручка за всю неделю:", total_revenue)

    best_day = max(days, key=lambda day: day["revenue"])
    print("День с самой большой выручкой:", best_day["day"])

    avg_per_order = {day["day"]: day["revenue"] / day["orders"]
                     for day in days}
    print("Средняя выручка на один заказ по дням:", avg_per_order)

    high_returns = [day["day"]
                    for day in days if day["returns"] / day["orders"] > 0.2]
    print("Дни, где возвратов больше 20%:", high_returns)


if __name__ == '__main__':
    main()
