from collections import defaultdict


def main():
    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]

    stats = defaultdict(lambda: {"product": "", "count": 0, "sum_stars": 0})
    for review in reviews:
        stats[review["id"]]["product"] = review["product"].lower()
        stats[review["id"]]["count"] += 1
        stats[review["id"]]["sum_stars"] += review["stars"]

    print("Средняя оценка каждого товара:")
    for entry in stats.values():
        avg = entry["sum_stars"] / entry["count"]
        print(f'{entry["product"]}: {avg}')

    worst = min(
        (
            [entry["product"], entry["sum_stars"] / entry["count"]]
            for entry in stats.values()
            if entry["count"] >= 2
        ),
        key=lambda x: x[1],
    )
    print(f'Худший товар (от 2 отзывов): {worst[0]}')

    low_count = sum(1 for review in reviews if review["stars"] <= 2)
    share = low_count / len(reviews)
    print(f"Отзывов на 1–2 звезды: {low_count}")
    print(f"Их доля от всех отзывов: {share}")


if __name__ == '__main__':
    main()
