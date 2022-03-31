import os
import numpy as np

def create_data(sig_name, datapath):
    files = os.listdir(datapath)
    sample_size = 512
    output_data = []
    input_data = []
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
        input_data = np.array(input_data, dtype="float32")
        output_data = np.array(output_data, dtype = "int32")
    return (input_data, output_data)
