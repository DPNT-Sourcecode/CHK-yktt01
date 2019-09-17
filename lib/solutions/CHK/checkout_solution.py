import typing as t

prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

#Tabular price table only allows one offer per item
offers = {
    'A': (3, 130),
    'B': (2, 45),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    raise NotImplementedError()


