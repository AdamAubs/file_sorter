import os
import sys 
import logging
import shutil
import json
import fnmatch
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler

source_dir = '/Users/AdamsHole/Downloads'

with open('file_types.json') as file:
    file_types = json.load(file)

class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        file_extension =  os.path.splitext(event.src_path)[1].lower()
        source_file = event.src_path
        image_destination_folder = '/Users/AdamsHole/Desktop/Images'
        document_destination_folder = '/Users/AdamsHole/Desktop/Document'
        video_destination_folder = '/Users/AdamsHole/Desktop/Video'
        audio_destination_folder = '/Users/AdamsHole/Desktop/Audio'
        screen_shot_folder = '/Users/AdamsHole/Desktop/Images/Screen_Shots'

        if event.is_directory:
            print('file not found')
            return
        elif event.event_type == 'created':
            if file_extension in file_types["image"]:
                print('this is an image file')
                print("File extension:", file_extension)
                print("File path:", event.src_path)
                shutil.move(source_file, image_destination_folder)
                print(f"File moved: {source_file} --> {os.path.join(screen_shot_folder, os.path.basename(source_file))}")
            
                
                image_files = os.path.basename(event.src_path)
                print(image_files)
                print(event.src_path)
                print(image_destination_folder)
                print(os.path.join(image_destination_folder, os.path.basename(source_file)))
                new_screen_shot_file = os.path.join(image_destination_folder, os.path.basename(source_file))

                if fnmatch.fnmatch(image_files, 'Screen Shot*'):
                    print(f"The file {image_files} is a screen shot")
                    shutil.move(new_screen_shot_file, screen_shot_folder)
                    #print(f"File moved: {image_files} --> {screen_shot_folder}")
                

            if file_extension in file_types["document"]:
                print('this is an document file')
                print("File extension:", file_extension)
                print("File path:", event.src_path)
                shutil.move(source_file, document_destination_folder)
                print(f"File moved: {source_file} --> {document_destination_folder}")
            
            if file_extension in file_types["video"]:
                print('this is an video file')
                print("File extension:", file_extension)
                print("File path:", event.src_path)
                shutil.move(source_file, video_destination_folder)
                print(f"File moved: {source_file} --> {video_destination_folder}")
            
            if file_extension in file_types["audio"]:
                print('this is an audio file')
                print("File extension:", file_extension)
                print("File path:", event.src_path)
                shutil.move(source_file, audio_destination_folder)
                print(f"File moved: {source_file} --> {audio_destination_folder}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()