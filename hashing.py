import hashlib
import timeit

# Deterministic
# Chaotic
# Non-reversible

start_time = timeit.default_timer()
end_time = start_time + 5

name = "Mico"
counter = 0

while timeit.default_timer() < end_time:
    # Encode our input
    encoded = name.encode("utf-8")
    # Hash our encoding
    hashed = hashlib.md5(encoded)
    # Get the digest of the hash
    digest = hashed.hexdigest()
    counter += 1



print(digest)