#!/usr/bin/python

import sys

from csv_importer import CategorizedFidelityCsvImporter

if len(sys.argv) > 1:
    categorized_fidelity_csv_importer = CategorizedFidelityCsvImporter(sys.argv[1])
    sum = 0
    for transaction in categorized_fidelity_csv_importer.transactions[10]:
        sum += transaction.values[11]
    print(sum)
else:
    print("Usage: python " + sys.argv[0] + " <fidelity-csv>")
