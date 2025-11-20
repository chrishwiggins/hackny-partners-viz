#!/usr/bin/env python3
import csv
import json
from collections import defaultdict

# Read the Alumni CSV
alumni_file = '../../AlumNY/data/AlumNY/data/Alumni.csv'

partners = defaultdict(lambda: {'count': 0, 'years': set()})

with open(alumni_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        host = row['Host'].strip()
        cohort = row['Cohort'].strip()

        if host and cohort:
            partners[host]['count'] += 1
            try:
                partners[host]['years'].add(int(cohort))
            except ValueError:
                pass

# Convert to list format
partners_list = []
for name, data in partners.items():
    partners_list.append({
        'name': name,
        'count': data['count'],
        'years': sorted(list(data['years']))
    })

# Sort by count descending
partners_list.sort(key=lambda x: x['count'], reverse=True)

# Write to JSON
with open('partners.json', 'w', encoding='utf-8') as f:
    json.dump(partners_list, f, indent=2)

print(f"Generated partners.json with {len(partners_list)} partners")
print(f"Total fellows: {sum(p['count'] for p in partners_list)}")
