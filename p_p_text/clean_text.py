#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 20:08:55 2022

@author: oscar
"""

import re


class cleanText():
    # to_do esta clase limpia el texto



    def __init__(self, input_text: str) -> None:

        # inicializo las variables
        self.input_text = input_text


    def c_numbers(self, not_clear: bool = True) -> str:
        '''
        Esta función elimina los numeros de un cadena de texto

        Parameters
        ----------
        not_clear : bool, optional si no quiero eliminar los numeros
            DESCRIPTION. The default is True.

        Returns
        -------
        str
            DESCRIPTION. texto sin numeros

        '''

        if not_clear:
            c_numbers_pattern = re.compile(r"\@[a-zA-Z0-9\-\_]+\b")
            out_put_txt = re.sub(c_numbers_pattern, " ", self.input_text)
        else: out_put_txt = self.input_text

        return out_put_txt


    def c_mentios(self):

        # este metodo borra las @ Valentina

    def c_emojis(self,not_clear: bool = True) -> str:
        '''
        Esta función elimina los emojis de una cadena de texto

        Parameters
        ----------
        not_clear : bool:opcional si no quiero eliminar los emojis
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION. texto sin emojis

        '''

        if not_clear:
            c_emojis_pattern = re.compile(r"[^a-zA-Z\u00C0-\u00FF ]")
            out_put_txt = re.sub(c_emojis_pattern, ' ', input_tex)

        else: out_put_txt = self.input_text

        return out_put_txt
        # este metodo bora :) Rossemberg
        
    def c_hasgtags(self, not_clear: bool = True) -> str:
        '''
        Este metodo elimina los hastags del texto.



    def c_url(self,not_clear: bool = True) -> str:
        """
        Esta función elimina url de un cadena de texto

        Parameters
        ----------
        not_clear : bool, optional
            DESCRIPTION. The default is True.

        Returns
        -------
        str
            DESCRIPTION. texto sin URL

        """

        # Terminé mi tarea Jhonny Osorio
        
        if not_clear:
            c_url_pattern = re.compile(r"\bhttps:.+\b")
            out_put_txt = re.sub(c_url_pattern, " ", self.input_text)
        else: 
            out_put_txt = self.input_text

        return out_put_txt
            
        Parameters
        ----------
        not_clear : bool, optional
            DESCRIPTION. The default is True.

        Returns
        -------
        str
            DESCRIPTION. El texto sin los hastags.


        '''

        # borra # Miguel
        
        if not_clear:
            c_hast_pattern = re.compile(r"\#[a-zA-Z0-9\-\_]+\b")
            out_put_txt = re.sub(c_hast_pattern, " ", self.input_text)
            
        else: out_put_txt = self.input_text

        return out_put_txt


