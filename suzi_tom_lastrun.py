#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on May 09, 2022, at 12:48
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'suzi_tom'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\OneDrive - Open University of Israel\\sofi\\work\\seminar-asi_tal\\suzi_tom\\suzi_tom_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "setup_for_exp"
setup_for_expClock = core.Clock()
block1=[]
block2=[]
block3=[]
block4=[]
blocks=[]
list_F=[]
list_N=[]
short_time=0.25
long_time=1
num_of_lists=16
lists_in_block=4
words=[]

image = visual.ImageStim(
    win=win,
    name='image', 
    image='intro/Slide4.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "demographics"
demographicsClock = core.Clock()
win.allowStencil = True
demographics_for_ = visual.Form(win=win, name='demographics_for_',
    items='demographics.xlsx',
    textHeight=0.03,
    font='Arial',
    randomize=False,
    style='custom...',
    fillColor=None, borderColor=None, itemColor='white', 
    responseColor='white', markerColor='red', colorSpace='rgb', 
    size=(1,1),
    pos=(0, 0),
    itemPadding=0.05
)
next = visual.ButtonStim(win, 
    text='->', font='Arial',
    pos=(0.7, -0.5),
    letterHeight=0.03,
    size=(0.1,0.1), borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='next'
)
next.buttonClock = core.Clock()

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.ImageStim(
    win=win,
    name='intro_text', 
    image='intro/Slide1.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(1.7,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "train"
trainClock = core.Clock()
train_words=[]
show_train_word=""
tezt_train = visual.TextStim(win=win, name='tezt_train',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

# Initialize components for Routine "empty_train"
empty_trainClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "strat_train_test"
strat_train_testClock = core.Clock()
training_text = visual.TextStim(win=win, name='training_text',
    text='מבחן לדוגמה מתחיל',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

# Initialize components for Routine "training_test"
training_testClock = core.Clock()
new_word="המילה בטוח חדשה"
old_word="המילה בטוח ישנה"
current_train_word=""
counter_train_word=0
slider_2 = visual.Slider(win=win, name='slider_2',
    startValue=None, size=(1, 0.1), pos=(0, -0.4), units=None,
    labels=["1","6"], ticks=[1, 2, 3, 4, 5, 6], granularity=0.0,
    style='radio', styleTweaks=(), opacity=None,
    color='white', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-1, readOnly=False)
six_tick = visual.TextStim(win=win, name='six_tick',
    text='6',
    font='Open Sans',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
one_tick = visual.TextStim(win=win, name='one_tick',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
new_word_label_2 = visual.TextStim(win=win, name='new_word_label_2',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-4.0);
old_word_label_2 = visual.TextStim(win=win, name='old_word_label_2',
    text='',
    font='Open Sans',
    pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-5.0);
text_train_word = visual.TextStim(win=win, name='text_train_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-6.0);
two_tick = visual.TextStim(win=win, name='two_tick',
    text='2',
    font='Open Sans',
    pos=(-0.3, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);
three_tick = visual.TextStim(win=win, name='three_tick',
    text='3',
    font='Open Sans',
    pos=(-0.1, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
four_tick = visual.TextStim(win=win, name='four_tick',
    text='4',
    font='Open Sans',
    pos=(0.1, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
five_tick = visual.TextStim(win=win, name='five_tick',
    text='5',
    font='Open Sans',
    pos=(0.3, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
rating = keyboard.Keyboard()

# Initialize components for Routine "end_of_training"
end_of_trainingClock = core.Clock()
test_end_text = visual.ImageStim(
    win=win,
    name='test_end_text', 
    image='intro/Slide2.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(2,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
next_key = keyboard.Keyboard()

# Initialize components for Routine "lists_order"
lists_orderClock = core.Clock()
count_list=0




   


# Initialize components for Routine "orgenize_blocks"
orgenize_blocksClock = core.Clock()
word_counter=0
list_counter=0
block_counter=0

# Initialize components for Routine "part_start"
part_startClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "list_part"
list_partClock = core.Clock()
number_list = visual.TextStim(win=win, name='number_list',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "words_loader"
words_loaderClock = core.Clock()

current_file_name=""
showing_the_stim = visual.TextStim(win=win, name='showing_the_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

# Initialize components for Routine "empty_test"
empty_testClock = core.Clock()
blank_times = visual.TextStim(win=win, name='blank_times',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "insert_target_word"
insert_target_wordClock = core.Clock()



# Initialize components for Routine "insert_other"
insert_otherClock = core.Clock()

# Initialize components for Routine "record_lists"
record_listsClock = core.Clock()
# Set experiment start values for variable component list_name
list_name = ''
list_nameContainer = []
# Set experiment start values for variable component list_time
list_time = ''
list_timeContainer = []

# Initialize components for Routine "start_test"
start_testClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "test"
testClock = core.Clock()
new_word="המילה בטוח חדשה"
old_word="המילה בטוח ישנה"
current_word=""
current_test_word=0
word_type=-1
word_file=""
correct_answer=0
correct_rating=0
rating_test = keyboard.Keyboard()
# Set experiment start values for variable component correct_raiting_for_answer
correct_raiting_for_answer = 0
correct_raiting_for_answerContainer = []
# Set experiment start values for variable component correct
correct = 0
correctContainer = []
# Set experiment start values for variable component scoring_word
scoring_word = ''
scoring_wordContainer = []
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6), granularity=0.0,
    style='radio', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-5, readOnly=False)
new_word_label = visual.TextStim(win=win, name='new_word_label',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-6.0);
old_word_label = visual.TextStim(win=win, name='old_word_label',
    text='',
    font='Open Sans',
    pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-7.0);
show_word = visual.TextStim(win=win, name='show_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-8.0);
# Set experiment start values for variable component worf_list_name
worf_list_name = ''
worf_list_nameContainer = []
# Set experiment start values for variable component word_type
word_type = ''
word_typeContainer = []
var_1_label = visual.TextStim(win=win, name='var_1_label',
    text='1',
    font='Open Sans',
    pos=(-0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
var_2_label = visual.TextStim(win=win, name='var_2_label',
    text='2',
    font='Open Sans',
    pos=(-0.3, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
three_label = visual.TextStim(win=win, name='three_label',
    text='3',
    font='Open Sans',
    pos=(-0.1, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
four_label = visual.TextStim(win=win, name='four_label',
    text='4',
    font='Open Sans',
    pos=(0.1, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
five_label = visual.TextStim(win=win, name='five_label',
    text='5',
    font='Open Sans',
    pos=(0.3, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
six_label = visual.TextStim(win=win, name='six_label',
    text='6',
    font='Open Sans',
    pos=(0.5, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);

# Initialize components for Routine "record_block"
record_blockClock = core.Clock()
text_end_of_block = visual.TextStim(win=win, name='text_end_of_block',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

# Initialize components for Routine "end_block"
end_blockClock = core.Clock()
ending = visual.ImageStim(
    win=win,
    name='ending', 
    image='intro/Slide3.PNG', mask=None,
    ori=0.0, pos=(0, 0), size=(2,1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup_for_exp"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
setup_for_expComponents = [image, key_resp_2]
for thisComponent in setup_for_expComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
setup_for_expClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "setup_for_exp"-------
while continueRoutine:
    # get current time
    t = setup_for_expClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setup_for_expClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *key_resp_2* updates
    if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in setup_for_expComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "setup_for_exp"-------
for thisComponent in setup_for_expComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "setup_for_exp" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demographics"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
demographicsComponents = [demographics_for_, next]
for thisComponent in demographicsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
demographicsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "demographics"-------
while continueRoutine:
    # get current time
    t = demographicsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=demographicsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *demographics_for_* updates
    if demographics_for_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        demographics_for_.frameNStart = frameN  # exact frame index
        demographics_for_.tStart = t  # local t and not account for scr refresh
        demographics_for_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(demographics_for_, 'tStartRefresh')  # time at next scr refresh
        demographics_for_.setAutoDraw(True)
    
    # *next* updates
    if next.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        next.frameNStart = frameN  # exact frame index
        next.tStart = t  # local t and not account for scr refresh
        next.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(next, 'tStartRefresh')  # time at next scr refresh
        next.setAutoDraw(True)
    if next.status == STARTED:
        # check whether next has been pressed
        if next.isClicked:
            if not next.wasClicked:
                next.timesOn.append(next.buttonClock.getTime()) # store time of first click
                next.timesOff.append(next.buttonClock.getTime()) # store time clicked until
            else:
                next.timesOff[-1] = next.buttonClock.getTime() # update time clicked until
            if not next.wasClicked:
                continueRoutine = False  # end routine when next is clicked
                None
            next.wasClicked = True  # if next is still clicked next frame, it is not a new click
        else:
            next.wasClicked = False  # if next is clicked next frame, it is a new click
    else:
        next.wasClicked = False  # if next is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demographicsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demographics"-------
for thisComponent in demographicsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
demographics_for_.addDataToExp(thisExp, 'rows')
demographics_for_.autodraw = False
thisExp.addData('next.started', next.tStartRefresh)
thisExp.addData('next.stopped', next.tStopRefresh)
thisExp.addData('next.numClicks', next.numClicks)
if next.numClicks:
   thisExp.addData('next.timesOn', next.timesOn)
   thisExp.addData('next.timesOff', next.timesOff)
else:
   thisExp.addData('next.timesOn', "")
   thisExp.addData('next.timesOff', "")
# the Routine "demographics" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
introComponents = [intro_text, key_resp]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_text.started', intro_text.tStartRefresh)
thisExp.addData('intro_text.stopped', intro_text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training_and_test_loop = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='training_and_test_loop')
thisExp.addLoop(training_and_test_loop)  # add the loop to the experiment
thisTraining_and_test_loop = training_and_test_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining_and_test_loop.rgb)
if thisTraining_and_test_loop != None:
    for paramName in thisTraining_and_test_loop:
        exec('{} = thisTraining_and_test_loop[paramName]'.format(paramName))

for thisTraining_and_test_loop in training_and_test_loop:
    currentLoop = training_and_test_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_and_test_loop.rgb)
    if thisTraining_and_test_loop != None:
        for paramName in thisTraining_and_test_loop:
            exec('{} = thisTraining_and_test_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    training_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('firsttest.xlsx', selection='1:13'),
        seed=None, name='training_loop')
    thisExp.addLoop(training_loop)  # add the loop to the experiment
    thisTraining_loop = training_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_loop.rgb)
    if thisTraining_loop != None:
        for paramName in thisTraining_loop:
            exec('{} = thisTraining_loop[paramName]'.format(paramName))
    
    for thisTraining_loop in training_loop:
        currentLoop = training_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_loop.rgb)
        if thisTraining_loop != None:
            for paramName in thisTraining_loop:
                exec('{} = thisTraining_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "train"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        train_words.append(word)
        show_train_word=word
        tezt_train.setText(show_train_word)
        # keep track of which components have finished
        trainComponents = [tezt_train]
        for thisComponent in trainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "train"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trainClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trainClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *tezt_train* updates
            if tezt_train.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tezt_train.frameNStart = frameN  # exact frame index
                tezt_train.tStart = t  # local t and not account for scr refresh
                tezt_train.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tezt_train, 'tStartRefresh')  # time at next scr refresh
                tezt_train.setAutoDraw(True)
            if tezt_train.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > tezt_train.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    tezt_train.tStop = t  # not accounting for scr refresh
                    tezt_train.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(tezt_train, 'tStopRefresh')  # time at next scr refresh
                    tezt_train.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "train"-------
        for thisComponent in trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "empty_train"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        blank.setText('')
        # keep track of which components have finished
        empty_trainComponents = [blank]
        for thisComponent in empty_trainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        empty_trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "empty_train"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = empty_trainClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=empty_trainClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                    blank.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in empty_trainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "empty_train"-------
        for thisComponent in empty_trainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        training_loop.addData('blank.started', blank.tStartRefresh)
        training_loop.addData('blank.stopped', blank.tStopRefresh)
    # completed 1.0 repeats of 'training_loop'
    
    
    # ------Prepare to start Routine "strat_train_test"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    shuffle(train_words)
    # keep track of which components have finished
    strat_train_testComponents = [training_text]
    for thisComponent in strat_train_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    strat_train_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "strat_train_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = strat_train_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=strat_train_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *training_text* updates
        if training_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            training_text.frameNStart = frameN  # exact frame index
            training_text.tStart = t  # local t and not account for scr refresh
            training_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(training_text, 'tStartRefresh')  # time at next scr refresh
            training_text.setAutoDraw(True)
        if training_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > training_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                training_text.tStop = t  # not accounting for scr refresh
                training_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(training_text, 'tStopRefresh')  # time at next scr refresh
                training_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in strat_train_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "strat_train_test"-------
    for thisComponent in strat_train_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # set up handler to look after randomisation of conditions etc
    training_test_loop = data.TrialHandler(nReps=5.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='training_test_loop')
    thisExp.addLoop(training_test_loop)  # add the loop to the experiment
    thisTraining_test_loop = training_test_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining_test_loop.rgb)
    if thisTraining_test_loop != None:
        for paramName in thisTraining_test_loop:
            exec('{} = thisTraining_test_loop[paramName]'.format(paramName))
    
    for thisTraining_test_loop in training_test_loop:
        currentLoop = training_test_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTraining_test_loop.rgb)
        if thisTraining_test_loop != None:
            for paramName in thisTraining_test_loop:
                exec('{} = thisTraining_test_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "training_test"-------
        continueRoutine = True
        # update component parameters for each repeat
        current_train_word=train_words[counter_train_word]
        slider_2.reset()
        one_tick.setText('1')
        new_word_label_2.setText(new_word )
        old_word_label_2.setText(old_word               
)
        text_train_word.setText(current_train_word)
        rating.keys = []
        rating.rt = []
        _rating_allKeys = []
        # keep track of which components have finished
        training_testComponents = [slider_2, six_tick, one_tick, new_word_label_2, old_word_label_2, text_train_word, two_tick, three_tick, four_tick, five_tick, rating]
        for thisComponent in training_testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        training_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "training_test"-------
        while continueRoutine:
            # get current time
            t = training_testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=training_testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *slider_2* updates
            if slider_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider_2.frameNStart = frameN  # exact frame index
                slider_2.tStart = t  # local t and not account for scr refresh
                slider_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider_2, 'tStartRefresh')  # time at next scr refresh
                slider_2.setAutoDraw(True)
            
            # Check slider_2 for response to end routine
            if slider_2.getRating() is not None and slider_2.status == STARTED:
                continueRoutine = False
            
            # *six_tick* updates
            if six_tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                six_tick.frameNStart = frameN  # exact frame index
                six_tick.tStart = t  # local t and not account for scr refresh
                six_tick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(six_tick, 'tStartRefresh')  # time at next scr refresh
                six_tick.setAutoDraw(True)
            
            # *one_tick* updates
            if one_tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                one_tick.frameNStart = frameN  # exact frame index
                one_tick.tStart = t  # local t and not account for scr refresh
                one_tick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(one_tick, 'tStartRefresh')  # time at next scr refresh
                one_tick.setAutoDraw(True)
            
            # *new_word_label_2* updates
            if new_word_label_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                new_word_label_2.frameNStart = frameN  # exact frame index
                new_word_label_2.tStart = t  # local t and not account for scr refresh
                new_word_label_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(new_word_label_2, 'tStartRefresh')  # time at next scr refresh
                new_word_label_2.setAutoDraw(True)
            
            # *old_word_label_2* updates
            if old_word_label_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                old_word_label_2.frameNStart = frameN  # exact frame index
                old_word_label_2.tStart = t  # local t and not account for scr refresh
                old_word_label_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(old_word_label_2, 'tStartRefresh')  # time at next scr refresh
                old_word_label_2.setAutoDraw(True)
            
            # *text_train_word* updates
            if text_train_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_train_word.frameNStart = frameN  # exact frame index
                text_train_word.tStart = t  # local t and not account for scr refresh
                text_train_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_train_word, 'tStartRefresh')  # time at next scr refresh
                text_train_word.setAutoDraw(True)
            
            # *two_tick* updates
            if two_tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                two_tick.frameNStart = frameN  # exact frame index
                two_tick.tStart = t  # local t and not account for scr refresh
                two_tick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(two_tick, 'tStartRefresh')  # time at next scr refresh
                two_tick.setAutoDraw(True)
            
            # *three_tick* updates
            if three_tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                three_tick.frameNStart = frameN  # exact frame index
                three_tick.tStart = t  # local t and not account for scr refresh
                three_tick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(three_tick, 'tStartRefresh')  # time at next scr refresh
                three_tick.setAutoDraw(True)
            
            # *four_tick* updates
            if four_tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                four_tick.frameNStart = frameN  # exact frame index
                four_tick.tStart = t  # local t and not account for scr refresh
                four_tick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(four_tick, 'tStartRefresh')  # time at next scr refresh
                four_tick.setAutoDraw(True)
            
            # *five_tick* updates
            if five_tick.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_tick.frameNStart = frameN  # exact frame index
                five_tick.tStart = t  # local t and not account for scr refresh
                five_tick.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_tick, 'tStartRefresh')  # time at next scr refresh
                five_tick.setAutoDraw(True)
            
            # *rating* updates
            if rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating.frameNStart = frameN  # exact frame index
                rating.tStart = t  # local t and not account for scr refresh
                rating.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
                rating.status = STARTED
                # keyboard checking is just starting
                rating.clock.reset()  # now t=0
            if rating.status == STARTED:
                theseKeys = rating.getKeys(keyList=['1', '2', '3', '4', '5', '6'], waitRelease=False)
                _rating_allKeys.extend(theseKeys)
                if len(_rating_allKeys):
                    rating.keys = _rating_allKeys[-1].name  # just the last key pressed
                    rating.rt = _rating_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in training_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "training_test"-------
        for thisComponent in training_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        counter_train_word+=1
        training_test_loop.addData('slider_2.response', slider_2.getRating())
        training_test_loop.addData('slider_2.history', slider_2.getHistory())
        training_test_loop.addData('one_tick.started', one_tick.tStartRefresh)
        training_test_loop.addData('one_tick.stopped', one_tick.tStopRefresh)
        # check responses
        if rating.keys in ['', [], None]:  # No response was made
            rating.keys = None
        training_test_loop.addData('rating.keys',rating.keys)
        if rating.keys != None:  # we had a response
            training_test_loop.addData('rating.rt', rating.rt)
        # the Routine "training_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 5.0 repeats of 'training_test_loop'
    
    
    # ------Prepare to start Routine "end_of_training"-------
    continueRoutine = True
    # update component parameters for each repeat
    next_key.keys = []
    next_key.rt = []
    _next_key_allKeys = []
    # keep track of which components have finished
    end_of_trainingComponents = [test_end_text, next_key]
    for thisComponent in end_of_trainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    end_of_trainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "end_of_training"-------
    while continueRoutine:
        # get current time
        t = end_of_trainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=end_of_trainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_end_text* updates
        if test_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_end_text.frameNStart = frameN  # exact frame index
            test_end_text.tStart = t  # local t and not account for scr refresh
            test_end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_end_text, 'tStartRefresh')  # time at next scr refresh
            test_end_text.setAutoDraw(True)
        
        # *next_key* updates
        if next_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            next_key.frameNStart = frameN  # exact frame index
            next_key.tStart = t  # local t and not account for scr refresh
            next_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(next_key, 'tStartRefresh')  # time at next scr refresh
            next_key.status = STARTED
            # keyboard checking is just starting
            next_key.clock.reset()  # now t=0
            next_key.clearEvents(eventType='keyboard')
        if next_key.status == STARTED:
            theseKeys = next_key.getKeys(keyList=None, waitRelease=False)
            _next_key_allKeys.extend(theseKeys)
            if len(_next_key_allKeys):
                next_key.keys = [key.name for key in _next_key_allKeys]  # storing all keys
                next_key.rt = [key.rt for key in _next_key_allKeys]
                # was this correct?
                if (next_key.keys == str('')) or (next_key.keys == ''):
                    next_key.corr = 1
                else:
                    next_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in end_of_trainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "end_of_training"-------
    for thisComponent in end_of_trainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    print(next_key.keys[0])
    if next_key.keys[0]=='space':
        training_and_test_loop.finished=True
    training_and_test_loop.addData('test_end_text.started', test_end_text.tStartRefresh)
    training_and_test_loop.addData('test_end_text.stopped', test_end_text.tStopRefresh)
    # check responses
    if next_key.keys in ['', [], None]:  # No response was made
        next_key.keys = None
        # was no response the correct answer?!
        if str('').lower() == 'none':
           next_key.corr = 1;  # correct non-response
        else:
           next_key.corr = 0;  # failed to respond (incorrectly)
    # store data for training_and_test_loop (TrialHandler)
    training_and_test_loop.addData('next_key.keys',next_key.keys)
    training_and_test_loop.addData('next_key.corr', next_key.corr)
    if next_key.keys != None:  # we had a response
        training_and_test_loop.addData('next_key.rt', next_key.rt)
    # the Routine "end_of_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'training_and_test_loop'


# set up handler to look after randomisation of conditions etc
lists_names = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('file_names1.xlsx'),
    seed=None, name='lists_names')
thisExp.addLoop(lists_names)  # add the loop to the experiment
thisLists_name = lists_names.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLists_name.rgb)
if thisLists_name != None:
    for paramName in thisLists_name:
        exec('{} = thisLists_name[paramName]'.format(paramName))

for thisLists_name in lists_names:
    currentLoop = lists_names
    # abbreviate parameter names if possible (e.g. rgb = thisLists_name.rgb)
    if thisLists_name != None:
        for paramName in thisLists_name:
            exec('{} = thisLists_name[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "lists_order"-------
    continueRoutine = True
    # update component parameters for each repeat
    if count_list%2==0:
        list_F.append([file_F,short_time])
        list_N.append([file_N,short_time])
    else:
        list_F.append([file_F,long_time])
        list_N.append([file_N,long_time])
    count_list+=1
    # keep track of which components have finished
    lists_orderComponents = []
    for thisComponent in lists_orderComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    lists_orderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "lists_order"-------
    while continueRoutine:
        # get current time
        t = lists_orderClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=lists_orderClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in lists_orderComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "lists_order"-------
    for thisComponent in lists_orderComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "lists_order" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'lists_names'


# ------Prepare to start Routine "orgenize_blocks"-------
continueRoutine = True
# update component parameters for each repeat
shuffle(list_F[:num_of_lists])
shuffle(list_N[:num_of_lists])
shuffle(list_F[num_of_lists:])
shuffle(list_N[num_of_lists:])
for l in range(0,lists_in_block):
    block1.append(list_F[l])
    block1.append(list_N[l])
for l in range(lists_in_block,2*lists_in_block):
    block2.append(list_F[l])
    block2.append(list_N[l])
for l in range(2*lists_in_block,3*lists_in_block):
    block3.append(list_F[l])
    block3.append(list_N[l])
for l in range(3*lists_in_block,4*lists_in_block):
    block4.append(list_F[l])
    block4.append(list_N[l])
blocks.append(block1)
blocks.append(block2)
blocks.append(block3)
blocks.append(block4)
for block in blocks:
    shuffle(block)
    print(block)
    print(" / ")


# keep track of which components have finished
orgenize_blocksComponents = []
for thisComponent in orgenize_blocksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
orgenize_blocksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "orgenize_blocks"-------
while continueRoutine:
    # get current time
    t = orgenize_blocksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=orgenize_blocksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in orgenize_blocksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "orgenize_blocks"-------
for thisComponent in orgenize_blocksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "orgenize_blocks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks_loop = data.TrialHandler(nReps=4.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blocks_loop')
thisExp.addLoop(blocks_loop)  # add the loop to the experiment
thisBlocks_loop = blocks_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
if thisBlocks_loop != None:
    for paramName in thisBlocks_loop:
        exec('{} = thisBlocks_loop[paramName]'.format(paramName))

for thisBlocks_loop in blocks_loop:
    currentLoop = blocks_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlocks_loop.rgb)
    if thisBlocks_loop != None:
        for paramName in thisBlocks_loop:
            exec('{} = thisBlocks_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "part_start"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    text_2.setText('חלק\n')
    text_3.setText(block_counter+1)
    # keep track of which components have finished
    part_startComponents = [text_2, text_3]
    for thisComponent in part_startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    part_startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "part_start"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = part_startClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=part_startClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        if text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in part_startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "part_start"-------
    for thisComponent in part_startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_loop.addData('text_2.started', text_2.tStartRefresh)
    blocks_loop.addData('text_2.stopped', text_2.tStopRefresh)
    blocks_loop.addData('text_3.started', text_3.tStartRefresh)
    blocks_loop.addData('text_3.stopped', text_3.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    list_loop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='list_loop')
    thisExp.addLoop(list_loop)  # add the loop to the experiment
    thisList_loop = list_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisList_loop.rgb)
    if thisList_loop != None:
        for paramName in thisList_loop:
            exec('{} = thisList_loop[paramName]'.format(paramName))
    
    for thisList_loop in list_loop:
        currentLoop = list_loop
        # abbreviate parameter names if possible (e.g. rgb = thisList_loop.rgb)
        if thisList_loop != None:
            for paramName in thisList_loop:
                exec('{} = thisList_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "list_part"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        number_list.setText('רשימה\n')
        text_5.setText(list_counter+1)
        # keep track of which components have finished
        list_partComponents = [number_list, text_5]
        for thisComponent in list_partComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        list_partClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "list_part"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = list_partClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=list_partClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *number_list* updates
            if number_list.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                number_list.frameNStart = frameN  # exact frame index
                number_list.tStart = t  # local t and not account for scr refresh
                number_list.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(number_list, 'tStartRefresh')  # time at next scr refresh
                number_list.setAutoDraw(True)
            if number_list.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > number_list.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    number_list.tStop = t  # not accounting for scr refresh
                    number_list.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(number_list, 'tStopRefresh')  # time at next scr refresh
                    number_list.setAutoDraw(False)
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in list_partComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "list_part"-------
        for thisComponent in list_partComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        list_loop.addData('number_list.started', number_list.tStartRefresh)
        list_loop.addData('number_list.stopped', number_list.tStopRefresh)
        list_loop.addData('text_5.started', text_5.tStartRefresh)
        list_loop.addData('text_5.stopped', text_5.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        loading_words = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(blocks[block_counter][list_counter][0], selection='1:13'),
            seed=None, name='loading_words')
        thisExp.addLoop(loading_words)  # add the loop to the experiment
        thisLoading_word = loading_words.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoading_word.rgb)
        if thisLoading_word != None:
            for paramName in thisLoading_word:
                exec('{} = thisLoading_word[paramName]'.format(paramName))
        
        for thisLoading_word in loading_words:
            currentLoop = loading_words
            # abbreviate parameter names if possible (e.g. rgb = thisLoading_word.rgb)
            if thisLoading_word != None:
                for paramName in thisLoading_word:
                    exec('{} = thisLoading_word[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "words_loader"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            
            if word_counter==0 or word_counter==6 or word_counter==11:
                current_file_name=blocks[block_counter][list_counter][0]
                words.append([word,current_file_name,0])
            time_show=blocks[block_counter][list_counter][1]
            print(words[0][1])
            word_counter+=1
            
            
            showing_the_stim.setText(word)
            # keep track of which components have finished
            words_loaderComponents = [showing_the_stim]
            for thisComponent in words_loaderComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            words_loaderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "words_loader"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = words_loaderClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=words_loaderClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *showing_the_stim* updates
                if showing_the_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    showing_the_stim.frameNStart = frameN  # exact frame index
                    showing_the_stim.tStart = t  # local t and not account for scr refresh
                    showing_the_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(showing_the_stim, 'tStartRefresh')  # time at next scr refresh
                    showing_the_stim.setAutoDraw(True)
                if showing_the_stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > showing_the_stim.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        showing_the_stim.tStop = t  # not accounting for scr refresh
                        showing_the_stim.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(showing_the_stim, 'tStopRefresh')  # time at next scr refresh
                        showing_the_stim.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in words_loaderComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "words_loader"-------
            for thisComponent in words_loaderComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            
            # ------Prepare to start Routine "empty_test"-------
            continueRoutine = True
            # update component parameters for each repeat
            blank_times.setText('')
            # keep track of which components have finished
            empty_testComponents = [blank_times]
            for thisComponent in empty_testComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            empty_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "empty_test"-------
            while continueRoutine:
                # get current time
                t = empty_testClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=empty_testClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank_times* updates
                if blank_times.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank_times.frameNStart = frameN  # exact frame index
                    blank_times.tStart = t  # local t and not account for scr refresh
                    blank_times.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank_times, 'tStartRefresh')  # time at next scr refresh
                    blank_times.setAutoDraw(True)
                if blank_times.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank_times.tStartRefresh + time_show-frameTolerance:
                        # keep track of stop time/frame for later
                        blank_times.tStop = t  # not accounting for scr refresh
                        blank_times.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(blank_times, 'tStopRefresh')  # time at next scr refresh
                        blank_times.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in empty_testComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "empty_test"-------
            for thisComponent in empty_testComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            loading_words.addData('blank_times.started', blank_times.tStartRefresh)
            loading_words.addData('blank_times.stopped', blank_times.tStopRefresh)
            # the Routine "empty_test" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1.0 repeats of 'loading_words'
        
        
        # set up handler to look after randomisation of conditions etc
        target_word_loop = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(blocks[block_counter][list_counter][0], selection='0'),
            seed=None, name='target_word_loop')
        thisExp.addLoop(target_word_loop)  # add the loop to the experiment
        thisTarget_word_loop = target_word_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTarget_word_loop.rgb)
        if thisTarget_word_loop != None:
            for paramName in thisTarget_word_loop:
                exec('{} = thisTarget_word_loop[paramName]'.format(paramName))
        
        for thisTarget_word_loop in target_word_loop:
            currentLoop = target_word_loop
            # abbreviate parameter names if possible (e.g. rgb = thisTarget_word_loop.rgb)
            if thisTarget_word_loop != None:
                for paramName in thisTarget_word_loop:
                    exec('{} = thisTarget_word_loop[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "insert_target_word"-------
            continueRoutine = True
            # update component parameters for each repeat
            current_file_name=blocks[block_counter][list_counter][0]
            words.append([word,current_file_name,2])
            # keep track of which components have finished
            insert_target_wordComponents = []
            for thisComponent in insert_target_wordComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            insert_target_wordClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "insert_target_word"-------
            while continueRoutine:
                # get current time
                t = insert_target_wordClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=insert_target_wordClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in insert_target_wordComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "insert_target_word"-------
            for thisComponent in insert_target_wordComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "insert_target_word" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'target_word_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        insert_other_lists = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(blocks[block_counter][list_counter][0], selection='13:15'),
            seed=None, name='insert_other_lists')
        thisExp.addLoop(insert_other_lists)  # add the loop to the experiment
        thisInsert_other_list = insert_other_lists.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisInsert_other_list.rgb)
        if thisInsert_other_list != None:
            for paramName in thisInsert_other_list:
                exec('{} = thisInsert_other_list[paramName]'.format(paramName))
        
        for thisInsert_other_list in insert_other_lists:
            currentLoop = insert_other_lists
            # abbreviate parameter names if possible (e.g. rgb = thisInsert_other_list.rgb)
            if thisInsert_other_list != None:
                for paramName in thisInsert_other_list:
                    exec('{} = thisInsert_other_list[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "insert_other"-------
            continueRoutine = True
            # update component parameters for each repeat
            current_file_name=blocks[block_counter][list_counter][0]
            words.append([word,current_file_name,1])
            
            
            
            # keep track of which components have finished
            insert_otherComponents = []
            for thisComponent in insert_otherComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            insert_otherClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "insert_other"-------
            while continueRoutine:
                # get current time
                t = insert_otherClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=insert_otherClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in insert_otherComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "insert_other"-------
            for thisComponent in insert_otherComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # the Routine "insert_other" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1.0 repeats of 'insert_other_lists'
        
        
        # ------Prepare to start Routine "record_lists"-------
        continueRoutine = True
        # update component parameters for each repeat
        list_name = blocks[block_counter][list_counter][0]  # Set routine start values for list_name
        list_time = blocks[block_counter][list_counter][1]  # Set routine start values for list_time
        shuffle(words)
        word_counter=0
        list_counter+=1
        # keep track of which components have finished
        record_listsComponents = []
        for thisComponent in record_listsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        record_listsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "record_lists"-------
        while continueRoutine:
            # get current time
            t = record_listsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=record_listsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in record_listsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "record_lists"-------
        for thisComponent in record_listsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('list_name.routineEndVal', list_name)  # Save end routine value
        thisExp.addData('list_time.routineEndVal', list_time)  # Save end routine value
        # the Routine "record_lists" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'list_loop'
    
    
    # ------Prepare to start Routine "start_test"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    text_4.setText('מבחן חלק:\n')
    text_6.setText(block_counter+1)
    # keep track of which components have finished
    start_testComponents = [text_4, text_6]
    for thisComponent in start_testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    start_testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "start_test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = start_testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=start_testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in start_testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "start_test"-------
    for thisComponent in start_testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_loop.addData('text_4.started', text_4.tStartRefresh)
    blocks_loop.addData('text_4.stopped', text_4.tStopRefresh)
    blocks_loop.addData('text_6.started', text_6.tStartRefresh)
    blocks_loop.addData('text_6.stopped', text_6.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    test_loop = data.TrialHandler(nReps=len(words), method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='test_loop')
    thisExp.addLoop(test_loop)  # add the loop to the experiment
    thisTest_loop = test_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest_loop.rgb)
    if thisTest_loop != None:
        for paramName in thisTest_loop:
            exec('{} = thisTest_loop[paramName]'.format(paramName))
    
    for thisTest_loop in test_loop:
        currentLoop = test_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTest_loop.rgb)
        if thisTest_loop != None:
            for paramName in thisTest_loop:
                exec('{} = thisTest_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "test"-------
        continueRoutine = True
        # update component parameters for each repeat
        current_word=words[current_test_word][0]
        word_type=words[current_test_word][2]
        word_file=words[current_test_word][1]
        
        
        
        rating_test.keys = []
        rating_test.rt = []
        _rating_test_allKeys = []
        correct_raiting_for_answer = correct_rating  # Set routine start values for correct_raiting_for_answer
        correct = correct_answer  # Set routine start values for correct
        scoring_word = current_word  # Set routine start values for scoring_word
        slider.reset()
        new_word_label.setText(new_word               
)
        old_word_label.setText(old_word               
)
        show_word.setText(current_word)
        worf_list_name = word_file  # Set routine start values for worf_list_name
        word_type = word_type  # Set routine start values for word_type
        # keep track of which components have finished
        testComponents = [rating_test, slider, new_word_label, old_word_label, show_word, var_1_label, var_2_label, three_label, four_label, five_label, six_label]
        for thisComponent in testComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "test"-------
        while continueRoutine:
            # get current time
            t = testClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=testClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *rating_test* updates
            if rating_test.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                rating_test.frameNStart = frameN  # exact frame index
                rating_test.tStart = t  # local t and not account for scr refresh
                rating_test.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(rating_test, 'tStartRefresh')  # time at next scr refresh
                rating_test.status = STARTED
                # keyboard checking is just starting
                rating_test.clock.reset()  # now t=0
            if rating_test.status == STARTED:
                theseKeys = rating_test.getKeys(keyList=['1', '2', '3', '4', '5', '6'], waitRelease=False)
                _rating_test_allKeys.extend(theseKeys)
                if len(_rating_test_allKeys):
                    rating_test.keys = [key.name for key in _rating_test_allKeys]  # storing all keys
                    rating_test.rt = [key.rt for key in _rating_test_allKeys]
                    # a response ends the routine
                    continueRoutine = False
            
            # *slider* updates
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                slider.frameNStart = frameN  # exact frame index
                slider.tStart = t  # local t and not account for scr refresh
                slider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
                slider.setAutoDraw(True)
            
            # Check slider for response to end routine
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False
            
            # *new_word_label* updates
            if new_word_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                new_word_label.frameNStart = frameN  # exact frame index
                new_word_label.tStart = t  # local t and not account for scr refresh
                new_word_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(new_word_label, 'tStartRefresh')  # time at next scr refresh
                new_word_label.setAutoDraw(True)
            
            # *old_word_label* updates
            if old_word_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                old_word_label.frameNStart = frameN  # exact frame index
                old_word_label.tStart = t  # local t and not account for scr refresh
                old_word_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(old_word_label, 'tStartRefresh')  # time at next scr refresh
                old_word_label.setAutoDraw(True)
            
            # *show_word* updates
            if show_word.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                show_word.frameNStart = frameN  # exact frame index
                show_word.tStart = t  # local t and not account for scr refresh
                show_word.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(show_word, 'tStartRefresh')  # time at next scr refresh
                show_word.setAutoDraw(True)
            
            # *var_1_label* updates
            if var_1_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                var_1_label.frameNStart = frameN  # exact frame index
                var_1_label.tStart = t  # local t and not account for scr refresh
                var_1_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_1_label, 'tStartRefresh')  # time at next scr refresh
                var_1_label.setAutoDraw(True)
            
            # *var_2_label* updates
            if var_2_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                var_2_label.frameNStart = frameN  # exact frame index
                var_2_label.tStart = t  # local t and not account for scr refresh
                var_2_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(var_2_label, 'tStartRefresh')  # time at next scr refresh
                var_2_label.setAutoDraw(True)
            
            # *three_label* updates
            if three_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                three_label.frameNStart = frameN  # exact frame index
                three_label.tStart = t  # local t and not account for scr refresh
                three_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(three_label, 'tStartRefresh')  # time at next scr refresh
                three_label.setAutoDraw(True)
            
            # *four_label* updates
            if four_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                four_label.frameNStart = frameN  # exact frame index
                four_label.tStart = t  # local t and not account for scr refresh
                four_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(four_label, 'tStartRefresh')  # time at next scr refresh
                four_label.setAutoDraw(True)
            
            # *five_label* updates
            if five_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                five_label.frameNStart = frameN  # exact frame index
                five_label.tStart = t  # local t and not account for scr refresh
                five_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(five_label, 'tStartRefresh')  # time at next scr refresh
                five_label.setAutoDraw(True)
            
            # *six_label* updates
            if six_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                six_label.frameNStart = frameN  # exact frame index
                six_label.tStart = t  # local t and not account for scr refresh
                six_label.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(six_label, 'tStartRefresh')  # time at next scr refresh
                six_label.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "test"-------
        for thisComponent in testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        current_test_word+=1
        key_ratings=rating_test.keys
        key_rating=int(key_ratings[0])
        if word_type==0:
            if key_rating>3 and key_rating<7:
                correct_answer=1
            else:
                correcot_answer=0
        else:
            if key_rating>0 and key_rating<4:
                correct_answer=1
            else:
                correct_answer=0
            correct_rating= -1*key_rating+7
        
        # check responses
        if rating_test.keys in ['', [], None]:  # No response was made
            rating_test.keys = None
        test_loop.addData('rating_test.keys',rating_test.keys)
        if rating_test.keys != None:  # we had a response
            test_loop.addData('rating_test.rt', rating_test.rt)
        thisExp.addData('correct_raiting_for_answer.routineEndVal', correct_raiting_for_answer)  # Save end routine value
        thisExp.addData('correct.routineEndVal', correct)  # Save end routine value
        thisExp.addData('scoring_word.routineEndVal', scoring_word)  # Save end routine value
        test_loop.addData('slider.response', slider.getRating())
        test_loop.addData('slider.history', slider.getHistory())
        thisExp.addData('worf_list_name.routineEndVal', worf_list_name)  # Save end routine value
        thisExp.addData('word_type.routineEndVal', word_type)  # Save end routine value
        # the Routine "test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed len(words) repeats of 'test_loop'
    
    
    # ------Prepare to start Routine "record_block"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    word_counter=0
    list_counter=0
    words=[]
    block_counter+=1
    current_test_word=0
    # keep track of which components have finished
    record_blockComponents = [text_end_of_block]
    for thisComponent in record_blockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    record_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "record_block"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = record_blockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=record_blockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_end_of_block* updates
        if text_end_of_block.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_end_of_block.frameNStart = frameN  # exact frame index
            text_end_of_block.tStart = t  # local t and not account for scr refresh
            text_end_of_block.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_end_of_block, 'tStartRefresh')  # time at next scr refresh
            text_end_of_block.setAutoDraw(True)
        if text_end_of_block.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_end_of_block.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_end_of_block.tStop = t  # not accounting for scr refresh
                text_end_of_block.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_end_of_block, 'tStopRefresh')  # time at next scr refresh
                text_end_of_block.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in record_blockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "record_block"-------
    for thisComponent in record_blockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks_loop.addData('text_end_of_block.started', text_end_of_block.tStartRefresh)
    blocks_loop.addData('text_end_of_block.stopped', text_end_of_block.tStopRefresh)
# completed 4.0 repeats of 'blocks_loop'


# ------Prepare to start Routine "end_block"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_blockComponents = [ending]
for thisComponent in end_blockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_blockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_block"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_blockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_blockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ending* updates
    if ending.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ending.frameNStart = frameN  # exact frame index
        ending.tStart = t  # local t and not account for scr refresh
        ending.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ending, 'tStartRefresh')  # time at next scr refresh
        ending.setAutoDraw(True)
    if ending.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ending.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            ending.tStop = t  # not accounting for scr refresh
            ending.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ending, 'tStopRefresh')  # time at next scr refresh
            ending.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_blockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_block"-------
for thisComponent in end_blockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ending.started', ending.tStartRefresh)
thisExp.addData('ending.stopped', ending.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
