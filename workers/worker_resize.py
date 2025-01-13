# workers/worker_resize.py
import zmq
from PIL import Image
import os

OUTPUT_PATH = "output/resized"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

def main():
    context = zmq.Context()

    # PULL socket pour recevoir les tâches
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://localhost:5557")  # Adresse du ventilator

    # PUSH socket pour envoyer les résultats
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://localhost:5558")  # Adresse du broker

    print("Worker 1 (Redimensionnement) connecté...")
    while True:
        task = receiver.recv_string()  # Chemin de l'image
        try:
            # Redimensionner l'image
            with Image.open(task) as img:
                img_resized = img.resize((256, 256))
                output_file = os.path.join(OUTPUT_PATH, os.path.basename(task))
                img_resized.save(output_file)
                print(f"Image redimensionnée : {output_file}")
                sender.send_string(f"Image redimensionnée : {output_file}")
        except Exception as e:
            print(f"Erreur lors du traitement de {task} : {e}")

if __name__ == "__main__":
    main()
