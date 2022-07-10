def main():
    x = int(input("x = "))
    print(f"{x} square is", square(x))

def square(n):
    return n ** 2  # pow(n,2) dá no mesmo

main()
