import subprocess
subprocess.run(["python", "-m", "venv", "myenv"])
subprocess.run(["pip", "install", "python-docx"])
from docx import Document
user_input = input("Введите текст для сохранения в Word-файле: ")
doc = Document()
doc.add_paragraph(user_input)
doc.save("output.docx")
