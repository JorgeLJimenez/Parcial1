# Parcial1
## Estudiante H 
- [ ] **Introducción:** En termodinámica las variables de presión P, temperatura T, volumen V pueden cambiar y dependiendo de como cambien estas variables se dice que se tiene un proceso termodinámico particular. Los más importantes son el adiabático, isobárico, isocórico e isotermo. Dependiendo de como sea este cambio se va a tener un calor y una energía asociados al proceso.

La siguiente tabla muestra el calor y el trabajo generados entre el punto 1 y el punto 2 para diferentes procesos

|  |                                                 *Q*                                                  |                                                 *W*                                                  |
| -------- |:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|
|     Isocórico     |                         ![](https://latex.codecogs.com/gif.latex?3R%28T_2-T_1%29)                         |                                                     0                                                     |
|    Isobárico      |      ![](https://latex.codecogs.com/gif.latex?5R%28T_2-T_1%29)                                                                                                      |           ![](https://latex.codecogs.com/gif.latex?P%28V_2-V_1%29)                                                                                                |
|      Isotérmico    | ![](https://latex.codecogs.com/gif.latex?2RT%5Cln%20%5Cleft%28%5Cfrac%7BV_2%7D%7BV_1%7D%20%5Cright%20%29) | ![](https://latex.codecogs.com/gif.latex?2RT%5Cln%20%5Cleft%28%5Cfrac%7BV_2%7D%7BV_1%7D%20%5Cright%20%29) |
| Adiabático     |                                                   0                                                    |                                                                                                    ![](https://latex.codecogs.com/gif.latex?-3R%28T_2-T_1%29)  |

## ¿Qué hace el programa?

El programa tiene definida una clase llamada *Cycle* que recibe una lista de n filas y cuatro columnas en donde en las tres primeras se encuentran respectivamente P, V, T y en la cuarta el proceso que seguirá para llegar al siguiente valor de la tabla. por defecto dentro del programa se define un ejemplo de la lista

```[[1,2,4,"adiabatic"],[3,16,1,"isochoric"],[7,16,2,"isothermal"],[1,3,2,"isobaric"]]```

Lo que significa que en el estado 1, P=1, V=2, T=4 y el proceso que seguirá para llegar al estado 2 es un proceso adiabático, así hasta llegar al estado 4, donde P=1, V=3, T=2, que seguirá un proceso isobárico para retornar finalmente al estado 1. Se completa el ciclo.

### PARTE 1 DEFINICIÓN DE LA CLASE

```
class Cycle:
    def __init__(self,state):  
        self.state = state 
        n = len(state) 
        m = 4 
        self.shape = [n, m]
        
M1 = Cycle([[1,2,4,"adiabatic"],[3,16,1,"isochoric"],[7,16,2,"isothermal"],[1,3,2,"isobaric"]])
```

Defino la case Cycle. Esta recibe la lista nx4 que contiene la información del ciclo. Se inicializan los atributos: *state* que guarda la lista, *n* que guarda el número de filas (o de estados), *m* que será igual a 4 siempre, y *shape* que guarda los dos anteriores en una lista de dos columnas. Adicional, se define el objeto M1 de la clase Cycle que se usará a continuación.

### PARTE 2 IMPRESIÓN DE LOS ESTADOS Y PROCESOS EN UN CICLO

Al poner el objeto M1 dentro del print, se llama al método especial *str* que retorna la variable cadena *answer* y se imprime en pantalla la descripción del ciclo termodinámico. Para este fin, defino answer como una cadena vacía, luego hago un *for* que me itere en el número de filas/estados, en cada iteración hago una concatenación donde voy agregando el siguiente estado termodinámico, con la ayuda del método *print_state* que recibe como argumento el índice de la fila/estado.

```
print(M1)
```

```
    def __str__(self): 
        answer=""
        for i in range(self.shape[0]): 
            answer = answer + self._print_state_(i) 
        answer=answer+"Cycle finished.\n\n"
        return(answer)
```

En el *print_state*, se hace un condicional en donde primero se restringirá de la primera fila/estado hasta la penúltima fila/estado. En cada iteración del *for*, *print_state* retorna la variable *answer* que contiene la descripción de un solo estado, que se concatenará al *answer* del *str*. El *else* es necesario porque el último proceso va del estado n al estado 1, por esta razón solo se pone el *str(1)*. Cuando termina el *for* se concatena un mensaje para avisar al usuario de que el ciclo ha terminado. Finalmente se retorna *answer* al print para la consecuente impresión al usuario de la descripción de todo el ciclo termodinámico.

```
    def _print_state_(self,i): 
        if i < self.shape[0]-1: 
            answer=("Equilibrium State "+str(i+1)+"\n"+"Pressure: {0} Pascal\nVolume: {1} cubic meter\nTemperature: {2} Kelvin".
                format(str(self.state[i][0]), str(self.state[i][1]), str(self.state[i][2]))
                +"\n"+"There is an "+str(self.state[i][3])+" process from equilibrium state "+str(i+1)+" to equilibrium state "+str(i+2)+"\n\n")
        else: 
            answer=("Equilibrium State "+str(i+1)+"\n"+"Pressure: {0} Pascal\nVolume: {1} cubic meter\nTemperature: {2} Kelvin".
                format(str(self.state[i][0]), str(self.state[i][1]), str(self.state[i][2]))
                +"\n"+"There is an "+str(self.state[i][3])+" process from equilibrium state "+str(i+1)+" to equilibrium state "+str(1)+"\n\n")
        return(answer)
```

## PARTE 3 CÁLCULO E IMPRESIÓN DEL CALOR Y TRABAJO EN UN CICLO

En el método de impresión en pantalla, doy como argumento el método *compute_heatWork* que recibe el objeto *M1*, la lista que contiene la información del ciclo.

```
print(M1._compute_heatWork_(M1))
```

Debido a que este método es un poco largo, para fines prácticos se hará referencia a parte del código o comando por su intervalo de lineas que ocupa en el código del archivo Parcial1.py.

Este método en resumen calcula el calor y trabajo generados de la transición de un estado j a un estado j+1, y cada uno de estos Qj,Wj se guarda en la lista *answer1*. El *for* (línea 37) permite iterar en cada fila/estado. El *if* (línea 38) hace lo debido para las primeras n-1 filas/estados, y su respectivo else redefine las variables debido a que el proceso se devuelve del n al 1. Dentro de este *if-else*, los otros if-elif-else permiten hace el cálculo termodinámico correspondiente al proceso que se da del estado j (i+1) al estado j+1 (i+2). Estos cálculo se guardan en las variables Q y W y se agregan con el método *append* a la última fila de *answer1*, redondeados a un decimal usando el método *round*. Este algoritmo se repite con el *for* hasta tener la información energética de cada proceso. Después, el *for* (línea 93) itera en cada estado y hace la sumatoria de los Q y W de cada proceso para guardar el Q_total y W_total del ciclo termodinámico  en la lista *answer2*. Finalmete *compute_heatWork* retorna o *answer1* o *answer2* solo modificando dentro del código la variable de retorno, y sea cual sea se mostrará al usuario.