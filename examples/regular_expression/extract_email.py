import re
import easygui as gui

infile = gui.fileopenbox(msg='Select file to open', title='Open file', default='*.txt')
if infile:
    with open(infile) as f:
        doc = f.readlines()
        gui.textbox(msg='Showing contents of text file', title='Text file reader', text=doc)
else:
    exit()
    
text = ''.join(doc)

emails = []
pat = r'[\w\.\-]+@[\w\.\-]+'
res = re.finditer(pat, text)
for i, j in enumerate(res, start=1):
    print(i, j.group(), sep='.')
    emails.append(j.group() + '\n')


gui.textbox(msg='Extracted data', title='View Data', text=emails)
ans = gui.ynbox(msg='Do you want to save your data?')
if ans:
    # File save dialog box
    file = gui.filesavebox(default='emails.csv', filetypes='*.csv')
    if file == None:
        exit()
    with open(file, 'w') as savefile:
        savefile.writelines(emails)
    