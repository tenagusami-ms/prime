# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    integers = list(range(2, 100))
    primes = list()

    primes.append(integers[0])
    integers2 = [i for i in integers if i % 2 != 0]

    primes.append(integers2[0])
    integers3 = [i for i in integers2 if i % 3 != 0]

    primes.append(integers3[0])
    integers4 = [i for i in integers3 if i % 5 != 0]

    print(integers)
    print(integers2)
    print(integers3)
    print(integers4)
    print(primes)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
