import sqlite3


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            seat_price = seat.is_free()
            card.validate(seat_price)
            seat.occupy()


class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id

    def is_free(self):
        conn = sqlite3.connect("my_cinema.db")
        cursor = conn.execute("""
            SELECT "taken", "price" FROM "Seat" WHERE "seat_id"=?
            """, [self.seat_id])
        result = cursor.fetchall()[0]
        if result[0] == 0:
            price = result[1]
            return price
        else:
            print("The seat is already taken, choose another one.")
        conn.close()

    def occupy(self):
        conn = sqlite3.connect("my_cinema.db")
        conn.execute("""
            UPDATE "Seat" SET "taken"=1 WHERE "seat_id"=?
            """, [self.seat_id])
        conn.commit()
        conn.close()


class Card:
    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        conn = sqlite3.connect("banking.db")
        cursor = conn.execute("""
            SELECT "balance" FROM "Card" WHERE "number"=? 
            """, [self.number])
        result = cursor.fetchone()[0] - price
        conn.close()
        print(result)
        return result


user_name = input("Enter your name: ").title()
user_seat = input("Enter seat: ").title()
card_type = input("Enter card type: ").title()
card_number = input("Enter card number: ")
card_cvc = input("Enter card cvc: ")
card_holder = input("Enter card holder: ").title()


user = User(user_name)
seat = Seat(user_seat)
card = Card(card_type, card_number, card_cvc, card_holder)

user.buy(seat, card)


