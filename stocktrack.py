from setup import initialize
import os


def main():
    for file in ["stocks.csv", "tranasctions.csv", "properties.ini"]:
        if not os.path.exists(file):
            initialize()
            break


if __name__ == "__main__":
    main()


        
            