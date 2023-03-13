import glob
import os
from pathlib import Path
import shutil

folder_path = '/Users/rahul.madan/Downloads/Takeout/Google Photos/Nov 2021/'
total = glob.glob(folder_path + '*')
json = glob.glob(folder_path + '*.json')
mp3 = glob.glob(folder_path + '*.mp4')
jpg = glob.glob(folder_path + '*.jpg')
JPG = glob.glob(folder_path + '*.JPG')
jpeg = glob.glob(folder_path + '*.jpeg')
HEIC = glob.glob(folder_path + '*.HEIC')
mov = glob.glob(folder_path + '*.mov')

all_files = []
all_media = []
all_metadata = []

all_media.extend([video[len(folder_path):] for video in mp3])
all_media.extend([image[len(folder_path):] for image in jpg])
all_media.extend([image[len(folder_path):] for image in JPG])
all_media.extend([image[len(folder_path):] for image in jpeg])
all_media.extend([image[len(folder_path):] for image in HEIC])
all_media.extend([image[len(folder_path):] for image in mov])

all_metadata.extend([metadata[len(folder_path):] for metadata in json])
all_metadata.remove("metadata.json")

all_files.extend([files[len(folder_path):] for files in total])

print(all_files)
print("Total files: ", len(all_files))
print("Total metadata files: ", len(all_metadata))
print("Total media files: ", len(all_media))

missing = []

for file in all_files:
    if file not in all_media and file not in all_metadata:
        missing.append(file)
print("Check for any missed extension except metadat.json")
print(missing)

missing_media = []

for media in all_media:
    if media + ".json" not in all_metadata:
        missing_media.append(media)

print()
print(len(missing_media))
print("media which do not have metadata file or metadata file is not named correctly: \n", missing_media)

missing_metadata = []
for metadata in all_metadata:
    if Path(metadata).stem not in all_media:
        missing_metadata.append(metadata)

print(len(missing_metadata))
print("Json files which are not used: \n", missing_metadata)

# write a code to detect image names which have name longer than 46 characters (excluding extension .mp3, .jpeg) and rename their json files

for media in all_media:
    if len(media) > 46:
        extension = media.split(".")[-1]
        try:
            os.rename(folder_path + media[:46] + ".json", folder_path + media + ".json")
        except FileNotFoundError:
            pass


#updating lists

missing_media = []

for media in all_media:
    if media + ".json" not in all_metadata:
        missing_media.append(media)

print()
print(len(missing_media))
print("media which do not have metadata file or metadata file is not named correctly: \n", missing_media)

missing_metadata = []
for metadata in all_metadata:
    if Path(metadata).stem not in all_media:
        missing_metadata.append(metadata)

print(len(missing_metadata))
print("Json files which are not used: \n", missing_metadata)

# updating lists completed



# write a code to make duplicate .json file if 'edited' present in media file name

for media in missing_media:
    if Path(media).stem.endswith("-edited"):
        extension = media.split(".")[-1]
        shutil.copy(folder_path+Path(media).stem[:len(Path(media).stem)-7]+"."+extension+".json",folder_path+media+".json")

#updating lists

missing_media = []

for media in all_media:
    if media + ".json" not in all_metadata:
        missing_media.append(media)

print()
print(len(missing_media))
print("media which do not have metadata file or metadata file is not named correctly: \n", missing_media)

missing_metadata = []
for metadata in all_metadata:
    if Path(metadata).stem not in all_media:
        missing_metadata.append(metadata)

print(len(missing_metadata))
print("Json files which are not used: \n", missing_metadata)

# updating lists completed



# write a code to rename json files which have '(1)' in .json file name

for metadata in missing_metadata:
    os.rename(folder_path+metadata,Path(Path(metadata).stem).stem)


# decide a uniform media name, based on timestamp, location name, persons, etc

# process image with

# make index of images based on faces

# make index based on latitude longitude

# use aws recognition to put labels
