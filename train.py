import numpy as np
import tensorflow as tf
import os
import dataset
# import tensorflow_datasets as tfds

def train(data_path, model_name, data_type):
    train_path = os.path.join(data_path, 'Training')
    validation_path = os.path.join(data_path, "Validation")
    if data_type == "EDA":
        sig_name = "EDA_microsiemens"
        train_data = dataset.create_data(sig_name, train_path)
        # xxx = np.array(np.array([3.4, 4, 3.7])).astype(np.float32)
        x_train = np.asarray(train_data[0]).astype(np.float32)
        y_train = np.asarray(train_data[1]).astype(np.int32)
        train_input = train_data[0].astype(np.float32)
        validation_data = dataset.create_data(sig_name, validation_path)
        # (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
        # train_labels = train_labels[:1000]
        # test_labels = test_labels[:1000]

        # train_images = train_images[:1000].reshape(-1, 28 * 28) / 255.0
        # test_images = test_images[:1000].reshape(-1, 28 * 28) / 255.0

        # print(train_data[0][0][0])
        # flatten model.
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(512, activation='relu', input_shape=(784, )),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10)
        ])
        model.compile(
            optimizer=tf.keras.optimizers.Adam(0.001),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics = [tf.keras.metrics.Accuracy(), tf.keras.metrics.Recall(), tf.keras.metrics.Precision(), tf.keras.metrics.Accuracy()],
        )
        model.summary()
        model.fit(
            x_train,
            y_train,
            epochs=5,
            validation_data = validation_data,
        )
        model.save(data_type.lower()+'.h5')
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