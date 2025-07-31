import example

def main():
    result= example.pi()
    print(result)  # Output: 3.14159

    result = example.square_root(16)
    print(result)  # Output: 4.0

    result = example.power(2, 3)
    print(result)  # Output: 8.0

    example.main()
    # print(result)  # Output: 120

# print(__name__)  # Output: __main__
if __name__ == "__main__":
    main()