import math

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
        # print("guitar: {}:{}".format(fret, string + 1))
        note = self.guitar_dic[fret][string]
        return note

    def find_eq_uku(self, note):
        notes = []
        for i in range(12):
            for j in range(3, -1, -1):
                if self.ukulele_dic[i][j] == note:
                    notes.append("{}:{}".format(i, j + 1))
        return notes

    def guitar_note_is_valid(self, instrument, note):
        fret, string = note.split(':')
        # is valid
        if 12 >= fret >= 0 and 6 >= string >= 1:
            return True
        # isn't
        else:
            return False

    def select_closest_eq_note_gtu(self, note_guitar, eq_ukulele):
        if note_guitar != None and len(eq_ukulele) > 0:
            closest = None
            dif_closest = math.inf
            fret_g, string_g = note_guitar.split(':')
            for note in eq_ukulele:
                fret_eq, string_eq = note.split(':')
                dif_now = abs(int(fret_g) - int(fret_eq))
                if dif_now < dif_closest:
                    closest = note
                    dif_closest = dif_now
            return closest
        else:
            return None

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
        for i in range(13):
            print("{0:3} | ".format(i), end='')
            for j in range(4):
                print("{0:5s}  ".format(self.ukulele_dic[i][j]), end=' ')
            print()

    def guitar_to_ukulele(self, ng):
        """
        Pass fret:string position or note to convert to ukulele fret:position

        How to use?
        guitar_to_ukulele("1:2") or guitar_to_ukulele("A#") or 
        guitar_to_ukulele("Eb") or guitar_to_ukulele("F#/Gb")

        and will return: ["1:4"] or ["1:4", "3:1", "6:3", "10:2"]
        """
        # check format input
        if ng.find(':') >= 0:
            fret, string = ng.split(':')
            note = self.find_note_guitar(int(fret), int(string) - 1)
            fs = self.find_eq_uku(note)
            right = self.select_closest_eq_note_gtu(ng, fs)
            return right
        elif len(ng) == 2:
            return None
        elif len(ng) == 5 and ng.find('/') >= 0:
            return None
        else:
            print("[ERROR] Format not especified.")
            return None

    def print_tab_guitar(self, tab_guitar):
        number_patterns = int(len(tab_guitar)/6)
        for p in range(number_patterns):
            print()
            print(tab_guitar[6*p], end='')
            print(tab_guitar[6*p + 1], end='')
            print(tab_guitar[6*p + 2], end='')
            print(tab_guitar[6*p + 3], end='')
            print(tab_guitar[6*p + 4], end='')
            print(tab_guitar[6*p + 5], end='')
            print()

    def print_tab_ukulele(self, tab_ukulele):
        number_patterns = int(len(tab_ukulele)/4)
        for p in range(number_patterns):
            print()
            print(tab_ukulele[4*p])
            print(tab_ukulele[4*p + 1])
            print(tab_ukulele[4*p + 2])
            print(tab_ukulele[4*p + 3])
            print()

    def process_tab_guitar(self, tab_guitar):
        number_patterns = int(len(tab_guitar)/6)

        # inicialization of ukulele tablature
        tab_ukulele = []

        uk = []
        for pattern in range(number_patterns):
            if tab_guitar[6*pattern][0] == '-':
                start_point = 0
            elif tab_guitar[6*pattern][0] == '|':
                start_point = 1
            elif tab_guitar[6*pattern][0] == 'e':
                start_point = 2

            st1 = tab_guitar[6*pattern]
            st2 = tab_guitar[6*pattern + 1]
            st3 = tab_guitar[6*pattern + 2]
            st4 = tab_guitar[6*pattern + 3]
            st5 = tab_guitar[6*pattern + 4]
            st6 = tab_guitar[6*pattern + 5]

            uk.append(list("A|{}|".format(''.join(['-' for l in range(len(st1) - 4)]))))
            uk.append(list("E|{}|".format(''.join(['-' for l in range(len(st1) - 4)]))))
            uk.append(list("C|{}|".format(''.join(['-' for l in range(len(st1) - 4)]))))
            uk.append(list("G|{}|".format(''.join(['-' for l in range(len(st1) - 4)]))))

            stop = len(tab_guitar[6*pattern]) - 2
            i = start_point

            flag_dig_s1 = False
            flag_dig_s2 = False
            flag_dig_s3 = False
            flag_dig_s4 = False
            flag_dig_s5 = False
            flag_dig_s6 = False
            while i < stop:
               # print("i = {}".format(i))
                # e
                if st1[i].isdecimal():
                    if flag_dig_s1:
                        flag_dig_s1 = False
                    else:
                        if st1[i+1].isdecimal():
                            eq = self.guitar_to_ukulele("{}:{}".format(''.join([st1[i], st1[i+1]]), 1))
                            flag_dig_s1 = True
                        else:
                            eq = self.guitar_to_ukulele("{}:{}".format(st1[i], 1))
                        fret, string = eq.split(':')
                        print("ukulele: {}:{}".format(fret, string))
                        if int(fret) >= 10:
                            if st1[i+1].isdecimal():
                                uk[int(string) - 1][i-1] = fret[0]
                                uk[int(string) - 1][i] = fret[1]
                            else:
                                uk[int(string) - 1][i] = fret[0]
                                uk[int(string) - 1][i+1] = fret[1]
                        else:
                            uk[int(string) - 1][i] = fret

                # B
                if st2[i].isdecimal():
                    if flag_dig_s2:
                        flag_dig_s2 = False
                    else:
                        if st2[i + 1].isdecimal():
                            eq = self.guitar_to_ukulele("{}:{}".format(''.join([st2[i], st2[i+1]]), 2))
                            flag_dig_s2 = True
                        else:
                            eq = self.guitar_to_ukulele("{}:{}".format(st2[i], 2))
                        fret, string = eq.split(':')
                        #print("ukulele: {}:{}".format(fret, string))
                        if int(fret) >= 10:
                            if st2[i+1].isdecimal():
                                uk[int(string) - 1][i-1] = fret[0]
                                uk[int(string) - 1][i] = fret[1]
                            else:
                                uk[int(string) - 1][i] = fret[0]
                                uk[int(string) - 1][i+1] = fret[1]
                        else:
                            uk[int(string) - 1][i] = fret

                # G
                if st3[i].isdecimal():
                    if flag_dig_s3:
                        flag_dig_s3 = False
                    else:
                        if st3[i + 1].isdecimal():
                            eq = self.guitar_to_ukulele("{}:{}".format(''.join([st3[i], st3[i+1]]), 3))
                            flag_dig_s3 = True
                        else:
                            eq = self.guitar_to_ukulele("{}:{}".format(st3[i], 3))
                        fret, string = eq.split(':')
                        ##print("ukulele: {}:{}".format(fret, string))
                        if int(fret) > 10:
                            if st3[i+1].isdecimal():
                                uk[int(string) - 1][i-1] = fret[0]
                                uk[int(string) - 1][i] = fret[1]
                            else:
                                uk[int(string) - 1][i] = fret[0]
                                uk[int(string) - 1][i+1] = fret[1]
                        else:
                            uk[int(string) - 1][i] = fret

                # D
                if st4[i].isdecimal():
                    if flag_dig_s4:
                        flag_dig_s4 = False
                    else:
                        if st4[i + 1].isdecimal():
                            eq = self.guitar_to_ukulele("{}:{}".format(''.join([st4[i], st4[i+1]]), 4))
                            flag_dig_s4 = True
                        else:
                            eq = self.guitar_to_ukulele("{}:{}".format(st4[i], 4))
                            flag_dig_s4 = False
                        if eq != None:
                            fret, string = eq.split(':')
                            #print("ukulele: {}:{}".format(fret, string))
                            if int(fret) > 10:
                                if st4[i+1].isdecimal():
                                    uk[int(string) - 1][i-1] = fret[0]
                                    uk[int(string) - 1][i] = fret[1]
                                else:
                                    uk[int(string) - 1][i] = fret[0]
                                    uk[int(string) - 1][i+1] = fret[1]
                            else:
                                uk[int(string) - 1][i] = fret

                # A
                if st5[i].isdecimal():
                    if flag_dig_s5:
                        flag_dig_s5 = False
                    else:
                        if st5[i + 1].isdecimal():
                            eq = self.guitar_to_ukulele("{}:{}".format(''.join([st5[i], st5[i+1]]), 5))
                            flag_dig_s5 = True
                        else:
                            eq = self.guitar_to_ukulele("{}:{}".format(st5[i], 5))
                            flag_dig_s5 = False
                        if eq != None:
                            fret, string = eq.split(':')
                            # print("ukulele: {}:{}".format(fret, string))
                            if int(fret) > 10:
                                if st5[i+1].isdecimal():
                                    uk[int(string) - 1][i-1] = fret[0]
                                    uk[int(string) - 1][i] = fret[1]
                                else:
                                    uk[int(string) - 1][i] = fret[0]
                                    uk[int(string) - 1][i+1] = fret[1]
                            else:
                                uk[int(string) - 1][i] = fret

                # E
                if st6[i].isdecimal():
                    if flag_dig_s6:
                        flag_dig_s6 = False
                    else:
                        if st6[i + 1].isdecimal():
                            eq = self.guitar_to_ukulele("{}:{}".format(''.join([st6[i], st6[i+1]]), 6))
                            flag_dig_s6 = True
                        else:
                            eq = self.guitar_to_ukulele("{}:{}".format(st6[i], 6))
                        if eq != None:
                            fret, string = eq.split(':')
                            #print("ukulele: {}:{}".format(fret, string))
                            if int(fret) > 10:
                                if st6[i+1].isdecimal():
                                    uk[int(string) - 1][i-1] = fret[0]
                                    uk[int(string) - 1][i] = fret[1]
                                else:
                                    uk[int(string) - 1][i] = fret[0]
                                    uk[int(string) - 1][i+1] = fret[1]
                            else:
                                uk[int(string) - 1][i] = fret
                i = i + 1

            tab_ukulele.append(''.join(uk[0]))
            tab_ukulele.append(''.join(uk[1]))
            tab_ukulele.append(''.join(uk[2]))
            tab_ukulele.append(''.join(uk[3]))
            uk = []

        return tab_ukulele

    def tabguitar_to_tabukulele(self, tab_guitar):
        """
        Usage:
            tab_guitar is a file that contains ONLY the tab for guitar

            tabguitar_to_tabukulele('file_with_tab.txt')

            and return a text with equivalent tab on ukulele
        """
        print("Processing \'{}\'...".format(tab_guitar))
        file = open(tab_guitar, 'r')
        
        if file.readable():
            tab = file.readlines()
            tab = [line for line in tab if len(line) > 1]
            self.print_tab_guitar(tab)
            if len(tab)%6 == 0:
                tab_ukulele = self.process_tab_guitar(tab)
                return tab_ukulele
            else:
                print("[ERROR] Wrong tab pattern")
                return None

    def ukulele_to_guitar(self, nu):
        pass

c = Conv()
c.print_guitar()
c.print_ukulele()
#print(c.guitar_to_ukulele('Bb'))
#print(c.guitar_to_ukulele('F#'))
print(c.guitar_to_ukulele('8:4'))
print(c.guitar_to_ukulele('6:3'))
print(c.guitar_to_ukulele('0:3'))
c.print_tab_ukulele(c.tabguitar_to_tabukulele('belivier_teste.txt'))
c.print_tab_ukulele(c.tabguitar_to_tabukulele('where_is_my_mind.txt'))
c.print_tab_ukulele(c.tabguitar_to_tabukulele('ghost_towns.txt'))