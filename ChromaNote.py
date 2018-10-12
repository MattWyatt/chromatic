import Note


class ChromaNote(Note.Note):
    def __init__(self, r, g, b, volume=0.5):
        def normalize_color_value(color):
            return round(((87 * color) / 255) + 1)

        def get_frequency(note_num):
            return 440 * (2 ** (1/12)) ** (note_num - 49)

        avg = (r + g + b) / 3

        super().__init__(get_frequency(normalize_color_value(avg)), volume)


