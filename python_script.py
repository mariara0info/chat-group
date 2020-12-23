# Importamos todo lo necesario
import os
from flask import Flask, flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = '../../chat/Archivos'

@app.route("/")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('HTML_for_Textbox.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  fa = request.files['archivo']
  filename = secure_filename(fa.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  fa.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

  # Retornamos una respuesta satisfactoria
  resul12 = resuelvelo()
  return render_template('Result_for_Textbox.html', SName =   '  '.join(resul12))  
  #return "<h1>Archivo subido exitosamente</h1>"
  

def resuelvelo():
     import requests
     from bs4 import BeautifulSoup as bs
     from io import open
     import numpy as np
     import pandas as pd

     df = pd.read_csv('../../chat/Archivos/links.txt')
     lola= np.asarray(df)
     chat= list()
     linder=list()
     image1=list()
     archivo = open('../../chat/grupos.txt', 'w' , encoding='UTF8')

     for s in lola:
          listToStr = ' '.join([str(elem) for elem in s]) 
          #print(listToStr)
          r = requests.get(listToStr)
          soup = bs(r.content, 'html.parser')
          first_header = soup.find('h2', {"class":"_2yzk"})
          first_imagen = soup.find("span", {"class":"_2z9j"})
          fit_imagen = str(first_imagen).replace('<span class="_2z9j" style="background-image: url(','')
          f_imagen = str(fit_imagen).replace(')"></span>','')
          fi_imagen = str(f_imagen).replace('amp;','')
     
          if len(first_header.text) != 0:
               chat.append(first_header.text)
               linder.append(listToStr)
               image1.append(fi_imagen)
               archivo.write(first_header.text +'\n')
               archivo.write(listToStr +'\n')
               archivo.write(fi_imagen +'\n')                
            
     archivo.close()
     return linder
    
if __name__ == '__main__':
 # Iniciamos la aplicación
 app.run(debug=True)