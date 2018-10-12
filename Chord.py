import Note


class Chord:
    def __init__(self, notes, volume=0.5):
        self.size = len(notes)

        note_arr = []
        for freq in notes:
            note_arr.append(Note.Note(freq, volume))

        self.chord = tuple(note_arr)
