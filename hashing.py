import hashlib
import timeit

# Deterministic
# Chaotic
# Non-reversible

def calculate_hashes():
    start_time = timeit.default_timer()
    end_time = start_time + 20

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
    print("Hashed {:,} times in 20 seconds.".format(counter))
    print("Average of {:,} hashes per second.".format(counter / 20))

