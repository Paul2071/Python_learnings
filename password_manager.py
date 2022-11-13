master_password = input ("What is the master password? ")

#this is how you define a function in python. When you call view(), you will do whatever is indented 
#for is a for loop, with each element called "line"
#each element is then stripped of formatting (in this case the break carriage) and stored in the variable data
#data is the split aloing the pipe operator- as there is account|password, data will look like data = ["account", "password"]
# then we assing each element in the data array to user and user_pw
def view ():
    with open("passwords.txt", "r") as f:
       for line in f.readlines():
           data = line.rstrip()
           user, user_pw = data.split("|")
           print("Account:", user, "| Password:", user_pw,)
           
           

def add():
    name = input ("Account name: ")
    password = input ("Password: ")

    #"with" will automatically close the file afterwards
    # can write as file = open("passwords.txt", "a") but file will stay open 
    # open will open the file given, the main modes are w, r and a
    # w = write create a new file or override if already exists (clear the existing file)
    # r = read mode. cant write anything into it, just read it.
    # a = append. add something to end of existing file, create new file if doesnt exist.
    with open("passwords.txt", "a") as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input ("Would you like to add a new password or view existing? Type VIEW or ADD or Q to quit ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue