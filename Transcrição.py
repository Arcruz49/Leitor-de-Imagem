import pyautogui
import pytesseract
import keyboard
from PIL import ImageGrab
import sys 

try:
    output_file = "D:/transcrição/sessao.txt"
    writenText = ""
    
    capturing = False 
    text_buffer = ""  

    # Função para iniciar a captura de screenshots
    def start_capture():
        global capturing
        capturing = True
        print("Iniciando a captura de screenshots...")

    # Função para parar a captura de screenshots e encerrar o programa
    def stop_capture():
        global capturing, text_buffer  # Declare como global
        capturing = False
        print("Parando a captura de screenshots...")
        
        #escreve no arquivo
        with open(output_file, "a") as file:
            file.write(text_buffer)
        text_buffer = "" 
        
        sys.exit(0)

    # Função das teclas
    keyboard.add_hotkey("D", start_capture)
    keyboard.add_hotkey("esc", stop_capture)
    OldText = " "
    while True:
        if capturing:
            screenshot = ImageGrab.grab()
            screenshot = "C:/Users/Arthur/Desktop/image.png"
            NewText = pytesseract.image_to_string(screenshot)
            if (NewText and NewText != OldText):
                text_buffer += NewText  
            OldText = NewText

except pyautogui.ImageNotFoundException:
    print("Erro ao capturar a imagem")

except OSError:
    print("Não foi possível criar o arquivo")
