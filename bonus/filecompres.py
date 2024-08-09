import FreeSimpleGUI as sg
label1 = sg.Text("Select files to compress")
inp1 = sg.Input()
choos1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
inp2 = sg.Input()
choos2 = sg.FolderBrowse("Choose")
s
compres = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, inp1, choos1],
                           [label2,inp2,choos2],
                           [compres]])
window.read()
window.close()