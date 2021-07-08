# Example data structure


class Database:
    def __init__():
        # song_metadata = {}
        database = {}

    def store_fingerprint(self, fingerprints, song_title, times):
        # key: (freq, neighbor_freq, time_delta)), value: (song, time_of_occurence)
        # store fingerprints of 1 song
        for i in in range(len(fingerprints)):
            f = fingerprints[i]

            if f in self.database:
                self.database[f].append((song_title, times[i]))
            else:
                self.database[f] = [(song_title, times[i])]

    def search_fingerprint(self, fingerprints):
        # key: fingerprints, value: (song, time_of_occurence)
        # all fingerprints of a song are given, return most likely song

        from collections import Counter
        c = Counter()

        for f in fingerprints:
            if f in self.database:
                c[("song title", "time delay"))] += 1

            # consider returning counts here or in notebook
        return song

    '''def save_song(self, song_name, author):
        # save song metadata with a unique ID
        self.song_metadata[len(self.song_metadata)] = (song_name, author)
        return len(self.song_metadata) # return the ID?'''

    def load_database(self):
        import pickle

        with open("fingerprints.pkl", mode = "rb") as fingerprints_file:
            self.database=pickle.load(fingerprints_file)

        return

    def save_database(self):

        with open("fingerprints.pkl", mode = "wb") as fingerprints_file:
            pickle.dump(self.database, fingerprints_file)
        return
