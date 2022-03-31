import numpy as np
import tensorflow as tf
import os
import dataset

def train(data_path, model_name, data_type):
    train_path = os.path.join(data_path, 'Training')
    validation_path = os.path.join(data_path, "Validation")
    if data_type == "EDA":
        sig_name = "EDA_microsiemens"
        train_data = dataset.create_data(sig_name, train_path)
        validation_data = dataset.create_data(sig_name, validation_path)
        # flatten model.
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(256, activation='relu', input_shape=(512, )),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(10)
        ])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(0.001),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics = [tf.keras.metrics.Accuracy(), tf.keras.metrics.Recall(), tf.keras.metrics.Precision()],
        )
        # model.compile(
        #     optimizer=tf.keras.optimizers.Adam(0.001),
        #     loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        #     metrics = [tf.keras.metrics.SparseCategoricalAccuracy()],
        # )
        model.summary()
        model.fit(
            train_data[0],
            train_data[1],
            epochs=20,
            validation_data = validation_data,
        )
        model.save(model_name+'h5')
        # # case of cnn model.
        # model = tf.keras.models.Sequential([
        #     tf.keras.layers.Conv2D()
        # ])
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