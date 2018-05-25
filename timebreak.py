import time
import  webbrowser
total_break=3
total_count=0
print("this program started on "+time.ctime())
while(total_count<total_break):
   time.sleep(2*60*60)
   webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
   total_count=total_count+1
