import random
diff_list = []
sorted_list = []
# printing the random number
randomlist = random.sample(range(0, 1000), 6)
print(randomlist)
# sorting the random number
randomlist.sort()
print(randomlist)

# difference between the adjacent number
for i in range(1,len(randomlist)):
    diff_list.append(randomlist[i] - randomlist[i-1])
print(diff_list)

#Most common distance
def frequent_val(diff_list):
    temp = 0
    num = diff_list[0]
    for i in diff_list:
        curr_val = diff_list.count(i)
        if (curr_val > temp):
            temp = curr_val
            num = i
    return num
print(frequent_val(diff_list))