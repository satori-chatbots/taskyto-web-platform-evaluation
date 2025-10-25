# -----> File: save_sighting.py <-----
def main(nombre_comun, coordenadas, forma_avistamiento):
    with open('sightings.txt', 'a') as file:
        file.write(f"{nombre_comun}, {coordenadas}, {forma_avistamiento}\n")
    return "El avistamiento ha sido guardado exitosamente."
