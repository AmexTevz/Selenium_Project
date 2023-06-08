from baseclass import Base
from options import Results
import csv

base = Base()
result = Results(base.driver)

base.item_search(result.item)
base.buy_it_now()
combined_info = []
print(f'Scraping EBAY for {result.item}')
while True:
    for i in zip(result.titles(), result.prices(), result.links()):
        if 'to' not in i[1] and result.number_of_entries != len(combined_info):
            combined_info.append(i)
    if result.number_of_entries > len(combined_info):
        try:
            base.next_page()
            continue
        except:
            break
    else:
        break

filename = input('CSV File Name? :')
csv_file_path = f'/PATH/TO/YOUR/DIRECTORY/{filename}.csv' # INSERT THE PATH WHERE YOU WANT THE FILE TO BE CREATED.

if filename != '':  # WILL SKIP THE CSV FILE CREATION IF LEFT BLANK.
    num = 1
    with open(csv_file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Name', 'Price', 'Link'])
        for i in combined_info:
            listed = list(i)
            row_result = [num, listed[0],float(listed[1]),listed[2]]
            writer.writerow(row_result)
            num += 1
        print('CSV File Created')
else:
    print('CSV FILE SKIPPED')

base.close_window()
