# 🎵 Secuenciador Musical - Proyecto Final de Graficación

**Instituto Tecnológico de Ensenada (ITE)**  
**Autor:** Armando Roberto Pérez Banda  
**Matrícula:** 24760228  
**Materia:** Graficación por Computadora

---

## 📖 Descripción

Secuenciador musical interactivo desarrollado en Python que permite crear patrones rítmicos y melódicos mediante una interfaz visual tipo grid (cuadrícula). El usuario puede colocar notas en diferentes posiciones, reproducirlas en tiempo real y guardar sus composiciones en una base de datos.

El proyecto combina conceptos de programación gráfica, manejo de audio, animaciones y persistencia de datos para crear una experiencia musical interactiva inspirada en secuenciadores clásicos de música 8-bit.

---

## ✨ Características Principales

- **Grid Interactivo:** Cuadrícula de 7 filas × 32 columnas para colocar notas musicales
- **7 Instrumentos Diferentes:** Cada fila representa un instrumento único con sonido distintivo
- **Reproducción en Tiempo Real:** Sistema de playback que reproduce las notas secuencialmente
- **Animaciones Bounce:** Efectos visuales de rebote al reproducir cada nota
- **Persistencia de Datos:** Guarda y carga composiciones usando SQLite
- **Canciones Precargadas:** Incluye 4 composiciones de ejemplo listas para reproducir
- **Interfaz Visual Intuitiva:** Botones con íconos y sprites personalizados

---

## 🎮 Instrumentos Disponibles

| Fila | Instrumento  | Sprite | Descripción                        |
| ---- | ------------ | ------ | ---------------------------------- |
| 0    | Beep Agudo   | 🔊     | Onda cuadrada aguda (sq_agudo2)    |
| 1    | Mouse Alto   | 🐭     | Onda cuadrada alta (sq_alto2)      |
| 2    | Yellow Medio | 🟡     | Onda cuadrada media (sq_medio2)    |
| 3    | Drop Agudo   | 💧     | Onda triangular aguda (tri_agudo2) |
| 4    | Organ Medio  | 👻     | Onda triangular media (tri_medio2) |
| 5    | Ghost Grave  | 👁️     | Onda triangular grave (tri_grave2) |
| 6    | Drum         | 🥁     | Percusión/ruido (noise_snare2)     |

---

## 🎹 Canciones Incluidas

### 1. **Deck The Halls (Robótico)**

- Tempo: 0.18s por beat
- Estilo: Melodía navideña con sonidos 8-bit
- Características: Bajo pulsante constante + contratiempos

### 2. **Escala de Prueba**

- Tempo: 0.20s por beat
- Estilo: Escala ascendente y descendente simple
- Uso: Ideal para probar el sistema

### 3. **We Wish You a Merry Christmas**

- Tempo: 0.20s por beat
- Estilo: Canción navideña lenta y melódica
- Características: Ritmo binario robótico

### 4. **Wily's Castle (Mega Man II)**

- Tempo: 0.12s por beat (¡MUY RÁPIDO!)
- Estilo: Chiptune agresivo con arpegios
- Características: Bajo pulsante intenso

---

## 🛠️ Requisitos del Sistema

### Software Necesario

- **Python 3.10** o superior
- **Pygame 2.x**

### Instalación de Dependencias

```bash
# Instalar Pygame
pip install pygame
```

---

## 📂 Estructura del Proyecto

```
proyecto_graficacion/
│
├── main.py              # Archivo principal del programa
├── grid.py              # Lógica del grid y dibujado de notas
├── orquesta.py          # Carga y reproducción de sonidos
├── botones.py           # Sistema de botones interactivos
├── personaje.py         # Personaje "maestro" (playhead)
├── database.py          # Gestión de base de datos SQLite
├── canciones.py         # Canciones precargadas
│
├── sounds/              # Archivos de audio (.wav)
│   ├── sq_agudo2.wav
│   ├── sq_alto2.wav
│   ├── sq_medio2.wav
│   ├── tri_agudo2.wav
│   ├── tri_medio2.wav
│   ├── tri_grave2.wav
│   └── noise_snare2.wav
│
├── imagenes/            # Sprites e íconos
│   ├── beep.png
│   ├── mouse.png
│   ├── yellow.png
│   ├── drop.png
│   ├── organ.png
│   ├── ghost.png
│   ├── drum.png
│   ├── MAESTRO.png
│   ├── PLAY.png
│   ├── STOP.png
│   ├── ERASER.png
│   ├── SAVE.png
│   ├── LOAD.png
│   └── EXIT.png
│
├── mi_base_de_datos.db  # Base de datos SQLite (se crea automáticamente)
└── README.md            # Este archivo
```

---

## 🚀 Cómo Ejecutar el Proyecto

1. **Clonar o descargar el repositorio**

```bash
git clone https://github.com/tu_usuario/proyecto_graficacion.git
cd proyecto_graficacion
```

2. **Verificar que tengas Python 3.10+ instalado**

```bash
python --version
```

3. **Instalar Pygame**

```bash
pip install pygame
```

4. **Ejecutar el programa**

```bash
python main.py
```

---

## 🎮 Controles y Uso

### Botones Principales (Superior Izquierda)

