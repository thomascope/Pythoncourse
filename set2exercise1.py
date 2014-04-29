# Part 1

trialList=[]
for wordcolors in ['red','green','blue']:
    for inkcolors in ['red','green','blue']:
        trialList += [{'word':wordcolors, 'ink':inkcolors}]
print(trialList)

# The above was my solution, but the example answer is much more pretty:

colors = ['red', 'green', 'blue']
trialList = [{'word': word, 'ink': ink} for ink in colors for word in colors]

# Part 2 (&3)

for thistrial,junk in enumerate(trialList):
    print('for this trial, the ink is %s and the word is %s' %(trialList[thistrial]['ink'],trialList[thistrial]['word']))

# Or, again, the example is a little simpler:

for trial in trialList:
    print 'for this trial, the ink is', trial['ink'], 'and the word is', trial['word']

# Part 4

for thistrial,trial in enumerate(trialList):
    if trial['ink'] == trial['word']:
        congruency = 'congruent!' 
    else: 
        congruency = 'incongruent'
    print("for trial %i, the ink is %s and the word is %s. It's %s" %(thistrial+1,trialList[thistrial]['ink'],trialList[thistrial]['word'],congruency))