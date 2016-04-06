import csv
import json
import codecs
import re

nodes = open("nodesNW.csv", "r")
reader = csv.reader(nodes, delimiter=";", quotechar='"')

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
for row in reader:
    if row[1].lower() == "entity":
        name = row[2]
        name = re.sub("\(.*\)", "", name)
        name = re.sub("\(.*$", "", name)  # A few names have unmatched parenthesis, mildly infuriating
        for suffix in fishy_suffixes:
            name = name.replace(suffix, "")
            name = name.replace(suffix.lower(), "")
            name = name.replace(suffix.upper(), "")
        name = re.sub("\s+", " ", name).strip()
        name = name.replace(" .", "")
        name = name.replace(" ,", "")
        names.add(name.strip())
        types.add(row[7])
        addresses.add(row[3].replace(name, ""))  # name is contained in the address
        #from IPython import embed; embed()

# Remove an eventual empty element, instead of checking during the loop
for data in (types, names, addresses):
    try:
        data.remove("")
    except KeyError:
        pass

print "Extracted: "
print "{} types".format(len(types))
print "{} names".format(len(names))
print "{} addresses".format(len(addresses))

with codecs.open("names.json", "w", encoding="utf8") as f:
    f.write(json.dumps(list(names)))
with codecs.open("types.json", "w", encoding="utf8") as f:
    f.write(json.dumps(list(types)))
with codecs.open("addresses.json", "w", encoding="utf8") as f:
    f.write(json.dumps(list(addresses)))
    