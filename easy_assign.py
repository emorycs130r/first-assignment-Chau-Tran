
'''

This file contains the functions that you need for completing this assignment. 

1. append_two_strings() --> Function to append a string2 to string1. -- 30%
2. append_character() --> Function to append a character to the end of string. -- 30% 
3. append_num_to_string() --> Function to append a number to the end of a string. -- 40%

Failure to follow the variable name guides will lead to reduction of 10 points. 

DO NOT EDIT THE FUNCTION NAMES.


'''

def append_two_strings(string_1, string_2):

    return f"{string_1}{string_2}"



def append_character(string_1, char_1):

    return f"{string_1}{char_1}"
    


def append_num_to_string(string_1, num_1):

    return f"{string_1} {num_1}"
    


if __name__ == "__main__":

    append_two_strings("Hey Vish!", " How you doing?")
    append_character("My day was o" , "k.")
    append_num_to_string( "Guess how many classes I had?" , 4)