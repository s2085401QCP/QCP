from grovers import *
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display
import random
import numpy as np

qubits = 4
wanted_state = random.randint(0, 2**qubits)
print(f"Wanted state is: {format(wanted_state, '0%ib' % qubits)}")
def oracle(a):
    if a == wanted_state:
        return 1
    else:
        return 0

arr = np.arange(2**qubits) 
grovers = Grovers(oracle, arr)
labels = [format(i, '0%ib' % grovers.n_qubits_) for i in range(grovers.n_states_)]
j = 0
amplitudes = np.zeros((grovers.iterations * 2 + 1, grovers.n_states_))
grovers.register.setEqualSuperposition()
for i in range(grovers.n_states_):
    amplitudes[j, i] = grovers.register.state_[i].real 
j += 1    
for i in range(grovers.iterations):
    grovers.applyOracle()
    for p in range(grovers.n_states_):
        amplitudes[j, p] = grovers.register.state_[p].real
    j += 1
    grovers.flipByMean()
    for m in range(grovers.n_states_):
        amplitudes[j, m] = grovers.register.state_[m].real
    j += 1

def animation(i):
    fig.clear()
    if i % 2 != 0:
        plt.title("After Oracle application")
    else:
        plt.title("After Diffusion application")
    if i == 0:
        plt.title("Grovers Algorithm, register in equal superposition")
    plt.bar(arr, amplitudes[i, :])
    plt.ylabel("Amplitude")
    plt.xlabel("States")
    plt.xticks(arr, labels, rotation = "vertical")
    
fig = plt.figure()
anim = FuncAnimation(fig, animation, frames = grovers.iterations * 2 + 1, interval = 1500, repeat = False)
video = anim.to_html5_video()
html = HTML(video)
  
# draw the animation
display(html)
plt.close()





