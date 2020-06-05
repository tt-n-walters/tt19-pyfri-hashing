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
        hash(name)
        counter += 1

    print("Finished hashes.")
    print("Hashed {:,} times in 10 seconds.".format(counter))
    print("Average of {:,} hashes per second.".format(counter / 10))


def get_variations(password):
    variations = []
    for i in range(10):
        v = password + str(i)
        variations.append(v)
    print(variations)


if __name__ == "__main__":

    cipher = "5b56830ba7a84275fb1125f327f8ce6c"

    for password in open("rockyou.txt", encoding="latin-1"):
        password = password.strip()
        hashed = hash(password)
        if hashed == cipher:
            print("Found it!", password)
            break
    else:
        print("Doesn't exist!")

