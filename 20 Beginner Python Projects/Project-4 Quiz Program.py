quiz={
    "quiz-1":{
        "Question":"What is the capital of pakistan ?",
        "Answer":"islamabad"
    },
    "quiz-2":{
        "Question":"The prime minister of the paistan is ?",
        "Answer":"shahbazsharif"
    },
    "quiz-3":{
        "Question":"The banana in urdu ?",
        "Answer":"kela"
    },
   
}

score=0

for key,value in quiz.items():
    print(value['Question'])
    answer=input("Answer:")
    
    if answer.lower()==value['Answer']:
        print("Correct")
        score=score+1
        print("Your Score is: "+str(score))
    else:
        print("Wrong!")
        print("The anser is :"+value['Answer'])
        print("Your Score is: "+str(score))
    print("="*45)
    print("You got "+str(score)+" out of 3 questions corectly")
    