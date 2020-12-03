import tkinter as tk


class Autocorrect:

    def __init__(self, fileName):
        self.file = fileName
        self.dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [
        ], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}

    def createDict(self):
        fp = open(self.file)
        word = fp.readline()
        word = fp.readline()  # one more to skip the comment line in the beginning of the txt file
        while word:
            self.dict[word[0].lower()].append(word[:-1])
            word = fp.readline()

    def longestCommonSub(self, word1, word2):
        c = []
        # created c matrix of length word1 as the num rows and word2 length be num columns
        for x in range(len(word1)):
            c.append([])

            for y in range(len(word2)):
                c[x].append(0)

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    c[i][j] = 1 + c[i-1][j-1]
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                else:
                    c[i][j] = c[i][j-1]
        return c[len(word1)-1][len(word2)-1]

    def searchDict(self, word):
        bestWord = None
        bestScore = 0
        lengthDiff = None
        for i in range(len(self.dict[word[0].lower()])):
            score = self.longestCommonSub(word, self.dict[word[0].lower()][i])
            if score > bestScore:                    # A better score overeall
                bestWord = self.dict[word[0].lower()][i]
                bestScore = score
            if score is bestScore:                   # Handling tie breakers
                if lengthDiff is None or (abs(len(word) - len(self.dict[word[0].lower()][i]))) < lengthDiff:
                    bestWord = self.dict[word[0].lower()][i]
                    lengthDiff = abs(
                        len(word) - len(self.dict[word[0].lower()][i]))
        return bestWord


def autocorrect():
    word = userInput.get()
    # to make sure to clear the previous words
    blankSpace = tk.Label(
        root, text="                                                                                                        ")
    windowBox.create_window(400, 320, window=blankSpace)

    # geting the user corrected word
    autcorrectWord = tk.Label(root, text=str(auto.searchDict(word)))
    windowBox.create_window(400, 320, window=autcorrectWord)


# The GUI
root = tk.Tk()
root.title("Autocorrector")
windowBox = tk.Canvas(root, width=750, height=600, bg="light steel blue")
windowBox.pack()

userInput = tk.Entry(root)
windowBox.create_window(400, 200, window=userInput)
auto = Autocorrect('allwords.txt')
auto.createDict()

submit = tk.Button(text='Autocorrect', command=autocorrect,
                   bg='DodgerBlue2', fg='white')
windowBox.create_window(400, 250, window=submit)

root.mainloop()
