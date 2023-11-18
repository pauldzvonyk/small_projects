from fpdf import FPDF
import webbrowser
import os


class PdfReport:
    """
    Creates a PDF file that contains the information about flatmates, such as
    their names, period when they stayed in the house and amount that each
    of them has to pay
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")  # default parameters (just to remember what they are)
        pdf.add_page()

        # Add icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family="Times", size=24, style="I")
        pdf.cell(w=0, h=60, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert period label and value
        pdf.set_font(family="Times", size=18, style="I")
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=200, h=40, txt=bill.period, border=0, align="R", ln=1)

        # Insert 1st name and relative amount to be paid
        pdf.set_font(family="Times", size=14, style="I")
        pdf.cell(w=100, h=40, txt=f"{flatmate1.name} pays", border=0)
        pdf.cell(w=170, h=40, txt=str(flatmate1.pays(bill, flatmate2)), border=0, align="R")
        pdf.cell(w=30, h=40, txt="$", border=0, align="C", ln=1)

        # insert 2nd name and relative amount to be paid
        pdf.cell(w=100, h=40, txt=f"{flatmate2.name} pays", border=0)
        pdf.cell(w=170, h=40, txt=str(flatmate2.pays(bill, flatmate1)), border=0, align="R")
        pdf.cell(w=30, h=40, txt="$", border=0, align="C", ln=1)

        # Change directory at this point to allow .output & .open methods below to execute smoothly
        os.chdir("files")

        # Create and save PDF file
        pdf.output(self.filename)

        # Automatically open PDF on RUN command
        webbrowser.open(self.filename)
