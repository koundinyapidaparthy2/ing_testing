import json
import re

def parse(filename='100KTtlingv2.txt'):
    # Dictionary to store extracted book data with EAN as the key
    books = {}

    # Regular expression to split by 3 or more spaces
    bisac_split_regex = re.compile(r'\s{3,}')

    # Open the text file and read lines
    with open(filename, 'r', encoding='iso-8859-1') as file:
        for eachline in file:
            # Extract the relevant fields based on the provided character positions
            ean = eachline[442:459].strip()              # EAN: 443 – 459
            title = eachline[11:161].strip()             # Title: 12 – 161
            publisher_name = eachline[351:396].strip()   # Publisher Name: 352 – 396
            
            # Split the BISAC codes based on 3 or more spaces
            bisac = bisac_split_regex.split(eachline[463:670].strip())  # BISAC: 464 – 670
            
            # Other fields go into the description
            contributor_name = eachline[225:265].strip() # Contributor Name: 226 – 265
            contributor_role = eachline[265:267].strip() # Contributor Role: 266 – 267
            binding = eachline[410:412].strip()          # Binding: 411 – 412
            lc = eachline[697:742].strip()               # LC: 698 – 742
            lccn = eachline[678:690].strip()             # LCCN: 679 – 690
            series_id = eachline[212:221].strip()        # Series ID: 213 – 221
            age_group = eachline[670:672].strip()        # Age Group: 671 – 672
            dimensions = eachline[804:819].strip()       # Dimensions: 805 – 819
            page_count = eachline[787:792].strip()       # Page Count: 788 – 792

            # Create the JSON structure
            books[ean] = {
                'ean': ean,
                'title': title,
                'publisher': publisher_name,
                'bisac': bisac,
                'description': {
                    'Author': contributor_name,
                    'Binding': binding,
                    'LC Subjects': lc,
                    'Series': series_id,
                    'Target Age Group': age_group,
                    'Dimensions': dimensions,
                    'Page Count': page_count
                }
            }

    # Write the dictionary to a JSON file
    with open('books.json', 'w') as json_file:
        json.dump(books, json_file, indent=4)

    print("Conversion complete. Check 'books.json'.")

# Call the function
parse()
