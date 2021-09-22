
########### Web Page Generator Part One, Two ######################

#Import of modules tkinter and webbrowser
from tkinter import *
from tkinter import ttk
import webbrowser

# created an instance of tkinter frame
window = Tk()
# gave the window a title, hight and width, and background color
window.title("Web Page Generator")
window.geometry("450x50")
window.configure(bg='lightgray')
#function for creating a file, inputing data into the file and then closing the file
#also reopen the file to display the data in the file on the console then close file again.
def clicked():
    
# open() will create a file nameing the file the first parameter set as the name of the file
#and then type of file (simpleHTML.html in this case), the second parameter can have several
#different aurguments set in place, in this case "w" (write) will create a file if the specified
#file does not exist.    
    f = open("simpleHTML.html", "w")

#f.write is adding data to the file in a text type form. In this case in the form of HTML.
    f.write("<html>\n\t<body>\n\t\t<h1>\n\t" + txt_input.get() + "\n\t\t</h1>\n\t</body>\n</html>")

#f.close will close the file
    f.close

#this open method will save in the variable f the data of the file.  The HTML text that was
#previously imputed with the f.write method, "r" =  read
    f = open("simpleHTML.html", "r")

#display in the console the data from the HTML file
    print(f.read())
    f.close
    
##webbrowser imported can open the file in a new browser window utilizing the python
##method open_new_tab()
    webbrowser.open_new_tab("simpleHTML.html")

#tkinter button for calling the function clicked()

button_1 = Button(window, text="Generate HTML", command=clicked)
button_1.grid(row=0, column=0, pady=(10,0), padx=(10,0), ipadx=10, sticky=W)

#input box to input information that the function can take to input into HTML code in the file
#and display the file once the code in saved to the file in a default web browser.
txt_input = Entry(window,width=50)
txt_input.grid(row=0, column=2, padx=(10,0), pady=(10,0), ipady=2)

#call to the mainloop method to keep the app running.
if __name__ == '__main__':
    window.mainloop()
