import random
diff_list = []
sorted_list = []
# printing the random number
randomlist = random.sample(range(0, 1000), 15)
print(randomlist)
# sorting the random number
randomlist.sort()
print(randomlist)

# difference between the adjacent number
for i in range(1,len(randomlist)):
    diff_list.append(randomlist[i] - randomlist[i-1])
print(diff_list)

#Most common distance
def  frequent_val(diff_list):
    temp = 0
    itteraions = 0
    a = 0
    num = diff_list[0]
    for i in diff_list:
        curr_val = diff_list.count(i)
        #print("in for: ",curr_val)
        if (curr_val > temp):
            temp = curr_val
            num = i
            a = a+1
    if a > 1:
        return num,a

print(frequent_val(diff_list))
