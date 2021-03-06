Instructions:

To run the app you can double click on the kivyapp.exe file.  By default the password that you need to use for the first screen is "password123". 
The default answer for the images is the top row of buttons from left to right (123).
There is also a file called kiviapp.ini.  This file is automatically generated with default values so if you ever delete by mistake or want to "reset"
everything back to the default you can just delete the kivyapp.ini file and it will be recreated automatically the next time you run the kivyapp.exe.


Configuration:

All of the configuration for the app is inside the kivyapp.ini file.  All you need to do is open the file with a text editor like Notepad and you can change any of the
text you see in the app and of course you can also change the password and any of the images you see.

Note: Any time you save a change to the kivyapp.ini file you should close the kivyapp.exe program and reopen it if it was already running in order for the change
to fully take effect.

To configure the images on the second screen.  In the kivyapp.ini file you will see a section called [images] with names image1 through image9.  By default 
the program expects to find the location of these default images in the same folder that the kivyapp.exe is in, but you can change that as long as
you specify the path to your images relative to where the kivyapp.exe program is located.  Example you could create a folder called "images" and 
put all of your images in there as long as you specify the image location for the images like: image1 = images\circle.png OR image1 = C:\images\circle.png.

You should be able to use any images you want to specify, however you may want to use the same resolution as the default images which are all 128 x 128.
Larger size images might work but it hasn't been tested or if they are too large may run outside of the button dimensions causing them to get cut off.

Note: the default images included are not auto generated if they are deleted.

To change the sequence of images you need to press on the second screen look for the "imageanswer" field in the kivyapp.ini file.  The default value
is imageanswer = 123.  This means you should push the image buttons in the top row from left to right.  The images on the second grid are counted
from 1 to 9, where image one button starts in the upper left corner to the bottom right most image button.  

Example, if you change to imageanswer = 159 then you would need to press the top left most button, the center button, then the bottom right most button before advancing
to the success screen.  If you change imageanswer = 98765 then it means you would need to press image9, image8, image7, image6, the image5 in that order to advance to the
success screen.  You could also repeat image presses and make imageanswer = 556677

Note: there is maximum length you can configure for imageanswer, but you should only use numbers 1 - 9 since each digit
represent one of the nine images on the screen you need to press in that correct sequence in order to advance.  If you configure it beyond that it will produce an error.



Note: if you make any mistake while editing the kivyapp.ini file you can just delete it and the next time you run the kivyapp.exe it will just recreate it with the
default settings.


