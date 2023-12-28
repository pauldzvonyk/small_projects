import sqlite3


class User:

    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        pass


class Seat:

    def __init__(self, database, seat_id, price):
        self.database = database
        self.seat_id = seat_id
        self.price = price

    def is_free(self):
        pass

    def occupy(self):
        pass


class Card:

    def __init__(self, database, type, number, cvc, holder):
        self.database = database
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self):
        pass


class Ticket:

    def __init__(self, id, user, price, seat):
        self.id = id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self, path):
        pass