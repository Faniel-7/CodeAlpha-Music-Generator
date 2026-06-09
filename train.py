import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import ModelCheckpoint

SEQUENCES_FILE = "data/sequences.pkl"
MODEL_FILE = "models/music_model.keras"

with open(SEQUENCES_FILE, "rb") as f:
    data = pickle.load(f)

network_input = data["network_input"]
network_output = data["network_output"]

print("Loading model...")
model = load_model(MODEL_FILE)

checkpoint = ModelCheckpoint(
    "models/best_model.keras",
    monitor="loss",
    verbose=1,
    save_best_only=True,
    mode="min"
)

print("Starting training...")

history = model.fit(
    network_input,
    network_output,
    epochs=20,
    batch_size=64,
    callbacks=[checkpoint]
)

print("Training completed!")