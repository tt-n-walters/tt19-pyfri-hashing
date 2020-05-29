import hashlib


name = "Nico"

# Encode our input
encoded = name.encode("utf-8")

# Hash our encoding
hashed = hashlib.md5(encoded)

# Get the digest of the hash
digest = hashed.hexdigest()

print(digest)