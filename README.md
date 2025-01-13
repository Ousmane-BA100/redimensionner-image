# redimensionner-image
# Projet : Redimensionnement et Conversion d'Images avec PUSH-PULL en ZeroMQ

## Description
Ce projet implémente un système distribué pour traiter un jeu d'images en utilisant l'architecture PUSH-PULL de ZeroMQ. Il comprend :

- **Un ventilateur (Client)** : Envoie des tâches (images) aux travailleurs.
- **Deux travailleurs** :
  - Chaque travailleur traite les images en les redimensionnant et en les convertissant en noir et blanc.
- **Un collecteur (Sink)** : Récupère les résultats traités.

Le projet inclut également un dossier `output` pour stocker les images résultantes.

---

## Structure du Projet

```plaintext
redimensionner-image/
|   broker/
|   |-- sink.py         # Collecteur qui récupère les résultats des travailleurs
|
|   client/
|   |-- ventilator.py   # Ventilateur qui envoie les tâches
|
|   workers/
|   |-- worker.py       # Travailleurs qui redimensionnent et convertissent les images
|
|   dataset/         # Contient les images à traiter
|
|   output/          # Contient les résultats traités
    |-- bw/             # Images converties en noir et blanc
    |-- resized/        # Images redimensionnées
```

---

## Prérequis

- **Python 3.x**
- Bibliothèques Python nécessaires :
  ```bash
  pip install pyzmq pillow
  ```

---

## Instructions d’Exécution

### Étape 1 : Préparer les fichiers

- Placez vos images dans le dossier `dataset/`.
- Assurez-vous que les dossiers `output/bw/` et `output/resized/` existent.

### Étape 2 : Lancer les composants

#### 1. Lancer le Sink (Collecteur)
Le Sink doit être démarré en premier :
```bash
python broker/sink.py
```

#### 2. Lancer les Travailleurs
Chaque travailleur doit être démarré sur une machine différente. Pour lancer un travailleur :
```bash
python workers/worker.py
```
Répétez cette commande sur chaque machine attribuée aux travailleurs.

#### 3. Lancer le Ventilateur (Client)
Lancez le ventilateur pour envoyer les tâches :
```bash
python client/ventilator.py
```

---

## Fonctionnement

1. **Ventilateur (Client)** :
   - Lit les images du dossier `dataset/` et les envoie aux travailleurs via un socket `PUSH`.

2. **Travailleurs** :
   - Reçoivent les tâches via un socket `PULL`.
   - Redimensionnent les images et les convertissent en noir et blanc.
   - Envoient les résultats au Sink via un socket `PUSH`.

3. **Sink** :
   - Reçoit les images traitées et les sauvegarde dans le dossier `output/`.

---

## Tester sur une seule machine
Pour simuler une exécution distribuée sur une seule machine, ouvrez plusieurs terminaux et :

1. Lancez le Sink dans le premier terminal.
2. Lancez deux instances du travailleur (un par terminal).
3. Lancez le ventilateur dans un autre terminal.

---

## Résultats
- Les images converties en noir et blanc sont sauvegardées dans `output/bw/`.
- Les images redimensionnées sont sauvegardées dans `output/resized/`.

---

## Notes
- Vous pouvez configurer les adresses IP des sockets ZeroMQ dans les fichiers correspondants pour tester sur un réseau local.
- Assurez-vous que toutes les machines sont connectées au même réseau pour une exécution distribuée.

---

## Auteur
Ce projet a été développé pour illustrer le parallélisme des tâches en utilisant ZeroMQ et Python.
