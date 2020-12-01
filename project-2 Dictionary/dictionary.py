print('WELCOME TO OCTAN3SHELL DICTIONARY')
import json
from difflib import get_close_matches
data= json.load(open("data.json"))


def translate(word):
    word= word.lower()
    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word , data.keys())) > 0:
         print("did u mean %s intead" %get_close_matches(word , data.keys())[0])
         decide=input("press y if yes and press n if not")
         if decide=="y":
             return data [get_close_matches(word , data.keys())[0]]
         elif decide=="n":
             return ("word is not available brahhhhh")
         else:
             return ("wrong choice bud see again")


    else:
        print('word is not available brahhhhh')

word=input("Enter the word you want to search = ")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
