import pickle
from collections import Counter

with open("data/notes.pkl", "rb") as f:
    notes = pickle.load(f)

print(f"Total notes: {len(notes)}")

unique_notes = len(set(notes))
print(f"Unique notes: {unique_notes}")

counter = Counter(notes)

print("\nTop 10 most common notes:")
for note, count in counter.most_common(10):
    print(f"{note}: {count}")