n1 = int(input("Enter with the first number: ")) 
n2 = int(input("Enter with the second number: ")) 
n3 = int(input("Enter with the third number: ")) 

def soma():
    if (n1 == n2 == n3):
        return (n1 + n2 + n3) * 3
    else:
        return n1 + n2 + n3

print(soma())