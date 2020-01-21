import subprocess
import datetime
import os



# settings
writer_path = "C:\Program Files\LibreOffice\program\swriter.exe"
journal_base_path = "C:\Users\wayne\Dropbox\journal"

# get current date with strings for month folder and file names
current_month_dir_path =  os.path.join(datetime.datetime.now().strftime("%Y-%m-%b"))
current_file_name = os.path.join(journal_base_path ,datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"))

# check for current month dir

# create current month dir if does not exists


# check for current day file

# if there is not a current day file create that file

# open current day file


# python open command 
