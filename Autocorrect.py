class Autocorrect:

    def __init__(self, fileName):
        self.file = fileName
        self.dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [
        ], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}

    def createDict(self):
        fp = open('allwords.txt')
        word = fp.readline()
        while word:
            self.dict[word[0].lower()].append(word[:-1])
            word = fp.readline()

    def searchDict(self, word):
        # NOT FINISHED
        print("Set up searchDict function")

    def run(self, word):
        # NOT FINISHED
        print("Set up run function to return suggestions based on word")
