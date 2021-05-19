# -*- coding: utf-8 -*-
"""
Created on Wed May 19 10:55:18 2021

@author:Naveen Kumar Vasudevan, 
        Doctoral Candidate, 
        The Xi Research Group, 
        Department of Chemical Engineering,
        McMaster University, 
        Hamilton, 
        Canada.
        
        naveenovan@gmail.com
        https://naveenovan.wixsite.com/kuroonai
"""

import PySimpleGUI as sg
import clipboard
import string


layout = [

    [sg.Text("Choose whether to encrypt or decrypt the text"), sg.Combo(list(['encrypt','decrypt']), size=(20,4), key='crypt')],
    [sg.Text("Enter or paste input text")],
    [sg.Multiline("", size=(80, 10), key='inputtext'), sg.Button("Paste")],
    [sg.Text("To delete, select a portion of text and click delete"), sg.Button("Delete")],
    [sg.Text("Select the rotation number")],
    [sg.Spin(list(range(0,26)), size=(20, 1), key='rotnum')],
    [sg.Button('Operate', key='operate')],
    [sg.Text("The output text")],
    [sg.Multiline("", size=(80, 10), key='outputtext'), sg.Button("Copy", key='copy')],
]

window = sg.Window("Kuroonai's Caesar cipher", layout)

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Paste":
        try:                       
            window['inputtext'].Widget.delete("sel.first", "sel.last")
        except:                  
            pass
        text = clipboard.paste()   
        window['inputtext'].Widget.insert("insert", text)
        
    elif event == "Delete":
        try:
            window['inputtext'].Widget.delete("sel.first", "sel.last")
        except:   
            pass
    
    elif event == "operate":
        if values['crypt'] == 'encrypt' :crypt = 1
        else:  crypt = 0
        rotnum = int(values['rotnum'])
        data = values['inputtext']
        actual = list(string.ascii_letters)
        ciphered = list(actual[rotnum:] + actual[:rotnum])
        
        out = ''
        
        for iind, i in enumerate(data):
            letters = list(i)
            
            newword = ''
            for  j in letters:
                if crypt == True:
                    if j in ciphered:newword += actual[ciphered.index(j)]
                    else : newword += j
                else:
                    if j in actual:newword += ciphered[actual.index(j)]
                    else : newword += j

            
            out += newword

        window["outputtext"].update(out)
    
    elif event == 'copy': clipboard.copy(out) 
        

window.close()
