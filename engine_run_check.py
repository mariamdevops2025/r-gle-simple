import json
from check_rule import check_rule
import os

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

# Charger la règle 
rule = load_json("../rule_not_public_ip.json")

# Choisir l'architecture à tester (modifier pour mettre le nom du fichier à tester )
architecture = load_json("../resources/architecture_ok.json")

print("\n🔍 Vérification de la règle de sécurité\n")

for resource_id, resource in architecture.items():
    result = check_rule(resource, rule)

    if result is None:
        continue  # règle non applicable

    status, message = result
    if status:
        print(f"✔ {resource_id} : OK")
    else:
        print(f"❌ {resource_id} : {message}")
