import json
import random
import bottle
import markov

app = bottle.Bottle()

with open("names.json", "r") as f:
    names = json.loads(f.read())
with open("addresses.json", "r") as f:
    addresses = json.loads(f.read())
with open("types.json", "r") as f:
    types = json.loads(f.read())

markov = markov.Markov(names)

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


@app.route("/")
@bottle.view("offshore.template")
def main_page():
    n_elements = random.randint(1, 3)
    markov_name = markov.generate_markov_text(size=n_elements)
    company_name = "{} {}".format(markov_name, random.choice(fishy_suffixes))
    values = {"name": company_name , "address": random.choice(addresses), "type": random.choice(types)}
    return values

bottle.run(app, server="flup", host='localhost', port=8080)
