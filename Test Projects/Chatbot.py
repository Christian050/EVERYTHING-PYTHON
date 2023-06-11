import re
from Packages import longResponse as long



def messageProbability(userMessage, recognizedWords, singleResponse=False, requiredWords=[]):
    messageCertainty = 0
    HasRequiredWords = True

    for word in userMessage:
        if word in recognizedWords:
            messageCertainty += 1

    percentage = float(messageCertainty) / float(len(recognizedWords))
    
    for word in requiredWords:
        if word not in userMessage:
            HasRequiredWords = False
            break
    
    if HasRequiredWords or singleResponse:
        return int(percentage*100)
    else:
        return 0
    
def scanMessages(message):
    HighProbabilityList = {}

    def response(botResponse, ListOfWords, singleResponse=False, requiredWords=[]):
        nonlocal HighProbabilityList
        HighProbabilityList[botResponse] = messageProbability(message, ListOfWords, singleResponse, requiredWords)
        
    response('Good Day, would you like to create account for cloud banking?', ['hello', 'hey', 'hi', 'sign up'], singleResponse=True)
    response('Please enter your first name and last name in one message and text "done".', ['create account', 'yes', 'i want to create an account'], requiredWords=['create account', 'yes', 'create', 'account'])
    response('Enter your email address and type "done" on a new line', ['next'], requiredWords=['next'])
    response('Almost there, type in your date of Birth (DD/MM/YYYY)', ['next'], requiredWords=['next'])
    response('Your password is "123456". Type to confirm your password.', ['123456'], requiredWords=['123456'])
    response('Account creation was successful, Thank you for using cloud services. Type "complete".', ['complete'], requiredWords=['complete'])
    
    bestMatch = max(HighProbabilityList, key=HighProbabilityList.get)
    print(HighProbabilityList)
    
    return bestMatch


def getResponse(userInput):
    splitMessage = re.split(r'\s+|[,;?!.-]\s*', userInput.lower())
    response = scanMessages(splitMessage)a
    return response




while True:
    print('Bot: ' + getResponse(input('You: ')))