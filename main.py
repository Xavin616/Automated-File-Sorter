#! /usr/bin/python3

import os, shutil
from shutil import move
from plyer import notification

filetypes = {
    'videos': ['.mp4', '.mkv', '.srt'],
    'music': ['.mp3', 'wav'],
    'pictures': ['.jpg', '.jpeg', '.png', '.webm', '.gif', '.svg'],
    'documents': ['.pdf', '.doc', '.txt', '.html', '.xml', '.json', '.zip', '.xpi', '.tar.gz', '.colors', '.deb']
}

def notify(title, message):
    notification.notify(
        title = title,
        message = message,

        timeout = 3
    )

def condition(name, filetype):
    condition = any(i in name for i in filetypes[filetype])
    return condition

def movefile(file, folder, filetype):
    print(f"Found File: {file} in {folder}")
    path = os.path.join(folder, file)
    newpath = "/home/xavin/" + filetype.capitalize()
    if folder == newpath:
        print(f"{file} already in {newpath}")
    else:
        print(f"Moving {file} --> /{filetype.capitalize()}")
        move(path, newpath)

def main():
    for folder, subs, files in os.walk("/home/xavin"):
        if any(x in folder for x in ["/lib", "/.git", "__pycache__", "/bin","/share", "/node_modules","/home/xavin/."]):
            continue

        for file in files:
            try: 
                if condition(file, 'videos'):
                    movefile(file, folder, 'videos')
                elif condition(file, 'documents'):
                    movefile(file, folder, 'documents')
                elif condition(file, 'pictures'):
                    movefile(file, folder, 'pictures')
                elif condition(file, 'music'):
                    movefile(file, folder, 'music')
                else: print("Continuing....")
            except Exception as e:
                print(f"Error encountered")
                notify("File Sorting Error", "An error occurred during file sorting.")
    print("Files have been sorted")
    notify("File Sorting Success", "Sorting of files in /home/xavin has been completed")

if __name__ == "__main__":
    main()