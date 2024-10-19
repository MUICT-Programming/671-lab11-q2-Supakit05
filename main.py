n = int(input())
def summation(n):
    lst1 = []
    lst2 = []
    for y in range(n):
        lst1.append(int(input()))
    for z in range(n):
        lst2.append(int(input()))   
    updated_list = [lst1[i]+lst2[i]for i in range(n)] 
    return updated_list
def find_min_max(updatedlist):
    min_value = min(updatedlist)
    max_value = max(updatedlist)
    return min_value,max_value
updated_list = summation(n)
print(updated_list)
min_value , max_value = find_min_max(updated_list)
print((min_value , max_value))
