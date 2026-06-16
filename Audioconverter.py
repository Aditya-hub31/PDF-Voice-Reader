import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

book = askopenfilename()  #select a file...
pdfreader = PyPDF2.PdfReader(open(book, 'rb')) 
pages = len(pdfreader.pages) 

player = pyttsx3.init() #text to speech engine

for num in range(0, pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    player.say(text)

player.runAndWait()
  