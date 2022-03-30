import dataset


def test(data_path, model_name, data_type):
    test_path = os.path.join(data_path, 'Testing')
    if data_type == "EDA":
        sig_name = "EDA_microsiemens"
        (in_data, out_data) = dataset.create_data(sig_name, train_path)
        nd_in_data = np.array(in_data)
        print(type(nd_in_data[0]))
        nd_out_data = np.array(out_data, dtype='float32')
        model = tf.keras.models.load_model(data_type.lower()+'h5')
        loss, acc = model.evaluate(test_in_data, test_out_data, verbose=2)

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