import glob

folder_path = '/Users/rahul.madan/Downloads/Takeout/Google Photos/Nov 2021/'

Total = glob.glob(folder_path+'*')
json = glob.glob(folder_path+'*.json')
mp3 = glob.glob(folder_path+'*.mp4')
jpg = glob.glob(folder_path+'*.jpg')
JPG = glob.glob(folder_path+'*.JPG')
jpeg = glob.glob(folder_path+'*.jpeg')
HEIC = glob.glob(folder_path+'*.HEIC')
mov = glob.glob(folder_path+'*.mov')

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

all_files.extend([files[len(folder_path):] for files in Total])


print("Total files: ", len(all_files))
print("Total metadata files: ", len(all_metadata))
print("Total media files: ", len(all_metadata))

missing = []

for file in all_files:
    if file not in all_media and file not in all_metadata:
        missing.append(file)


print(missing)

