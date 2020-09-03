import sys

import regex

from NLP.Assignment1_Transliteration.telugu_transliteration.schemes import Scheme

# Roman schemes
# -------------
HK = 'hk'

s = str.split
if sys.version_info < (3, 0):
    # noinspection PyUnresolvedReferences
    s = unicode.split


class RomanScheme(Scheme):
    def __init__(self, data=None, synonym_map=None, name=None):
        super(RomanScheme, self).__init__(data=data, synonym_map=synonym_map, name=name, is_roman=True)
    
    # def get_standard_form(self, data):
    #     """Roman schemes define multiple representations of the same devanAgarI character. This method gets a library-standard representation.
    #
    #     data : a text in the given scheme.
    #     """
    #     if self.synonym_map is None:
    #         return data
    #     from NLP.telugu_transliteration import *
    #     return transliterate(data=transliterate(_from=self.name, _to=sanscript.DEVANAGARI, data=data), _from=sanscript.DEVANAGARI, _to=self.name)

    @classmethod
    def simplify_accent_notation(cls, text):
        # References: https://en.wikipedia.org/wiki/Combining_Diacritical_Marks
        text = text.replace("á", "á")
        text = text.replace("í", "í")
        text = text.replace("ú", "ú")
        text = text.replace("ŕ", "ŕ")
        text = text.replace("é", "é")
        text = text.replace("ó", "ó")

        text = text.replace("à", "à")
        text = text.replace("ì", "ì")
        text = text.replace("ù", "ù")
        text = text.replace("è", "è")
        text = text.replace("ò", "ò")
        
        text = regex.sub("([̀́])([̥̇¯̄]+)", "\\2\\1", text)
        return text

    @classmethod
    def to_shatapatha_svara(cls, text):
        # References: https://en.wikipedia.org/wiki/Combining_Diacritical_Marks
        text = text.replace("́", "᳘")
        text = text.replace("̀", "᳘")
        text = regex.sub("᳘([ंःँ])", "\\1᳘", text)
        return text

class HkScheme(RomanScheme):
    def __init__(self):
        super(HkScheme, self).__init__({
            'vowels': s("""a A i I u U R RR lR lRR e ai o au"""),
            'marks': s("""A i I u U R RR lR lRR e ai o au"""),
            'virama': [''],
            'yogavaahas': s('M H ~'),
            'consonants': s("""
                            k kh g gh G
                            c ch j jh J
                            T Th D Dh N
                            t th d dh n
                            p ph b bh m
                            y r l v
                            z S s h
                            L kS jJ
                            """),
            'symbols': s("""
                       OM ' | ||
                       0 1 2 3 4 5 6 7 8 9
                       """)
        }, name=HK, synonym_map={"|": ["."], "||": [".."]})


SCHEMES = {
    HK: HkScheme(),
}

ALL_SCHEME_IDS = SCHEMES.keys()

