"""
Based on OOP (Object-Oriented Programming).
"""
from modules.statement import Statement

statement_main = Statement()

while True:
    event = float(input(" 1 - įvesti pajamas, \n 2 - įvesti išlaidas, \n 3 - balansas \n 4 - ataskaita \n"
                        " 5 - išvalyti biudžetą \n 6 - išeiti iš programos \n ---> "))
    if event == 1:
        amount = float(input("Įveskite pajamas: "))
        statement_main.credit(amount)
    if event == 2:
        amount = float(input("Įveskite išlaidas: "))
        statement_main.debit(amount)
    if event == 3:
        statement_main.balance()
    if event == 4:
        statement_main.publication()
    if event == 5:
        statement_main.cleen_statement()
    if event == 6:
        print("\n Viso Gero")
        break
