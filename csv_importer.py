from transaction import Transaction

class FidelityCsvImporter(object):
    transactions = []

    def __init__(self, filepath):
        f = open(filepath, "r")
        lines = []
        index_line = []
        count = 0
        for line in f:
            items = line.strip().split(",")
            if len(items) > 5:
                if count > 0:
                    lines.append(items)
                else:
                    index_line = items
                count += 1
        for line in lines:
            transaction = Transaction()
            transaction.process_values(index_line, line)
            self.transactions.append(transaction)
        print("{0} records found!\n".format(count))
        f.close()
