from music21 import converter, instrument, note, chord
import os

MIDI_FOLDER = "data/midi"

def extract_notes_from_midi(file_path):
    notes = []
    midi = converter.parse(file_path)
       
    for element in midi.recurse():
        if isinstance(element, note.Note):
            notes.append(str(element.pitch))
        elif isinstance(element, chord.Chord):
            notes.append('.'.join(str(n) for n in element.normalOrder))
    return notes

def main():
    midi_files = [
    f for f in os.listdir(MIDI_FOLDER)
    if f.endswith(".mid") or f.endswith(".midi")
    ]

    print(f"Found {len(midi_files)} MIDI file.\n")

    if not midi_files:
        print("No MIDI files found.")
        return

    first_file = os.path.join(MIDI_FOLDER, midi_files[0])
    print(f"Reading: {first_file}\n")

    notes =extract_notes_from_midi(first_file)

    print (f"total notes extracted: {len(notes)}\n")
    print("First 100 notes:")
    print (notes[:100])

if __name__ == "__main__":
    main()