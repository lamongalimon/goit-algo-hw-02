from queue import Queue
import random

queue = Queue()

def generate_request():
    request = random.randint(1, 100) 
    queue.put(request)

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Обробка заявки: {request}")
    else:
        print("Черга пуста")

def main():
    for _ in range(10):
        generate_request()

    while not queue.empty():
        process_request()

if __name__ == "__main__":
    main()