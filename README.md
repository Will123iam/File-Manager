# File-Manager for Mac
A file manager application I am developing in my free time! It can show you any file on your computer and if it is a .mp3, then you can play it within the app.
This application is still in development, however, you can download and test it out now!

I started this project as I belived it would give my self a challenge. 
Developing this application to its current state has provided me with a greater understanding on the inner workings of tkinter and how to integrat it within my programs.
This program has been developed primarily using Object Orientated Programing (OOP) and is one of my first real attempts at OOP programing.

OOP provides so many advantages over procedual programming, allowing me to easily access varibles through out the program without the use of global or passing them through function after function.
Additionally, using OOP alongside tkinter allows for easy method calling and more contextual UI's.

## Download and run
To get started you need to download the repository and install the modules within the "requirements.txt". Then simply run the "Login.py" file to get started!

## Using the application
These simple steps explain how to use the file manager app with pictures.

### Opening a path
Appon launching the app, you should see a small window appear with a box to type a path within. Simply type the path you wish to open a press "Ok".
When relaunching the app, your most resent opened path will be stored and automatically filed in to the entry filed for you.

If the path you entered dose not exsist on your computer, then a red error message will appear at the bottom of the screen and you can update the path.

<img width="512" height="340" alt="Screenshot 2026-06-08 at 9 22 50 pm" src="https://github.com/user-attachments/assets/3986828b-7373-4e65-a2d1-e1bb38fc9c3d" />

### Navigating the side bar
Now you have entered a path, a larger window should appear displaying all the files within the path you just enterd, along the right hand side of the screen.
To simply open a folder click on it with the left mouse button. If the directory you have opened as a lot of files, you my need to scroll down with the mouse wheel.
After clicking on a file a new widget should appear within the main section of the screen. Here you can see all the files within the folder you just clicked on!

<img width="1312" height="940" alt="Screenshot 2026-06-08 at 10 02 57 pm" src="https://github.com/user-attachments/assets/139a9f14-d529-46d6-8fcb-6c3589517db0" />
<img width="1312" height="940" alt="Screenshot 2026-06-08 at 10 03 36 pm" src="https://github.com/user-attachments/assets/f11d408e-d131-4cff-8293-08d0c7dcb149" />

The open directory path is displayed in the bottom left of the screen, and the size of the text changes to ensure it fits.
If you would like to close a file you have clicked on, simply press the "Closs" button in the top left of that files widget.
(Currently "Back" dose not function)

Opening multiple files at once uses the additional space around the currently placed file widgets to open the new one.

### Playing a .mp3 file
To play a .mp3 file, simply savigate to where it is stored on you computer and click it. If it is supported the file icon should show as an mp3 file.
The media controll box in the bottom right correner of the app will now say the name of the file being played, the progress through the file and play / pause options.

<img width="1312" height="940" alt="Screenshot 2026-06-08 at 10 08 39 pm" src="https://github.com/user-attachments/assets/38c8e49a-1383-4f58-b4e2-3268b710fd2c" />


