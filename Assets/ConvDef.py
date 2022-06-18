# Modules
import os, time

# Defines Converters of letters to something else
Converted, ConvVer = [], '1.b2'

# Responsible for writing to a text file
def WriteResult(ogtext):
    Mode = ''
    if os.path.exists('./Results.txt') == True:
        Mode = 'a+'
    else:
        Mode = 'w+'
    Result = open('Results.txt',Mode,encoding='utf8')
    try:
        Result.write("\n"+ogtext+"\n")
        Result.write("".join(Converted))
        Result.write("\n")
        print('')
        print("".join(Converted))
        print('\nResults written to Results.txt in ROOT FOLDER.')
    except Exception as err:
        print('FATAL :',err)
    Result.close()
    time.sleep(2)
    clrConverted()

def clrConverted():
    global Converted
    Converted = []

def NumSeq(Char):
    match Char:
        case ' ':
            Converted.append(' | ')
        case 'a':
            Converted.append(' 2 ')
        case 'b':
            Converted.append(' 22 ')
        case 'c':
            Converted.append(' 222')
        case 'd':
            Converted.append(' 3 ')
        case 'e':
            Converted.append(' 33 ')
        case 'f':
            Converted.append(' 333')
        case 'g':
            Converted.append(' 4 ')
        case 'h':
            Converted.append(' 44 ')
        case 'i':
            Converted.append(' 444')
        case 'j':
            Converted.append(' 5 ')
        case 'k':
            Converted.append(' 55 ')
        case 'l':
            Converted.append(' 555')
        case 'm':
            Converted.append(' 6 ')
        case 'n':
            Converted.append(' 66 ')
        case 'o':
            Converted.append(' 666')
        case 'p':
            Converted.append(' 7 ')
        case 'q':
            Converted.append(' 77 ')
        case 'r':
            Converted.append(' 777 ')
        case 's':
            Converted.append(' 7777')
        case 't':
            Converted.append(' 8 ')
        case 'u':
            Converted.append(' 88 ')
        case 'v':
            Converted.append(' 888')
        case 'w':
            Converted.append(' 9 ')
        case 'x':
            Converted.append(' 99 ')
        case 'y':
            Converted.append(' 999 ')
        case 'z':
            Converted.append(' 9999')
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
            Converted.append('`'+Char)
        case '|':
            Converted.append('?')
        case _:
            Converted.append(' '+Char)

def NumSeqComp(Char):
    match Char:
        case ' ':
            Converted.append(' | ')
        case 'a':
            Converted.append(' 21 ')
        case 'b':
            Converted.append(' 22 ')
        case 'c':
            Converted.append(' 23 ')
        case 'd':
            Converted.append(' 31 ')
        case 'e':
            Converted.append(' 32 ')
        case 'f':
            Converted.append(' 33 ')
        case 'g':
            Converted.append(' 41 ')
        case 'h':
            Converted.append(' 42 ')
        case 'i':
            Converted.append(' 43 ')
        case 'j':
            Converted.append(' 51 ')
        case 'k':
            Converted.append(' 52 ')
        case 'l':
            Converted.append(' 53 ')
        case 'm':
            Converted.append(' 61 ')
        case 'n':
            Converted.append(' 62 ')
        case 'o':
            Converted.append(' 63 ')
        case 'p':
            Converted.append(' 71 ')
        case 'q':
            Converted.append(' 72 ')
        case 'r':
            Converted.append(' 73 ')
        case 's':
            Converted.append(' 74 ')
        case 't':
            Converted.append(' 81 ')
        case 'u':
            Converted.append(' 82 ')
        case 'v':
            Converted.append(' 83 ')
        case 'w':
            Converted.append(' 91 ')
        case 'x':
            Converted.append(' 92 ')
        case 'y':
            Converted.append(' 93 ')
        case 'z':
            Converted.append(' 94')
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
            Converted.append('`'+Char)
        case '|':
            Converted.append('?')
        case _:
            Converted.append(' '+Char)

def QwertyJpKana(Char,Switch):
    match Switch:
        case 1:
            Qwerty2JpKana(Char)
        case 2:
            print('WORK IN PROGRESS')

# ADD THE CHARACTERS THAT HAS THOSE QUOTE STUFF
def Qwerty2JpKana(Char):
    match Char:
        case ' ':
            Converted.append(' ')
        case 'a':
            Converted.append('ち')
        case 'b':
            Converted.append('こ')
        case 'c':
            Converted.append('そ')
        case 'd':
            Converted.append('し')
        case 'e':
            Converted.append('い')
        case 'E':
            Converted.append('ぃ')
        case 'f':
            Converted.append('は')
        case 'g':
            Converted.append('き')
        case 'h':
            Converted.append('く')
        case 'i':
            Converted.append('に')
        case 'j':
            Converted.append('ま')
        case 'k':
            Converted.append('の')
        case 'l':
            Converted.append('り')
        case 'm':
            Converted.append('も')
        case 'n':
            Converted.append('み')
        case 'o':
            Converted.append('ら')
        case 'O':
            Converted.append('○')
        case 'p':
            Converted.append('せ')
        case 'q':
            Converted.append('た')
        case 'r':
            Converted.append('す')
        case 's':
            Converted.append('と')
        case 't':
            Converted.append('か')
        case 'u':
            Converted.append('な')
        case 'v':
            Converted.append('ひ')
        case 'w':
            Converted.append('て')
        case 'x':
            Converted.append('さ')
        case 'y':
            Converted.append('ん')
        case 'z':
            Converted.append('つ')
        case 'Z':
            Converted.append('っ')
        case ';':
            Converted.append('れ')
        case "'":
            Converted.append('け')
        case ',':
            Converted.append('ね')
        case '<':
            Converted.append('、')
        case '.':
            Converted.append('る')
        case '>':
            Converted.append('。')
        case '/':
            Converted.append('め')
        case '?':
            Converted.append('・')
        case '[':
            Converted.append('゛')
        case '{':
            Converted.append('「')
        case ']':
            Converted.append('゜')
        case '}':
            Converted.append('」')
        case '\\':
            Converted.append('む')
        case '`':
            Converted.append('ろ')
        case '1':
            Converted.append('ぬ')
        case '2':
            Converted.append('ふ')
        case '3':
            Converted.append('あ')
        case '#':
            Converted.append('ぁ')
        case '4':
            Converted.append('う')
        case '$':
            Converted.append('ぅ')
        case '5':
            Converted.append('え')
        case '%':
            Converted.append('ぇ')
        case '6':
            Converted.append('お')
        case '^':
            Converted.append('ぉ')
        case '7':
            Converted.append('や')
        case '&':
            Converted.append('ゃ')
        case '8':
            Converted.append('ゆ')
        case '*':
            Converted.append('ゅ')
        case '9':
            Converted.append('よ')
        case '(':
            Converted.append('ょ')
        case '0':
            Converted.append('わ')
        case ')':
            Converted.append('を')
        case '-':
            Converted.append('ほ')
        case '=':
            Converted.append('へ')
        case _:
            Converted.append('['+Char+']')
