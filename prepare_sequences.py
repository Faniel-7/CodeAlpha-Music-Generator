import pickle
import numpy as np
from collections import Counter

NOTES_FILE = "data/notes.pkl"
OUTPUT_FILE = "data/sequences.pkl"

SEQUENCE_LENGTH = 50  # good starting point for a small dataset

def load_notes(path):
    with open(path, "rb") as f:
        notes = pickle.load(f)
    return notes

def create_sequences(notes, sequence_length=50):
    pitchnames = sorted(set(notes))
    note_to_int = {note: number for number, note in enumerate(pitchnames)}
    int_to_note = {number: note for note, number in note_to_int.items()}

    network_input = []
    network_output = []

    for i in range(len(notes) - sequence_length):
        seq_in = notes[i:i + sequence_length]
        seq_out = notes[i + sequence_length]

        network_input.append([note_to_int[n] for n in seq_in])
        network_output.append(note_to_int[seq_out])

    n_patterns = len(network_input)

    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(len(pitchnames))

    network_output = np.array(network_output)

    return {
        "network_input": network_input,
        "network_output": network_output,
        "note_to_int": note_to_int,
        "int_to_note": int_to_note,
        "pitchnames": pitchnames,
        "sequence_length": sequence_length,
    }

def save_data(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)

def main():
    print("Loading notes...")
    notes = load_notes(NOTES_FILE)

    print(f"Total notes loaded: {len(notes)}")
    print(f"Unique notes: {len(set(notes))}")

    if len(notes) <= SEQUENCE_LENGTH:
        print("Not enough notes to create sequences.")
        return

    print("Creating sequences...")
    data = create_sequences(notes, SEQUENCE_LENGTH)

    print(f"Number of training patterns: {len(data['network_input'])}")
    print(f"Sequence length: {data['sequence_length']}")
    print(f"Vocabulary size: {len(data['pitchnames'])}")

    print("First input sequence:")
    print(data["network_input"][0])

    print("First output note index:")
    print(data["network_output"][0])

    save_data(data, OUTPUT_FILE)
    print(f"Saved prepared data to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()