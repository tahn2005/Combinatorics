from itertools import combinations

def listallcombos(char_set, k):
    allcombos = combinations(char_set, k)
    for combos in allcombos:
        print(''.join(combos))


def main():
    pool = ['M', 'A', 'R', 'K', 'O', 'V']

    i = 4
    listallcombos(pool, i)

if __name__ == "__main__":
    main()
