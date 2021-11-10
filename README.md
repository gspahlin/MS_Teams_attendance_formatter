# MS_Teams_attendance_formatter
Takes the .csv file given for attendence purposes by MS Teams, and rewrites it in a more useful format

MS Teams is a useful and popular teleconferencing suit. It's currently being used by many organizations for meetings, classes and informal conversations. One of
the more useful features of MS teams (particularly in the context of teaching and learning) is the ability to download a .csv with attendance information. The usefulness
of this feature is somewhat attenuated by its annoyances, though. The names of the people in your meeting show up in a single column, so they will be alphabetized
by first name. The attendance sheet also reads like an event log - every attendee shows up several times based on whether they were entering or leaving. 
<br><br>
<img src="https://github.com/gspahlin/MS_Teams_attendance_formatter/blob/master/figs/preformat.jpg">

This program is designed to quickly reformat an MS Teams output to make it more readable and to give information about how much time an attendee spent in a meeting
rather than about how many times they entered and left. Running the program will quickly write a new .csv with the format seen below.
<br><br>
<img src="https://github.com/gspahlin/MS_Teams_attendance_formatter/blob/master/figs/postformat.jpg">

The output is alphabetized by last name, and names are printed last, first. This works regardless of middle names. The script also calculates the total time the
attendees were in the room, so that you can easily see that for meetings where participants experienced connection problems or similar.

If you want to use the script simply download the .exe file and place it in a folder on your desktop, then follow the directions below.


Directions. 

1) In MS teams you can obtain an attendance list in .CSV format. You can download this in the participants section of the meeting. Here is a tutorial (https://www.youtube.com/watch?v=iAkZ1tlj1qg) 
if you've never done that. Step 1 is to download that list.

2) Go to the downloads folder and open the csv with excel. 

3) MS Teams will not export the .csv correctly so you need to resave the file - use the "save as" option to save the file to the same folder as 
attendance_formatter_v1.exe, and select the CSV UTF-8 option when saving the file.

4) Double click the .exe file. A console window will show up - you will be asked to type the name of the input file first, and then hit enter. You will get the same 
prompt to tell the program what to save your reformatted output as. 

Note: Your MS Teams output file must be formatted specifically as shown in the pictures and examples in this repo. Unless the software has changed, this is how it
will be formatted if you don't change the .csv file. Changing the format will cause the program to fail. The program also assumes that names will be in the format first last, and separated by a space.

Files and Folders

attendance_formatter_v1.exe - working program to reformat you attendance csv. This can be downloaded and run, as is. This program was written in python first
and then converted to an exe using auto-py-to-exe. This file is a little larger than you may expect (27 mb), as it requires Pandas and Numpy. 

attendance_formatter_v1.py - this is a python script version of the same program. you can use this instead if you have python installed, and know how to use it

meetingAttendanceList.csv - a simulated MS Teams output file with fake names

output1.csv - the output generated by processing the teams output with attendance_formatter_v1.exe
