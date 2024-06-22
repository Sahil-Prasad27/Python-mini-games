#quiz game in python in terminal 


questions =[
    "What does G stands for in Gpay",
    "Which part of the computer is called the brain of the computer"
]

answer =[
    "Google",
    "CPU"
]
score = 0

for i in range(0, len(questions)):
    print(questions[i])
    user_answer = input("Answer: ")
    
    if user_answer == answer[i]:
        print("Correct")
        score = score+1
    else:
        print("Incorrect")
        
print(f"your total score {score}")