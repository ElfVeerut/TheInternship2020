


hangman = []
score = 0
set_digit = int(input("Insert 12 digit number: "))

while len(str(set_digit)) != 12:
    set_digit = int(input("Insert 12 digit number: "))

for i in range(12):
    hangman.append("_")

print (" ".join(hangman))

for _ in range(5):
    input_digit = int(input('Guess number from 0-9: '))
    while input_digit not in range(0,10):
        input_digit = int(input('Guess number from 0-9 again:'))
    if str(input_digit) not in str(set_digit):
        hangman.append(str(input_digit))
    for i in range(12):
        
        if str(input_digit) == str(set_digit)[i]:
            hangman[i] = str(input_digit)
            score += 1
        
    print (" ".join(hangman))
print (f"score: {score}")

    

