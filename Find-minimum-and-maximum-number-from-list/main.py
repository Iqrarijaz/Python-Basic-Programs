given_list=[1, 3, 5, 7, 8, 88, 44, 55, 99, 2, 22, 3, 44]
maximum_number=given_list[0]
for i in given_list:
    if i>maximum_number:
        maximum_number=i
print("Maximum number in given List is : " + str(maximum_number))
minimum_number=given_list[0]
for i in given_list:
    if minimum_number>i:
        minimum_number=i
print("Minimum number in given List is : " + str(minimum_number))