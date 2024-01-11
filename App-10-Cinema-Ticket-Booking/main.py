import sqlite3
import random
from fpdf import FPDF


class User:
    def __init__(self, name):
        self.name = name

    def buy(self, seat, card):
        if seat.is_free():
            seat_price = seat.is_free()
            card.validate(seat_price)
            seat.occupy()
            ticket_id = random.randint(100000, 999999)
            print_ticket = Ticket(id=ticket_id, user=self.name, price=seat_price, seat_number=seat.seat_id)
            print_ticket.to_pdf()


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
        try:
            conn = sqlite3.connect("banking.db")
            cursor = conn.execute("""
                SELECT "balance" FROM "Card" WHERE "number"=? AND "cvc"=?
                """, [self.number, self.cvc])
            result = cursor.fetchone()[0] - price
            conn.execute("""
                        UPDATE "Card" SET "balance"=? WHERE "number"=?
                        """, [result, self.number])
            conn.commit()
            conn.close()
            print("Purchase successful, we will send you a ticket in pdf format. Thank you very much!")
            return result
        except TypeError:
            print("Invalid card, try again.")


class Ticket:
    def __init__(self, id, user, price, seat_number):
        self.id = id
        self.user = user
        self.price = price
        self.seat_number = seat_number

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
        pdf.output("ticket.pdf")


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
