import random

# Lista de jugadores por equipo original
jugadores = {
    "Equipo A": ["Rin Itoshi", "Aryu Jyubei", "Tokimitsu Aoshi", "Isagi Yoichi", "Bachira Meguru"],
    "Equipo B": ["Nagi Seishirou", "Barou Shouei", "Chigiri Hyoma", "Kunigami Rensuke", "Reo Mikage"],
    "Equipo C": ["Shidou Ryusei", "Niko Ikki", "Otoya Eita", "Hiori Yo", "Kenyu Yukimiya"],
    "Equipo D": ["Karasu Tabito", "Igaguri Gagamaru", "Nanase Nijiro", "Kurona Ranze", "Zantetsu Tsurugi"],
    "Equipo E": ["Aiku Oliver", "Naruhaya Asahi", "Gurimu Igarashi", "Yuzu Wakatsuki", "Kira Ryosuke"]
}

# Todos los jugadores en una sola lista
todos_jugadores = [jugador for equipo in jugadores.values() for jugador in equipo]

# Función para generar equipos aleatorios
def generar_equipos(jugadores, num_equipos=5):
    random.shuffle(jugadores)  # Mezcla los jugadores de forma aleatoria
    equipos = {f"Equipo {i+1}": [] for i in range(num_equipos)}
    
    for i, jugador in enumerate(jugadores):
        equipo_key = f"Equipo {i % num_equipos + 1}"
        equipos[equipo_key].append(jugador)
    
    return equipos

# Generar equipos aleatorios
equipos_aleatorios = generar_equipos(todos_jugadores)

# Imprimir los equipos generados
for equipo, jugadores in equipos_aleatorios.items():
    print(f"\n{equipo}:")
    for jugador in jugadores:
        print(f"- {jugador}")