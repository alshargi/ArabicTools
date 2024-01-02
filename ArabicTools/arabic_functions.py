# -*- coding: utf-8 -*-

import re
import os
from colorama import Fore
from colorama import Style
from datetime import datetime



def log(string):
    now = str(datetime.now())
    print(Fore.BLUE + now + ' ' + Style.RESET_ALL + string)
#------------------------------------------

def load_txt_file(p):
    log("Loading - on it.....")
    klist = []
    with open(p) as fword:
        klist = fword.read().splitlines()
    return klist
#------------------------------------------
  
def load_txt_file_ISO(p):
    log("Loading - on it.....")
    all_data = []
    with open(p, encoding = "ISO-8859-1") as fword:
        all_data = fword.read().splitlines()
    return all_data
#------------------------------------------

def load_txt_file_utf8(p):
    log("Loading  - on it.....")
    all_data = []
    with open(p, encoding="utf-8") as fword:
        all_data = fword.read().splitlines()
    return all_data
#------------------------------------------

def save_list_to_file(xlist, xpath):
    file1 = open(xpath,"w") 
    for i in xlist:
        file1.writelines("{}\n".format(i))    
    file1.close() 
    log("Saved to " + str(xpath))



#------------------------------------------ backwlter
# Your Arabic letters dictionary
araletters = {u"\u0627":'A',
u"\u0628":'b', u"\u062A":'t', u"\u062B":'v', u"\u062C":'j',
u"\u062D":'H', u"\u062E":'x', u"\u062F":'d', u"\u0630":'*', u"\u0631":'r',
u"\u0632":'z', u"\u0633":'s', u"\u0634":'$', u"\u0635":'S', u"\u0636":'D',
u"\u0637":'T', u"\u0638":'Z', u"\u0639":'E', u"\u063A":'g', u"\u0641":'f',
u"\u0642":'q', u"\u0643":'k', u"\u0644":'l', u"\u0645":'m', u"\u0646":'n',
u"\u0647":'h', u"\u0648":'w', u"\u0649":'Y', u"\u064A":'y',
u"\u0622":'|', u"\u064E":'a', u"\u064F":'u', u"\u0650":'i',
u"\u0651":'~', u"\u0652":'o', u"\u064B":'F', u"\u064C":'N',
u"\u064D":'K', u"\u0621":'\'', u"\u0623":'>', u"\u0625":'<',
u"\u0624":'&', u"\u0626":'}', u"\u0629":'p', " ":' '
}

def split(word):
    return [char for char in word]

def get_key(v):
    for key, value in araletters.items():
        if v == value:
            return key
    return ""

def get_val(k):
    for key, value in araletters.items():
        if k == key:
            return value
    return ""



def convert_ara_to_bw(xsent):
    res = ''
    splstr = split(xsent)
    for x in splstr:
        cara = get_val(x)
        if cara != '':
            res += cara
        else:
            res += x
    return res

def convert_bw_to_ara(xsent):
    res = ''
    splstr = split(xsent)
    for x in splstr:
        cara = get_key(x)
        if cara != '':
            res += cara
        else:
            res += x
    return res

def clean_bkw(name):
    return convert_ara_to_bw(str(name))

#------------------------------------------ split big arabic files



def custom_arabic_sentence_splitter(text):
    pattern = re.compile(r'(?<![ء-ي٠-٩]\.[ء-ي٠-٩]\.)(?<=\.|\؟)\s')
    sentences = re.split(pattern, text)
    return sentences


def SplitBigArabicText(file_path, output_directory, numberSentSplit):
    log("Working on it.....")
    try:
        fnum = 1
        with open(file_path, 'r', encoding='utf-8') as file:
            os.makedirs(output_directory, exist_ok=True)
            sentence_buffer = []
            file_number = 1

            for line_number, line in enumerate(file, start=1):
                line_replaced = re.sub(r'(?<!\b[0-9٠-٩]\.|[ء-ي٠-٩]\.)\.', ' . ', line)
                sentences = custom_arabic_sentence_splitter(line_replaced)
                sentence_buffer.extend(sentences)

                while len(sentence_buffer) >= numberSentSplit:
                    output_file_path = f"{output_directory}Output_Sentences_{file_number}.txt"
                    with open(output_file_path, 'w', encoding='utf-8') as output_file:
                        for sentence in sentence_buffer[:numberSentSplit]:
                            output_file.write(f"{sentence.replace(' .', '.').strip()}\n")

                    sentence_buffer = sentence_buffer[numberSentSplit:]
                    file_number += 1
                    fnum += 1

            if sentence_buffer:
                output_file_path = f"{output_directory}Output_Sentences_{file_number}.txt"
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    for sentence in sentence_buffer:
                        output_file.write(f"{sentence.replace(' .', '.').strip()}\n")
            
            return "Operation successful, Saved files : " + str(fnum)
    except Exception as e:
        return f"Error: {e}"

    

#------------------------------------------ xxx
    
