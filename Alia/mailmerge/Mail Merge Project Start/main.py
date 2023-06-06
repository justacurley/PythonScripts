#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
template = open("Input/Letters/starting_letter.txt")
starting_template = template.read()
with open("Input/Names/invited_names.txt") as nameys:
    for name in nameys.readlines():  
        name = name.strip()  
        current_template = starting_template
        current_template = current_template.replace('[name]',name)
        output = open(f"Output/ReadyToSend/{name}.txt","w")
        output.write(current_template)
        output.close()
template.close()

