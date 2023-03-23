#AUTOR: JORGE LUIS JIMÉNEZ
#ESTE PROGRAMA PERMITE VER UN CICLO TERMODINÁMICO CON SUS RESPECTIVOS PROCESOS Y CALCULAR EL TRABAJO Y EL CALOR EN ESE CICLO.

import math
class Cycle:
    #Creo el constructor de la clase Cycle con el método __init__. In the constructor you can set variables and call methods
    def __init__(self,state):  
        #Cuando creo un objeto, se inicializan sus atributos o variables gracias al método __init__. 
        #Instance is an object that belongs to a class. For instance, list is a class in Python. When we create a list, we have an instance of the list class.
        #SELF represents the instance of class. This handy keyword allows you to access variables, attributes, and methods of a defined class in Python.
        self.state = state #Para una lista de nx4. las tres primeras guardan datos numéricos P,V,T y la última el proceso en string.
        n = len(state) #n filas, que significa n procesos en un ciclo
        m = 4 #4 columnas [P,V,T,"SIGUIENTE PROCESO"] 
        self.shape = [n, m]
    def __str__(self): #The __str__() method returns a human-readable, or informal, string representation of an object.
        answer=""
        for i in range(self.shape[0]): #i<4, i=0,1,2,3
            answer = answer + self._print_state_(i) #concateno la descrición del siguiente estado para cada iteración
        answer=answer+"Cycle finished.\n\n"
        return(answer)
    def _print_state_(self,i): #
        if i < self.shape[0]-1: #i+1=número de estado, i<n, i=0,1,2,...,(n-1)-1 
            answer=("Equilibrium State "+str(i+1)+"\n"+"Pressure: {0} Pascal\nVolume: {1} cubic meter\nTemperature: {2} Kelvin".
                format(str(self.state[i][0]), str(self.state[i][1]), str(self.state[i][2]))
                +"\n"+"There is an "+str(self.state[i][3])+" process from equilibrium state "+str(i+1)+" to equilibrium state "+str(i+2)+"\n\n")
        else: #i=n-1 (dado que el proceso va del estado n al estado inicial 1, solo se cambia str(i+2) por str(1) en la parte final de la cadena)
            answer=("Equilibrium State "+str(i+1)+"\n"+"Pressure: {0} Pascal\nVolume: {1} cubic meter\nTemperature: {2} Kelvin".
                format(str(self.state[i][0]), str(self.state[i][1]), str(self.state[i][2]))
                +"\n"+"There is an "+str(self.state[i][3])+" process from equilibrium state "+str(i+1)+" to equilibrium state "+str(1)+"\n\n")
        return(answer)
    def _compute_heatWork_(self,state):
        state=state
        R=8.314
        answer1=[]      #answer1 es una lista de trabajo-energía de cada proceso en un ciclo: [[Q1,W1],[Q2,W2],...,[Qn,Wn]]
        answer2=[0,0]   #answer2 es una lista de trabajo-energía total en un ciclo: [Q_total, W_total]

        for i in range(self.shape[0]): #itera en los estados 1,2,...,n-1. (i=0,1,...,n-2)
            if i < self.shape[0]-1: #Si estados en un estado que no sea el último (estado n), haga...
                P1=self.state[i][0]
                #P2=self.state[i+1][0] #NO SE USA
                V1=self.state[i][1]
                V2=self.state[i+1][1]
                T1=self.state[i][2]
                T2=self.state[i+1][2]
            
                if self.state[i][3]=="adiabatic":
                    Q=0
                    W=-3*R*(T2-T1)
                #return("adiabatic")
                elif self.state[i][3]=="isobaric":
                    Q=5*R*(T2-T1)
                    W=P1*(V2-V1)
                #return("isobaric")
                elif self.state[i][3]=="isochoric":
                    Q=3*R*(T2-T1)
                    W=0
                #return("isochoric")
                elif self.state[i][3]=="isothermal":
                    Q=2*R*T1*math.log(V2/V1,2.7182818284)
                    W=2*R*T1*math.log(V2/V1,2.7182818284)
                #return("isothermal")
                else:
                    return("...")  
                answer1.append([round(Q,1),round(W,1)])
            else:
                P1=self.state[i][0]
                #P2=self.state[0][0] #NO SE USA
                V1=self.state[i][1]
                V2=self.state[0][1]
                T1=self.state[i][2]
                T2=self.state[0][2]
            
                if self.state[i][3]=="adiabatic":
                    Q=0
                    W=-3*R*(T2-T1)
                #return("adiabatic")
                elif self.state[i][3]=="isobaric":
                    Q=5*R*(T2-T1)
                    W=P1*(V2-V1)
                #return("isobaric")
                elif self.state[i][3]=="isochoric":
                    Q=3*R*(T2-T1)
                    W=0
                #return("isochoric")
                elif self.state[i][3]=="isothermal":
                    Q=2*R*T1*math.log(V2/V1,2.7182818284)
                    W=2*R*T1*math.log(V2/V1,2.7182818284)
                #return("isothermal")
                else:
                    return("...")  
                answer1.append([round(Q,1),round(W,1)])
        
        for i in range(self.shape[0]): #aqui se hace la sumatoria de los calores y trabajos en cada proceso, para obtener los Q Y W totales.
            answer2[0]=answer2[0]+answer1[i][0]
            answer2[1]=answer2[1]+answer1[i][1]
        answer2[0]=round(answer2[0],1)
        answer2[1]=round(answer2[1],1)
        return(answer2) #OBSERVACIÓN: retorne answer1 para ver el proceso en detalle, o retorne answer2 para ver el calor y trabajo total.
    
               # Estado 1              Estado 2                Estado 3            Estado 4            Estado 5
M1 = Cycle([[1,2,4,"adiabatic"],[3,16,1,"isochoric"],[7,16,2,"isothermal"],[1,3,2,"isobaric"]])

print(M1)
print("Total work and total heat spend to the system [Q_total, W_total]:") #comentario para el retorno de answer2
#print("Work and heat spend to the system in each process of the cycle [[Q(1->2),W(1->2)],[Q(2->3),W(2->3)],...,[Q(n->1),W(n->1)]]:") #comentario para el retorno de answer1
print(M1._compute_heatWork_(M1))

#R=8.314
#[P,V,T,SIGUIENTE PROCESO]
#answer1 es una lista de calor-trabajo de cada proceso en un ciclo: [[Q(1->2),W(1->2)],[Q(2->3),W(2->3)],...,[Q(n->1),W(n->1)]]
#answer2 es una lista de calor-trabajo total en un ciclo: [Q_total, W_total]
#[[0, 74.8], [24.9, 0], [-55.7, -55.7], [83.1, -1]]