import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# # flatten model.
# model = tf.keras.models.Sequential([
#     tf.keras.layers.Dense(10, activation='relu', input_shape=(20, )),
#     tf.keras.layers.Dense(3)
# ])
# model.compile(
#     optimizer=tf.keras.optimizers.Adam(0.001),
#     loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
#     # metrics = [tf.keras.metrics.Accuracy(), tf.keras.metrics.Recall(), tf.keras.metrics.Precision(), tf.keras.metrics.Accuracy()],
# )
# model.summary()


# # Call model on a test input
# x = np.random.rand(10, 20)
# y = np.array([1,2,3,4,3,2,3, 2,3,4])
# print(type(x))
# model.fit(
#     x,
#     y,
#     epochs=5,
#     # validation_data = validation_data,
# )
# model.save('aa.h5')
# # model = keras.Sequential(
# #     [
# #         layers.Dense(2, activation="relu", name="layer1", input_shape=(3, )),
# #         layers.Dense(4, activation="relu", name="layer2")
# #     ]
# # )
# # y = model(x)
# # print(y)
ds_train_x = []
for i in range(100):
    input_row = []
    for i in range(512):
        input_row.append(np.random.randint(0,1000))
    ds_train_x.append(input_row)
ds_train_x = np.array(ds_train_x, dtype='float32')

# ds_train_x = np.random.rand(100, 784)
ds_train_y = np.array([1, 2,3, 0]*25)
# model = tf.keras.models.Sequential([
#     # tf.keras.layers.Flatten(input_shape = (784,)),
#     tf.keras.layers.Dense(128, activation='relu', input_shape = (784,)),
#     tf.keras.layers.Dense(10)
# ])
model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(512, activation='relu', input_shape=(512, )),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(4)
        ])
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001),
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics = [tf.keras.metrics.SparseCategoricalAccuracy()],
)

model.summary()

model.fit(
    ds_train_x,
    ds_train_y,
    epochs = 6,
    # validation_data = validataiondata,
)