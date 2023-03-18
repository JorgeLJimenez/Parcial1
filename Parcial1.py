import math
class Cycle:
    def __init__(self,state): 
        self.state = state
        n = len(state) #n filas
        m = len(state[0]) #m=4 columnas [P,V,T,PROCESO]
        self.shape = [n, m]        
    def __str__(self):
        #for i in range(self.shape[0]-1):
        answer=""
        for i in range(self.shape[0]):
            answer = answer + self._print_state_(i)
        answer=answer+"Cycle finished.\n\n"
        return(answer)
    def _print_state_(self,i):
        if i < self.shape[0]-1:
            answer=("Equilibrium State "+str(i+1)+"\n"+"Pressure: {0} Pascal\nVolume: {1} cubic meter\nTemperature: {2} Kelvin".
                format(str(self.state[i][0]), str(self.state[i][1]), str(self.state[i][2]))
                +"\n"+"There is an "+str(self.state[i][3])+" process from equilibrium state "+str(i+1)+" to equilibrium state "+str(i+2)+"\n\n")
        else:
            answer=("Equilibrium State "+str(i+1)+"\n"+"Pressure: {0} Pascal\nVolume: {1} cubic meter\nTemperature: {2} Kelvin".
                format(str(self.state[i][0]), str(self.state[i][1]), str(self.state[i][2]))
                +"\n"+"There is an "+str(self.state[i][3])+" process from equilibrium state "+str(i+1)+" to equilibrium state "+str(0)+"\n\n")
        return(answer)
    def _compute_heatWork_(self,state):
        P1=self.state[0][0]
        P2=self.state[1][0]
        V1=self.state[0][1]
        V2=self.state[1][1]
        T1=self.state[0][2]
        T2=self.state[1][2]
        R=8.314
        answer1=[]      #answer1 es una lista de trabajo-energía de cada proceso en un ciclo: [[W1,Q1],[W2,Q2],...,[Wn,Qn]]
        answer2=[0,0]   #answer2 es una lista de trabajo-energía total en un ciclo: [W_total, Q_total]

        for i in range(self.shape[0]):

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
                Q=2*R*math.log(V2/V1,2.7182818284)
                W=2*R*T1*math.log(V2/V1,2.7182818284)
            #return("isothermal")
            else:
                return("...")
            answer1.append([round(W,1),round(Q,1)])
        for i in range(self.shape[0]):
            answer2[0]=answer2[0]+answer1[i][0]
            answer2[1]=answer2[1]+answer1[i][1]
        answer2[0]=round(answer2[0],1)
        answer2[1]=round(answer2[1],1)
        return(answer2)
          
M = Cycle([[1,2,4,"adiabatic"],[3,16,1,"isochoric"],[7,16,4,"isothermal"],[1,3,2,"isobaric"]])
print(M)

print(M._compute_heatWork_(M))

#Ciclo 1
#State '1'
#Pressure: P
#Volume: V
#Temperature: T
#---------------------------------------------
#adiabatic process from state'1' to state '2'
#---------------------------------------------
#State '1'
#Pressure: P
#Volume: V
#Temperature: T