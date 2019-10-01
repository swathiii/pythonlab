
name = input("What is your name?\n") 

print("Good Luck,", name, "!!" ) 
  
number = '8'
  
print("Guess the number between 1 to 10") 
  
guesses = '' 
  
turns = 3
  
while turns > 0: 
      
    failed = 0
       
    for int in number:  
          
        if int in guesses:  
            print(int) 
              
        else:  
            print("_") 
              
            failed += 1
              
  
    if failed == 0: 
    
        print("\nCongratulations! You Win")  
          
        print("The number is: ", number)  
        break
      
    guess = input("guess a number:") 

    guesses += guess  
      
    if guess not in number: 
          
        turns -= 1

        print("Wrong!\n") 
          
        print("You have", + turns, 'more guesses') 
          
          
        if turns == 0: 
            print("You Loose :( ")