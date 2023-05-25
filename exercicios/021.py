'''Tocando MP3'''
from msilib.schema import SelfReg
from typing import Self


Self.playing = True
Self.Reg.mp3.play()
'''Tocando MP3 e alternando o volume'''
Self.playing = True
Self.mp3.play()