| Botón        | Función                                      |
| ------------ | -------------------------------------------- |
| ▶️ **PLAY**  | Inicia la reproducción de la composición     |
| ⏹️ **STOP**  | Detiene la reproducción                      |
| 🧹 **CLEAR** | Limpia todas las notas del grid              |
| 💾 **SAVE**  | Guarda la composición actual en la BD (ID=1) |
| 📂 **LOAD**  | Carga la composición guardada desde la BD    |
| 🚪 **EXIT**  | Cierra el programa                           |

### Botones de Canciones (Superior Derecha)

- **Deck The Halls** - Carga canción navideña robótica
- **Prueba** - Carga escala de prueba
- **Canción Lenta** - Carga "We Wish You a Merry Christmas"
- **Canción Rápida** - Carga "Wily's Castle"

### Interacción con el Grid

- **Click Izquierdo:** Añadir/eliminar nota en la posición seleccionada
- Las notas se representan con sprites según el instrumento
- Durante la reproducción, el "Maestro" se mueve sobre el grid
- Las notas reproducidas realizan una animación de rebote

---

## 🗄️ Sistema de Base de Datos

El proyecto utiliza **SQLite** para almacenar composiciones.

### Estructura de Tablas

**Tabla `canciones`:**

```sql
id INTEGER PRIMARY KEY
nombre TEXT NOT NULL
```

**Tabla `notas`:**

```sql
id INTEGER PRIMARY KEY
cancion_id INTEGER (FK)
fila INTEGER
columna INTEGER
```

### Comportamiento de Guardado

- Al guardar, se **sobrescribe** la canción con ID=1
- El botón "LOAD" siempre carga la última canción guardada
- El nombre incluye un timestamp único

---

## 🎨 Aspectos Técnicos Destacados

### Animaciones

- **Bounce Effect:** Usa funciones seno y exponencial para simular rebotes físicos
- **Playhead Dinámico:** El personaje "Maestro" rebota al reproducir notas

### Audio

- **16 Canales de Mezcla:** Permite reproducir múltiples sonidos simultáneamente
- **Frecuencia:** 44100 Hz, 16-bit, estéreo
- **Buffer Optimizado:** 512 samples para baja latencia

### Renderizado

- **60 FPS:** Actualización constante para animaciones fluidas
- **Grid Escalable:** Configuración mediante constantes fácilmente modificables

---

## 🔧 Configuración Avanzada

### Modificar Dimensiones del Grid

En `main.py`, ajusta estas constantes:

```python
GRID_FILAS = 7        # Número de instrumentos
GRID_COLUMNAS = 32    # Pasos en la secuencia
CELDA_ANCHO = 50      # Ancho de cada celda en píxeles
CELDA_ALTO = 60       # Alto de cada celda en píxeles
```

### Ajustar Tempo Global

```python
tiempo_por_beat = 0.20  # Segundos por columna (menor = más rápido)
```

---

## 📚 Módulos y Responsabilidades

| Módulo         | Responsabilidad                               |
| -------------- | --------------------------------------------- |
| `main.py`      | Loop principal, eventos, coordinación         |
| `grid.py`      | Lógica del grid, detección de mouse, dibujado |
| `orquesta.py`  | Carga y reproducción de audio                 |
| `botones.py`   | Sistema de botones con hover y callbacks      |
| `personaje.py` | Animación del playhead (Maestro)              |
| `database.py`  | CRUD de canciones en SQLite                   |
| `canciones.py` | Definición de canciones predeterminadas       |

---

## 🐛 Solución de Problemas

### El audio no se reproduce

- Verifica que los archivos `.wav` estén en la carpeta `sounds/`
- Asegúrate de que Pygame Mixer esté correctamente inicializado

### Las imágenes no aparecen

- Confirma que todos los sprites estén en la carpeta `imagenes/`
- Los archivos deben tener los nombres exactos especificados en el código

### Error de base de datos

- Elimina `mi_base_de_datos.db` y reinicia el programa
- Las tablas se crearán automáticamente

---

## 🎓 Conceptos de Graficación Aplicados

- **Renderizado 2D:** Pygame para dibujado de primitivas y sprites
- **Sistema de Coordenadas:** Conversión mouse → grid
- **Animaciones Procedurales:** Funciones matemáticas para efectos visuales
- **Buffer Doble:** Flip de pantalla para evitar parpadeo
- **Sprites y Texturas:** Manejo de imágenes PNG con transparencia
- **UI Interactiva:** Sistema de eventos y detección de colisiones

---

## 🎯 Posibles Mejoras Futuras

- [ ] Exportar composiciones como archivos MIDI o WAV
- [ ] Múltiples ranuras de guardado
- [ ] Editor de tempo en tiempo real (BPM slider)
- [ ] Más instrumentos y samples de audio
- [ ] Modo de grabación en vivo (teclado MIDI)
- [ ] Efectos de audio (reverb, delay, filtros)
- [ ] Visualizador de forma de onda
- [ ] Soporte para patrones más largos (64, 128 beats)

---

## 📄 Licencia

Proyecto académico desarrollado para la materia de Graficación por Computadora.  
Instituto Tecnológico de Ensenada - 2024/2025

---

## 👨‍💻 Autor

**Armando Roberto Pérez Banda**  
Matrícula: 24760228  
Instituto Tecnológico de Ensenada

---

## 🙏 Agradecimientos

- Profesor de Graficación por Computadora - ITE
- Documentación oficial de Pygame
- Comunidad de desarrollo de Python

---

¡Disfruta creando música! 🎶✨
