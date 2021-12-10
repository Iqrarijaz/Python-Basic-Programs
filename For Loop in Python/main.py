# print X as many times as number in List
# for example first number is 5 so print X 5 times
numbers=[5,2,5,2,2]
Value=["X"]
for item in numbers:
    for j in Value:
        print(item*j)


# sum of number from 0 to 9
sum=0
for item in  range(9):
    sum=sum+item
print( f'\nsum from 0 to 9 is : {sum}')