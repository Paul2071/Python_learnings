name = input ("What is your name? ")
print("You are one of the few to survive the invasion", name, ", now, can you survive the night? CAPITALISED words are the choices you can make")

answer = input("You come to the end of a muddy path. Do you go LEFT or RIGHT? ").lower()

if answer == "left":
    answer = input("Heading left, you see further signs of the beast that is stalking you. But you seem safe for now. Up ahead is a river. Do you SWIM across or use the BRIDGE? ")

    if answer == "swim":
        print("Swimming the river seems safe. You head across. Half way through, the exertions of the last few days catch up with you and you slip slowly beneath the surface. You lose.")  
    elif answer == "bridge":
        print("As you cross the bridge there are signs of devasation everywhere you look. Smashed cars, broken trees uprooted from the nearby forest and people not as fortunate as yourself. Coming to end of the bridge, your worst fears are realised. The beast stands before you and you know there is no escape. You lose.")  
    else:
        print("You take too long making a decision, you lose.")
           
            
            


elif answer == "right":
    answer = input("Heading right, there is smoke on the horizon that you could make before dark. Nearby is a cabin that you could sleep in overnight. Do you head to the SMOKE or the CABIN? ").lower()

    if answer == "smoke":
        print ("Pressing on through the night, the smoke seems to always be just around the corner. You can hear the beast in the distance, getting closer and closer. Eventually, you reach an encampment of other survivors that welcome you and offer shelter. You are safe. As you fall asleep, you wonder if you have doomed these people by leading the beast here... You win.")

    elif answer == "cabin":
        print ("Sanctuary! Settling in, it is the first time in a few days that you have shelter and are grateful to be out of the elements. Unfortunately, the walls of the cabin are no barrier to the beasts claws. You lose.")

    else:
        print("You take too long making a decision, you lose.")
           
    
else:
    print("Not an option at this time. Try again")


  