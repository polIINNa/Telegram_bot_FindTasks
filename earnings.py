'''Работа с доходами: добавление, статистика'''

import db
from typing import NamedTuple, List


class Earning(NamedTuple):
    price: int


def add_earning(raw_price: str) -> Earning:
    price = int(raw_price)
    db.insert(price)
    return Earning(
        price=price
    )


def show_earnings() -> List[Earning]:
    rows = db.fetchall()
    earnings = [Earning(price=row[0]) for row in rows]
    return earnings
