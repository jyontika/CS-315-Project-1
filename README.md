# CS-315-Project-1
#### @authors: Jyontika Kapoor, Ashley You, Ryan Boone, Audrey Yip, Josie Ramírez, Miraya Gupta
##### Project Topic: Followers

This project is conducted by six students at Wellesley College CS-315: Data Science for the Web.
We are replicating a TikTok experiment paper by Boeker and Urman at the University of Zurich.

#### Methods to run tests:
1. Please clone the repo; leave the files in its folder
2. Open the control_saves.py and testing_saves.py
3. Run both at the same by opening two terminals and directing both terminals to the folder containing this repo
4. Enter the line below in one terminal:

```
python -m pytest tiktok/control_saves.py --html=report_active.html
```
5. Immediately enter the next line below:

```
python -m pytest tiktok/testing_saves.py --html=report_control.html

```
6. Two windows should pop up with the page to the Tiktok login page and make sure to keep track of which page is for the control and which is for the testing
7. Put the username and password
8. The browsers should close when the script is finished
9. Three files will show up in the data folder:
       a) data_saved_videos = all of the data from the videos the script saved
       b) save_data_all_videos = all of the data from the testing batches
       c) control_data_all_videos = all of the data from the control batches
