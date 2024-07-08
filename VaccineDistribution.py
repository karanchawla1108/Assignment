# You are asked to create a report generation module for your organisation’s Vaccine Distribution software. The report will consist of heading lines, then one line per entry, and then several summary lines giving the total number of each vaccine type to be sent, and the cost of the total shipment. The lines will be 40 characters long.

# A report is generated for each site. As well as asking the user for the site name, you will ask details about the requested order for each vaccine:

# the type of vaccine (e.g., Moderna, Pfizer or AstraZeneca);
# the number of vaccines requested of that type; and
# the shipping fee for 100 doses of the vaccine.
# Note that, since the vaccines are shipped in batches of 100, the shipping fee applies even to partial batches with fewer than 100 doses.

# If the name of the vaccine is empty (the user just presses Enter) it means there are no more items and you will instead ask the user for the amount of cash paid.

# Once all these details are collected, you should print a shipping order report. The formatting of the report must be as follows:

# The first heading line has to say the company name, Vaccines2U, on the left in upper case, then spaces, then ‘SHIPPING ORDER’ on the right. The second heading line has to say ‘VAT GB123456789’ of the left and site location (in upper case) on the right.
# There must be a blank line between the heading lines and the items.
# The item lines must have 25 columns for the vaccine name, 5 columns for the quantity sold (an integer) and 10 columns for the shipping price (the quantity times the shipping price; with two decimal places). The vaccine name must be printed in uppercase.
# Above the item lines you should print the table headings, "Vaccine", "Qty." and "Cost", aligned to the column data.
# There must be a blank line between the items and the summary lines.
# The summary lines must be, in order: (i) ‘TOTAL’ in 30 columns followed by the total in 10 columns (with two decimal places), and similarly for (ii) ‘VAT INCLUDED IN TOTAL’, (iii) ‘CASH PAID’ and (iv) ‘CHANGE’. The VAT included in the total is calculated using the standard rate of 20%.
# Sample session with the program:

# Vaccination site? Jameson House
# Vaccine type? AstraZeneca
# Number of vaccines requested? 70000
# Shipping fee per 100 doses? 1.25
# Vaccine type? Pfizer
# Number of vaccines requested? 85000
# Shipping fee per 100 doses? .9
# Vaccine type? 
# Cash paid? 3000
# VACCINES2U                SHIPPING ORDER
# VAT GB123456789            JAMESON HOUSE
# ​
# Vaccine                   Qty.      Cost





site_name = str(input("Vaccination site? "))

vaccine_records = []

# Exit the loop if vaccine_typ is empty.
while True:
    vaccine_typ = str(input("Vaccine type? ").upper())

    if not vaccine_typ:
        break

    num_vaccine = int(input("Number of vaccines requested? "))
    ship = float(input("Shipping fee per 100 doses? "))

    # Calculate the cost and add to the vaccine_records.
    cost = num_vaccine / 100 * ship
    record = (vaccine_typ, num_vaccine, cost)
    vaccine_records.append(record)

cash = float(input("Cash paid? "))
print("VACCINES2U                SHIPPING ORDER")
print(f"VAT GB123456789            {site_name.upper()}")
print()
print("Vaccine                   Qty.      Cost")

# Print vaccine record.
for record in vaccine_records:
    print(f"{record[0]:25}{record[1]:<9}{record[2]:.2f}")

# Calculate the total amount.
total_cost = sum(record[2] for record in vaccine_records)

# Print summary lines.
print()
print(f'TOTAL{" "*28}{total_cost:.2f}')
vat = total_cost - (total_cost / (1 +0.2))
print(f'VAT INCLUDED IN TOTAL{" "*13}{vat:.2f}')
print(f'CASH PAID{" "*24}{cash:.2f}')
change = cash - total_cost
print(f'CHANGE{" "*27}{change:.2f}')

