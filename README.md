# CS-315-Project-1
#### @authors: Jyontika Kapoor, Ashley You, Ryan Boone, Audrey Yip, Josie Ramírez, Miraya Gupta
## Project Topic: Followers

This project is conducted by six students at Wellesley College CS-315: Data Science for the Web.
We are replicating a TikTok experiment paper by Boeker and Urman at the University of Zurich.

## Data Collection
#### Methods to run tests:
1. Please clone the repo; leave the files in its folder
2. pip install seleniumbase in terminal if you haven't already
3. Open the control_saves.py and testing_saves.py
4. Run both at the same by opening two terminals and directing both terminals to the folder containing this repo
5. Enter the line below in one terminal:

```
python -m pytest control_saves.py --html=report_active.html
```
5. Immediately enter the next line below:

```
python -m pytest testing_saves.py --html=report_control.html

```
6. Two windows should pop up with the page to the Tiktok login page and **make sure to keep track of which page is for the control and which is for the testing**
7. Put the username and password
8. The browsers should close when the script is finished
9. Three files will show up in the data folder: <br />
       a) data_saved_videos = all of the data from the videos the script saved <br />
       b) save_data_all_videos = all of the data from the testing batches <br />
       c) control_data_all_videos = all of the data from the control batches <br />

## data_copy_for_eni 
This folder is a duplicate of our data, but with each CSV file in the folder of the student who ran it. 


## Data Analysis
All notebooks and files used are in the Our-Data-Analysis folder:

1. **Jaccard-And-Summary-Analysis.ipynb** : Includes code for exploratory analysis, calculating summary statistics, graphing distribution of batch sizes, and analyzing difference of feeds using the Jaccard Index.
2. **Bar-Plots.ipynb** : This notebook includes codes for graphics that count the frequency of hashtags, authors, etc. It also includes graphics made for summary statistics.
3. **Popularity Analysis** : This notebook includes code for creating dataframes for each paired user test run, calculating popularity metrics (likes/shares/comments/saves) and graphing these metrics. 
