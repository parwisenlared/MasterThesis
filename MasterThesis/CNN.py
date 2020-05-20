import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers



model = keras.Sequential(
    [
        layers.Dense(2, activation="relu"),
        layers.Dense(3, activation="relu"),
        layers.Dense(4),
    ]
)

if __name__ == "__main__":
    model.layers