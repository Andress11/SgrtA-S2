import numpy as np
from matplotlib import pyplot  as plt

# PARAMETROS TEMPORALES
n = 10        # numero de orbitas 
k = (1000)*n # numero de pasos

t = np.zeros(k)
dt = 0.01

# ARREGLOS POSICIÓN Y VELOCIDAD: MASA 1

X1, Vx1, Ax1 = np.zeros((3, k))
Y1, Vy1, Ay1 = np.zeros((3, k))

# ARREGLOS POSICIÓN Y VELOCIDAD: MASA 2

X2, Vx2, Ax2 = np.zeros((3, k))
Y2, Vy2, Ay2 = np.zeros((3, k))

# ARREGLOS PARA EL CENTRO DE MASA 

Xcm,XEcm = np.zeros((2,k))
Ycm,YEcm = np.zeros((2,k))

# ARREGLOS PARA LA ENERGÍA 

E,EE = np.zeros((2,k))
ET = np.ones(k)
Ep = np.zeros([k])
EEp = np.zeros([k])

XE1, VEx1, AEx1 = np.zeros((3, k))
YE1, VEy1, AEy1 = np.zeros((3, k))


XE2, VEx2, AEx2 = np.zeros((3, k))
YE2, VEy2, AEy2 = np.zeros((3, k))

# CONDICIONES INICIALES (VALORES 0 DE LOS ARREGLOS)

# MASA 1 

m1 =  (4.154*10**6)/19.5

X1[0] = XE1[0] = 0
Y1[0] = YE2[0] = 0

Vx1[0] = VEx1[0] = 0
Vy1[0] = VEy1[0] = 0

# MASA 2

m2 = 1

X2[0] = XE2[0] = -59.83198246
Y2[0] = YE2[0] =  54.1572504

Vx2[0] = VEx2[0] = 6.23976882
Vy2[0] = VEy2[0] = 9.13067002

mu = (m1*m2)/(m1+m2)

# PARAMETROS DE 
#Define universal gravitation constant
G = 6.67408*10**(-11) #N-m2/kg2
m_nd = 19.5*(1.989*10**30) #kg #mass of the s2
r_nd = 122.2*(1.496*10**11) #952 #*(1.496*10**11)  #Distancia sgtrA* - s2
v_nd = 30000 #m/s #relative velocity of earth around the sun
t_nd = 14.53*365*24*3600 #s 

K1 = G*t_nd*m_nd/(r_nd**2*v_nd)
K2 = (v_nd*t_nd/r_nd)

# CALCULO DE LA ACELERACIÓN PARA LOS ARREGLOS DE EULER

Ax1[0]=(m2*K1)*(X2[0]-X1[0])/((X1[0]-X2[0])**2+(Y1[0]-Y2[0])**2)**1.5
Ay1[0]=(m2*K1)*(Y2[0]-Y1[0])/((X1[0]-X2[0])**2+(Y1[0]-Y2[0])**2)**1.5

Ax2[0]=(m1*K1)*(X1[0]-X2[0])/((X2[0]-X1[0])**2+(Y1[0]-Y2[0])**2)**1.5
Ay2[0]=(m1*K1)*(Y1[0]-Y2[0])/((X2[0]-X1[0])**2+(Y2[0]-Y1[0])**2)**1.5

# CALCULO DE LA ACELERACIÓN PARA LOS ARREGLOS DE EULER - CROMER

AEx1[0]=(m2*K1)*(XE2[0]-XE1[0])/((XE1[0]-XE2[0])**2+(YE1[0]-YE2[0])**2)**1.5
AEy1[0]=(m2*K1)*(YE2[0]-YE1[0])/((XE1[0]-XE2[0])**2+(YE1[0]-YE2[0])**2)**1.5

AEx2[0]=(m1*K1)*(XE1[0]-XE2[0])/((XE2[0]-XE1[0])**2+(YE1[0]-YE2[0])**2)**1.5
AEy2[0]=(m1*K1)*(YE1[0]-YE2[0])/((XE2[0]-XE1[0])**2+(YE2[0]-YE1[0])**2)**1.5

