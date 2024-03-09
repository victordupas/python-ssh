import pyttsx3, PyPDF2
pdfreader = PyPDF2.PdfReader(open('teste.pdf','rb'))

reader = pyttsx3.init()
for page in range(len(pdfreader.pages)):
    text = pdfreader._get_page(page).extract_text()
    legible_text = text.strip().replace('\n',' ')
    print(legible_text)
    reader.say(legible_text)
    reader.save_to_file(legible_text,'arquivo.mp3')
    reader.runAndWait()
reader.stop