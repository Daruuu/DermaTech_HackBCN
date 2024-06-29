import openai
import os
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Carga la clave API desde el archivo .env
#openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = os.getenv('OPENAI_API_KEY')

def obtener_respuesta_chatgpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Cambia el motor según tus necesidades
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagnostico', methods=['POST'])
def diagnostico():
    pregunta = request.form.get('pregunta')
    if pregunta:
        respuesta = obtener_respuesta_chatgpt(pregunta)
        return render_template('result.html', pregunta=pregunta, respuesta=respuesta)
    else:
        return jsonify({'error': 'No se proporcionó ninguna pregunta'}), 400

if __name__ == '__main__':
    app.run(debug=True)

