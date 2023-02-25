#SecretMessage_1

def convert_given_msg_to_secret_msg(given_message):
    
    #1) converting all the chars into lowercase
    given_message = given_message.lower()
    #print(given_message)
    length_of_msg = len(given_message)
    
    
    #creating a dictionary to assign secret message values
    secret_message_dict = {}
    rev = 122 #unicode value of character z
    for i in range(97,122+1):
        forward_char = chr(i) #conveting unicode value to character
        rev_char = chr(rev)
        secret_message_dict[forward_char] = rev_char #adding items to dictionary
        rev = rev -1
    
    secret_message = ""
    for k in range(length_of_msg):
        char = given_message[k]
        condition = char == char.lower() and not(char == char.upper())
        if condition:
            for key,val in secret_message_dict.items():
                if  char == key:
                    secret_message += val
        else:
            secret_message += char
    
    return secret_message
    
    
given_message = input()
#print(given_message)

secret_message = convert_given_msg_to_secret_msg(given_message)
print(secret_message)