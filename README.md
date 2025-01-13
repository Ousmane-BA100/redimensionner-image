# Projet : Redimensionnement et Conversion d'Images avec PUSH-PULL en ZeroMQ

## Description
Ce projet implémente un système distribué pour traiter un jeu d'images en utilisant l'architecture PUSH-PULL de ZeroMQ. Il comprend :

- **Un ventilateur (Client)** : Envoie des tâches (images) aux travailleurs.
- **Deux travailleurs** :
  - Un pour redimensionner les images.
  - Un pour les convertir en noir et blanc.
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
|   |-- worker_resize.py  # Travailleur qui redimensionne les images
|   |-- worker_bw.py      # Travailleur qui convertit les images en noir et blanc
|
|   dataset/            # Contient les images à traiter
|
|   output/             # Contient les résultats traités
    |-- bw/             # Images converties en noir et blanc
    |-- resized/        # Images redimensionnées
