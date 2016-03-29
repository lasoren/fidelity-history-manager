from csv_importer import FidelityCsvImporter

fidelity_csv_importer = FidelityCsvImporter('2013Jan.csv')

for transaction in fidelity_csv_importer.transactions:
    print(transaction)

