import random
def play():
  print("//==================================================//")
  pg = input("||    DO YOU WANT TO CONTINUE TYPE 'Y/N' OR 'y/n'   ")
  print("//==================================================//\n")
  if pg == 'y' or pg == 'Y' or pg == 'N' or pg == 'n':
    return pg
  else:
    play() 
def guessNumGame():
  playa = 'y'
  s = 0

  while playa == 'y' or playa == 'Y':

    computerNum = random.randint(1,50)
    print("//======================================\\")
    userNum = int(input("||  ENTER A NUMBER BETWEEN 1 TO 10 :  "))
    print("//======================================\\\n")
    diff = computerNum-userNum
    if computerNum==userNum:
      s += 50
      print("//=======================================//")
      print("||  WOW, SAME NUMBER YOU GET 50 POINTS   ||")
      print("||                                       ||")
      print("||  YOUR SCORE                      ",s,end="")
      print("  ||\n||                                       ||")
      print("//=======================================//\n")
    elif abs(diff)<=5:
      s += 25
      print("//=================================================//")
      print("||  YOU ARE NEAR TO THE NUMBER AND GET 25 POINTS   ||")
      print("||                                                 ||")
      print("||  YOUR SCORE                                ",s,end="")
      print("  ||\n||                                                 ||")
      print("//=================================================//\n")
    elif abs(diff)<=10:
      s += 10
      print("//=================================================//")
      print("||  YOU ARE NEAR TO THE NUMBER AND GET 10 POINTS   ||")
      print("||                                                 ||")
      print("||  YOUR SCORE                                ",s,end="")
      print("  ||\n||                                                 ||")
      print("//=================================================//\n")
    else:
      print("SORRY GOOD LOCK NEXT TIME \n\n")
    playa = play()
  print("//=================================================//")
  print("||                                                 ||")
  print("||  YOUR FINAL SCORE                          ",s,end="")
  print("  ||\n||                                                 ||")
  print("//=================================================//\n")
guessNumGame()
