# -*- coding: utf-8 -*-

import unicodedata

from stanford_ner.StanfordNER import StanfordNER

def from_unicode_to_ascii(string):
	return unicodedata.normalize("NFKD", string).encode("ascii", "ignore")

def clean():
	StanfordNER.disconnect_all()