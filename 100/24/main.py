#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def new_letter(name):
    with open("Input/Letters/starting_letter.txt") as template:
        blank=template.read()
        return blank.replace("[name]",name)
        


with open("Input/Names/invited_names.txt") as names:
    for name in names:
        name=name.strip()
        letter = new_letter(name)
        path = f"Output/ReadyToSend/invite_for_{name}.txt"
        with open(path,"w") as output:
            print(name)
            output.write(letter)
