#Import necessary libraries
from psychopy import visual, event, core, data, gui

#set experiment parameters
info = {} #a dictionary
#present dialog to collect info
info['Participant'] = ''
dlg = gui.DlgFromDict(info)
if not dlg.OK:
    core.quit()
info['fixTime'] = 1.0 # seconds
info['cueTime'] = 0.2
info['probeTime'] = 0.2
info['dateStr'] = data.getDateStr() #will create str of current date/time
filename = "data/" + info['Participant'] + "_" + info['dateStr']

#Create window
win = visual.Window([1024,768], fullscr=False, units = 'pix', rgb = 'DodgerBlue')
core.wait(1)

#create a fixation point
fixation = visual.Circle(win, size = 25,
    lineColor = 'DarkOrchid', fillColor = 'Fuchsia',
    lineWidth = 3.0)
#fixation.setAutoDraw(True)

#create a probe
probe = visual.ImageStim(win, image=None, mask='gauss', units='', pos=(300.0, 0.0), size=80, ori=0.0, color='HoneyDew')

#create cues
arrowvertices = [[-30,-20], [-30,20], [30,0]]
rightcue = visual.ShapeStim(win,
    vertices = arrowvertices,
    lineColor = 'red', fillColor = 'salmon')
#
#run one trial
#fixation.draw()
#win.flip()
#core.wait(info['fixTime'])
#
#rightcue.draw()
#win.flip()
#core.wait(info['cueTime'])
#
#probe.draw()
#win.flip()
#core.wait(info['probeTime'])

#setup experimental conditions
conditions = data.importConditions('posnerconds.csv')
trials = data.TrialHandler(trialList=conditions, nReps=5)

#add trials to the experiment handler to store data
thisExp = data.ExperimentHandler(
        name='Posner', version='1.0', #not needed, just handy
        extraInfo = info, #the info we created earlier
        dataFileName = filename, # using our string with data/name_date
        )
thisExp.addLoop(trials) #there could be other loops (like practice loops)

#A loop of trials
respClock = core.Clock()
for trialnum,trialdata in enumerate(trials):
    fixation.draw()
    win.flip()
    respClock.reset()
    core.wait(info['fixTime'])
    
    rightcue.setOri(trialdata['cueOri'])
    rightcue.draw()
    win.flip()
    core.wait(info['cueTime'])
    
    probe.setPos([trialdata['probeX'], 0.0])
    probe.draw()
    win.flip()
    core.wait(info['probeTime'])
    
    #clear screen
    win.flip()
    #wait for response
    keys = event.waitKeys(keyList = ['left','right','escape'])
    resp = keys[0]
    rt = respClock.getTime()
    
    # check if response is correct
    if trialdata['probeX']>0 and resp=='right':
        corr = 1
    elif trialdata['probeX']<0 and resp=='left':
        corr = 1
    elif resp=='escape':
        break #will end the innermost loop, not necessarily `trials`
        core.quit() #from psychopy lib will exit Python
    else:
        corr = 0
    # collect responses
    trials.addData('resp', resp)
    trials.addData('rt', rt)
    trials.addData('corr', corr)
    thisExp.nextEntry()

print(trialdata)
print(trialnum)

