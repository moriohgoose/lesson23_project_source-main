from typing import Any, Iterable


# все ф-ции принимают что-то что можно перечислять (строки в нашем случае)

def filter_query(value: str, data: Iterable[str]):
    # проверяет есть ли подстрока value в строках data
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any):
    # получаем уникальную выборку данных
    return set(data)


def limit_query(value: str, data: Iterable[str]):
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]):
    # разделяет строки по пробелам и формирует их в колонку
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)

