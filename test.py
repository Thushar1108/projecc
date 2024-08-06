def leap(n):
    if n % 4 == 0 and n % 400 == 0:
        print("True")
    elif n % 4 == 0 and n % 100 == 0:
        print("False")
    elif n % 4 != 0:
        print("False")
while True:
    print(leap(int(input("Enter the year: "))))