import pickle
import numpy as np
import os

from music21 import instrument, note, chord, stream
from tensorflow.keras.models import load_model

def sample_with_temperature(preds, temperature=1.0):
    preds = np.asarray(preds).astype("float64")
    preds = np.log(preds + 1e-8) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds[0], 1)
    return np.argmax(probas)

def get_next_song_number(output_folder="output"):
    os.makedirs(output_folder, exist_ok=True)
    existing = [
        f for f in os.listdir(output_folder)
        if f.startswith("generated_song") and f.endswith(".mid")
    ]

    numbers = []
    for f in existing:
        name = f.replace("generated_song", "").replace(".mid", "")
        if name.isdigit():
            numbers.append(int(name))

    return max(numbers, default=0) + 1

MODEL_PATH = "models/best_model.keras"
NOTES_PATH = "data/notes.pkl"

print("Loading notes...")

with open(NOTES_PATH, "rb") as f:
    notes = pickle.load(f)

pitchnames = sorted(set(notes))

note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

sequence_length = 50

network_input = []

for i in range(len(notes) - sequence_length):
    sequence = notes[i:i + sequence_length]
    network_input.append([note_to_int[n] for n in sequence])

n_patterns = len(network_input)

print("Loading model...")
model = load_model(MODEL_PATH)

start = np.random.randint(0, len(network_input)-1)

pattern = network_input[start]

prediction_output = []

print("Generating notes...")

for note_index in range(700):

    prediction_input = np.reshape(
        pattern,
        (1, len(pattern), 1)
    )

    prediction_input = prediction_input / float(len(pitchnames))

    prediction = model.predict(
        prediction_input,
        verbose=0
    )

    index = sample_with_temperature(prediction, temperature=1.0)

    result = int_to_note[index]

    prediction_output.append(result)

    pattern.append(index)

    pattern = pattern[1:]

print("Generated", len(prediction_output), "notes")

offset = 0
output_notes = []

for pattern in prediction_output:

    if "." in pattern or pattern.isdigit():

        notes_in_chord = pattern.split(".")
        chord_notes = []

        for current_note in notes_in_chord:
            new_note = note.Note(int(current_note))
            new_note.storedInstrument = instrument.Piano()
            chord_notes.append(new_note)

        new_chord = chord.Chord(chord_notes)
        new_chord.offset = offset
        output_notes.append(new_chord)

    else:

        new_note = note.Note(pattern)
        new_note.offset = offset
        new_note.storedInstrument = instrument.Piano()

        output_notes.append(new_note)

    offset += 0.5

midi_stream = stream.Stream(output_notes)

midi_stream.write(
    "midi",
    fp="output/generated_music.mid"
)

song_number = get_next_song_number("output")
filename = f"output/generated_song{song_number}.mid"

midi_stream.write("midi", fp=filename)

print(f"Saved to {filename}")