import os
import shutil


# Define where to move each file
destinations = {
    'jpeg': 'OneDrive/cleaned/',
    'jpg': 'OneDrive/cleaned/',
    'png': 'OneDrive/cleaned/',
    'gif': 'OneDrive/cleaned/',
    'mp3': 'Music',
    'mp4': 'Videos/cleaned/',
    'avi': 'Videos/cleaned/',
    'zip': 'Documents/cleaned/',
    'rar': 'Documents/cleaned/',
    '7z': 'Documents/cleaned/',
    'pdf': 'Documents/cleaned/',
    'exe': 'Documents/installers/',
}


# Define WHERE and HOW to clean
home = '/mnt/c/Users/pkvj2'
folder = 'Downloads'
folder_to_clean = os.path.join(home, folder)
mode = 'default' # default or in-place
print()
print('Cleaning:',folder_to_clean)


for dest in destinations.values():
    path_dest = os.path.join(home,dest)
    if(not os.path.exists(path_dest)):
        os.mkdir(path_dest)

# Starts cleaning process
files = os.listdir(folder_to_clean)

for f in files:
    if(os.path.isfile(os.path.join(folder_to_clean, f))):
        extension = f.split('.')[-1].lower()
        error = False
        
        try:
            destinations[extension]
        except KeyError:
            print(f' - {extension} has no specified destination')
            error = True
            
        if(not error):
            shutil.move(
                os.path.join(folder_to_clean, f),
                os.path.join(home, destinations[extension], f)
            )


print('Folder cleaned!')
print()