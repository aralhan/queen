import itertools

NO_OF_ROWS = 8
ps = list(itertools.permutations(range(NO_OF_ROWS)))
cols = list(range(NO_OF_ROWS))
result = []


def check_is_diagonal(p):
    for r1, c1 in enumerate(p):
        for r2, c2 in enumerate(p):
            if r1 == r2 and c1 == c2:
                continue
            else:
                if abs(r1-r2) == abs(c1-c2):  
                    # if no of rows and no cols offset is same then they are at each other diagonal
                    return False
    return True


def solve():
    for p in ps:
        if check_is_diagonal(p):
            result.append(p)


def main():
    """Initialize and solve the n queens puzzle"""
    solve()
    print(len(result))
    for p in result:
        print(p)

if __name__ == "__main__":
    # execute only if run as a script
    main()
