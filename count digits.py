a = input("Enter digit: ")
count = 0
for digit in a:
    count += count
if count ==1:
    print('one digit')
elif count == 2:
    print('two digit')
elif count == 3:
    print('three digit')
else:
    print('four digit')