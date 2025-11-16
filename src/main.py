import time

def main():
    print("Tower-Guard is alive and running...")

    try:
        while True:
            print("Tower-Guard heartbeat: container is alive.")
            time.sleep(10)  # heartbeat every 10 seconds for testing
    except KeyboardInterrupt:
        print("Shutting down Tower-Guard gracefully.")

if __name__ == "__main__":
    main()
