import dataset
import os
import numpy as np
import tensorflow as tf

def test(data_path, model_name, data_type):
    test_path = os.path.join(data_path, 'Testing')
    if data_type == "EDA":
        sig_name = "EDA_microsiemens"
        test_data = dataset.create_data(sig_name, test_path)
        model = tf.keras.models.load_model(model_name+'h5')
        loss, acc = model.evaluate(test_data[0], test_data[1], verbose=2)

    elif data_type == "mmhg":
        sig_name = "BP_mmHg"
    elif data_type == "mean":
        sig_name = "LA Mean BP_mmHg"
    elif data_type == "sys":
        sig_name = "LA Systolic BP_mmHg"
    elif data_type == "rate":
        sig_name = "Pulse Rate_BPM"
    elif data_type == "DIA":
        sig_name = "BP Dia_mmHg"
    elif data_type == "volt":
        sig_name = "Resp_Volts"
    elif data_type == "resp":
        sig_name = "Respiration Rate_BPM"
    elif data_type == "all":
        sig_name = "All Signals"
    else:
        print("Not specified data_type parameter")
        return 0