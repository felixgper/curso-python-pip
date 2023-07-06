import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):    
    #fig es la figura y ax se refiere a las coordenadas donde se va a comenzara a graficar
    #La función subplot () puede ayudar a crear un gráfico mientras que puedes crear el segundo superponiéndolo al primero
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f"./imgs/{name}.png")
    #show() te permite visualizar los gráficos tanto si trabajas en la línea de comandos, con un script o en el intérprete de IPython.
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    #abajo le estamos diciendo que la grafica lo organice en el centro y en forma de circulo.
    ax.axis("equal")
    plt.savefig("pie.png")
    plt.close()

#La línea if name == 'main': comprueba si el archivo actual se está ejecutando como el archivo principal del programa. Si se está ejecutando como el archivo principal, es decir, si no se está importando desde otro archivo, el código dentro del bloque " if " se ejecutará.
if __name__== "__main__":
    labels = ["a", "b", "c"]
    values = [10, 40, 800]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
