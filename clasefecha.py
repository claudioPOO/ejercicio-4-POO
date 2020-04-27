class FechaHora:
    __dia=0
    __mes=0
    __año=0
    __hora=0
    __minutos=0
    __segundos=0
    def __init__(self,d=1,mes=1,año=2020,hora=0,minutos=0,segundos=0):
        self.__dia=d
        self.__mes=mes
        self.__año=año
        self.__hora=hora
        self.__minutos=minutos
        self.__segundos=segundos
    def Mostrar(self):
        print('DIA  MES  AÑO')
        print('%d\%d\%d'%(self.__dia,self.__mes,self.__año))
        print('%d hs %d min %d seg'%(self.__hora,self.__minutos,self.__segundos))
    def PonerEnHora(self,hora=0,minutos=0,segundos=0):
        self.__hora=hora
        self.__minutos=minutos
        self.__segundos=segundos
    def AdelantarHora(self,hora=0,minutos=0,segundos=0):
        self.__hora+=hora
        self.__minutos+=minutos
        self.__segundos+=segundos              
        if(self.__minutos>=60):
         self.__minutos=0
         self.__hora+=1
        if(self.__hora>=24):
            hora+=self.__hora
            self.__hora=int(hora)-24
            self.__dia+=1
            if(self.__dia==30 and self.__mes==4 or self.__mes==5 or self.__mes==6 or self.__mes==9 or self.__mes==11):
                self.__dia=1
                self.__mes+=1
            if(self.__dia==31 and self.__mes==1 or self.__mes==3 or self.__mes== 7 or self.__mes==8 or self.__mes==10):
                self.__dia=1
                self.__mes+=1
            if(self.__dia==31 and self.__mes==12):
                self.__año+=1
                self.__dia=1
                self.__mes=1
            if(self.__dia==28 and  self.__mes==2):
                if(self.__año%100==0):
                    if(self.__año%400==0):
                       self.__dia+=1
                    elif(self.__año%4==0):
                         self.__dia+=1
                    else:
                        self.__dia=1
                        self.__mes+=1
                        hora+=self.__hora
                        self.__hora=int(hora)-24
            if(self.__dia==29 and  self.__mes==2):
                self.__mes+=1
                self.__dia=1