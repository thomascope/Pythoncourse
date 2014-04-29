from psychopy.iohub import EventConstants, lanchHubServer
from psychopy import visual, core, data, event, logging, sound, gui
#import numpy
#import os

#set experiment parameters
info = {} #a dictionary
#present dialog to collect info
info['Participant'] = ''
info['RespMethod'] = ['Keyboard', 'Mouse', 'USBBox']
#info['Participant'] = ''
#info['Participant'] = ''
dlg = gui.DlgFromDict(info)