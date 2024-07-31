import multiprocessing

def square_numbers(numbers, result_queue):
    for num in numbers:
        result_queue.put(num * num)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result_queue = multiprocessing.Queue()

    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=square_numbers, args=(numbers, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        results.append(result_queue.get())

    print("results", results)