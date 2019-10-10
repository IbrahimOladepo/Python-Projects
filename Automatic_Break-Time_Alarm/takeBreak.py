import webbrowser
import time

totalBreak = 5
countBreak = 0

while(countBreak < totalBreak):
  print("Starting session: ", (countBreak + 1))
  time.sleep(60*30)
  webbrowser.open("BREAKEST.mp4")
  countBreak = countBreak + 1
