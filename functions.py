from typing import Any, Iterable, Iterator
import re

# все ф-ции принимают что-то что можно перечислять (строки в нашем случае)


def filter_query(value: str, data: Iterable[str]) -> Iterator[str]:
    # проверяет есть ли подстрока value в строках data
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args: Any, **kwargs: Any) -> set[str]:
    # получаем уникальную выборку данных
    return set(data)


def limit_query(value: str, data: Iterable[str]) -> list[str]:
    limit: int = int(value)
    return list(data)[:limit]


def map_query(value: str, data: Iterable[str]) -> Iterator[str]:
    # разделяет строки по пробелам и формирует их в колонку
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def sort_query(value: str, data: Iterable[str]) -> list[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def regex_query(value: str, data: Iterable[str]) -> Iterator[str]:
    pattern: re.Pattern = re.compile(value)
    return filter(lambda x: re.search(pattern, x), data)

