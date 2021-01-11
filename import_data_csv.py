#!/usr/bin/env python

"""
    Script to import book data from .csv file to Model Database DJango
    To execute this script run: 
                                1) manage.py shell
                                2) exec(open('import_data_csv.py').read())
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

import csv
from quotes.models import Quotation, Category

CSV_PATH = 'quote_data/halloween.txt'
CAT_ID = 13

contSuccess = 0
# Remove all data from Table
#Book.objects.all().delete()

with open(CSV_PATH, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|', quotechar=';')
    print('Loading...')
    for row in spamreader:
        Quotation.objects.create(category=Category.objects.get(pk = (CAT_ID)), quote=row[0])
        contSuccess += 1
    print(f'{str(contSuccess)} inserted successfully! ')

