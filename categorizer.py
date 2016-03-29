
CATEGORIES_LOCATION = 'categories.txt'


class CategoryImporter(object):
    categories = [
        "Not classified",
        "General"
    ]

    output_str = ""

    def __init__(self):
        f = open(CATEGORIES_LOCATION)
        count = 0
        for line in f:
            self.categories.append(line.strip())
            count += 1
        # Setup output string.
        for i in xrange(len(self.categories)):
            self.output_str += "   ({0}) {1}   ".format(i, self.categories[i])
        self.output_str += "\n"

    def __str__(self):
        return self.output_str

class Categorizer(object):
    category_importer = CategoryImporter()

    def categorize_transactions(self, transactions):
        for transaction in transactions:
            # TODO(luke): Automate categorization with filters.
            if transaction.category == 0:
                print(transaction)
                categorization = raw_input("What category does this transaction belong"
                                           "in?\n{0}".format(self.category_importer))
                categorization = int(categorization)
                transaction.set_category(categorization)

                filter = raw_input("Create a filter by specifying what "
                                   "field you used to identify this "
                                   "transaction:\n{0}".format(""))
                regex = raw_input("Enter the regex you can use to find this "
                                  "item again:\n")
