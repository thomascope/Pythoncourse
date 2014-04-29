from psychopy.iohub import EventConstants, launchHubServer
from psychopy import visual

windowsize=[800,600]
io = launchHubServer()
keyboard = io.devices.keyboard
mouse = io.devices.mouse
win = visual.Window(windowsize, fullscr=False)
stim = visual.GratingStim(win, mask = 'gauss', sf=6, units='', pos=([-0.3, 0.0]))

for frameN in range(1200):
    stim.setOri(frameN*2)
    stim.draw()
    win.flip()
    
    #get mouse state
    position, posDelta = mouse.getPositionAndDelta()
    mouse_dX,mouse_dY=posDelta    
    left_button, middle_button, right_button = mouse.getCurrentButtonStates()
    
    if left_button:
        print position
        xpos = position[0]*2.0/windowsize[0]
        ypos = position[1]*2.0/windowsize[1]
        stim.setPos([xpos, ypos])
        stim.draw()
        win.flip()
    
    # get keyboard state
    keys = keyboard.getEvents()
    for thiskey in keys:
        print thiskey
        
        



#keyboard_events = #
#for kb_event in keyboard_events:k#
#    print kb_event # to see all info about this event
#    # get specific event fields.
#    evtT = kb_event.time
#    #event type
#    eventType = kb_event.type # an integer
#    eventTypeStr = EventConstants.getName(eventType)
#
#    #some event types have extra fields
#    key_pressed = kb_event.key
#    mods = kb_event.modifiers
#
