def main():
    
    infile = open('info_security.txt', 'r')
    outfile = open('encrypted.txt', 'w')

    for line in infile:
        #gets each line in the txt file
        words = line.split()
        for word in words:
            #gets each word in the line
            letter = [i for i in word]
            newWord = ''
            #gets each letter in the word
            for index in letter:
                newWord = newWord+encrypt(index)
            outfile.write(newWord + ' ')

    outfile.close()

def encrypt(letter):

    encryption = {'A':'!',
                    'a':'1',
                    'B':'@',
                    'b':'2',
                    'C':'#',
                    'c':'3',
                    'D':'$',
                    'd':'4',
                    'E':'%',
                    'e':'5',
                    'F':'^',
                    'f':'6',
                    'G':'&',
                    'g':'7',
                    'H':'*',
                    'h':'8',
                    'I':'(',
                    'i':'9',
                    'J':')',
                    'j':'0',
                    'K':'-',
                    'k':'_',
                    'L':'+',
                    'l':'=',
                    'M':'{',
                    'm':'[',
                    'N':'}',
                    'n':']',
                    'O':'~',
                    'o':'`',
                    'P':':',
                    'p':';',
                    'Q':'|',
                    'q':'<',
                    'R':'>',
                    'r':'/',
                    'S':'q',
                    's':'w',
                    'T':'e',
                    't':'r',
                    'U':'t',
                    'u':'y',
                    'V':'u',
                    'v':'i',
                    'W':'o',
                    'w':'p',
                    'X':'a',
                    'x':'s',
                    'Y':'d',
                    'y':'f',
                    'Z':'g',
                    'z':'h',
                    '.':'.',
                    ',':',',
                    ':':':'}
   
    return encryption[letter]

main()
