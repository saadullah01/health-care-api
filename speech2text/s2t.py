import getopt
import queue
import sys
import threading
import time

# api call queue & lock
task_q = queue.Queue()
lock_q = threading.Lock()

# Flag to end threads
task_done = 0

# Speech-to-text simulating function
def speech2text():
    while not task_done:
        # Getting item from the queue by acquiring lock
        lock_q.acquire()
        item = task_q.get()
        lock_q.release()
        print("item " + str(item) + " processing")
        time.sleep(5)
        print("item " + str(item) + " done")

# Main function
def main(argv):
    '''
        Function to get arguments for number of cores and 
        threads per core to run multiple threads and handle
        the specific number of api requests at a time
    '''
    num_of_cores = None
    threads_per_core = None
    num_API_requests = None

    try:
        opts, _ = getopt.getopt(argv, "h:c:t:n:", ["help", "cores", "threads", "num"])
    except:
        print("python3 s2t.py -c <number_of_cores> -t <threads_per_core> -n <number_of_API_requests>")
        sys.exit(1)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print("python3 s2t.py -c <number_of_cores> -t <threads_per_core> -n <number_of_API_requests>")
            sys.exit(2)
        elif opt in ('-c', '--cores'):
            num_of_cores = int(arg)
        elif opt in ('-t', '--threads'):
            threads_per_core = int(arg)
        elif opt in ('-n', '--num'):
            num_API_requests = int(arg)

    num_of_threads = num_of_cores * threads_per_core
    threads = []

    # initializing requests
    for _ in range(num_of_threads):
        t = threading.Thread(target=speech2text)
        threads.append(t)
        t.start()

    # initializing API requests
    for item in range(num_API_requests):
        task_q.put(item)

    # Wait till the queue is empty
    while not task_q.empty():
        pass

    # Flag to kill all threads
    global task_done
    task_done = 1

    # Joining all threads
    for t in threads:
        t.join()

if __name__ == "__main__":
    main(sys.argv[1:])