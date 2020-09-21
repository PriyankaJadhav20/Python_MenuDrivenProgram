import os
import pyttsx3

pyttsx3.speak('Welcome to your miniature virtual operating system')

while True:
    p = input('what can i do for you?')
    if ('run' in p or 'open') and 'chrome' in p:
        if ('dont' in p or 'do not' in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('chrome')
    if ('run' in p or 'open') and ('notepad' in p) or ('editor' in p):
        if ('dont' in p or 'do not' in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('notepad')
    if ('run' in p or 'open') and ('media' in p) or ('player' in p) or ('windows media player' in p):
        if ('dont' in p or 'do not' in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('wmplayer')
    if ('run' in p or 'open') and ('notebook' in p) or ('jupyter' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('jupyter notebook')
    if ('run' in p or 'open') and ('spotify' in p):
        if ('dont' in p or 'do not' in p or "don't" in p):
            print('Okay....i wont open it for you =\ ')
        else:    
            os.system('spotify')
    
    
    if 'break' in p or 'quit' in p:
        pyttsx3.speak('Goodbye and have a good day')
        break