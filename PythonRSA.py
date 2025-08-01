def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_coprime(f):
    for d in range(2, f):
        if gcd(d, f) == 1:
            return d


def modinv(a, m):
    # Extended Euclidean Algorithm
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def rsa_encrypt_decrypt():
    answer = int(input("Eng = 1 or Rus = 2: "))
    if answer == 1:
        abc = "abcdefghijklmnopqrstuvwxyz"
    elif answer == 2:
        abc = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    abc_dict = {c: i + 1 for i, c in enumerate(abc)}
    rev_abc_dict = {i + 1: c for i, c in enumerate(abc)}

    msg = input("\nEnter a message: ").lower()
    X = [abc_dict[c] for c in msg if c in abc_dict]

    print("X:", X)

    p = int(input("\nChoose prime p: "))
    q = int(input("\nChoose prime q > p: "))

    while q <= p or p == 2 and q == 3 or p == 2 and q == 5 or p == 2 and q == 7 or p == 3 and q == 5:
        print("Invalid numbers. Try again.")
        p = int(input("\nChoose prime p: "))
        q = int(input("\nChoose prime q > p: "))

    n = p * q
    f = (p - 1) * (q - 1)
    print("\nn=", n)
    print("f=", f)

    d = find_coprime(f)
    e = modinv(d, f)

    Y = [(x**e) % n for x in X]
    X1 = [(y**d) % n for y in Y]

    decrypted_msg = "".join(rev_abc_dict.get(x, "?") for x in X1)

    print("d:", d)
    print("e:", e)
    print("\nEncrypted (Y):", Y)
    print("\nDecrypted (X1):", X1)
    print("\nDecrypted message:", decrypted_msg)


if __name__ == "__main__":
    rsa_encrypt_decrypt()

input("\nPress Enter to exit...")