while True:
    firstName=input('Hi! What is your name? ')
    if firstName.isalpha() and len(firstName)>0:
        print('Hey there,',firstName,)
        break
    else:
        print('Error')
while True:
    numberInput=input('What number would you like to choose?')
    if numberInput.isnumeric():
      print('Awesome, your number is', numberInput)
      numberInput=int(numberInput)
      for x in range(0, numberInput+1, 2):
        print(x)
    else:
      print('Please enter a NUMBER..!')
