class Conv:
    def __init__(self):
        self.guitar_dic = []
        self.ukulele_dic = []

        # populate guitar dictionary of notes
        self.guitar_dic.append(list(reversed(['E', 'A', 'D', 'G', 'B', 'E'])))
        self.guitar_dic.append(list(reversed(['F', 'A#/Bb', 'D#/Eb', 'G#/Ab', 'C', 'F'])))
        self.guitar_dic.append(list(reversed(['F#/Gb', 'B', 'E', 'A', 'C#/Db', 'F#/Gb'])))
        self.guitar_dic.append(list(reversed(['G', 'C', 'F', 'A#/Bb', 'D', 'G'])))
        self.guitar_dic.append(list(reversed(['G#/Ab', 'C#/Db', 'F#/Gb', 'B', 'D#/Eb', 'G#/Ab'])))
        self.guitar_dic.append(list(reversed(['A', 'D', 'G', 'C', 'E', 'A'])))
        self.guitar_dic.append(list(reversed(['A#/Bb', 'D#/Eb', 'G#/Ab', 'C#/Db', 'F', 'A#/Bb'])))
        self.guitar_dic.append(list(reversed(['B', 'E', 'A', 'D', 'F#/Gb', 'B'])))
        self.guitar_dic.append(list(reversed(['C', 'F', 'A#/Bb', 'D#/Eb', 'G', 'C'])))
        self.guitar_dic.append(list(reversed(['C#/Db', 'F#/Gb', 'B', 'E', 'G#/Ab', 'C#/Db'])))
        self.guitar_dic.append(list(reversed(['D', 'G', 'C', 'F', 'A', 'D'])))
        self.guitar_dic.append(list(reversed(['D#/Eb', 'G#/Ab', 'C#/Db', 'F#/Gb', 'A#/Bb', 'D#/Eb'])))
        self.guitar_dic.append(list(reversed(['E', 'A', 'D', 'G', 'B', 'E'])))

        # populate ukulele dictionary of notes
        self.ukulele_dic.append(list(reversed(['G', 'C', 'E', 'A'])))
        self.ukulele_dic.append(list(reversed(['G#/Ab', 'C#/Db', 'F', 'A#/Bb'])))
        self.ukulele_dic.append(list(reversed(['A', 'D', 'F#/Gb', 'B'])))
        self.ukulele_dic.append(list(reversed(['A#/Bb', 'D#/Eb', 'G', 'C'])))
        self.ukulele_dic.append(list(reversed(['B', 'E', 'G#/Ab', 'C#/Db'])))
        self.ukulele_dic.append(list(reversed(['C', 'F', 'A', 'D'])))
        self.ukulele_dic.append(list(reversed(['C#/Db', 'F#/Gb', 'A#/Bb', 'D#/Eb'])))
        self.ukulele_dic.append(list(reversed(['D', 'G', 'B', 'E'])))
        self.ukulele_dic.append(list(reversed(['D#/Eb', 'G#/Ab', 'C', 'F'])))
        self.ukulele_dic.append(list(reversed(['E', 'A', 'C#/Db', 'F#/Gb'])))
        self.ukulele_dic.append(list(reversed(['F', 'A#/Bb', 'D', 'G'])))
        self.ukulele_dic.append(list(reversed(['F#/Gb', 'B', 'D#/Eb', 'G#/Ab'])))
        self.ukulele_dic.append(list(reversed(['G', 'C', 'E', 'A'])))

    def find_note_guitar(self, fret, string):
        note = self.guitar_dic[fret][string]
        print("Note: {}".format(note))
        return note

    def find_eq_uku(self, note):
        notes = []
        for i in range(12):
            for j in range(3, -1, -1):
                if self.ukulele_dic[i][j] == note:
                    notes.append("{}:{}".format(i, j + 1))
        return notes

    def print_guitar(self):
        print("\n     Standard tunning")
        print("---------------------------------------------------")
        for i in range(13):
            print("{0:3} | ".format(i), end='')
            for j in range(6):
                print("{0:5s}  ".format(self.guitar_dic[i][j]), end=' ')
            print()

    def print_ukulele(self):
        print("\n     Soprano standard tunning")
        print("-----------------------------------")
        """
        for i in range(4):
            print("{0:5d}   ".format(i), end='')
        print()
        print("-----------------------------------")
        """
        for i in range(13):
            print("{0:3} | ".format(i), end='')
            for j in range(4):
                print("{0:5s}  ".format(self.ukulele_dic[i][j]), end=' ')
            print()

    def guitar_to_ukulele(self, ng):
        """
        Pass fret:string position or note to convert to ukulele fret:position

        How to use?
        guitar_to_ukulele("1:2") or guitar_to_ukulele("A#")

        and will return: ["1:4"] or ["1:4", "3:1", "6:3", "10:2"]
        """
        # check format input
        if ng.find(':') >= 0:
            fret, string = ng.split(':')
            note = self.find_note_guitar(int(fret), int(string) - 1)
            fs = self.find_eq_uku(note)
            return fs
        elif len(ng) == 2:
            return None
        elif len(ng) == 5 and ng.find('/') >= 0:
            return None
        else:
            print("[ERROR] Format not especified.")
            return None

    def ukulele_to_guitar(self, nu):
        pass

c = Conv()
c.print_guitar()
c.print_ukulele()
#print(c.guitar_to_ukulele('Bb'))
#print(c.guitar_to_ukulele('F#'))
print(c.guitar_to_ukulele('2:5'))
print(c.guitar_to_ukulele('2:4'))
print(c.guitar_to_ukulele('0:3'))
