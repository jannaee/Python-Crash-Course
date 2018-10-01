import time
import webbrowser
#imports allow python to open a web browser


total_breaks = 3
break_count = 0

print ("Starting..." + time.ctime())
while (break_count < 3):
    time.sleep(2700)#program runs every 45 minutes 3 times
    webbrowser.open("https://www.youtube.com/watch?v=5txHGxJRwtQ")
    break_count += 1

print ("done son")


    
