# 🚀 Space Invaders Hybridge

Proyecto educativo para aprender **Programación Orientada a Objetos (POO)** en Python mediante la construcción de un clon del clásico **Space Invaders** utilizando la biblioteca **Pygame**.

---

## 📁 Estructura del Proyecto

```
spaceinvaders/
├── main.py                  # 🎮 Punto de entrada y orquestador del juego
├── ShipClass.py             # 🛸 Clase base Ship (nave genérica)
├── BulletClass.py           # 💥 Clase Bullet (proyectiles)
├── PlayerClass.py           # 🧑‍🚀 Clase Player (nave del jugador)
├── EnemyClass.py            # 👾 Clase Enemy (naves enemigas)
├── GameClass.py             # 🏆 Clase Game (estado y lógica del juego)
├── DrawingClass.py          # 🎨 Clase Drawing (renderizado gráfico)
├── MenuPrincipalClass.py    # 📋 Clase MenuPrincipal (menú de navegación)
├── MenuPuntajeClass.py      # 🥇 Clase MenuPuntajes (tabla de puntajes)
├── AcercaDeMenuClass.py     # ℹ️  Clase MenuAcercaDe (pantalla informativa)
├── VentanaNombre.py         # ✏️  Clase PantallaNombre (registro de récords)
├── puntajes.txt             # 💾 Archivo de persistencia de puntajes
├── calificaciones.txt       # 💾 Archivo de calificaciones
├── img/                     # 🖼️  Recursos gráficos
│   ├── background.png       #     Fondo del juego
│   ├── player_image.png     #     Sprite del jugador
│   ├── bullet_image.png     #     Sprite de la bala
│   ├── enemy_blue_image.png #     Sprite enemigo azul
│   ├── enemy_green_image.png#     Sprite enemigo verde
│   ├── enemy_purple_image.png#    Sprite enemigo morado
│   ├── shot_blue.png        #     Disparo enemigo azul
│   ├── shot_green.png       #     Disparo enemigo verde
│   ├── shot_purple.png      #     Disparo enemigo morado
│   ├── menu_fondo.jpg       #     Fondo del menú
│   ├── hybridge.gif         #     Logo Hybridge
│   └── title_icon.png       #     Ícono de la ventana
└── sounds/                  # 🔊 Recursos de audio
    ├── background_song.mp3  #     Música de fondo (menú)
    ├── explosion.wav        #     Efecto de explosión
    └── ganar.mp3            #     Efecto al superar récord
```

---

## 🗺️ Diagrama de Herencia de Clases

```
        Ship (Clase Base)
       /              \
    Player           Enemy
      |
    Bullet
```

| Relación | Tipo | Descripción |
|:---------|:-----|:------------|
| `Player` → `Ship` | Herencia | Player hereda posición, salud y método `draw()` |
| `Enemy` → `Ship` | Herencia | Enemy hereda posición, salud y método `draw()` |
| `Player` → `Bullet` | Composición | Player crea y administra una lista de objetos `Bullet` |

---

## 📚 Plan de Clases (6 sesiones)

### 🟢 Clase 1 — Fundamentos de Pygame y Estructura Base

**Tema:** Introducción a Pygame, ventana del juego y carga de recursos.

**Archivos que se abordan:**
| Archivo | Qué se aprende |
|:--------|:---------------|
| `main.py` (líneas 1–34) | Importaciones, inicialización de Pygame, carga de imágenes y sonidos, creación de la ventana del juego |

**Conceptos clave:**
- Instalación y configuración de Pygame
- `pygame.init()`, `pygame.display.set_mode()`
- Carga de imágenes con `pygame.image.load()`
- Carga de sonidos con `pygame.mixer`
- Constantes del juego (WIDTH, HEIGHT, FPS)
- Estructura de directorios para recursos (`img/`, `sounds/`)

---

### 🔵 Clase 2 — Programación Orientada a Objetos: Clases Base

**Tema:** Creación de clases, atributos, métodos, y el concepto de herencia.

**Archivos que se abordan:**
| Archivo | Qué se aprende |
|:--------|:---------------|
| `ShipClass.py` | Clase base `Ship`: constructor `__init__`, atributos (`x`, `y`, `health`), métodos (`draw`, `get_width`, `get_height`) |
| `BulletClass.py` | Clase `Bullet`: constructor con parámetros, método `move()`, detección de colisiones con `pygame.mask` |

**Conceptos clave:**
- Definición de clases y el método `__init__`
- Atributos de instancia (`self.x`, `self.y`)
- Métodos de instancia
- Encapsulamiento
- Introducción a **Masks** de Pygame para colisiones pixel-perfect
- El objeto como unidad de diseño

---

### 🟡 Clase 3 — Herencia: El Jugador y los Enemigos

**Tema:** Herencia de clases, polimorfismo, y lógica de movimiento.

**Archivos que se abordan:**
| Archivo | Qué se aprende |
|:--------|:---------------|
| `PlayerClass.py` | Clase `Player` que hereda de `Ship`: uso de `super().__init__()`, movimiento con teclado (`pygame.key.get_pressed()`), sistema de disparos y cooldown |
| `EnemyClass.py` | Clase `Enemy` que hereda de `Ship`: diccionario de colores para variantes, creación masiva de enemigos con `create()`, movimiento automático descendente |

