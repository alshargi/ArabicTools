# -*- coding: utf-8 -*-

#from ArabicPreprocssingFunctions import SplitBigArabicText
#import FaisalARAtools.FaisalARAtools.arabic_functions as yagi


import arabic_functions as Fa
import arabic_statistics as Fp


# Example usage
#file_path = '/Users/kingyhrash/Downloads/Output_1.txt'
#output_directory = '/Users/kingyhrash/Desktop/ml/'
#numberSentSplit = 1000

#message = Fa.SplitBigArabicText(file_path, output_directory, numberSentSplit)
#Fa.log(message)





#output_path = "/Users/kingyhrash/Desktop/db/jo-corpus/result.txt"
#folder_path = '/Users/kingyhrash/Desktop/db/jo-corpus/cc/'
#arabic_word_frequency(folder_path,  output_path)
#log("Saved to" + str(output_path))



output_path = "/Users/kingyhrash/Desktop/db/jo-corpus/result.txt"
folder_path = '/Users/kingyhrash/Desktop/db/jo-corpus/cc/'

Fp.arabic_punctuation_frequency_xml(folder_path,  output_path, ".,][/]")
Fp.log("Saved to" + str(output_path))







