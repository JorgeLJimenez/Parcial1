import math
class State:
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
    #def _energy_(self,lista):
    #   heatWork=[]self.lista[]
    #  return()
          
M = State([[1,2,4,"adiabatic"],[3,16,1,"isochoric"],[7,16,4,"isothermal"],[1,3,2,"isobaric"]])
print(M)

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