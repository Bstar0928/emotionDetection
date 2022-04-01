import os
import numpy as np

def create_data(sig_name, datapath):
    files = os.listdir(datapath)
    sample_size = 576
    output_data = []
    input_data = np.array([])
    max_len = 1000
    if sig_name == "All Signals":
        for filename in files:
            name_meanings = filename.split("_")
            if int(name_meanings[1]) > 10:
                    break
            output_data.append(int(name_meanings[1]) - 1)
            input_row = []
            with open(os.path.join(datapath, filename), 'r') as f:
                count = 0
                while count < sample_size:
                    count += 1
                    val = f.readline()
                    if not val:
                        break
                    val = float(val[:-2])
                    input_row.append(val)
            input_data.append(input_row)
            if len(input_row) < max_len:
                max_len = len(input_row)
        print(max_len)
        input_data = np.array(input_data, dtype="float32")
        output_data = np.array(output_data, dtype = "int32")
        print(len(output_data))
    else:
        for filename in files:
            if sig_name in filename:
                name_meanings = filename.split("_")
                if int(name_meanings[1]) > 10:
                    break
                output_data.append(int(name_meanings[1])-1)
                row = np.loadtxt(os.path.join(datapath, filename), dtype='float32')
                
                input_row = row[:sample_size].reshape((24, 24))
                np.append(input_data, input_row)
                # input_data.append(input_row)
                if len(input_row) < max_len:
                    max_len = len(input_row)
        print('max len'+str(len(input_data[0])))
        # input_data = np.array(input_data, dtype="float32")
        output_data = np.array(output_data, dtype = "int32")
        print(len(input_data[0]))
    return (input_data, output_data)
