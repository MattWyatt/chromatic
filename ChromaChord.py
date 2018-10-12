import Chord


class ChromaChord(Chord.Chord):
    def __init__(self, r, g, b, volume=0.5):
        def normalize_color_value(color):
            return round(((87 * color) / 255) + 1)

        def get_frequency(note_num):
            return 440 * (2 ** (1/12)) ** (note_num - 49)

        red_freq = get_frequency(normalize_color_value(r))
        green_freq = get_frequency(normalize_color_value(g))
        blue_freq = get_frequency(normalize_color_value(b))

        super().__init__((red_freq, green_freq, blue_freq), (volume, volume, volume))
