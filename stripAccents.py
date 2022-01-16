# -*- coding: utf-8 -*-
import unicodedata

#UTILITY FUNCTION TO STRIP ACCENTS SINCE WE ARE DEALING WITH A MEXICAN WEBSITE

def strip_accents(s):

    try:
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                       if unicodedata.category(c) != 'Mn')
    except:
        return s

