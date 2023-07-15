import elevation
import PySimpleGUI as sg
import sys
import os

# os.chdir(sys._MEIPASS)

if hasattr(sys, '_MEIPASS'):
    # PyInstaller >= 1.6
    os.chdir(sys._MEIPASS)
    os.environ["PATH"] += os.path.sep + sys._MEIPASS
elif '_MEIPASS2' in os.environ:
    # PyInstaller < 1.6 (tested on 1.5 only)
    os.chdir(os.environ['_MEIPASS2'])
    os.environ["PATH"] += os.path.sep + os.environ['_MEIPASS2']
else:
    pass

font=(sg.DEFAULT_FONT, 16)

layout = [
    [sg.Text('Input PDF file:', font=font),  sg.InputText(font=font), sg.FilesBrowse(font=font)],
    [sg.Text('Prompt:', font=font), sg.Multiline('What is the title of this document?', font=font)],
    [sg.Button('Submit', font=font)],
    [sg.Text('Answer:', font=font), sg.Multiline('output will appear here', font=font)]
]

window = sg.Window('Ask Your Document', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Submit':
        input_file = values[0]
        basename = '.'.join(values[0].split('.')[0:]) # get the name of the file, without extension (eg. your_document.pdf would be your_document here)
        ext = values[0].split('.')[-1].lower() # get the extension of the file (e.g. pdf)
        if ext.lower() != 'pdf':
            # TODO display an error here if file is wrong type
            continue # go back to waiting for a button event to occur

        # TODO actual code here for ask your document!

window.close()
