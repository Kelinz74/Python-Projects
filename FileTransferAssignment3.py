import shutil
import os
import os.path, time
import datetime
from datetime import datetime, timedelta
import tkinter
from tkinter import *
from tkinter import ttk, Button
from tkinter.filedialog import askdirectory

#utilizing the module datetime have taken todays date - 24 hours and broke it down into seconds
#to compare time within the last 24 hours and the modifcation time stamp of a txt file
date_N_days_ago = datetime.now() - timedelta(days = 1)
current_time_stamp = date_N_days_ago.timestamp()

# created an instance of tkinter frame
tk = tkinter.Tk()
# gave the tk window a title
tk.title('Daily File Transfer')
#function for displaying a window of your window directory that you can create and or choose a
#a folder to copy files from and a folder to paste files to.  Will also only copy the files
#with a file modification timestamp of within the last 24 hours.
def processFiles():
    #display the folder directory and ask for a folder = copy from
    sourceDir = askdirectory()+"/"
    #display in an entry box sourceDir
    labelFilePath1.insert(0, sourceDir)
    #display the folder directory and ask for a folder = paste to
    targetDir = askdirectory()+"/"
    #display in an entry box targetDir
    labelFilePath2.insert(0, targetDir)
    #creat a list of filds from sourceDir folder = file names
    files = os.listdir(sourceDir)
    #iterate through the files with a for loop
    for i in files:
        #getmtime() to get the modified date from a file. comparing it to a time from from now
        #to 24 hourse ago represented by second gauging from the epoch of when time started
        #dependent upon platform
        if os.path.getmtime(sourceDir + i) > current_time_stamp:
            #copy the files from the source folder to the target folder
            shutil.copy(sourceDir+i, targetDir)
            
#tkinter button to call processFiles() function
fileTransfer_button = Button(tk, bg='lightblue', text="File Transfer", command = processFiles)
fileTransfer_button.grid(row=1,column=0,rowspan=4, padx=10, pady=10, ipady=10)

#lables to display information and entry boxes to display information.
labelFilePath1name = Label(tk, text='Folder Business', font=("Helvetica", 10))
labelFilePath1name.grid(row=1, column=1)
labelFilePath1 = Entry(tk, bg='lightblue', font=("Helvetica", 10), width=115)
labelFilePath1.grid(row=2, column=1)
labelFilePath2name = Label(tk, text='Folder Copy Business', font=("Helvetica", 10))
labelFilePath2name.grid(row=3, column=1)
labelFilePath2 = Entry(tk, bg='lightblue', font=("Helvetica", 10), width=115)
labelFilePath2.grid(row=4, column=1, pady=(0,15))
#size of the tkinter window
tk.geometry('915x100')

if __name__ == '__main__':
    tk.mainloop()
    
