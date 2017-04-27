import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
import matplotlib.animation as animation

beta = lambda v, dt, dx: v * dt / dx

gaussian = lambda x, u=0.5, ro=0.05: np.exp((x - u) / (2 * ro ** 2))

time_steps = 100
b_0 = .5
b_max = 1.2
b = b_0

x_len = 110
dx = 1 / x_len
x_linspace = np.linspace(0, 1, x_len)
initial1 = gaussian(np.zeros(x_len))
initial2 = initial1


def next_time_step(current, previous, left, right, beta):
    a = 2 * (1 - beta ** 2) * current
    b = previous
    c = beta ** 2 * (left + right)
    return a - b + c


def step(current_state, prev_state, beta):
    left = np.concatenate((np.zeros(2), current_state[:-2]))
    right = np.concatenate((current_state[2:], np.zeros(2)))
    current = np.concatenate((np.zeros(1), current_state[1:-1], np.zeros(1)))
    previous = np.concatenate((np.zeros(1), prev_state[1:-1], np.zeros(1)))

    next_state = next_time_step(current, previous, left, right, beta)
    return next_state


def time_loop(initial1, initial2, beta):
    state_list = [initial1, initial2]
    prev = initial1
    current = initial2

    for s in range(time_steps):
        next_state = step(current, prev, beta)
        prev = current
        current = next_state

        state_list.append(current)

    return state_list


state_list = time_loop(initial1, initial2, b)

ln, = plt.plot([], [], 'ro', animated=True)


def animate(frame):
    ln.set_data(frame)


# #Limits
# ax.set_xlim((0, 1))
# ax.set_ylim((-1, 1))

# Line to be altered in animation
# //line, = ax.plot([], [],'k', lw=2)



# Figure and axes to manipulate
figure, ax = plt.subplots()

# Limits
ax.set_xlim((0, 1))
ax.set_ylim((-1, 1))

# Line to be altered in animation
line, = ax.plot([], [], 'k', lw=2)

# map the output datasets into plots
frames = list(map(lambda l: plt.plot(l), state_list))
im_ani = animation.FuncAnimation(figure, animate, frames=state_list, interval=100, repeat_delay=3000, blit=True)
plt.show()





# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return (line,)

# def animate(i):
#     # Compute updates here!
#     line.set_data(x, un)
#     return (line,)

# # call the animator. blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=100, interval=20, blit=True)
# HTML(anim.to_html5_video())

# pass

