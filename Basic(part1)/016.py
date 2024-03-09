n = int(input("Enter with a number: "))
def diff(n):
    if (n <= 17):
        return 17 - n
    else:
        return (n - 17) * 2

print(diff(n))