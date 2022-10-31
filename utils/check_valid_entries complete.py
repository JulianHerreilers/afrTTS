from this import d
import shutil, os
from split_num_letters import split_nums_letters as split_n_l


def preprocess_entire_dataset (data_file_name, dict_file_name, processed_data_file_name):
    data_file = open(data_file_name, 'r')
    dict_file = open(dict_file_name, 'r')
    lines_data = data_file.readlines()
    lines_dict = dict_file.readlines()
    dict_file.close()
    data_file.close()

    dict = []
    for i in range(0, len(lines_dict)):
        lines_dict[i] = lines_dict[i].split()
        dict.append(lines_dict[i][0])

    
    total_nums = 0
    total_words_added = 0
    total_words = 0
    #Converting to lowercase
    for i in range(0, len(lines_data)):
        a = lines_data[i].split()[1:]
        data_str = " ".join(str(word) for word in a)
        extra_line = split_n_l(data_str)
        index = lines_data[i].split()
        index = index[0]
        line = " ".join(str(word) for word in extra_line)
        lines_data[i] = []
        line = index + " " + line
        lines_data[i]= line.split()
        total_words += len(lines_data[i])
        # lines_data[i]= lines_data[i].split()
        

        for j in range(0, len(lines_data[i])):
            #if lines_data[i][j].isdigit(): total_nums+=1
            lines_data[i][j] = lines_data[i][j].replace("-", " ")
            lines_data[i][j] = lines_data[i][j].replace("+", " ")
            lines_data[i][j] = lines_data[i][j].replace("%", "persent")
            lines_data[i][j] = lines_data[i][j].replace('\"', "")
            if lines_data[i][j] != "'n": lines_data[i][j] = lines_data[i][j].replace('\'', " ")
            lines_data[i][j] = lines_data[i][j].replace("!", "")
            lines_data[i][j] = lines_data[i][j].replace("?", "")
            lines_data[i][j] = lines_data[i][j].replace(".", "")
            lines_data[i][j] = lines_data[i][j].replace(",", "")
            if j > 0: lines_data[i][j] = lines_data[i][j].replace("_", "")
            lines_data[i][j] = lines_data[i][j].lower()

    with open(processed_data_file_name, 'w') as file:
        for i in range(0, len(lines_data)):
            new_line = " ".join([str(word) for word in lines_data[i]])
            file.write('%s \n' %new_line)
    file.close()

    print("Data lowercased")
    #total_words = 0
    files = []
    file = open("metadata_incomplete_with_nums.csv", "w")
    with open(processed_data_file_name) as data:
        data_arr=data.readlines()
        for i in range(0, len(data_arr)):
            line = data_arr[i].split()
            length = len(line) - 1
            fixed_line = "".join(line[0])
            fixed_line = fixed_line+"|"
            size = 0
            for j in range(1, len(line)):
                
                for k in range(0, len(dict)):
                    if line[j] == dict[k]:
                        total_words_added +=1
                        word_added = 1
                        if j==1: fixed_line=fixed_line+line[j]
                        else: fixed_line=fixed_line+" "+line[j]
                        size+=1
                    
                #if word_added==0: print(f"word not in: .{line[j]}.")
            #processed_data=''.join(word for word in data_arr[i].split() if word in dict)
            fixed_line = fixed_line+"\n"
            # print(len(line))
            # print(fixed_line)
            # print("Size:%d", size)
            if size:
                file.write(fixed_line)
                file_name = "afr_data\wavs\\"+str(line[0])+".wav"
                files.append(file_name)
            fixed_line=""
        print("done")
    file.close()


    print("all incomplete sentences removed")

    print("Similarity Checked and absent words removed")


    print(f"Total nums added:{total_nums}")
    print(f"Total words:{total_words}")
    print(f"Total words added:{total_words_added}")


    




data_file_name = 'TTScorpora.tsv'
dict_file_name = 'rcrl_apd.1.4.1.txt'
processed_data_file_name = 'test.csv'
preprocess_entire_dataset (data_file_name, dict_file_name, processed_data_file_name)