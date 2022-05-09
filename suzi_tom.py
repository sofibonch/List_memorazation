#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on April 27, 2022, at 10:46
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
expInfo = {'participant': '2'}
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
    originPath='D:\\OneDrive - Open University of Israel\\sofi\\work\\seminar-asi_tal\\suzi_tom\\suzi_tom.py',
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
long_time=0.25
num_of_lists=16
lists_in_block=4
words=[]

text_5 = visual.TextStim(win=win, name='text_5',
    text='ניסוי מתחיל',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

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
    size=(1, 0.7),
    pos=(0, 0),
    itemPadding=0.05
)
next = visual.ButtonStim(win, 
    text='->', font='Arvo',
    pos=(0, 0),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='bottom-right',
    name='next'
)
next.buttonClock = core.Clock()

# Initialize components for Routine "lists_order"
lists_orderClock = core.Clock()
count_list=0




   


# Initialize components for Routine "orgenize_blocks"
orgenize_blocksClock = core.Clock()

# Initialize components for Routine "words_loader"
words_loaderClock = core.Clock()
word_counter=0
list_counter=0
block_counter=0

showing_the_stim = visual.TextStim(win=win, name='showing_the_stim',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

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
text_4 = visual.TextStim(win=win, name='text_4',
    text='מבחן מתחיל',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-3.0);

# Initialize components for Routine "test"
testClock = core.Clock()
new_word="המילה בטוח חדשה"
old_word="המילה בטוח ישנה"
current_word=""
current_test_word=0
# Set experiment start values for variable component scoring_word
scoring_word = ''
scoring_wordContainer = []
slider = visual.Slider(win=win, name='slider',
    startValue=None, size=(1, 0.1), pos=(0, -0.4), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6), granularity=0.0,
    style='radio', styleTweaks=(), opacity=None,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)
new_word_label = visual.TextStim(win=win, name='new_word_label',
    text='',
    font='Open Sans',
    pos=(-0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-3.0);
old_word_label = visual.TextStim(win=win, name='old_word_label',
    text='',
    font='Open Sans',
    pos=(0.5, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-4.0);
show_word = visual.TextStim(win=win, name='show_word',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-5.0);

# Initialize components for Routine "record_block"
record_blockClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='מבחן הסתיים',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=-1.0);

# Initialize components for Routine "end_2"
end_2Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='ניסוי נגמר',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='RTL',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "setup_for_exp"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
setup_for_expComponents = [text_5]
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
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = setup_for_expClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=setup_for_expClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
        if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
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
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)

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
blocks_loop = data.TrialHandler(nReps=2.0, method='sequential', 
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
    
    # set up handler to look after randomisation of conditions etc
    list_loop = data.TrialHandler(nReps=2.0, method='random', 
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
        
        # set up handler to look after randomisation of conditions etc
        loading_words = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(blocks[block_counter][list_counter][0], selection='0:12'),
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
            # update component parameters for each repeat
            if word_counter==0 or word_counter==6 or word_counter==11:
                words.append(word)
            time_show=blocks[block_counter][list_counter][1]
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
            while continueRoutine:
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
                    if tThisFlipGlobal > showing_the_stim.tStartRefresh + time_show-frameTolerance:
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
            # the Routine "words_loader" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1.0 repeats of 'loading_words'
        
        
        # set up handler to look after randomisation of conditions etc
        insert_other_lists = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(blocks[block_counter][list_counter][0], selection='12:15'),
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
            words.append(word)
            
            
            
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
        record_listsComponents = [text_4]
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
                if tThisFlipGlobal > text_4.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
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
        list_loop.addData('text_4.started', text_4.tStartRefresh)
        list_loop.addData('text_4.stopped', text_4.tStopRefresh)
        # the Routine "record_lists" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'list_loop'
    
    
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
        current_word=words[current_test_word]
        scoring_word = current_word  # Set routine start values for scoring_word
        slider.reset()
        new_word_label.setText(new_word               
)
        old_word_label.setText(old_word               
)
        show_word.setText(current_word)
        # keep track of which components have finished
        testComponents = [slider, new_word_label, old_word_label, show_word]
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
        thisExp.addData('scoring_word.routineEndVal', scoring_word)  # Save end routine value
        test_loop.addData('slider.response', slider.getRating())
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
    block_counter+=1
    current_test_word=0
    # keep track of which components have finished
    record_blockComponents = [text_2]
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
            if tThisFlipGlobal > text_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_2.tStop = t  # not accounting for scr refresh
                text_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
                text_2.setAutoDraw(False)
        
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
    blocks_loop.addData('text_2.started', text_2.tStartRefresh)
    blocks_loop.addData('text_2.stopped', text_2.tStopRefresh)
# completed 2.0 repeats of 'blocks_loop'


# ------Prepare to start Routine "end_2"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_2Components = [text_3]
for thisComponent in end_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
        if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:
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
    for thisComponent in end_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_2"-------
for thisComponent in end_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

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
