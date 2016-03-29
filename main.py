from csv_importer import FidelityCsvImporter
from categorizer import Categorizer

fidelity_csv_importer = FidelityCsvImporter('2013Jan.csv')
categorizer = Categorizer()

categorizer.categorize_transactions(fidelity_csv_importer.transactions)

