# num = 1


# for i in range(1, 10):
#     num += 2
#     print(num)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    for num in range(1, 100):
        if is_prime(num):
            print(num, end=", ")

if __name__ == "__main__":
    main()
