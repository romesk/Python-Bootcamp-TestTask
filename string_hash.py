import hashlib


def hash_string(string: str, algorithm: str = "sha256") -> str:
    """
    Hash a string.
    :param string: string to hash
    :param algorithm: hashing algorithm. Default: "sha256"
    :return: hashed string
    """

    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"No algorithm found named '{algorithm}'. Possible values: {hashlib.algorithms_available}.")

    h = hashlib.new(algorithm)
    h.update(string.encode())
    return h.hexdigest()


def main() -> None:
    hashed = hash_string('Python Bootcamp')
    print(hashed)


if __name__ == '__main__':
    main()
