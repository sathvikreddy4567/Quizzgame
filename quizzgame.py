#Created a tuple variable for storing questions
questions=("How to find length of the variable in python ? :",
           "How to add element to the list (or) tuple in python ? :",
           "How many types of loops present in python ? :",
           " By using which function we can create function in python ? :")

#stored options in tuple form 
options=(("A. .pop()","B. .add()","C. .len()","D. .find()"),
         ("A. .len()","B. .joint()","C. .plus()","D. .add()"),
         ("A. 1","B. 2 ","C. 3","D. 4"),
         ("A. class","B. def ","C. __init__","D. function"))
#stored answers as a variable 
answers=("C","D","B","B")
attempts=[]
score=0
question_num=0
#for loop for printing questions
for question in questions:
    print('-----------------------------------------------------------------------------------')
    print(question)
    #for loop for priting options
    for option in options[question_num]:
        print(option)
     # taking user answer by using input function
    attempt=input("Enter your answer in (A,B,C,D):").upper()
    attempts.append(attempt)
    #checking the option correct or wrong by the user 
    if attempt==answers[question_num]:
        score+=1 #adding marks to the user 
        print("CORRECT ✅")
    else:
        print("INCORRECT ❌")
        print(f"{answers[question_num]} is the correct answer")
         
         
         

    question_num+=1
        
      
print('-------------------------------------------------------------------------------')
print("                             RESULT                                            ")
print('-------------------------------------------------------------------------------')

print("Answers :",end=" ")
#printing attempt and key to the user 
for answer in answers:
    print(answer,end="")
    
print()
    
print("Attempts",end=" ")
for attempt in attempts:
    print(attempt,end=" ")
    
print()
    
#Giving score to the user 
print(f"Your score is {score} out of 4")
#Giving compliment to the user according to the score 
if score==4:
    print("-----------------------Great---------------------------------")
elif score==3:
    print("------------------------Excellent-----------------------------")
elif score==2:
    print("-------------------------Good----------------------------------")
elif score==1:
    print("--------------------------Average-------------------------------")
else:
    print("----------------------------Poor-------------------------------- ")        