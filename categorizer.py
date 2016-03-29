import re

from transaction import INDEX_DICT

CATEGORIES_LOCATION = 'categories.txt'
REGULAR_LOCATION = 'regular.txt'


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
    regular_expressions = {}

    def __init__(self):
        f = open(REGULAR_LOCATION, "r")
        for line in f:
            tokens = line.strip().split(",")
            if tokens[0] in self.regular_expressions:
                self.regular_expressions[tokens[0]].append((tokens[1], tokens[2]))
            else:
                self.regular_expressions[tokens[0]] = [(tokens[1], tokens[2])]
        f.close()

    def __del__(self):
        # Write the regular expressions back to the file.
        f = open(REGULAR_LOCATION, "w")
        for key, list in self.regular_expressions.iteritems():
            for value in list:
                f.write("{0}, {1}, {2}\n".format(key, value[0], value[1]))
        f.close()

    def categorize_transactions(self, transactions):
        for transaction in transactions:
            self.__categorize_automatically(transaction)
            if transaction.category == 0:
                print(transaction)
                categorization = raw_input("What category does this transaction belong"
                                           "in?\n{0}".format(self.category_importer))
                categorization = int(categorization)
                transaction.set_category(categorization)

                filter = ""
                while filter not in INDEX_DICT:
                    filter = raw_input("Create a filter by specifying what "
                                       "field you used to identify this "
                                       "transaction:\n{0}".format(""))
                regex = ""
                found = False
                while not found:
                    regex = raw_input("Enter the regex you can use to find this "
                                      "item again:\n")
                    value_index = INDEX_DICT[filter]
                    match = re.search(regex, transaction.values[value_index])
                    if match != None:
                        found = True
                if filter in self.regular_expressions:
                    self.regular_expressions[filter].append((regex, categorization))
                else:
                    self.regular_expressions[filter] = [(regex, categorization)]

    def __categorize_automatically(self, transaction):
        for key, list in self.regular_expressions.iteritems():
            for value in list:
                value_index = INDEX_DICT[key]
                match = re.search(value[0], transaction.values[value_index])
                if match != None:
                    transaction.set_category(value[1])
                    break
