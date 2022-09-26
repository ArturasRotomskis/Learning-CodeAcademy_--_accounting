from modules.entry import Entry


class Credit(Entry):
    def __init__(self, amount, sender, additional_information):
        super().__init__(amount)
        self.sender = sender
        self.additional_information = additional_information

    def __str__(self):
        return f"Pajamos: {self.amount} Eur" \
               f", siuntėjas - {self.sender}" \
               f", informacija - {self.additional_information}"


"""
Outgoing funds.
May change this data.
"""
sender_names = [
    # Defined sender
    # select an index for the code
    "",
    "1 - darbdavys",        # 1
    "2 - darbdavys",        # 2
    "3 - darbdavys",        # 3
    "IT paslaugų firma",        # 4
    "Kompiuterių derinimo firma",       # 5
    "Mokymo įstaiga",       # 6
    "Klientas",     # 7
    "Praeivis",     # 8
]
sen_index = 6

additional_information_names = [
    # Additional information about the sender
    # select an index for the code
    "",
    "auto pavežėjimas",     # 1
    "kompiuterio taisymo paslauga",     # 2
    "TAXI",     # 3
    "Python programavimas",     # 4
    "IT Mokymas",       # 5
    "Kodo rašymas",     # 6
    "IT konsultacija",      # 7
]
add_index = 5
