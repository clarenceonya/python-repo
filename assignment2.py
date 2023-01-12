print("current and previous numbers and their sum in the range (9)")
previous_num = 0

#loop froom 1 to 9
for i in range(1, 10):
    x_sum = previous_num+i
    print("Current Number", i, "Previous Number " ,
          previous_num, "sum: ", x_sum)
# modify previous number
# set it to the current number
    previous_num = i