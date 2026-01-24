def avg(marks):
    total=0
    for i in range(4):
        total=total+marks[i]
    average=total/4
    return average

marksArr=[40,30,90,70]
print("Marks : " ,marksArr)
print("Average marks : ",avg(marksArr))
