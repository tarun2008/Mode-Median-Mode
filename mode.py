import csv
from collections import Counter

with open("data.csv", newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []
for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))
data = Counter(newData)
mode_data_for_range = {"100-120":0,"120-140":0,"140-160":0}
for weight,occurance in data.items():
    if 100<float(weight)<120:
        mode_data_for_range["100-120"] += occurance
    elif 120<float(weight)<140:
        mode_data_for_range["120-140"] += occurance
    elif 140<float(weight)<160:
        mode_data_for_range["140-160"] += occurance
modeRange,modeOccurance = 0,0
for range,occurance in mode_data_for_range.items():
    if occurance>modeOccurance:
        modeOccurance=occurance
        modeRange = [int(range.split('-')[0]),int(range.split('-')[1])]  
mode = float((modeRange[0]+modeRange[1])/2)
print(mode)                         