import numpy as np
import matplotlib.pyplot as plt

#Laster inn fila og henter tidsverdiene fra første kolonne og posisjonsverdiene fra andre kolonne.
data = np.loadtxt("data\sprettball.txt")
t = data[:,0]
s = data[:,1]

#Lager posisjonsgrafen.
plt.figure(1)
plt.plot(t,s)
plt.grid()
plt.title("Posisjon")
plt.xlabel("$t$ / s")
plt.ylabel("$s$ / m")
plt.show()