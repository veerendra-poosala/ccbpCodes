#SecretMessage_2

def convert_given_msg_to_secret_msg(given_message):
    
    #1) converting all the chars into lowercase
    given_message = given_message.lower()
    #print(given_message)
    length_of_msg = len(given_message)
    
    
    #creating a dictionary to assign secret message values
    secret_message_dict = {}
    rev = 1 #unicode value of character z
    for i in range(97,122+1):
        forward_char = chr(i) #conveting unicode value to character
        secret_message_dict[forward_char] = str(rev) #adding items to dictionary
        rev = rev+1
    
    secret_message = ""
    for k in range(length_of_msg):
        char = given_message[k]
        condition = char == char.lower() and not(char == char.upper())
        if condition:
            for key,val in secret_message_dict.items():
                if  char == key:
                    secret_message += "-"+val
        else:
            secret_message += " "
    
    #to remove unwanted hypens creating a new list with secret_message 
    new_sec_list = secret_message.split()
    new_sec_msg =" "
    
    for f in range(len(new_sec_list)):
        word = new_sec_list[f].strip("-") #removing hypens using string method strip()
        new_sec_msg += word + " "
            
    new_sec_msg = new_sec_msg.strip(" ") #removing extra spaces
    return new_sec_msg
    
    
given_message = input()
#print(given_message)

secret_message = convert_given_msg_to_secret_msg(given_message)
print(secret_message)