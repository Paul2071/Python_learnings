print("Welcome to my book quiz")


playing = input("Type yes if you want to play, no if you don't! ")

if playing.lower() != "yes":
    quit()

print("Cool, let's play!")

score = 0

answer = input("Who wrote Name of the Wind? ")
if answer.lower() == "patrick rothfuss":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Heathcliff is a character from which novel by Emily Bronte? ")
if answer.lower() == "wuthering heights":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("In Lord of the Rings, what is Frodo's last name? ")
if answer.lower() == "baggins":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the name of the author with the most published books? ")
if answer.lower() == "ryoki inoue":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Finish this Alice in Wonderland quote - 'How long is forever? Sometimes, just one ___' ")
if answer.lower() == "second":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print("You scored a total of " + str(score))
print("which equals " + str((score / 5) * 100) + "% ")
