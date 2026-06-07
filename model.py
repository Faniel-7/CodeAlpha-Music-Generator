import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

SEQUENCES_FILE = "data/sequences.pkl"
MODEL_OUTPUT = "models/music_model.keras"

def load_sequence_data(path):
    with open(path, "rb") as f:
        data = pickle.load(f)
    return data

def build_model(input_shape, output_units):
    model = Sequential()

    model.add(LSTM(256, input_shape=input_shape, return_sequences=True))
    model.add(Dropout(0.3))
    model.add(BatchNormalization())

    model.add(LSTM(256))
    model.add(Dropout(0.3))
    model.add(BatchNormalization())

    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.3))

    model.add(Dense(output_units, activation="softmax"))

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer=Adam(learning_rate=0.001),
        metrics=["accuracy"]
    )

    return model

def main():
    print("Loading training data...")
    data = load_sequence_data(SEQUENCES_FILE)

    network_input = data["network_input"]
    network_output = data["network_output"]

    print(f"Input shape: {network_input.shape}")
    print(f"Output shape: {network_output.shape}")

    # input_shape = (sequence_length, 1)
    input_shape = (network_input.shape[1], network_input.shape[2])
    output_units = len(data["pitchnames"])

    print("Building model...")
    model = build_model(input_shape, output_units)

    print("\nModel Summary:")
    model.summary()

    # Save the untrained model structure
    import os
    os.makedirs("models", exist_ok=True)
    model.save(MODEL_OUTPUT)
    print(f"\nModel saved to {MODEL_OUTPUT}")

if __name__ == "__main__":
    main()