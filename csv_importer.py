from transaction import Transaction

class FidelityCsvImporter(object):
    transactions = []

    def __init__(self, filepath):
        with open(filepath, "r") as f:
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


class CategorizedFidelityCsvImporter(object):
    transactions = {}

    def __init__(self, filepath):
        with open(filepath, "r") as f:
            lines = []
            index_line = []
            count = 0
            for line in f:
                items = line.strip().split(",")
                if len(items) > 5:
                    if count > 0:
                        lines.append(items)
                    else:
                        index_line = items[2:]
                    count += 1
            for line in lines:
                transaction = Transaction()
                transaction.process_values(index_line, line[2:])
                cat = int(line[0])
                transaction.set_category(cat)
                if cat not in self.transactions:
                    self.transactions[cat] = [transaction]
                else:
                    self.transactions[cat].append(transaction)
            print("{0} records found!\n".format(count))
            f.close()
