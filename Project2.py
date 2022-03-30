import sys
# import os
import train
import test

def main():
    if len(sys.argv) != 5:
        print("command usage: python Project2.py <testOrTrain> <data_directory_path> <model_name> <data_type>")
        sys.exit()
    mode = sys.argv[1]
    data_path = sys.argv[2]
    model_name = sys.argv[3]
    data_type = sys.argv[4]
    if mode == "train":
        train.train(data_path, model_name, data_type)
    elif mode == "test":
        test.test(data_path, model_name, data_type)
    else:
        print("First argument must be 'test' or 'train'")
        sys.exit()
if __name__=="__main__":
    main()