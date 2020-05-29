import hashlib
import timeit
import multiprocessing


def calculate_hashes():
    start_time = timeit.default_timer()
    end_time = start_time + 10

    name = "Mico"
    counter = 0

    print("Starting hashes.")
    while timeit.default_timer() < end_time:
        # Encode our input
        encoded = name.encode("utf-8")
        # Hash our encoding
        hashed = hashlib.md5(encoded)
        # Get the digest of the hash
        digest = hashed.hexdigest()
        counter += 1

    print("Finished hashes.")
    print("Hashed {:,} times in 10 seconds.".format(counter))
    print("Average of {:,} hashes per second.".format(counter / 10))


# Create an appropriate number of processes
processes = []
for _ in range(6):
    process = multiprocessing.Process(target=calculate_hashes)
    processes.append(process)

# Start each process
for process in processes:
    process.start()
