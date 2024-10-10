import flet as ft
import random

preguntas = [
    {"pregunta": "¿Quién es conocido como el padre de la física moderna?", 
    "opciones": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Niels Bohr"], 
    "respuesta": "Albert Einstein"},
    
    {"pregunta": "¿En qué siglo desarrolló Charles Darwin su teoría de la evolución por selección natural?", 
    "opciones": ["Siglo XVII", "Siglo XVIII", "Siglo XIX", "Siglo XX"], 
    "respuesta": "Siglo XIX"},
    
    {"pregunta": "¿Qué científico propuso la teoría heliocéntrica en el siglo XVI?", 
    "opciones": ["Johannes Kepler", "Nicolás Copérnico", "Tycho Brahe", "Ptolomeo"], 
    "respuesta": "Nicolás Copérnico"},
    
    {"pregunta": "¿Qué química pionera ganó dos premios Nobel en distintas disciplinas científicas?", 
    "opciones": ["Marie Curie", "Rosalind Franklin", "Ada Lovelace", "Lise Meitner"], 
    "respuesta": "Marie Curie"},
    
    {"pregunta": "¿Quién es considerado el inventor del cálculo infinitesimal junto con Newton?", 
    "opciones": ["René Descartes", "Blaise Pascal", "Gottfried Leibniz", "Pierre-Simon Laplace"], 
    "respuesta": "Gottfried Leibniz"},

    {"pregunta": "¿Quién fue el primero en observar microorganismos con un microscopio?", 
    "opciones": ["Antonie van Leeuwenhoek", "Robert Hooke", "Louis Pasteur", "Gregor Mendel"], 
    "respuesta": "Antonie van Leeuwenhoek"},
    
    {"pregunta": "¿Cuál es la famosa ecuación desarrollada por Albert Einstein?", 
    "opciones": ["F=ma", "E=mc^2", "a^2 + b^2 = c^2", "PV=nRT"], 
    "respuesta": "E=mc^2"},
    
    {"pregunta": "¿Quién propuso la teoría del Big Bang?", 
    "opciones": ["Edwin Hubble", "Albert Einstein", "Georges Lemaître", "Stephen Hawking"], 
    "respuesta": "Georges Lemaître"},
    
    {"pregunta": "¿Qué científico es conocido por sus leyes del movimiento?", 
    "opciones": ["Galileo Galilei", "Isaac Newton", "James Clerk Maxwell", "Michael Faraday"], 
    "respuesta": "Isaac Newton"},
    
    {"pregunta": "¿Quién descubrió la penicilina?", 
    "opciones": ["Alexander Fleming", "Marie Curie", "Louis Pasteur", "Robert Koch"], 
    "respuesta": "Alexander Fleming"},

    {"pregunta": "¿Qué astrónomo formuló las leyes del movimiento planetario?", 
    "opciones": ["Nicolás Copérnico", "Galileo Galilei", "Johannes Kepler", "Tycho Brahe"], 
    "respuesta": "Johannes Kepler"},
    
    {"pregunta": "¿Quién formuló la ley de la gravitación universal?", 
    "opciones": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], 
    "respuesta": "Isaac Newton"}
]

def main(page: ft.Page):
    page.title = "Trivia de Historia de la Ciencia"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#5F9EA0"
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    pregunta_actual = random.choice(preguntas)
    
    def nueva_pregunta():
        nonlocal pregunta_actual
        pregunta_actual = random.choice(preguntas)
        pregunta_text.value = pregunta_actual["pregunta"]
        for i, opcion in enumerate(opciones_botones):
            opcion.text = pregunta_actual["opciones"][i]
        respuesta_text.value = ""
        page.update()
    
    def verificar_respuesta(e):
        if e.control.text == pregunta_actual["respuesta"]:
            respuesta_text.value = "¡Correcto!"
        else:
            respuesta_text.value = f"Incorrecto. La respuesta correcta es: {pregunta_actual['respuesta']}"
        page.update()

    # Aquí agregamos la imagen, puede ser una imagen local o una URL
    imagen = ft.Image(src="imagen.jpg", 
                    width=200, height=200)

    pregunta_text = ft.Text(pregunta_actual["pregunta"], size=20)
    
    opciones_botones = [
        ft.ElevatedButton(text=pregunta_actual["opciones"][i], on_click=verificar_respuesta) 
        for i in range(4)
    ]
    respuesta_text = ft.Text("", size=18, color=ft.colors.WHITE)
    
    siguiente_pregunta_btn = ft.ElevatedButton(text="Nueva Pregunta", on_click=lambda _: nueva_pregunta())
    
    # Agregamos la imagen antes de la pregunta y las opciones
    page.add(
        imagen,
        pregunta_text, 
        ft.Column(opciones_botones, spacing=10),
        respuesta_text,
        siguiente_pregunta_btn
    )

ft.app(target=main)

