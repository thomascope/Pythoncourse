import set2exercise2

lists= ['hello','world']
for cnt,thisLetter in enumerate(lists):
    print cnt
    print thisLetter
print 'loop done'

myList=[]
for thisInt in range(5):
    thisEntry = {}
    thisEntry['val']=thisInt
    thisEntry['X3']=thisInt*3
    myList.append(thisEntry)
print 'myList is now', myList

print 'printing one entry per line:'
for thisEntry in myList:
    print thisEntry['X3']
   
print(myList[2]['X3'])
