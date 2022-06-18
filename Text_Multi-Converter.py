# Written in Python 3.10.0

# Modules
import os,  time

# Variables
action, Switch, Cmethod = [0,0], 0, ''


MainVer, ConvVer, MiscVer = '1.b5', '1.b1', '1.b0'

# Converters
# imported from another File
# ConvertersDef.py
import Assets.ConvDef as ConvDef

# Fun functions
import Assets.MiscDef as MiscDef

# Defining functions from ConfDef
clrConverted, WriteResult, Colour  = ConvDef.clrConverted, ConvDef.WriteResult, MiscDef.Colour

QwertyJpKana, NumSeq, NumSeqComp  = ConvDef.QwertyJpKana, ConvDef.NumSeq, ConvDef.NumSeqComp

# Self Explanatory
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Repsonsible for getting the user started
def splash():
    print('    Welcome to the Text Multi-Converter! ('+MainVer+'.'+ConvVer+'.'+MiscVer+')')
    print('''
    Please note that this program is NOT perfect.

    Using "CTRL + [KEY]" CAN crash this program!

    If you see '?' it means an unknown character is entered.''')
    if action[0] == 0:
        print('''
    Conversion method: 0 = Unset
                       1 = NumSeq               (s == 7777)
                       2 = NumSeqComp           (s == 74  )
                       3 = QWERTY <-> ひらがな  (a == ち  )

    NOTES: Method 3 requires a UTF-8 Compatible Font. (e.g. SumSum-Ext8)
        ''')
    else:
        print('\n    To change Conversion Method\n    type "~!exit" or "~!leave" (CASE SENSITIVE)\n')
    # Converter Mode Indicator
    global Cmethod, Switch
    match action[0]:
        case 1:
            Cmethod = 'NumSeq'
        case 2:
            Cmethod = 'NumSeqComp'
        case 3:
            Cmethod = ' QWERTY <-> ひらがな'
            match Switch:
                case 1:
                    Cmethod = ' (QWERTY --> JP-KANA)'
                case 2:
                    Cmethod = ' (JP-KANA --> QWERTY)'
        case _:
            Cmethod = 'Unset, Select a Method'
    print('    Current Conversion Method:', Cmethod,'\n')

    # Converter-specific comments
    match action[0]:
        case 1 | 2:
            print('    Words are separated with " | "')
        case 3:
            print('    Converts Keypresses to their ひらがな Counterparts, Vice Versa.\n')
            print('    Conversion results might appear as " ? ."\n    If so, Switch to a UTF-8 Compatible Text Font!\n    Font Such as "SumSum-Ext8"!')
            print('\n    Separate Each chatacter with a space.')

# Responsible for processing the text, writing to a text file
def ProcessConvert(method):
    global action, Switch
    Text = ''
    while True:
        clear()
        splash()
        match action[0]:
            case 3:
                if Switch == 0:
                    print('\n     1 = QWERTY to JP-KANA\n     2 = JP-KANA to QWERTY')
                    try:
                        Switch = int(input('Select : '))
                        match Switch:
                            case 1 | 2:
                                clear()
                                splash()
                                Text = input('\nText to Convert : ')
                            case _:
                                print('\nInvalid Selection!')
                                Switch = 0
                                time.sleep(2)
                    except Exception as Err:
                        Colour('0c')
                        print(f'ERROR : {Err}')
                        time.sleep(4)
                        Colour('0f')
                else:
                    Text = input('\nText to Convert : ')
            case _:
                # Reduntant and has no use or somehow idk or forgot how to trigger this
                Text = input('\nText to Convert : ').lower()
        if Text == '~!exit' or Text == '~!leave':
            action[0], Switch = 0, 0
            break
        else:
            try:
                match action[0]:
                    case 1 | 2:
                        if Text != "":
                            for Letter in list(Text):
                                method(Letter)
                            WriteResult(Text)
                            clear()
                        else:
                            print("You entered nothing!")
                            time.sleep(2)
                    case 3:
                        if Text != "":
                            for Letter in list(Text):
                                method(Letter,Switch)
                            WriteResult(Text)
                            clear()
                        else:
                            print("\nYou entered nothing!")
                            time.sleep(2)
            except Exception as Err:
                print(f'\nFATAL! : [{Err}]')
                Colour('0c')
                time.sleep(4)
                clrConverted()
                Colour('0f')

# Responsible for determining the conversion method
def ConversionMethod(method):
    global action
    match method:
        case 1:
            ProcessConvert(NumSeq)
        case 2:
            ProcessConvert(NumSeqComp)
        case 3:
            ProcessConvert(QwertyJpKana)
        case 177013:
            MiscDef.N177013()
            action[0] = 0
        case _:
            print('Select a Conversion Mode!')
            action[0] = 0
            time.sleep(2)

# Main Loop
while True:
    clear()
    splash()
    if action[0] == 0:
        try:
            action = [int(input('Select Conversion Method: ')),0]
        except Exception as Err:
            Colour('0c')
            print(f'\nSelect Valid Method!\nError : [{Err}]')
            time.sleep(1)
            Colour('0f')
    ConversionMethod(action[0])
