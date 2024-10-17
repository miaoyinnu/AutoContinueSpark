


def read_txt():
    with open("count.txt",mode="r") as file:
        count = file.read()

        return count


def write_txt():
    with open("count.txt",mode="r+") as file:
        count_str = file.read()
        count = int(count_str) + 1
        print(count)
        file.seek(0)
        file.write(str(count))
        file.truncate()

