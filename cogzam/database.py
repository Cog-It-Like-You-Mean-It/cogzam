# Example data structure


class Database:
    def __init__():
        #song_metadata = {}
        database = {}

    def store_fingerprint(self, fingerprints, song_title, times):
        # key: (freq, neighbor_freq, time_delta)), value: (song, time_of_occurence)
        # store fingerprints of 1 song
        for i in in range(len(fingerprints)):
            f = fingerprints[i]

            if f in self.database:
                self.database[f].append((song_title, time[i]))
            else:
                self.database[f] = [(song_title, time[i])]

        return

    def search_fingerprint(self, fingerprints):
        # key: fingerprints, value: (song, time_of_occurence)
        # all fingerprints of a song are given, return most likely song

        import collections.Counter
        retrieved_fingerprint = self.database[fingerprint]

        # consider returning counts here or in notebook
        return retrieved_fingerprint

    '''def save_song(self, song_name, author):
        # save song metadata with a unique ID
        self.song_metadata[len(self.song_metadata)] = (song_name, author)
        return len(self.song_metadata) # return the ID?'''

    def load_database(self):
        import pickle

        with open("fingerprints.pkl", mode="rb") as fingerprints_file:
            self.database = pickle.load(fingerprints_file)

        '''with open("song_metadata.pkl", mode="rb") as metadata_file:
            self.song_metadata = pickle.load(metadata_file)'''
        return

    def save_database():
        return
