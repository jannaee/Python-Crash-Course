import time
import webbrowser
#imports allow python to know bring in open a web browser


total_breaks = 3
break_count = 0

print ("Starting..." + time.ctime())
while (break_count < 3):
    time.sleep(5)#program reads for 5 seconds and run 3 times
    webbrowser.open("https://www.youtube.com/watch?v=5txHGxJRwtQ")
    break_count += 1

print ("Done son")


    
