from flat import Bill, Flatmate
from pdf_reports import PdfReport


name1 = input("What is the name of the first flatmate? ")
days_in_house1 = float(input(f"How many days did {name1} stay in the house? "))

name2 = input("What is the name of the second flatmate? ")
days_in_house2 = float(input(f"How many days did {name2} stay in the house? "))

period = input("What is the bill period? e.g. 'March 2023': ")
amount = float(input("Please, enter amount of the bill: "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: € ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: € ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