**Conceptos clave:**
- Herencia: `class Player(Ship)` y `class Enemy(Ship)`
- Llamada al constructor padre con `super().__init__()`
- Polimorfismo: cada subclase implementa su propia lógica de `move()`
- Listas de objetos (lista de enemigos, lista de balas)
- Manejo de entrada del teclado
- Uso de `random` para posiciones y colores aleatorios

---

### 🟠 Clase 4 — Game Loop: Lógica Central del Juego

**Tema:** El bucle principal del juego, colisiones, niveles y HUD.

**Archivos que se abordan:**
| Archivo | Qué se aprende |
|:--------|:---------------|
| `GameClass.py` | Clase `Game`: gestión de estados (vidas, nivel, puntaje), lógica de Game Over, sistema de HUD (vidas, nivel, balas), lectura de récords desde archivo |
| `DrawingClass.py` | Clase `Drawing`: renderizado del fondo, enemigos, jugador y HUD en cada frame |
| `main.py` (líneas 37–120) | Función `main()`: el Game Loop completo — detección de colisiones, progresión de niveles, integración de todas las clases |

**Conceptos clave:**
- **Game Loop**: el patrón `while run` con `clock.tick(FPS)`
- Composición de objetos: `Game` coordina `Player`, `Enemy` y `Drawing`
- Detección de colisiones entre balas y enemigos
- Sistema de niveles progresivos (más enemigos, mayor velocidad)
- Patrón de separación de responsabilidades (lógica vs. renderizado)
- Lectura de archivos de texto (`puntajes.txt`)

---

### 🟣 Clase 5 — Interfaces de Usuario: Menús con Pygame

**Tema:** Diseño de menús interactivos, manejo de eventos de mouse y teclado.

**Archivos que se abordan:**
| Archivo | Qué se aprende |
|:--------|:---------------|
| `MenuPrincipalClass.py` | Clase `MenuPrincipal`: menú con selector navegable por teclado (↑↓ + Enter), renderizado de texto y opciones, callbacks a funciones del juego |
| `MenuPuntajeClass.py` | Clase `MenuPuntajes`: carga y ordenamiento de puntajes desde archivo, tabla de mejores récords, botón de retroceso con clic |
| `AcercaDeMenuClass.py` | Clase `MenuAcercaDe`: pantalla informativa con texto dinámico (word wrap), enlace externo con `webbrowser.open()`, botón de retroceso |

**Conceptos clave:**
- Renderizado de texto con `pygame.font`
- Navegación con teclado: operador módulo `%` para ciclar opciones
- Manejo de eventos de mouse (`MOUSEBUTTONDOWN`, `collidepoint`)
- Patrón de **callbacks**: pasar funciones como parámetros (`init_game_mtd`, `back_mtd`)
- Diseño de interfaces: rectángulos selectores, botones, fondos
- Apertura de URLs externas desde Python

---

### 🔴 Clase 6 — Persistencia de Datos y Flujo de Navegación

**Tema:** Escritura/lectura de archivos, registro de puntajes y navegación entre pantallas.

**Archivos que se abordan:**
| Archivo | Qué se aprende |
|:--------|:---------------|
| `VentanaNombre.py` | Clase `PantallaNombre`: campo de texto interactivo (input box), captura de texto con `event.unicode`, escritura de puntajes en archivo, botón de acción |
| `main.py` (líneas 123–139) | Funciones `initGame()`, `initPuntaje()`, `initAbout()`, `menu_principal()`: sistema de navegación entre pantallas usando funciones como callbacks |
| `puntajes.txt` | Formato de persistencia: `nombre,puntaje` por línea |

**Conceptos clave:**
- Lectura y escritura de archivos con `open()` (modos `'r'`, `'w'`, `'a'`)
- Manejo de excepciones: `try/except` para `FileNotFoundError` y `PermissionError`
- Campos de texto interactivos en Pygame
- Validación y procesamiento de strings (`split()`, `strip()`)
- Flujo de navegación completo: Menú → Juego → Récord → Menú
- Ordenamiento de datos con `sorted()` y funciones `lambda`

---

## 🎮 Controles del Juego

| Tecla | Acción |
|:------|:-------|
| `↑` `W` | Mover nave arriba |
| `↓` `S` | Mover nave abajo |
| `←` `A` | Mover nave a la izquierda |
| `→` `D` | Mover nave a la derecha |
| `Espacio` | Disparar |
| `↑` `↓` | Navegar menú |
| `Enter` | Seleccionar opción del menú |

---

## ⚙️ Requisitos

- Python 3.x
- Pygame 2.x

```bash
pip install pygame
```

## ▶️ Ejecución

```bash
python main.py
```

---

## 🧩 Resumen Visual del Flujo

```
┌─────────────┐
│   main.py   │
│  (Inicio)   │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│  MenuPrincipal   │◄──────────────────────────┐
│  ┌────────────┐  │                           │
│  │ 1. Jugar   │──┼──► main() ──► Game Loop   │
│  │ 2. Puntaje │──┼──► MenuPuntajes ──────────┤
│  │ 3. Acerca  │──┼──► MenuAcercaDe ──────────┤
│  └────────────┘  │                           │
└──────────────────┘                           │
                                               │
       Game Over                               │
          │                                    │
          ▼                                    │
    ¿Nuevo récord?                             │
     /        \                                │
   Sí          No ─────────────────────────────┤
    │                                          │
    ▼                                          │
┌──────────────┐                               │
│ PantallaNombre│                              │
│ (Guardar)    │───────────────────────────────┘
└──────────────┘
```
