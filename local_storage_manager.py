import os
import datetime
from zipfile import ZipFile
import pathlib
import shutil


class GoogleTakeoutManager:
    def __init__(self):
        self.DATE_TODAY = datetime.datetime.today().strftime("%Y%m%d")
        self.DOWNLOAD_PATH = "C:/Users/SIX_l/Downloads"
        self.TEMP_FOLDER = self.DOWNLOAD_PATH + "/temp"
        self.SEARCH_TERM = f"takeout-{self.DATE_TODAY}"
        self.DESTINATION_PATH = f"C:/Users/SIX_l/GOOGLE.DRIVE.EXTRACTION.FILES.{self.DATE_TODAY}/"

    def run_management_program(self):
        self.extract_files_to_temp()
        self.move_image_files_to_destination()
        self.remove_json_clutter()
        self.calculate_file_size_reduction()
        self.delete_temp_folder()
        print("Operation completed.")

    def extract_files_to_temp(self):
        zipped_file = self.locate_google_takeout_zip()
        temp_destination = self.TEMP_FOLDER

        with ZipFile((self.DOWNLOAD_PATH + "/" + zipped_file), 'r') as zObject:
            zObject.extractall(path=temp_destination)
        print(f"Extracted {zipped_file}...")

    def locate_google_takeout_zip(self):
        search_term = self.SEARCH_TERM
        for root, dirs, files in os.walk(self.DOWNLOAD_PATH):
            for file in files:
                if search_term in file:
                    print(f"Found {search_term}...")
                    return file

    def move_image_files_to_destination(self):
        os.mkdir(self.DESTINATION_PATH)
        photo_folders_directory = self.TEMP_FOLDER + "/Takeout/Google Photos/"

        for root, dirs, files in os.walk(photo_folders_directory):
            for directory in dirs:
                if "Photo" in directory:
                    source_path = photo_folders_directory + directory
                    destination_path = self.DESTINATION_PATH + directory
                    os.rename(source_path, destination_path)

    def remove_json_clutter(self):
        folders = []
        for root, dirs, files in os.walk(self.DESTINATION_PATH):
            folders.append(root)
        folders.pop(0)
        for path in range(len(folders)):
            for root, dirs, files in os.walk(folders[path]):
                for file in files:
                    file_path = pathlib.Path(folders[path] + "/" + file)
                    if file_path.suffix == ".json":
                        os.remove(file_path)

    def calculate_file_size_reduction(self):
        original_size = os.path.getsize(self.TEMP_FOLDER)
        final_size = os.path.getsize(self.DESTINATION_PATH)
        bytes_saved = final_size - original_size
        print(f"The final output size was reduced by {bytes_saved} bytes!")

    def delete_temp_folder(self):
        shutil.rmtree(self.TEMP_FOLDER)
        print("The temp folder has been deleted.")
