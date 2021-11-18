import time

def console_print(console_text):
    """Especial print by Darkrayyss.

   Print with a special format

   Parameters:
   A text to print
   """
    print("\n\t|"+console_text+"|\n")
    time.sleep(0.9)
    return

def getkey():                   
    key = None
    key = input("Select your option: ")
    while (key not in "0123456789") or (key == '\0') or (key == ''):
        console_print("Please select a valid option")
        key = input("Select your option: ")
    return int(key)