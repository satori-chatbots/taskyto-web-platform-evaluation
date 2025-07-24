def main():
    try:
        with open('sightings.txt', 'r') as file:
            sightings = file.readlines()
            sightings_list = [sighting.strip() for sighting in sightings]
            return "\n".join(sightings_list) if sightings_list else "No hay avistamientos registrados."
    except Exception as e:
        return f"Ocurrió un error al recuperar los avistamientos: {str(e)}"