# workers/worker_bw.py
import zmq
from PIL import Image
import os

OUTPUT_PATH = "output/bw"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

def main():
    context = zmq.Context()

    # PULL socket pour recevoir les tâches
    receiver = context.socket(zmq.PULL)
    receiver.connect("tcp://192.168.1.10:5557")  # Adresse du ventilator

    # PUSH socket pour envoyer les résultats
    sender = context.socket(zmq.PUSH)
    sender.connect("tcp://192.168.1.10:5558")  # Adresse du broker

    print("Worker 2 (Noir et Blanc) connecté...")
    while True:
        task = receiver.recv_string()  # Chemin de l'image
        try:
            # Conversion en noir et blanc
            with Image.open(task) as img:
                img_bw = img.convert("L")
                output_file = os.path.join(OUTPUT_PATH, os.path.basename(task))
                img_bw.save(output_file)
                print(f"Image convertie en noir et blanc : {output_file}")
                sender.send_string(f"Image noir et blanc : {output_file}")
        except Exception as e:
            print(f"Erreur lors du traitement de {task} : {e}")

if __name__ == "__main__":
    main()
