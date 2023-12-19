###############################TIME SCHEMES######################################################

from scipy.optimize import newton


# Euler method
def Euler(F, U, dt, t):
    return U + dt * F(U, t)


#Runge-Kutta 4 method
def RK4 (F, U, dt, t) :
       k1 = F (U, t)
       k2 = F (U + k1 * dt/2, t + dt/2)
       k3 = F (U + k2 * dt/2, t + dt/2)
       k4 = F (U + k3 * dt, t + dt)
       return U + dt/6 * (k1 + 2 * k2 + 2 * k3 + k4)   

#Crank-Nicolson method
def CN (F, U, dt, t) :
      def Residual_CN (X) :
          return X - a - dt/2 * F(X, dt + t)  
      a = U + dt/2 * F(U, t)
      return newton (Residual_CN, U)

#Inverse_Euler method
def EI (F, U, dt, t) :
    def Residual_IE (X) :
         return X - U - dt * F (X, dt + t)
    return newton (Residual_IE, U)
     
     
# Leap-Frog

def LF(F, U, dt, t):
    U_mediopaso = U + 0.5 * dt * F(U, t)
    return U + dt * F(U_mediopaso, t)


def choose_integration_method():
    print("Choose an integration method:")
    print("1. Euler")
    print("2. Inverse Euler")
    print("3. Runge-Kutta 4")
    print("4. Crank-Nicolson")
    print("5. Leap-Frog")

    choice = input("Enter the number corresponding to the desired method: ")
    
    if choice == '1':
        return Euler
    elif choice == '2':
        return EI
    elif choice == '3':
        return RK4
    elif choice == '4':
        return CN
    elif choice == '5':
        return LF
    else:
        print("Invalid choice. Using default method (Euler).")
        return Euler   

