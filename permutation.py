from itertools import permutations
def main():
    sequence = ['0', '0', '0', '0', '1', '1', '1']
    allpermutations = set(permutations(sequence))

    for perm in sorted(allpermutations):
        print(''.join(perm))

if __name__ == "__main__":
    main()
