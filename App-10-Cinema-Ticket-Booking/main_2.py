import sqlite3


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        price = seat.get_price()
        if seat.is_free():
            if card.validate(price):
                seat.occupy()
        else:
            print("The seat is already taken, please choose another one.")


class Seat:
    database = "my_cinema.db"
    con = sqlite3.connect(database)

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        cursor = self.con.execute("""
                SELECT "price" FROM "Seat" WHERE "seat_id"=?
                """, [self.seat_id])
        fetched_price = cursor.fetchone()
        if fetched_price is not None:
            price = fetched_price[0]
            return price
        else:
            print("Seat doesn't exist!")

    def is_free(self):
        cursor = self.con.execute("""
                SELECT "taken" FROM "Seat" WHERE "seat_id"=?
                """, [self.seat_id])
        status = cursor.fetchone()[0]
        if status == 0:
            return True
        else:
            self.con.close()
            return False

    def occupy(self):
        self.con.execute("""
                    UPDATE "Seat" SET "taken"=1 WHERE "seat_id"=?
                    """, [self.seat_id])
        self.con.commit()
        self.con.close()


class Card:
    database = "banking.db"
    con = sqlite3.connect(database)

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        cursor = self.con.execute("""
            SELECT "balance" FROM "Card" WHERE "type"=? AND "number"=? AND "cvc"=? AND "holder"=?
            """, [self.type, self.number, self.cvc, self.holder])
        fetched_balance = cursor.fetchone()
        if fetched_balance is not None:
            initial_balance = fetched_balance[0]
            if initial_balance >= price:
                new_balance = initial_balance - price
                self.con.execute("""
                    UPDATE "Card" SET "balance"=? WHERE "type"=? AND "number"=? AND "cvc"=? AND "holder"=?
                    """, [new_balance, self.type, self.number, self.cvc, self.holder])
                print(new_balance)
                self.con.commit()
                self.con.close()
                return new_balance
            else:
                print("You have insufficient funds, see you next time!")
        else:
            print("Incorrect card, try again!")
        self.con.close()


class Ticket:

    def __init__(self, id, user, price, seat):
        self.id = id
        self.user = user
        self.price = price
        self.seat = seat

    def to_pdf(self):
        pass


user_name = input("Enter your name: ").title()
user_seat = input("Enter the seat number: ").title()

user = User(user_name)
seat = Seat(user_seat)

card_type = input("Enter the card type: ").title()
card_number = int(input("Enter the card number: "))
card_cvc = int(input("Enter the card cvc: "))
card_holder = input("Enter the card holder's name: ").title()

card = Card(card_type, card_number, card_cvc, card_holder)


user.buy(seat, card)
