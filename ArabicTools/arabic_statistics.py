"""
Author: Dr. Alshargi FAISAL
Date: December 24, 2023
Description: Python script to analyze JOCC corpus 
 - word,
 - number
 - punctuation
 - frequency
 - word_cloud
 - Zipfian plot
 - word_weights
as well as word length and sentence length, in an XML file.
"""
# pip install matplotlib
# pip install nltk
#pip install arabic-reshaper
# pip install python-bidi

from colorama import Fore
from colorama import Style
from datetime import datetime

import os
import xml.etree.ElementTree as ET
 
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
import string
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display

    
    

# Define custom punctuations
custom_punctuation = ""  

def log(string):
    now = str(datetime.now())
    print(Fore.BLUE + now + ' ' + Style.RESET_ALL + string)
#------------------------------------------

def save_list_tofile(xlist, xpath):
    file1 = open(xpath,"w") 
    for i in xlist:
        file1.writelines("{}\n".format(i))    
    file1.close() 
    


 
def tokenize_text(text):
    for custom_punct in custom_punctuation:
        text = text.replace(custom_punct, f" {custom_punct} ")
    tokens = nltk.word_tokenize(text)
    return tokens


def calculate_word_weights(word_freq):
    total_freq = sum(word_freq.values())
    weights = {word: freq / total_freq for word, freq in word_freq.items()}
    return weights




from collections import Counter
import os
import xml.etree.ElementTree as ET
import string


def arabic_punctuation_frequency_xml(folder_path, outputx, custmpunc):
    keep_all_result = []
    custom_punctuation = string.punctuation + "؛،؟«»,``•“~-،;!" + custmpunc  
    concatenated_text = ""
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".xml"):
                xml_file_path = os.path.join(folder_path, filename)
                log(f"\nReading XML file: {xml_file_path}")

                # Parse the XML file and extract text content
                tree = ET.parse(xml_file_path)
                root = tree.getroot()
                text_content = " ".join(s.text for paragraph in root.findall(".//Paragraph") for s in paragraph.findall(".//s"))

                # Concatenate the text content from each file
                concatenated_text += text_content

    except ET.ParseError as e:
        log(f"Error parsing XML file: {xml_file_path}")
        log(f"ParseError: {e}")

    # Tokenize the text
    tokens = tokenize_text(concatenated_text)

    # Filter tokens that are entirely composed of punctuation characters
    punctuation = [token for token in tokens if all(char in custom_punctuation for char in token)]
    punctuation_freq = Counter(punctuation)

    log("\nPunctuation Frequency:")
    keep_all_result.append("Punctuation Frequency")
    keep_all_result.append("{}\t{}".format("punct", "freq"))
    
    # Sort punctuation frequencies in descending order based on frequency
    for punct, freq in sorted(punctuation_freq.items(), key=lambda x: x[1], reverse=True):
        log(f"{punct}: {freq}")
        keep_all_result.append("{}\t{}".format(punct, freq))
    keep_all_result.append("")

    # Save result
    save_list_tofile(keep_all_result, outputx)
    
def arabic_word_frequency_xml(folder_path, outputx):
    keep_all_result = []
    concatenated_text = ""
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".xml"):
                xml_file_path = os.path.join(folder_path, filename)
                log(f"\nReading XML file: {xml_file_path}")

                # Parse the XML file and extract text content
                tree = ET.parse(xml_file_path)
                root = tree.getroot()
                text_content = " ".join(s.text for paragraph in root.findall(".//Paragraph") for s in paragraph.findall(".//s"))

                # Concatenate the text content from each file
                concatenated_text += text_content
             
            
    except ET.ParseError as e:
        log(f"Error parsing XML file: {xml_file_path}")
        log(f"ParseError: {e}")
        
        
    # Tokenize the text
    tokens = tokenize_text(concatenated_text)

    ########## Calculate word frequency
    word_freq = Counter(tokens)
    keep_all_result.append("Word Frequency")
    keep_all_result.append("{}\t{}".format("word", "freq"))
    for word, freq in list(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)):
        #print(f"{word}: {freq}")
        keep_all_result.append("{}\t{}".format(word, freq))
    keep_all_result.append("")


    # save result
    save_list_tofile(keep_all_result, outputx)

    
    
   

