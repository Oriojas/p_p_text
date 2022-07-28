# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:23:13 2022

@author: User
"""

from clean_text import cleanText as CL

file = "hola soy #miguel_pinto y vengo a saludar"

classObj = CL(input_text=file)

text = classObj.c_hasgtags()

print(f'El texto sin hastags es: {text}')