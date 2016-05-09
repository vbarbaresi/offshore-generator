import csv
import json
import re

nodes = open("Entities.csv", "r")
reader = csv.reader(nodes, delimiter=",", quotechar='"')

fishy_suffixes = [
    "Limited",
    "Ltd",
    "Ltd.",
    "Co.",
    "Assets",
    "Corporation",
    "Holdings",
    "Holding",
    "Corp.",
    "Corp",
    "Inc.",
    "Inc",
    "Fund",
    "Fund Management",
    "Strategy Fund",
    "International",
    "Technology",
    "Company",
    "Services",
    "Trading",
    "Consulting",
    "Investments",
    "Investment",
    "Group",
    "S.A.",
    "Pension Plan"]

types = set()
names = set()
addresses = set()
next(reader, None)  # skip header
for row in reader:
    try:
        row[0].decode("ascii")  # keep only ascii companies
    except UnicodeDecodeError:
        continue
    name = row[0]
    name = re.sub("\(.*\)", "", name)
    name = re.sub("\(.*$", "", name)  # A few names have unmatched parenthesis, mildly infuriating
    for suffix in fishy_suffixes:
        name = name.replace(suffix, "")
        name = name.replace(suffix.lower(), "")
        name = name.replace(suffix.upper(), "")
    name = re.sub("\s+", " ", name).strip()
    name = name.replace(" .", "")
    name = name.replace(" ,", "")
    for elem in name.split():
            names.add(elem.strip().title())
    types.add(row[5])
    addresses.add(row[6].replace(row[0], ""))  # name is contained in the address

# Remove an eventual empty element, instead of checking during the loop
for data in (types, names, addresses):
    data.discard("")

print("Extracted: ")
print("{} types".format(len(types)))
print("{} names".format(len(names)))
print("{} addresses".format(len(addresses)))

with open("names.json", "w") as f:
    json.dump(list(names), f)
with open("types.json", "w") as f:
    json.dump(list(types), f)
with open("addresses.json", "w") as f:
    json.dump(list(addresses), f)

