import os
import cv2 as cv2
from icrawler.builtin import GoogleImageCrawler

# crawer setting
folder_name = 'C://Github//VTDEEP//python//dataset//crawling//'
start_year = 2019
yearRange = 1
image_width = 512
image_height = 512
max_file_count = 700


classCount = 0
monthRange = 1

for className in os.listdir(folder_name):

    if className == '.DS_Store': continue

    classCount = 0
    fullPath = folder_name + "/" + className;

    google_crawler = GoogleImageCrawler(storage={'root_dir': folder_name + '/' + className + '/'})

    for year in range(yearRange):
       for month in range(monthRange):
           month += 1
           google_crawler.crawl(keyword=className,
                                filters={'date': ((start_year + year,  month, 1), (start_year + year, month, 28))},
                                max_num=max_file_count,
                                file_idx_offset='auto')
    classCount = classCount + 1
    fileIndex = 0

    if os.path.isdir(fullPath):
        fileList = os.listdir(fullPath)
        for fileName in fileList:
            if fileName == '.DS_Store' : continue

            filePath = fullPath + "/" + fileName
            filename, file_extension = os.path.splitext(filePath)
            if file_extension != '.jpg' and file_extension != '.bmp' and file_extension != '.gif' and file_extension != '.jpeg' and file_extension != '.png':
                os.remove(filePath)
                continue

            fileIndex = fileIndex + 1
            modifiedPath = fullPath + "/" + str(fileIndex) + "_" + str(classCount) + "_" + className + '.jpg'
            original = cv2.imread(filePath)

            if original is None:
                os.remove(filePath)
                fileIndex = fileIndex = fileIndex - 1
                continue

            if len(original.shape) != 3:
                os.remove(filePath)
                fileIndex = fileIndex = fileIndex - 1
                continue

            resizeImage = cv2.resize(original, (image_width, image_height), interpolation=cv2.INTER_AREA)
            npImage = []

            cv2.imwrite(modifiedPath, resizeImage)
            cv2.imshow('resize', resizeImage)
            cv2.waitKey(10)
            os.remove(filePath)