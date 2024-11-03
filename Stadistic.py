import json
import os
from ProblemsGenerator import ProblemsGenerator
from Solvers import solvers
import matplotlib.pyplot as plt

def calculate_mean(data):
    return sum(data) / len(data)

def save_results(n, avg_time):
    # Archivo de resultados
    filename = "execution_times.json"

    # Leer el archivo si existe
    if os.path.exists(filename):
        with open(filename, "r") as file:
            results = json.load(file)
    else:
        results = {}

    # Guardar los resultados en el diccionario
    results[str(n)] = avg_time

    # Escribir los resultados en el archivo JSON
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)

def plot_results():
    # Leer los resultados
    with open("execution_times.json", "r") as file:
        results = json.load(file)

    # Convertir datos para la gráfica
    sizes = list(map(int, results.keys()))
    times = list(results.values())

    # Crear la gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, marker="o", linestyle="-")
    plt.xlabel("Tamaño del puzzle (n)")
    plt.ylabel("Promedio de tiempo de ejecución (s)")
    plt.title("Tiempo de ejecución promedio vs Tamaño del puzzle")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    moves = 50  # Número de movimientos para generar el problema
    name = "problems.txt"
    print("Menu:")
    print("1. BFS")
    print("2. DFS")
    print("3. Greedy")
    print("4. A*")
    print("5. DFS unlimited")
    print("6. DFS iterative")
    print("7. Exit")
    algorithm = int(input("Choose the algorithm: "))

    if algorithm == 7:
        exit()

    n = int(input("Enter the size of the puzzle: "))
    nProblems = 1

    problems = []
    execution_times = []

    # Generación de problemas
    for i in range(nProblems):
        generator = ProblemsGenerator(n, moves)
        problem = generator.generate()
        problems.append(problem)

    # Guardar problemas en archivo de texto
    with open(name, "w") as file:
        for problem in problems:
            file.write(str(n) + "\n")
            for i in range(len(problem)):
                file.write(str(problem[i]) + " ")
                if (i + 1) % n == 0:
                    file.write("\n")
            file.write("------------------\n")

    print("Problems generated successfully.")
    print("Problems saved in", name)

    # Resolver problemas y almacenar tiempos de ejecución
    for i in range(nProblems):
        solver = solvers(problems[i], n)
        if algorithm == 1:
            result = solver.execute(1)
        elif algorithm == 2:
            result = solver.execute(2)
        elif algorithm == 3:
            result = solver.execute(3, 2)
        elif algorithm == 4:
            result = solver.execute(4, 2)
        elif algorithm == 5:
            result = solver.execute(5)
        elif algorithm == 6:
            result = solver.execute(6)

        execution_times.append(result.get(f"{['BFS', 'DFS', 'Greedy', 'A*', 'DFS unlimited', 'DFS iterative'][algorithm - 1]} time", 0))

    # Calcular promedio de tiempos y guardar en JSON
    avg_time = calculate_mean(execution_times)
    save_results(n, avg_time)

    # Leer el JSON y graficar
    plot_results()
