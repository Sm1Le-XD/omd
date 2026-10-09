from collections import Counter


def main():
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]

    total = len(queries)
    print("Всего поисковых запросов в ленте:", total)

    counts = Counter(queries)
    print("Сколько раз ввели каждый запрос:", dict(counts))

    most_popular, most_count = counts.most_common(1)[0]
    print("Самый частый запрос:", most_popular)
    print("Его доля от всех поисков:",
          f"{round(most_count / total, 2) * 100}%")

    once = [query for query, count in counts.items() if count == 1]
    print("Запросы, встретившиеся один раз:", once)


if __name__ == '__main__':
    main()
