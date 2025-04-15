def identify_hash(hash_string):
    hash_types = {
        32: "MD5",
        40: "SHA-1",
        56: "SHA-224",
        64: "SHA-256",
        96: "SHA-384",
        128: "SHA-512",

    }

    length = len(hash_string)
    hash_type = hash_types.get(length, "Unknown or unsupported hash type")

    print(f"\n[+] Hash: {hash_string}")
    print(f"[+] Identified as: {hash_type}")

if __name__ == "__main__":
    user_input = input("Enter a hash to identify: ")
    identify_hash(user_input.script())