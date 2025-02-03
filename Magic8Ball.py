#Magic8Ball.py
#Name:
#Date:
#Assignment:

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Generate Random Number and Month")
  #Prompt the user for their question.
  answers = ["January", "February", "March", "April", 
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
  #Answer question randomly with one of the options from your earlier list.
  length = len(answers)
  r = random.random() * 12
  
  r = int(r)
  
  
  print(r)
  response = answers[r]
  print(response)
  
if __name__ == '__main__':
  main()
