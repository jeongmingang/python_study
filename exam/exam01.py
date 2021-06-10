def gugu_dan():
    for second in range(1, 10):
        for first in range(2, 10):
            print('{} * {} = {}'.format(first, second, first * second), end='\t')
        print()


if __name__ == "__main__":
    gugu_dan()



