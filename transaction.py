import time

from datetime import datetime

# Maps the index line from Fidelity CSVs to the index in the
# values array in this class.
# DO NOT MODIFY EXISTING VALUES.
INDEX_DICT = {
    "Run Date": 0,
    "Account": 1,
    "Action": 2,
    "Symbol": 3,
    "Security Description": 4,
    "Security Type": 5,
    "Quantity": 6,
    "Price ($)": 7,
    "Commission ($)": 8,
    "Fees ($)": 9,
    "Accrued Interest ($)": 10,
    "Amount ($)": 11,
    "Settlement Date": 12
}


class Transaction(object):
    run_date = datetime.utcnow()
    account = ""
    action = ""
    symbol = ""
    security_description = ""
    security_type = ""
    quantity = 0.0
    price_us = 0.0
    commission_us = 0.0
    fees_us = 0.0
    accrued_interest = 0.0
    amount_us = 0.0
    settlement_date = None

    values = []
    sorted_dict = []

    category = 0

    def __init__(self):
        self.values = [
            self.run_date,
            self.account,
            self.action,
            self.symbol,
            self.security_description,
            self.security_type,
            self.quantity,
            self.price_us,
            self.commission_us,
            self.fees_us,
            self.accrued_interest,
            self.amount_us,
            self.settlement_date
        ]
        self.sorted_dict = sorted(INDEX_DICT.iteritems(), key=lambda item: item[1])

    def __str__(self):
        output = "TRANSACTION of CATEGORY: {0}\n".format(self.category)
        for key, value in self.sorted_dict:
            output += "{0}: {1}\n".format(key, self.values[value])
        return output

    def process_values(self, index_line, raw_line):
        for i in xrange(len(raw_line)):
            type = INDEX_DICT[index_line[i]]
            if type == 0 or type == 12:
                # Convert the string to a datetime.
                try:
                    raw_line[i] = datetime.fromtimestamp(time.mktime(
                        time.strptime(raw_line[i], "%m/%d/%Y")))
                except ValueError:
                    # TODO(luke): handle error with user input.
                    pass
            elif type >= 6 and type <= 11:
                try:
                    raw_line[i] = float(raw_line[i])
                except ValueError:
                    raw_line[i] = 0
        # Load the values into the Transaction object.
        self.__load_values(raw_line)

    def __load_values(self, processed_line):
        for i in xrange(len(self.values)):
            self.values[i] = processed_line[i]

    def set_category(self, category):
        self.category = category
