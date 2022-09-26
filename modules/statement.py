from modules.credit import Credit, sender_names, sen_index, additional_information_names, add_index
from modules.debit import Debit, payment_method_names, pay_index, purchased_goods_services_names, pur_index
import pickle


class Statement:
    def __init__(self):
        self.booksheet = get_booksheet()

    def set_booksheet(self):
        with open("booksheet.pkl", 'wb') as file:
            pickle.dump(self.booksheet, file)

    def credit(self, amount, sender=sender_names[sen_index],
               additional_information=additional_information_names[add_index]):
        report = Credit(amount, sender, additional_information)
        self.booksheet.append(report)
        self.set_booksheet()

    def debit(self, amount, payment_method=payment_method_names[pay_index],
              purchased_goods_services=purchased_goods_services_names[pur_index]):
        report = Debit(amount, payment_method, purchased_goods_services)
        self.booksheet.append(report)
        self.set_booksheet()

    def balance(self):
        common = 0
        for report in self.booksheet:
            if type(report) is Credit:
                common += report.amount
            if type(report) is Debit:
                common -= report.amount
        print("Balansas:")
        print(common)
        return common

    def publication(self):
        print("Ataskaita:")
        for report in self.booksheet:
            print(report)

    def cleen_statement(self):
        self.booksheet = []
        self.set_booksheet()


def get_booksheet():
    with open("booksheet.pkl", 'rb') as file:
        booksheet = pickle.load(file)
        return booksheet
