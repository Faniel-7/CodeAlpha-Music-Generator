from music21 import converter, instrument, note, chord
import os
import pickle

MIDI_FOLDER = "data/midi"
OUTPUT_FILE = "data/notes.pkl"

def extract_notes_from_midi(file_path):
    notes = []

    try:
        midi = converter.parse(file_path)

        for element in midi.recurse():
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    except Exception as e:
        print(f"Skipping {file_path} because of error: {e}")

    return notes

def process_all_midi_files():
    all_notes = []

    midi_files = [
        f for f in os.listdir(MIDI_FOLDER)
        if f.endswith(".mid") or f.endswith(".midi")
    ]

    print(f"Found {len(midi_files)} MIDI files.\n")

    for idx, midi_file in enumerate(midi_files, start=1):
        file_path = os.path.join(MIDI_FOLDER, midi_file)
        print(f"Processing {idx}/{len(midi_files)}: {midi_file}")

        notes = extract_notes_from_midi(file_path)
        print(f"  Notes extracted: {len(notes)}")

        all_notes.extend(notes)

    return all_notes

def save_notes(notes, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "wb") as f:
        pickle.dump(notes, f)

    print(f"\nSaved {len(notes)} notes to {output_file}")

def main():
    notes = process_all_midi_files()

    if len(notes) == 0:
        print("No notes were extracted. Check your MIDI files.")
        return

    print(f"\nTotal notes collected: {len(notes)}")
    print("First 50 notes:")
    print(notes[:50])

    save_notes(notes, OUTPUT_FILE)

if __name__ == "__main__":
    main()