for j in range(0,2):

  for i in range(1,k):

    # TIEMPO 
    t[i] = i*dt
  
    
    if (i<=3): # ESTE VALOR DEPENDE DEL GRADO DEL METODO DE AB
      
      if(j == 0): # EULER CROMER J = 0

        # POSICIÓN

        X1[i] = X1[i-1]+Vx1[i-1]*dt
        Y1[i] = Y1[i-1]+Vy1[i-1]*dt

        X2[i] = X2[i-1]+Vx2[i-1]*dt
        Y2[i] = Y2[i-1]+Vy2[i-1]*dt


        # ACELERACIÓN: MASA 1

        Ax1[i] = (m2*K1)*(X2[i]-X1[i])/((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**1.5
        Ay1[i] = (m2*K1)*(Y2[i]-Y1[i])/((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**1.5

        # ACELERACIÓN: MASA 2

        Ax2[i] = (m1*K1)*(X1[i]-X2[i])/((X2[i]-X1[i])**2+(Y1[i]-Y2[i])**2)**1.5
        Ay2[i] = (m1*K1)*(Y1[i]-Y2[i])/((X2[i]-X1[i])**2+(Y2[i]-Y1[i])**2)**1.5 

        # VELOCIDAD  

        Vx1[i] = (Vx1[i-1]+Ax1[i]*dt)
        Vy1[i] = (Vy1[i-1]+Ay1[i]*dt)

        Vx2[i] = (Vx2[i-1]+Ax2[i]*dt)
        Vy2[i] = (Vy2[i-1]+Ay2[i]*dt)
      
      else: #EULER NORMAL J = 1

        # POSICIÓN 

        XE1[i] = XE1[i-1]+VEx1[i-1]*dt
        YE1[i] = YE1[i-1]+VEy1[i-1]*dt

        XE2[i] = XE2[i-1]+VEx2[i-1]*dt
        YE2[i] = YE2[i-1]+VEy2[i-1]*dt


        # ACELERACIÓN: MASA 1

        AEx1[i] = (m2*K1)*(XE2[i]-XE1[i])/((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**1.5
        AEy1[i] = (m2*K1)*(YE2[i]-YE1[i])/((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**1.5

        # ACELERACIÓN: MASA 2

        AEx2[i] = (m1*K1)*(XE1[i]-XE2[i])/((XE2[i]-XE1[i])**2+(YE1[i]-YE2[i])**2)**1.5
        AEy2[i] = (m1*K1)*(YE1[i]-YE2[i])/((XE2[i]-XE1[i])**2+(YE2[i]-YE1[i])**2)**1.5 

       # VELOCIDAD 

        VEx1[i] = (VEx1[i-1]+AEx1[i-1]*dt)
        VEy1[i] = (VEy1[i-1]+AEy1[i-1]*dt)

        VEx2[i] = (VEx2[i-1]+AEx2[i-1]*dt)
        VEy2[i] = (VEy2[i-1]+AEy2[i-1]*dt)

    else:
      
      if(j == 0):

        # MÉTODO AB^4 - EULER CROMER

        # CALCULOS VELOCIDAD

        Vx1[i]= (Vx1[i-1]+(1/24)*dt*(-9*Ax1[i-4]+37*Ax1[i-3]-59*Ax1[i-2]+55*Ax1[i-1]))
        Vy1[i]= (Vy1[i-1]+(1/24)*dt*(-9*Ay1[i-4]+37*Ay1[i-3]-59*Ay1[i-2]+55*Ay1[i-1]))
      
        Vx2[i]= (Vx2[i-1]+(1/24)*dt*(-9*Ax2[i-4]+37*Ax2[i-3]-59*Ax2[i-2]+55*Ax2[i-1]))
        Vy2[i]= (Vy2[i-1]+(1/24)*dt*(-9*Ay2[i-4]+37*Ay2[i-3]-59*Ay2[i-2]+55*Ay2[i-1]))

        
        # CALCULOS DE LA POSICIÓN

        
        X1[i]=X1[i-1]+(1/24)*dt*(-9*Vx1[i-4]+37*Vx1[i-3]-59*Vx1[i-2]+55*Vx1[i-1])
        Y1[i]=Y1[i-1]+(1/24)*dt*(-9*Vy1[i-4]+37*Vy1[i-3]-59*Vy1[i-2]+55*Vy1[i-1])
          
        X2[i]=X2[i-1]+(1/24)*dt*(-9*Vx2[i-4]+37*Vx2[i-3]-59*Vx2[i-2]+55*Vx2[i-1])
        Y2[i]=Y2[i-1]+(1/24)*dt*(-9*Vy2[i-4]+37*Vy2[i-3]-59*Vy2[i-2]+55*Vy2[i-1])


        # ACELERACIÓN: MASA 1

        Ax1[i]= (m2*K1)*(X2[i]-X1[i])/((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**1.5
        Ay1[i]= (m2*K1)*(Y2[i]-Y1[i])/((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**1.5

        # ACELERACIÓN: MASA 2

        Ax2[i]= (m1*K1)*(X1[i]-X2[i])/((X2[i]-X1[i])**2+(Y1[i]-Y2[i])**2)**1.5
        Ay2[i]= (m1*K1)*(Y1[i]-Y2[i])/((X2[i]-X1[i])**2+(Y2[i]-Y1[i])**2)**1.5 

      else: 

        # MÉTODO AB^4 - EULER

        VEx1[i]= (VEx1[i-1]+(1/24)*dt*(-9*AEx1[i-4]+37*AEx1[i-3]-59*AEx1[i-2]+55*AEx1[i-1]))
        VEy1[i]= (VEy1[i-1]+(1/24)*dt*(-9*AEy1[i-4]+37*AEy1[i-3]-59*AEy1[i-2]+55*AEy1[i-1]))
      
        VEx2[i]= (VEx2[i-1]+(1/24)*dt*(-9*AEx2[i-4]+37*AEx2[i-3]-59*AEx2[i-2]+55*AEx2[i-1]))
        VEy2[i]= (VEy2[i-1]+(1/24)*dt*(-9*AEy2[i-4]+37*AEy2[i-3]-59*AEy2[i-2]+55*AEy2[i-1]))

        
        # CALCULOS DE LA POSICIÓN

        
        XE1[i]=XE1[i-1]+(1/24)*dt*(-9*VEx1[i-4]+37*VEx1[i-3]-59*VEx1[i-2]+55*VEx1[i-1])
        YE1[i]=YE1[i-1]+(1/24)*dt*(-9*VEy1[i-4]+37*VEy1[i-3]-59*VEy1[i-2]+55*VEy1[i-1])
          
        XE2[i]=XE2[i-1]+(1/24)*dt*(-9*VEx2[i-4]+37*VEx2[i-3]-59*VEx2[i-2]+55*VEx2[i-1])
        YE2[i]=YE2[i-1]+(1/24)*dt*(-9*VEy2[i-4]+37*VEy2[i-3]-59*VEy2[i-2]+55*VEy2[i-1])


        # ACELERACIÓN: MASA 1

        AEx1[i]= (m2*K1)*(XE2[i]-XE1[i])/((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**1.5
        AEy1[i]= (m2*K1)*(YE2[i]-YE1[i])/((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**1.5

        # ACELERACIÓN: MASA 2

        AEx2[i]= (m1*K1)*(XE1[i]-XE2[i])/((XE2[i]-XE1[i])**2+(YE1[i]-YE2[i])**2)**1.5
        AEy2[i]= (m1*K1)*(YE1[i]-YE2[i])/((XE2[i]-XE1[i])**2+(YE2[i]-YE1[i])**2)**1.5

for i in range(0,k):

  # CALCULOS PARA EL CENTRO DE MASA

  Xcm[i] = (m1*X1[i]+m2*X2[i])/(m1+m2)
  Ycm[i] = (m1*Y1[i]+m2*Y2[i])/(m1+m2)

  XEcm[i] = (m1*XE1[i]+m2*XE2[i])/(m1+m2)
  YEcm[i] = (m1*YE1[i]+m2*YE2[i])/(m1+m2)

  # CALCULO PARA LA ENERGÍA: POTENCIAL + CINETICA

  ET[i] = (0.5*mu*((Vx1[0]-Vx2[0])**2+((Vy1[0]-Vy2[0])**2))) - (m1*m2*K1)/(((X1[0]-X2[0])**2+(Y1[0]-Y2[0])**2)**0.5)
  E[i] = (0.5*mu*((Vx1[i]-Vx2[i])**2+((Vy1[i]-Vy2[i])**2))) - (m1*m2*K1)/(((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**0.5)
  EE[i] = (0.5*mu*((VEx1[i]-VEx2[i])**2+((VEy1[i]-VEy2[i])**2))) - (m1*m2*K1)/(((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**0.5)


  Ep[i] = abs((((ET[i] - E[i])/ET[i])*100))
  EEp[i] = abs((((ET[i] - EE[i])/ET[i])*100))

# CREA ENTRONO PARA LAS FIGURAS

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
fig.set_size_inches(22,12)


# GRAFICA LAS ORBITAS RESPECTO AL CENTRO DE MASA: AB4

ax1.set_title(" Órbitas dos cuerpos AB4(EulerCromer)",fontsize=14)
ax1.plot(X1-Xcm,Y1-Ycm,'o', label="cuerpo 1",c = "darkblue")
ax1.plot(X2-Xcm,Y2-Ycm,'', label="cuerpo 2",c = "red")
ax1.set_xlabel("x (UA)",fontsize=14)
ax1.set_ylabel("y (UA)",fontsize=14)

ax2.set_title("Órbitas dos cuerpos AB4(Euler)",fontsize=14)
ax2.plot(XE1-XEcm,YE1-YEcm,'o', label="cuerpo 1",c = "darkblue")
ax2.plot(XE2-XEcm,YE2-YEcm,'', label="cuerpo 2",c = "red")
ax2.set_xlabel("x",fontsize=14)
ax2.set_ylabel("y",fontsize=14)

# GRAFICA LA ENERGÍA TOTAL DEL SISTEMA: AB4

ax3.set_title("Energía total (AB4-EulerCromer)",fontsize = 14)
ax3.plot( t,E-ET,'',c = "darkblue")
ax3.grid(True)

ax4.set_title("Energía total (AB4-Euler)",fontsize = 14)
ax4.plot( t,EE-ET,'',c = "darkblue")
ax4.grid(True)


plt.savefig("Orbitas-Energia(AB4).png")
plt.show()

fig, (ax1,ax2)=plt.subplots(1,2)
fig.set_size_inches(20,6)

ax1.set_title("Energías AB4",fontsize = 14)
ax1.plot(t,E-ET,'',label = "Método AB4(EulerCromer)", c = "darkblue")
ax1.plot(t, EE-ET,'', label = "Método AB4(Euler)", c = "red")
ax1.plot(t,ET-ET,'',label ="Energía Teorica", linewidth = "2", color = "green" )
ax1.set_xlabel("Tiempo $(s)$",fontsize=14)
ax1.set_ylabel("Energía $(J)$",fontsize=14)
ax1.legend(loc="upper right",fontsize=5)
ax1.grid(True)

ax2.set_title("Error Energías AB4",fontsize = 14)
ax2.plot( t,Ep, c = "darkblue",label= "Cromer" )
ax2.plot(t, EEp,c = "red", label = "Euler" )
ax2.set_ylabel("Error Porcentual $(\%)$",fontsize=14)
ax2.legend(loc="upper left",fontsize=14)
ax2.grid(True)

plt.savefig("Comparacion-Energias_AB4.png")
plt.show()

for j in range(0,2):
    
    for i in range(0,k):

      t[i] = i*dt
      
      if(j == 0): # EULER CROMER J = 0

        # POSICIÓN

        X1[i] = X1[i-1]+Vx1[i-1]*dt
        Y1[i] = Y1[i-1]+Vy1[i-1]*dt

        X2[i] = X2[i-1]+Vx2[i-1]*dt
        Y2[i] = Y2[i-1]+Vy2[i-1]*dt


        # ACELERACIÓN: MASA 1

        Ax1[i] = (m2*K1)*(X2[i]-X1[i])/((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**1.5
        Ay1[i] = (m2*K1)*(Y2[i]-Y1[i])/((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**1.5

        # ACELERACIÓN: MASA 2

        Ax2[i] = (m1*K1)*(X1[i]-X2[i])/((X2[i]-X1[i])**2+(Y1[i]-Y2[i])**2)**1.5
        Ay2[i] = (m1*K1)*(Y1[i]-Y2[i])/((X2[i]-X1[i])**2+(Y2[i]-Y1[i])**2)**1.5 

        # VELOCIDAD  

        Vx1[i] = (Vx1[i-1]+Ax1[i]*dt)
        Vy1[i] = (Vy1[i-1]+Ay1[i]*dt)

        Vx2[i] = (Vx2[i-1]+Ax2[i]*dt)
        Vy2[i] = (Vy2[i-1]+Ay2[i]*dt)
      
      else: #EULER NORMAL J = 1

        # POSICIÓN 

        XE1[i] = XE1[i-1]+VEx1[i-1]*dt
        YE1[i] = YE1[i-1]+VEy1[i-1]*dt

        XE2[i] = XE2[i-1]+VEx2[i-1]*dt
        YE2[i] = YE2[i-1]+VEy2[i-1]*dt


        # ACELERACIÓN: MASA 1

        AEx1[i] = (m2*K1)*(XE2[i]-XE1[i])/((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**1.5
        AEy1[i] = (m2*K1)*(YE2[i]-YE1[i])/((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**1.5

        # ACELERACIÓN: MASA 2

        AEx2[i] = (m1*K1)*(XE1[i]-XE2[i])/((XE2[i]-XE1[i])**2+(YE1[i]-YE2[i])**2)**1.5
        AEy2[i] = (m1*K1)*(YE1[i]-YE2[i])/((XE2[i]-XE1[i])**2+(YE2[i]-YE1[i])**2)**1.5 

       # VELOCIDAD 

        VEx1[i] = (VEx1[i-1]+AEx1[i-1]*dt)
        VEy1[i] = (VEy1[i-1]+AEy1[i-1]*dt)

        VEx2[i] = (VEx2[i-1]+AEx2[i-1]*dt)
        VEy2[i] = (VEy2[i-1]+AEy2[i-1]*dt)

for i in range(0,k):

  # CALCULOS PARA EL CENTRO DE MASA

  Xcm[i] = (m1*X1[i]+m2*X2[i])/(m1+m2)
  Ycm[i] = (m1*Y1[i]+m2*Y2[i])/(m1+m2)

  XEcm[i] = (m1*XE1[i]+m2*XE2[i])/(m1+m2)
  YEcm[i] = (m1*YE1[i]+m2*YE2[i])/(m1+m2)

  # CALCULO PARA LA ENERGÍA: POTENCIAL + CINETICA

  E[i] = (0.5*mu*((Vx1[i]-Vx2[i])**2+((Vy1[i]-Vy2[i])**2))) - (m1*m2*K1)/(((X1[i]-X2[i])**2+(Y1[i]-Y2[i])**2)**0.5)
  EE[i] = (0.5*mu*((VEx1[i]-VEx2[i])**2+((VEy1[i]-VEy2[i])**2))) - (m1*m2*K1)/(((XE1[i]-XE2[i])**2+(YE1[i]-YE2[i])**2)**0.5)

fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2)
fig.set_size_inches(22,12)

# POSICIÓN

ax1.set_title("Orbitas dos cuerpos EulerCromer",fontsize=14)
ax1.plot(X1-Xcm,Y1-Ycm,'o', label="cuerpo 1",c = "darkblue")
ax1.plot(X2-Xcm,Y2-Ycm,'', label="cuerpo 2",c = "red")
ax1.set_xlabel("x (UA)",fontsize=14)
ax1.set_ylabel("y (UA)",fontsize=14)

ax2.set_title("Orbitas dos cuerpos Euler",fontsize=14)
ax2.plot(XE1-XEcm,YE1-YEcm,'o', label="cuerpo 1",c = "darkblue")
ax2.plot(XE2-XEcm,YE2-YEcm,'', label="cuerpo 2",c = "red")
ax2.set_xlabel("x (UA)",fontsize=14)
ax2.set_ylabel("y (UA)",fontsize=14)

# ENERGÍA

ax3.set_title("Energía total EulerCromer",fontsize = 14)
ax3.plot( t,E-ET,'',c = "darkblue")
ax3.set_xlabel("tiempo (s)",fontsize=14)
ax3.set_ylabel("Energía (J)",fontsize=14)
ax3.grid(True)

ax4.set_title("Energía total Euler)",fontsize = 14)
ax4.plot( t,EE-ET,'',c = "darkblue")
ax4.set_xlabel("tiempo (s)",fontsize=14)
ax4.set_ylabel("Energía (J)",fontsize=14)
ax4.grid(True)

plt.savefig("Orbitas-Energia(E-EC).png")
plt.show()
