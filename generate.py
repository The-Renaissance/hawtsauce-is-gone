import glob, os


dataset_path = 'Dataset/Images'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
file_extensions = [".jpg", ".JPG"]
for extension in file_extensions:
    for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*" + extension)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))

        if counter == index_test+1:
            counter = 1
            file_test.write(dataset_path + "/" + title + extension + "\n")
        else:
            file_train.write(dataset_path + "/" + title + extension + "\n")
            counter = counter + 1
