# Google Drive Space Maker Bot
## Declutter Google Drive with Selenium
### About the project
Once again my Google Drive is over capacity. I am not willing to pay for their cloud storage. 
Their solution, the associated Gmail account will stop receiving emails in a few weeks.
This is not the first time, and I am sure this is not the last. 

The project primary objective is to clean up the data delivered from Google. When Google sends
packets containing my images, 
a JSON file, containing data for each image, is also sent. For me these JSON files are clutter on my system that I will never clean up manually.

### Three objectives
1. Use Selenium to navigate my account and manage the download process.
2. Programmatically take the downloads, process, and file them appropriately. 
3. Implement Object Oriented Programing (OOPs)

### Google Drive Limitations
Google does not allow automated applications access to Google Drive. Login is prohibited.

Running the program now directs to the support documents and highlights this documentation with the use of Selenium.

<img src="./Screenshot 2024-11-14 110722.png">

### Local Storage Management
Within local_storage_manager.py, the class "GoogleTakeoutManager" resides. This class is named after the zipped
file google ships when exporting drive data. 

"GoogleTakeoutManager" manages the following:
+ Finding the target zip file
+ Unzipping the file into a temp folder
+ Navigating into the folder
+ Gathering only the necessary folders
+ Creating a new staging folder
+ Moving necessary folders to staging folder
+ Iterating through moved folders, deleting ".json" files
+ Calculating folder byte size reduction metric
+ Deleting temp folder 

### What was gained

This project acted as an entry into OPPs. Through the use of classes, whole operations may be tied together, 
freely able to share variable information, maintain partitioned code, provide clarity on the main file, 
and aide debugging efforts. 

OS, zipfile, pathlib, and shutil familiarity was also gained through implementation.

Although Selenium was not utilized in its full intent, it served as a toe-tip into the waters of automation. 

### Room for improvement

Hard coded paths litter "GoogleTakeoutManager" and make for a highly tailored application.
This makes for an app that can easily break if the local system changes, or if Google changes the format for their 
data export method. 



