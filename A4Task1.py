try:
    fh = open("sample.txt", "r")
    print("Reading File content:")
    for i, line in enumerate(fh, 1):
        print(f"line {i}:{line.strip()}")
    fh.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
