
Les fichiers JSON de test sont dans resources/ :

architecture_ok.json
architecture_ko.json

Le fichier rule_not_publique_ip.json définit la règle à appliquer.

run_check.py charge la règle et un fichier JSON d’architecture depuis /resources.

engine.py contient la fonction qui teste chaque ressource par rapport à la règle.

run_check.py affiche si chaque ressource respecte ou viole la règle.
ce dépot  contient un moteur minimaliste pour tester UNE SEULE règle de sécurité :

 La base de données ne doit pas avoir d'IP publique.



Comment tester la règle ?

1. Installer Python 3
2. Ouvrir un terminal
3. Aller dans le dossier `engine` :

cd engine

4. Lancer le test :

python run_check.py

 Le script analysera un fichier JSON d’architecture (défini dans `run_check.py`) et affichera si la règle est respectée ou non.

Donc pour tester vos propres fichiers, il suffit de l'ajouter dans le dossier "/resources" : resources/mon_architecture.json

puis dans le fichier "run_check.py", changez la ligne qui charge l’architecture :

architecture = load_json("../resources/mon_architecture.json") 

 et exécutez à nouveau :

python run_check.py


✔ Résultat attendu

Si la base de données n’a pas d’IP publique → OK
Si la base de données a une IP publique → ERREUR

 Objectif

Ce repo permet à l’équipe :

de valider la sécurité de leurs architectures JSON
de préparer l’intégration du moteur dans le projet final

Cette règle rule_not_publique_ip.json va détecter automatiquement si une DB générée a une IP publique.

Cela permet :

d’alerter l’utilisateur avant le déploiement, d’empêcher la génération d’infrastructure non sécurisée. 


