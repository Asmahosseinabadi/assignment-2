score_count=0
sum_number=0
while True:
    score=float(input("enter the student's score :"))
    score_count+=1
    sum_number=score+sum_number
    average=sum_number/score_count
    print("the average is: ",average)  
    if score=="exit":
        break





    

   