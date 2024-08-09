import curses
from curses import wrapper
import time
import random

def start(stdscr) :
    stdscr.clear()
    stdscr.addstr("Welcome to TYPING SPEED test !!\n")
    stdscr.addstr("Press any key to start : ")
    stdscr.refresh()
    stdscr.getkey()

lines = ["Mr. Arnold will be holding a meeting with a number of residents tonight.","To pay for his studies, Ryan works as a waiter in a restaurant.","Some residents were disappointed with the mayor's new policy.","Yuriko and Mina are going to Hawaii this summer.","Ted goes to the gym and exercises three times a week."]    

def display (stdscr,target,current,wpm=0) :
     stdscr.addstr(f"{target}\n")
     stdscr.addstr(f"WPM : {wpm}")
     for i,text in enumerate(current) :
            color = curses.color_pair(1)
            
            if (text != target[i]) :
               color =  curses.color_pair(2)
            
            stdscr.addstr(0,i,text,color)
            
            


def test (stdscr) :
    target_text =  random.choice(lines) 
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True :
     time_elapsed = max(time.time() - start_time , 1)
     wpm = round((len(current_text)/(time_elapsed/60))/5)
     stdscr.clear()
     display(stdscr,target_text,current_text,wpm)
     stdscr.refresh()

     if ("".join(current_text) == target_text) :
         stdscr.nodelay(False)
         break
     
     try :
        key = stdscr.getkey()
     except :
         continue

     if (ord(key) == 27) :
         break
     if (ord(key) == 8) :
          if (len(current_text) > 0) :
              current_text.pop()
     elif (len(current_text)<len(target_text)) :
          current_text.append(key)
     
     

     
def template(stdscr) :
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    start(stdscr)
    test(stdscr)
    stdscr.addstr(2,0,"You completed the test ! press any key to continue")
    stdscr.getkey()
wrapper(template)
