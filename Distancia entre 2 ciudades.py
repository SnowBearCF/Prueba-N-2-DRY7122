import requests

def get_route_info(start_city, end_city, vehicle_efficiency, api_key):
    url = "https://graphhopper.com/api/1/route"
    params = {
        'point': [start_city, end_city],
        'vehicle': 'car',
        'locale': 'es',
        'calc_points': 'false',  
        'key': api_key
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'paths' in data:
        path = data['paths'][0]
        distance_km = path['distance'] / 1000.0  
        time_sec = path['time'] / 1000.0  
        
        hours, remainder = divmod(time_sec, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        fuel_required = distance_km / vehicle_efficiency
        
        return distance_km, hours, minutes, seconds, fuel_required
    else:
        print("Error al obtener la ruta:", data)
        return None

def main():
    api_key = "9fb4f871-0302-43c3-bedd-05e0a54b4d59"
    while True:
        start_city = input("Ciudad de Origen (o 'q' para salir): ")
        if start_city.lower() == 'q':
            break
        
        end_city = input("Ciudad de Destino (o 'q' para salir): ")
        if end_city.lower() == 'q':
            break
        
        try:
            vehicle_efficiency = float(input("Rendimiento del vehículo (km/l): "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        result = get_route_info(start_city, end_city, vehicle_efficiency, api_key)
        
        if result:
            distance_km, hours, minutes, seconds, fuel_required = result
            print(f"\nNarrativa del Viaje:")
            print(f"Distancia: {distance_km:.2f} km")
            print(f"Duración: {int(hours)} horas, {int(minutes)} minutos, {int(seconds)} segundos")
            print(f"Combustible requerido: {fuel_required:.2f} litros")
        else:
            print("No se pudo calcular la ruta. Por favor, inténtelo de nuevo.")
    
    print("Programa terminado.")

if __name__ == "__main__":
    main()
