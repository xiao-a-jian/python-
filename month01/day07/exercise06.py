"""
    ######
    ******
    ######
    ******
    ######
    ******
    ######
"""
for r in range(7):
    for c in range(6):
        if r % 2 == 1:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
