import math
import matplotlib.pyplot as plt
import numpy as np

#MRU
def calcular_posicion_final_mru():

    print("\nMovimiento Rectilinio Uniforme")
    velocidad = float(input("Ingrese la velocidad en m/s: "))
    tiempo = float(input("Ingrese el tiempo en segundos: "))
    
    # Calcular la posición final
    posicion_final = velocidad * tiempo
    
    print(f"\nLa posición final es: {posicion_final} metros.")
    
    # Graficar el movimiento
    tiempo_grafica = np.linspace(0, tiempo, 100)
    posicion_grafica = velocidad * tiempo_grafica
    
    plt.plot(tiempo_grafica, posicion_grafica)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición (m)')
    plt.title('Gráfico de Posición en función del Tiempo (MRU)')
    plt.grid(True)
    plt.show()

#Caida Libre
def calcular_caida_libre():

    print("\nCaida Libre")
    altura_inicial = float(input("Ingrese la altura inicial en metros: "))
    gravedad = 9.8  # Asumimos gravedad estándar de 9.8 m/s^2
    
    # Calcular el tiempo de caída
    tiempo_caida = math.sqrt((2 * altura_inicial) / gravedad)
    
    # Calcular la velocidad final
    velocidad_final = gravedad * tiempo_caida
    
    print(f"\nTiempo de caída: {tiempo_caida} segundos")
    print(f"Velocidad final: {velocidad_final} m/s")
    
    # Graficar la caída libre
    tiempo_grafica = np.linspace(0, tiempo_caida, 100)
    altura_grafica = altura_inicial - 0.5 * gravedad * (tiempo_grafica ** 2)
    
    plt.plot(tiempo_grafica, altura_grafica)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Altura (m)')
    plt.title('Gráfico de Altura en función del Tiempo (Caída Libre)')
    plt.grid(True)
    plt.show()


#Tiro parabolico
def calcular_tiro_parabolico():

    print("\nTiro Parabolico")
    velocidad_inicial = float(input("Ingrese la velocidad inicial en m/s: "))
    angulo = math.radians(float(input("Ingrese el ángulo en grados: ")))
    gravedad = 9.8  # Asumimos gravedad estándar de 9.8 m/s^2
    
    # Calcular componentes horizontal y vertical de la velocidad inicial
    velocidad_inicial_x = velocidad_inicial * math.cos(angulo)
    velocidad_inicial_y = velocidad_inicial * math.sin(angulo)
    
    # Calcular el tiempo de vuelo
    tiempo_vuelo = (2 * velocidad_inicial_y) / gravedad
    
    # Calcular la altura máxima
    altura_maxima = (velocidad_inicial_y ** 2) / (2 * gravedad)
    
    # Calcular la distancia horizontal máxima
    distancia_maxima = velocidad_inicial_x * tiempo_vuelo
    
    print(f"\nTiempo de vuelo: {tiempo_vuelo} segundos")
    print(f"Altura máxima: {altura_maxima} metros")
    print(f"Distancia horizontal máxima: {distancia_maxima} metros")
    
    # Graficar la trayectoria del tiro parabólico
    tiempo_grafica = np.linspace(0, tiempo_vuelo, 100)
    x_grafica = velocidad_inicial_x * tiempo_grafica
    y_grafica = (velocidad_inicial_y * tiempo_grafica) - (0.5 * gravedad * (tiempo_grafica ** 2))
    
    plt.plot(x_grafica, y_grafica)
    plt.xlabel('Distancia Horizontal (m)')
    plt.ylabel('Altura (m)')
    plt.title('Trayectoria del Tiro Parabólico')
    plt.grid(True)
    plt.show()

#Ley de Coulomb
def ley_coulomb():

    print("\nLey De Coulomb")
    carga_1 = float(input("Ingrese la carga de la partícula 1 en Coulombs: "))
    carga_2 = float(input("Ingrese la carga de la partícula 2 en Coulombs: "))
    distancia = float(input("Ingrese la distancia entre las partículas en metros: "))
    k = 8.99e9  # Constante de Coulomb
    
    # Calcular la fuerza eléctrica
    fuerza = (k * carga_1 * carga_2) / (distancia ** 2)
    
    print(f"\nLa fuerza eléctrica entre las partículas es: {fuerza} Newtons.")
    
    # Graficar la fuerza en función de la distancia
    distancia_grafica = np.linspace(0.1, distancia, 100)
    fuerza_grafica = (k * carga_1 * carga_2) / (distancia_grafica ** 2)
    
    plt.plot(distancia_grafica, fuerza_grafica)
    plt.xlabel('Distancia (m)')
    plt.ylabel('Fuerza (N)')
    plt.title('Fuerza Eléctrica en función de la Distancia')
    plt.grid(True)
    plt.show()


#Menu principal
def main():
    opcion = 0
    
    while opcion != 5:
        print("\n--------------- Equipo 4 ---------------")
        print("\n----------------- MENU -----------------")
        print("1. Movimiento Rectilíneo Uniforme (MRU)")
        print("2. Caída Libre")
        print("3. Tiro Parabólico")
        print("4. Ley de Coulomb")
        print("5. Salir")
        
        opcion = int(input("Seleccione una opción (1-5): "))
        
        if opcion == 1:
            calcular_posicion_final_mru()
        elif opcion == 2:
            calcular_caida_libre()
        elif opcion == 3:
            calcular_tiro_parabolico()
        elif opcion == 4:
            ley_coulomb()
        elif opcion == 5:
            print("¡Hasta luego!")
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa principal
main()