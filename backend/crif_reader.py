from pdfreader import SimplePDFViewer
import arabic_reshaper, unicodedata, spacy
from bidi.algorithm import get_display

class CrifReader(object):

    def __init__(self):
        self.__nlp = spacy.load("en_core_web_sm")

    def __is_arabic(self, text):
        try:
            return any([unicodedata.name(ch).lower() for ch in text])
        except:
            return False

    def __reorder_arabic_string(self, text):
        return get_display(arabic_reshaper.reshape(text))

    def read(self, absolute_file_name):
        fd = open(absolute_file_name, "rb")
        viewer = SimplePDFViewer(fd)
        string_list = []
        while True:
            viewer.render()
            for canvas_id, canvas_data in viewer.canvas.forms.items():
                for string in canvas_data.strings:
                    if self.__is_arabic(string):
                        string = self.__reorder_arabic_string(string)
                    doc = self.__nlp(string.strip())
                    if len(doc) > 0:
                        string_list.append(string)
            try:
                viewer.next()
            except:
                break
        try:
            data_dict = {}
            for index in range(0, len(string_list), 2):
                data_dict[string_list[index]] = string_list[index+1]
        except Exception as e:
            pass
        return data_dict
