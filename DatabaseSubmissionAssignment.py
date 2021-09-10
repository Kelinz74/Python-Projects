
##Usint Python 3 and importing the sqlite3 module to build a database showing only .txt files
##from a list of mixed files.
import sqlite3

##a list of files to be sorted and only the txt files will be printed and added to a database
fileList = ('information.docx', 'Hello.txt','myImage.png', 'myMovie.mpg', 'World.txt', \
            'data.pdf', 'myPhoto.jpg')


##  a function to create a database that has 2 fields: an auto-increment primary integer
##  field and a field with the data type "string"
def Create_Database():
    conn = sqlite3.connect('DatabaseSubmissionAssignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_DataSub ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_DataType TEXT \
            )")
        conn.commit()
    conn.close()
  
##  a function to pull out the .txt from main list and create a new list, in turn using the .pop
##  method to get the txt files into individual values to be displayed in the database.

def tbl_fileList():
    ## part of the tbl_fileList function that seperates the .txt values from the main list.
    listFile =list(fileList)
    x = []
    for i in listFile:
        if '.txt' in i:
            x.append(i)
    txt1 = x.pop(0)
    x = x.pop(0)

    print(txt1)
    print(x)
    ## part of the tbl_fileList function that fills the colomn (col_DataType) in the database
    ## table with the .txt file names that was taken from the file list.
    conn = sqlite3.connect('DatabaseSubmissionAssignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_DataSub(col_DataType) VALUES (?)", \
                    [x])
        cur.execute("INSERT INTO tbl_DataSub(col_DataType) VALUES (?)", \
                    [txt1])
        conn.commit()
    conn.close()


if __name__ == "__main__":
    Create_Database()
    tbl_fileList()
    
    
