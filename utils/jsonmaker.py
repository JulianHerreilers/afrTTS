from ctypes import addressof
from importlib.metadata import metadata
import json

def trainjsonmaker(data_file_name, json_file_name):
    data_file = open(data_file_name, 'r')
    lines_data = data_file.readlines()
    data_file.close()

    file_names = []
    for i in range(0, len(lines_data)):
        lines_data[i] = lines_data[i].split("|")
        #address = lines_data[i][0].replace("|", "")
        address = lines_data[i][0]
        file_names.append(address)

    output=[]
    for i in range(0, 2400):
        temp = [
        "wavs/"+str(file_names[i]),
        "train/"+str(file_names[i])
    ]
        output.append(temp)



    json_object = json.dumps(output, indent=4)
    with open(json_file_name, "w") as outfile:
        outfile.write(json_object)


trainjsonmaker('metadata_incomplete_with_nums.csv','train.json')