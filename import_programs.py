import csv
from datetime import datetime
import os
import django

#Django Setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edunova.settings')
django.setup()

from programs.models import Programs

#open and read the CSV file
with open('programs.csv',newline='',encoding='utf-8') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        program=Programs(
            name=row['name'],
            description=row['description'],
        )
        program.save()
        print(f"Program '{program.name}' imported successfully.")