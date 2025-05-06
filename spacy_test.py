import spacy
from spacy.pipeline import EntityRuler

import json

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler", before="ner")

stations = []

with open("stations.json", "r") as file:
    data = json.load(file)

for item in data:
    stations.append(item["stationName"].lower())

patterns = [{"label": "STATION", "pattern": name} for name in stations]

ruler.add_patterns(patterns)

user_input = input("You: ")

origin = None
destination = None

doc = nlp(user_input)

for i, token in enumerate(doc):
    if token.text.lower() == "from" and i+1 < len(doc):
        origin = doc[i+1].text
    if token.text.lower() == "to" and i+1 < len(doc):
        destination = doc[i+1].text

for ent in doc.ents:
    print(ent.text, ent.label_)

print(doc.text)
print("Origin:", origin)
print("Destination:", destination)
