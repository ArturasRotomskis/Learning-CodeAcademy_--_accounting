from modules.entry import Entry


class Debit(Entry):
    def __init__(self, amount, payment_method, purchased_goods_services):
        super().__init__(amount)
        self.payment_method = payment_method
        self.purchased_goods_services = purchased_goods_services

    def __str__(self):
        return f"Išlaidos: {self.amount} Eur" \
               f", atsiskaitymo būdas - {self.payment_method}" \
               f", įsigyta - {self.purchased_goods_services}"


"""
Incoming funds.
May change this data.
"""
payment_method_names = [
    # Payment methods used by the sender
    # select an index for the code
    "",
    "grynais: eurai",       # 1
    "grynais: doleriai",        # 2
    "SEB banko kortelė",        # 3
    "swedbank kortelė",     # 4
    "Kreditų unija",        # 5
    "IBAN pavedimas",       # 6
    "SEPA pavedimas",       # 7
    "POST LT kurjeris",     # 8
    "BOLT cash pristatymas",        # 9
]
pay_index = 6

purchased_goods_services_names = [
    # Purchased goods and services
    # select an index for the code
    "",
    "TAXI",     # 1
    "Mobilusis ryšys",      # 2
    "Bolt",     # 3
    "Barbora",      # 4
    "Kompiuteris",      # 5
    "Programinė įranga",        # 6
    "Išmanusis telefonas",      # 7
]
pur_index = 6
