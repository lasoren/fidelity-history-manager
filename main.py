#!/usr/bin/python

import sys

from csv_importer import FidelityCsvImporter
from categorizer import Categorizer

if len(sys.argv) > 1:
    fidelity_csv_importer = FidelityCsvImporter(sys.argv[1])
    categorizer = Categorizer()

    categorizer.categorize_transactions(fidelity_csv_importer.transactions)

    print(fidelity_csv_importer.transactions[0].first_line_csv())
    for transaction in fidelity_csv_importer.transactions:
        print(transaction.to_csv())
else:
    print("Usage: python main.py <fidelity-csv>")


