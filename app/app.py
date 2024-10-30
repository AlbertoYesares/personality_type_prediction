import numpy as np 
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
import gradio as gr

with open('models/version_final_modelo_utilizado.pkl', 'rb') as f:
    model = pickle.load(f)

label_encoder = LabelEncoder()
label_encoder.fit(['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP', 
                   'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP'])

scaler = StandardScaler()

# Diccionario para traducir intereses del español al inglés
interest_translation = {
    "Desconocido": "Unknown",
    "Artes": "Arts",
    "Otros": "Others",
    "Tecnología": "Technology",
    "Deportes": "Sports"
}

feature_names = model.feature_names_in_

def predict_personality(age, gender, education, introversion_score, sensing_score, thinking_score, judging_score, interest):
    # Procesamiento de entrada
    gender = 0 if gender == 'Masculino' else 1  # Mapeo género a 0/1
    education = 1 if education == 'Soy licenciado' else 0  # Mapeo educación a 1/0

    # Traducir interés al inglés para el modelo
    interest = interest_translation[interest]
    
    # Codificar el interés como variable dummy
    interests = ['Unknown', 'Arts', 'Others', 'Technology', 'Sports']
    interest_encoded = [1 if interest == i else 0 for i in interests]

    # Escalar las variables numéricas
    input_data = np.array([[age, introversion_score, sensing_score, thinking_score, judging_score]])
    input_data_scaled = scaler.fit_transform(input_data)

    # Concatenar variables escaladas con las variables categóricas
    full_input = np.concatenate((input_data_scaled.flatten(), [gender, education] + interest_encoded))
    
    # Convertir full_input a un DataFrame con los nombres de las características originales
    full_input_df = pd.DataFrame([full_input], columns=feature_names)
    
    # Realizar la predicción
    prediction_encoded = model.predict(full_input_df)[0]
    
    # Decodificar la predicción de vuelta a la etiqueta original de personalidad
    personality_type = label_encoder.inverse_transform([prediction_encoded])[0]
    
    # Generar el enlace de información
    link = f"https://www.16personalities.com/es/personalidad-{personality_type.lower()}"
    
    # Mensaje final con la predicción y el enlace
    result_message = f"Tu tipo de personalidad es: {personality_type}\n\n[Más información sobre tu tipo de personalidad]({link})"
    
    return result_message


info_introversion = "Introversión (0)  vs. Extroversión (10)"
info_sensing = "Sensación (0)  vs. Intuición (10)"
info_thinking = "Pensamiento (0)  vs. Sentimiento (10)"
info_judging = "Percepción (0)  vs. Juicio (10)"

# Gradio
iface = gr.Interface(
    fn=predict_personality,
    inputs=[
        gr.Slider(18, 57, step=1, label="Edad"),
        gr.Radio(choices=["Masculino", "Femenino"], label="Género"),
        gr.Radio(choices=["Soy licenciado", "No lo soy"], label="Educación"),
        gr.Slider(0, 10, step=1, label=info_introversion, info="Indica tu nivel de preferencia por la reflexión y la introspección"),
        gr.Slider(0, 10, step=1, label=info_sensing, info="Mide tu inclinación hacia la observación de hechos y detalles concretos"),
        gr.Slider(0, 10, step=1, label=info_thinking, info="Evalúa tu preferencia por tomar decisiones de manera lógica y objetiva"),
        gr.Slider(0, 10, step=1, label=info_judging, info="Mide tu tendencia a estructurar y planificar tu vida"),
        gr.Dropdown(choices=["Desconocido", "Artes", "Otros", "Tecnología", "Deportes"], label="Intereses")
    ],
    outputs="markdown",  # Markdown para soportar enlaces
    title="Predicción de Tipo de Personalidad",
    description="Introduce los valores correctos para ver cuál es tu personalidad."
)

iface.launch()
