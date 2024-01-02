# Toolbox


ArabicTool is a Python package that contains handy functions. 


```bash
pip install git+https://github.com/alshargi/ArabicTools.git
```



## Usage
Features:



#### Demo of some of the features:
```python
# -*- coding: utf-8 -*-



from ArabicTools import arabic_punctuation_frequency_xml, log

output_path = "/Users/kingyhrash/Desktop/db/jo-corpus/result.txt"
folder_path = '/Users/kingyhrash/Desktop/db/jo-corpus/cc/'
arabic_punctuation_frequency_xml(folder_path,  output_path, ".,][/]")
log("Saved to" + str(output_path))



from ArabicTools import arabic_word_frequency, log

output_path = "/Users/kingyhrash/Desktop/db/jo-corpus/result.txt"
folder_path = '/Users/kingyhrash/Desktop/db/jo-corpus/cc/'
arabic_word_frequency(folder_path,  output_path)
log("Saved to" + str(output_path))







```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)








