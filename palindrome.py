"""A program that asks the user for one or more sentences and then lets the user know if it is a palindrome."""
import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    sentence = re.sub(r'[^A-Za-z]', '', sentence.lower())
#looping version
    for i in range(0,int(len(sentence)/2)):
        if sentence[i] != sentence[len(sentence)-1-i]:
            #print(i)
            return False
    return True

#recursive version
"""    if len(sentence) <= 1:
        return True
    elif sentence[0] == sentence[-1]:
        return is_palindrome(sentence[1:-1])
    return False"""



def main():
    # TODO: put your input/output code here
    sen = "No, sir, away. A papaya war is on!"#input("Please enter a sentence\n>>>")
    #print(re.sub(r'[^A-Za-z]', '', sen.lower()))
    print(is_palindrome(sen))



    pass


if __name__ == '__main__':
    main()
