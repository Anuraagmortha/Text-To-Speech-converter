import pyttsx3
import PyPDF2

def generate_audiobook(pdf_file, output_file):
    engine = pyttsx3.init()
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    # Set the voice properties (optional)
    # You can use the `engine.setProperty` method to set voice properties such as voice type, rate, and volume

    engine.save_to_file(text, output_file)
    engine.runAndWait()

generate_audiobook(r'C:\Users\Anurag\Desktop\fastapi\texttospeech.pdf', r'C:\Users\Anurag\Desktop\fastapi\output.wav')
