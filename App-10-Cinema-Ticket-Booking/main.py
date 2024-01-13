import sqlite3
from fpdf import FPDF
import random


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            price = seat.get_price()
            if card.validate(price=price):
                seat.occupy()
                ticket_id = random.randint(159856, 356824)
                ticket = Ticket(user=self.name, seat_number=seat.number, id=ticket_id, price=price)
                ticket.to_pdf()
        else:
            print("The seat is already occupied, please, choose another one.")


class Seat:
    con = sqlite3.connect("my_cinema.db")

    def __init__(self, number):
        self.number = number

    def is_free(self):
        cursor = self.con.execute("""SELECT "taken" FROM "Seat" WHERE "seat_id"=?""", [self.number])
        status = cursor.fetchone()[0]
        if status == 0:
            return True
        else:
            return False

    def occupy(self):
        self.con.execute("""UPDATE "Seat" SET "taken"=1 WHERE "seat_id"=?""", [self.number])
        self.con.commit()
        self.con.close()

    def get_price(self):
        cursor = self.con.execute("""SELECT "price" FROM "Seat" WHERE "seat_id"=?""", [self.number])
        price = cursor.fetchone()[0]
        return price


class Card:
    con = sqlite3.connect("banking.db")

    def __init__(self, type, card_number, cvc, holder):
        self.type = type
        self.card_number = card_number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        try:
            cursor = self.con.execute("""SELECT "balance" FROM "Card" WHERE "number"=? AND "cvc"=? AND "holder"=?""",
                                      [self.card_number, self.cvc, self.holder])

            new_balance = cursor.fetchone()[0] - price
            updated_balance = self.con.execute("""UPDATE "Card" SET "balance"=? WHERE "number"=? AND "cvc"=? AND 
            "holder"=?""",
                                               [new_balance, self.card_number, self.cvc, self.holder])
            self.con.commit()
            self.con.close()
            print("The purchase was successful, you will send you your ticket in pdf format")
            return updated_balance
        except TypeError:
            print("Something is wrong with your card, please, contact your bank.")


class Ticket:
    def __init__(self, user, seat_number, id, price):
        self.user = user
        self.seat_number = seat_number
        self.id = id
        self.price = price

    def to_pdf(self):
        pdf = FPDF(orientation="P", unit="pt", format="A4")  # default parameters (just to remember what they are)
        pdf.add_page()

        pdf.set_fill_color(215, 205, 210)
        pdf.set_font(family="Times", size=32, style="IB")
        pdf.cell(w=0, h=60, text="Your Ticket", border=1, align="C", fill=True, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font(family="Times", size=24, style="I")
        pdf.cell(w=60, h=40, text="Dear ", border="LTB")
        pdf.cell(w=250, h=40, text=str(self.user), align="C", border="TB")
        pdf.cell(w=0, h=40, text="Thank you very much!", border="TRB", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(w=200, h=40, text="Your Ticket ID is:   ", border="LTB")
        pdf.cell(w=0, h=40, text=str(self.id), border="TRB", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(w=150, h=40, text="Your seat is: ", border="LTB")
        pdf.cell(w=0, h=40, text=str(self.seat_number), border="TRB", new_x="LMARGIN", new_y="NEXT")
        pdf.cell(w=300, h=40, text="The price paid for the ticket is:", border="LTB")
        pdf.cell(w=60, h=40, text=str(self.price), border="TB")
        pdf.cell(w=0, h=40, text="Euros", border="TRB", new_x="LMARGIN", new_y="NEXT")
        pdf.output("your_ticket.pdf")


user_name = input("Please, enter your name: ").title()
seat_number = input("Please, enter your desired seat: ").title()
card_type = input("What is your card type? (Visa, MasterCard etc...): ").title()
while True:
    try:
        card_number = int(input("Enter your card number: "))
        card_cvc = int(input("Enter the cvc of your card: "))
        break
    except ValueError:
        print("The cards number and cvc contain only numbers.")
card_holder = input("Enter the name of the card holder: ").title()


user = User(user_name)
seat = Seat(seat_number)
card = Card(card_type, card_number, card_cvc, "John Smith")
user.buy(seat=seat, card=card)
