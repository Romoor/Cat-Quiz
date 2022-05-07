# ask user personality questions
# assign them one of my cats based on their answers

# Each asnwer has corresponding cat value (A B C)
# Answers put in array?
# Check to see What is the most common value

from collections import Counter

"Whats ur favorite color"

"Are u missing a body part"

"What do u look like"

colors = {"A": "Black", "B": "Black and white",
          "C": "Greay", "D": "Tan", "E": "Orange and white"}

bodyParts = {"C": "An eye", "D": "A heart", "A": "A brain",
             "E": "I'm only emotionally challenged", "B": "None, I am perfect in any and all ways"}

appearances = {"C": "A fat vaguely sad pirate", "D": "A very gluttonus rattlesnake", "A": "Like I have never had a thought in my life",
               "E": "No one knows my actual appearance. I haven't been seen by anyone since my birth", "B": "A bowling pin in a fursuit"}

phrase = {"C": "*Sad eyes*", "D": "It's not a phase mom", "A": "Steenky",
               "E": "*absolute quiet*", "B": "Kids stop it"}

answerChoices = []


def colorSelectQuiz(colors):
    print(colors)
    colorSelect = input("Select a color from that list (i.e. A) ")
    answerChoices.append(colorSelect)
    return print(colorSelect)


def bodySelectQuiz(bodyParts):
    print(bodyParts)
    bodySelect = input("Select what body part you are missing (i.e. A) ")
    answerChoices.append(bodySelect)
    return print(bodySelect)


def appSelectQuiz(appearances):
    print(appearances)
    appSelect = input(
        "Select an appearance from this list you think describes you (i.e. A) ")
    answerChoices.append(appSelect)
    return print(appSelect)


def phraseSelectQuiz(phrase):
    print(phrase)
    phraseSelect = input(
        "Select your catchphrase (i.e. A) ")
    answerChoices.append(phraseSelect)
    return print(phraseSelect)


colorSelectQuiz(colors)
bodySelectQuiz(bodyParts)
appSelectQuiz(appearances)
phraseSelectQuiz(phrase)


def Most_Common(answerChoices):
    data = Counter(answerChoices)
    answerDict = data.most_common(1)
    keyList = answerDict[0]
    answer = keyList[0]
    if answer.upper() == 'A':
        return print("You're most like Frances!")
    elif answer.upper() == 'B':
        return print("You're most like Freya!")
    elif answer.upper() == 'C':
        return print("You're most like Freddie!")
    elif answer.upper() == 'D':
        return print("You're most like Finn!")
    elif answer.upper() == 'E':
        return print("You're most like Fergie!")
    else:
        return print("Wow! You're a mix!")


Most_Common(answerChoices)
