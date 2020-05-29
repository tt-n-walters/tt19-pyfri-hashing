import hashlib
import timeit
import multiprocessing


def hash(name):
    # Encode our input
    encoded = name.encode("utf-8")
    # Hash our encoding
    hashed = hashlib.md5(encoded)
    # Get the digest of the hash
    digest = hashed.hexdigest()
    return digest


def calculate_hashes():
    start_time = timeit.default_timer()
    end_time = start_time + 10

    name = "Mico"
    counter = 0

    print("Starting hashes.")
    while timeit.default_timer() < end_time:

        counter += 1

    print("Finished hashes.")
    print("Hashed {:,} times in 10 seconds.".format(counter))
    print("Average of {:,} hashes per second.".format(counter / 10))


if __name__ == "__main__":
    # # Create an appropriate number of processes
    # processes = []
    # for _ in range(6):
    #     process = multiprocessing.Process(target=calculate_hashes)
    #     processes.append(process)

    # # Start each process
    # for process in processes:
    #     process.start()

    for password in open("rockyou.txt", encoding="latin-1"):
        password = password.strip()
        if password == "walters":
            print("Found it!")
            break
    else:
        print("Doesn't exist!")
