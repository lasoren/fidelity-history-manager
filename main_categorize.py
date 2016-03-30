#!/usr/bin/python

import sys

from csv_importer import FidelityCsvImporter
from categorizer import Categorizer

if len(sys.argv) > 1:
    fidelity_csv_importer = FidelityCsvImporter(sys.argv[1])
    categorizer = Categorizer()

    categorizer.categorize_transactions(fidelity_csv_importer.transactions)
    with open('categorized.csv', 'r+') as f:
        first_line = f.readline()
        if len(first_line) == 0:
            print >> f, fidelity_csv_importer.transactions[0].first_line_csv()
        f.close()
    with open('categorized.csv', 'a') as f:
        for transaction in fidelity_csv_importer.transactions:
            print >> f, transaction.to_csv()
        f.close()
else:
    print("Usage: python " + sys.argv[0] + " <fidelity-csv>")


