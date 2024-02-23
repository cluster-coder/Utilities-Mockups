'''
Given any text, this code will generate a username/password-like combination
'''

from random import choice, randint

#Tweek this text if you want something more custom
defaultText=('''We could not find enough words assoc*()`´[{]}~^;:,.<>/?°iated with Sheep, Sand, Lamb, Wolf.\n
Plea¨&se go back  %and $try an#other topic, or cont@inue to write@ a poem about missing.
      Someday, I may go to wander around the forest and hills, you know, just to get started on looking for these missing people,
      there is also a sheep of mine I really miss, the little lamb was eaten by the wolf
      repeated whole phrase 
      repeated whole phrase 
      repeated whole phrase 
      repeated whole phrase 
      repeated whole phrase 
      repeated whole phrase ''')


def textToUniqueWordTuple(text=defaultText):
    #Receives a text, parses only the alphanumeric characters and returns a tuple with each unique word 
    modifiedText=''

    for character in text:
        if character.isalnum() or character.isspace():
            modifiedText+=character

    AlnumSet=set()
    for word in modifiedText.split():
        AlnumSet.add(word)

    return tuple(AlnumSet)


def randomNameFromTuple(alphanumericTuple):
    #combines two random values from a sequence + a random number and returns it
    a=choice(alphanumericTuple)
    b=choice(alphanumericTuple)
    c=a+b+(str(randint(0,40)))
    print(c)
    return c


if __name__=='__main__':
    uniqueWordTuple = textToUniqueWordTuple(defaultText)
    for i in range(40):     #tweak this number if you want to see more or less
        randomNameFromTuple(uniqueWordTuple)