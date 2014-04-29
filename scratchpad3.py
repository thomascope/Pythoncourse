def change(input):
    input[0] = 'a'

myList = [1,2,3]
new = change(myList)
print new #surprise? (see note above)
print myList #should have changed