from os import system
from time import sleep
lett_morse = {"A":".-" , "B":"-..." , "C":"-.-." , "D":"-.." , "E":"." , "F":"..-." , "G":"--." , "H":"...." , "I":".." , "J":".---" , "K":"-.-" , "L":".-.." , "M":"--" , "N":"-." , "O":"---" , "P":".--." , "Q":"--.-" , "R":".-." , "S":"..." , "T":"-" , "U":"..-" , "V":"...-" , "W":".--" , "X":"-..-" , "Y":"-.--" , "Z":"--.." , "1":".----" , "2":"..---" , "3":"...--" , "4":"....-", "5":"....." , "6":"-...." , "7":"--..." , "8":"---.." , "9":"----." , "0":"-----" , " ":"  "}
#morse_lett = {".-":"A" , "-...":"B" , "-.-.":"C" , "-..":"D" , ".":"E" , "..-.":"F" , "--.":"G" , "....":"H" , "..":"I" , ".---":"J" , "-.-":"K" , ".-..":"L" ,  ,  ,  ,  ,  ,  ,  ,  }
morse_lett = {}
for i in lett_morse.keys():
    morse_lett.update({lett_morse[i]: i})
def print_result(type,invalid,string):
    """prints out the resulting string, checks for invalidation, displays accordingly"""
    if type == "morse":
        str1 = "(???)"
        num1 = 0.1
        str2 =  "Morse"
    else:
        str1 = "(?)"
        num1 = 0.3
        str2 =  "Text"
    if invalid:
        print(f"Invalid Charachters detected, replaced with {str1}")
    print(f"{str2}: ",end="")
    for i in range(len(string)):
        print(string[i],end="", flush=True)
        sleep(num1)
    print()
def text_to_morse(string,lett_morse,invalid):
    """asks the user for the message , then converts it to morse code and returns the converted message
    and wether there were any invalid charachters or not"""
    message = input("Enter Text: ")
    message_arr = [a.upper() for a in message]
    for ell in message_arr:
        if lett_morse.get(ell) != None:
            string += lett_morse.get(ell)
        else:
            invalid = True
            string += "(???)"
        string += " "
    return string, invalid
def morse_to_string(message_arr,string,invalid,morse_lett):
    """asks the user for the morse code message , then converts it to text and returns the converted message
    and wether there were any invalid charachters or not"""
    message = input("Enter Morse code: ")
    while True:
        if " " in message:
            if not (message[0] == message[1] == " "):
                message_arr.append( message[:message.index(" ")])
                message = message[message.index(" ")+1:]
                print(message)
            else:
                message_arr.append("  ")
                message = message[message.index(" ")+2:]
        else:
            if len(message) != 0:
                message_arr.append(message)
            break
    for ell in message_arr:
        if morse_lett.get(ell) != None:
            string += morse_lett.get(ell)
        else:
            invalid = True
            string += "(?)"
    return string, invalid
def set_up():
    """sets up all the variables to their default state, 
    gives the user the menu and returns the default variables and their decision in the menu"""
    string = ""
    invalid = False
    message_arr =[]
    while True:
        decision = input("""
                Menu
        1) Morse -> Text
        2) Text -> Morse
        3) Exit
        Choose option: """)
        if decision.isdigit() and 0<int(decision)<4:
            system("cls")
            decision = int(decision)
            sleep(1)
            break
        else:
            print("Invalid")
            sleep(1)
            system("cls")
    return decision,string,invalid,message_arr
def main():
    """asks the user whether they want to convert text to morse, morse to text, or exit the programs,
    then it asks them for the message that they chose to convert, and displays the converted message,
    if there were any invalid charachters it replaces them with question marks,
    after that it returns to the menu and the user may choose to translate a new message"""
    while True:
        decision,string,invalid,message_arr = set_up()
        if decision == 1:
            print("""
            Directions:

            type dashes with - and dots with .
            Do not start with a space
            Type single spaces between letters
            Type triple spaces between words
        

            """)
            string,invalid = morse_to_string(message_arr,string,invalid,morse_lett)
            print_result("text",invalid,string)
        elif decision == 2:
            string,invalid = text_to_morse(string,lett_morse,invalid)
            print_result("morse",invalid,string)
        elif decision == 3:
            break
    print("GOODBYE!!!")

if __name__ == "__main__":
    main()