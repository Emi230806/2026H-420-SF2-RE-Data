# Définition d'un dictionnaire

Un dictionnaire informatique est un type de structure de données qui associe des clés à des valeurs.

> [!NOTE]
> Une clé correspond à l'élément dont on souhaite associer une valeur.
> Par exemple, dans ce cas-ci, on assigne la valeur « Wayne » à la clé « nom »:       
        dict(clé: valeur) -----> dict('nom': 'Wayne')


## Les opérations principales

- `dict()` permet de créer un dictionnaire.
- `.get()` permet d'accéder à la valeur associée à une clé dans un dictionnaire tout en évitant une erreur.
- `.copy()` crée une copie surperficielle d'un dictionnaire.

    > [!NOTE]
    > `.copy()` est essentielle pour éviter les modifications accidentelles de l'original lorsqu'on travaille avec des copies.

- `.pop()` supprime une clé et retourne sa valeur

    > [!NOTE]
    > Par exemple,
    > etudiants = {"Alice": 15, "Bob": 12, "Charlie": 17}
    > note_bob = etudiants.pop("Bob")
    > print(note_bob)       # note_bob devrait retourner 12

- `.clear()` permet de supprimer tous ses éléments et de le vider complètement. (ne prend aucun paramètre)
- `.keys()` retourne toutes les clés de ce dictionnaire dans une liste. (ne prend aucun paramètre)
- `.values()` retourne toutes les valeurs de ce dictionnaire dans une liste. (ne prend aucun paramètre)
- `.items()` retourne toutes les paires clés-valeurs de ce dictionnaire dans un tuple. (ne prend aucune valeur)
- `.update()` permet de fusionner un dictionnaire avec un autre, en écrasant les clé existntes et en ajoutant les nouvelles clés.

    > [!NOTE]
    > Par exemple,
    > auto = {"marque": "Ford", "model": "Mustang", "année": 1964}
    > auto.update({"couleur": "Blanche"})
    > print(auto)           # auto devrait retourner {'marque': 'Ford', 'model': 'Mustang', 'année': 1964, 'couleur': 'Blanche'}


## Avantages et désavantages

| Avantages | Désavantages |
| :--- | ---: |
| Accès rapide aux valeurs |Les clés ne sont pas rangées (elles ne se mettent pas automatiquement en ordre alphabétique)|
| Flexibilité, peut être de n'importe quel type | L'insertion d'une nouvelle clé peut être complexe, surtout si la clé est déjà existante |

## Utilisations courantes

- Accès rapide aux données (Les dictionnaires permettent un acc`s rapide aux valeurs via des clés)
- Stockage dynamique (Ils peuvent être utilisés pour stoker des valeurs dans une seule clé, augmentant leur utilité dans divers algorithmes et applications)
- Création de structures de données (Les dictionnaires sont souvent utilisés pour créer des structure de données dynamiques comme des dictionnaires des villes et leur population)

