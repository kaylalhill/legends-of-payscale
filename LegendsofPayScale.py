# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 13:13:05 2012

@author: kaylah
"""
import time
def displayIntro():
    print('')
    print('*** LEGENDS OF PAYSCALE ***')
    print('')
    time.sleep(3)
    print('You emerge from the elevator into a mysterious land full of cubicles.')
    print('')
    print('Kayle, the Front Desk Overseer, tells you:')
    print('\'It\'s dangerous to go alone.  Take this!\'')
    print('')
    time.sleep(3)
    print('Kayle gives you a Soda.')
    time.sleep(5)
    print('')
    print('You wander down Registered Nurse Route and reach an open area.')
    print('There are two paths.')
    print('One path leads to the Mezzanine, while the other path leads to the Kitchen.')
    print('')
    
def choosePath():
    path = ''
    while path != 'Kitchen' and path != 'Mezzanine':
        print('Which path will you take? ("Kitchen" or "Mezzanine")')
        path = raw_input('--> ').title()
        
    return path
    
def checkPath(chosenPath):
    print('')
    print('You pass several people talking into what seems like thin air...')
    time.sleep(2)
    
    kitchenPath = 'Kitchen'
    
    if chosenPath == str(kitchenPath):
        print('And dodge flying ping-pong balls aimed at your head...')
        time.sleep(3)
        print('')
        print('...and you see Chef Patrick. He gives you a sandwich! What luck! +5 Happiness')
        time.sleep(5)
        print('')
        print('Munching on your sandwich, you ascend the stairs.')
    else:
        print('And ascend the stairs.')

def displayIntro2():
    time.sleep(2)
    print('At the top of the stairs you\'re greeted by the PSP Marketing Team.')
    print('You wave hi back.')
    time.sleep(3)
    print('')
    print('The Jeweler\'s Loop defines the perimeter of the Mezzanine.')
    print('To the left it leads across the catwalk.')
    print('To the right is unknown territory.')
    
def choosePath2():
    path2 = ''
    while path2 != 'Left' and path2 != 'Right':
        print('')
        print('Which way will you go? ("Left" or "Right")')
        path2 = raw_input('--> ').title()
        
    return path2

def checkPath2(chosenPath2):
    print('')
    print('Your heart beats rapidly in your chest as you continue your journey...')
    
    leftPath = 'Left'
    
    if chosenPath2 == str(leftPath):
        time.sleep(2)
        print('You look over the catwalk railing at the people in cubicles down below...')
        time.sleep(4)
        print('')
        print('...but you aren\'t watching where you\'re going, and you run into Adam!')
        print('')
        print('He insults you and you cry. +10 Despair')
        time.sleep(4)
        print('')
        print('You run away to drink your Soda and heal.')
        print('Phew. That was a close one.')
    else:
        time.sleep(2)
        print('You turn the corner, bracing for the worst...')
        time.sleep(3)
        print('')
        print('...and you find the Data Team! You\'re with cool people now.')
        print('Life is awesome. +10 Happiness')


playAgain = 'Yes'
while playAgain == 'Yes' or playAgain == 'Y':
    
    displayIntro()
    pathNumber = choosePath()
    checkPath(pathNumber)

    displayIntro2()
    pathNumber2 = choosePath2()
    checkPath2(pathNumber2)
    
    print('')        
    print('Would you like to play again? ("Yes" or "No")')
    playAgain = raw_input('--> ').title()
    
    if playAgain == 'No':
        print('Exited.')
        