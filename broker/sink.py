# broker/sink.py
import zmq

def main():
    context = zmq.Context()

    # PULL socket pour recevoir les résultats
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5558")  # L'écoute sur localhost ou réseau

    print("Broker (sink) démarré : collecte des résultats...")
    while True:
        result = receiver.recv_string()
        print(f"Résultat reçu : {result}")

if __name__ == "__main__":
    main()
