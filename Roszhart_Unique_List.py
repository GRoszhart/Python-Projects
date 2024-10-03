print("Welcome to the Unique List Program.")
print()
print("This program tests if a sequence of positive numbers is unique.")
print()

InputNumber = 0
InputSequence = []

while InputNumber != -1:
    InputNumber = int(input("Enter a positive number or -1 to quit: "))
    if InputNumber > 0:
        InputSequence.append(InputNumber)

print()

InputSet = set(InputSequence)

if len(InputSequence) != len(InputSet):
    print("The positive sequence {} is not unique.".format(InputSequence))
else:
    print("The positive sequence {} is unique.".format(InputSequence))

print()
print("Thanks for using my Unique List Program.")