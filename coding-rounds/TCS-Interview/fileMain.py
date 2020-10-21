def main():
    with open("input.txt") as fileObject:
        print(len(fileObject.readlines()))
if __name__ == "__main__":
    main()