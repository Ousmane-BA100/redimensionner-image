# client/ventilator.py
import zmq
import os
import time

DATASET_PATH = "dataset/mscoco_train2014_148images"

def main():
    context = zmq.Context()

    # PUSH socket pour envoyer les tâches
    socket = context.socket(zmq.PUSH)
    socket.bind("tcp://*:5557")  # Bind sur localhost ou réseau

    print("Client ventilator démarré : envoi des tâches aux workers...")
    images = [img for img in os.listdir(DATASET_PATH) if img.endswith((".jpg", ".png"))]

    for image in images:
        task = os.path.join(DATASET_PATH, image)
        socket.send_string(task)
        print(f"Tâche envoyée pour l'image : {image}")
        time.sleep(0.1)

    print("Toutes les tâches ont été envoyées.")
    context.term()

if __name__ == "__main__":
    main()
