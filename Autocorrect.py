class Autocorrect:

    def __init__(self, fileName):
        self.file = fileName
        self.dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [
        ], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}

    def createDict(self):
        fp = open(self.file)
        word = fp.readline()
        while word:
            self.dict[word[0].lower()].append(word[:-1])
            word = fp.readline()

    def longestCommonSub(self, word1, word2):
        c = []
        b = []
        # created c and b matrix of length word1 as the num rows and word2 length be num columns
        for x in range(len(word1)):
            c.append([])
            b.append([])
            for y in range(len(word2)):
                c[x].append(0)
                b[x].append(0)

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    c[i][j] = 1 + c[i-1][j-1]
                    b[i][j] = b[i-1][j-1]
                elif c[i-1][j] >= c[i][j-1]:
                    c[i][j] = c[i-1][j]
                    b[i][j] = b[i-1][j]
                else:
                    c[i][j] = c[i][j-1]
                    b[i][j] = b[i][j-1]
        return c[len(word1)-1][len(word2)-1]

    def searchDict(self, word):
        bestWord = None
        bestScore = 0
        for i in range(len(self.dict[word[0].lower()])):
            score = self.longestCommonSub(word, self.dict[word[0].lower()][i])
            if score > bestScore:
                bestWord = self.dict[word[0].lower()][i]
                bestScore = score
        return bestWord

    def run(self):
        self.createDict()
        while(1):
            word = input("Enter a word: ")
            print(auto.searchDict(word))
            contin = input("Continue? yes or no ")
            if contin.lower() == 'no' or contin.lower() == 'n':
                break


auto = Autocorrect('allwords.txt')
auto.run()
# auto.createDict()
# while(1):
#     word = input("Enter a word: ")
#     print(auto.searchDict(word))
#     contin = input("Continue? yes or no ")
#     if contin.lower() == 'no' or contin.lower() == 'n':
#         break
