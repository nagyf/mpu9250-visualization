import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Plotter:
    """
    Plots the sensor data using matplotlib
    """

    def __init__(self, data):
        self.data = data
        self.fig, self.axes = plt.subplots(3)
        self.fig.suptitle('MPU 9250')
        self.accel_lines = self.create_lines(self.axes[0], 3)
        self.gyro_lines = self.create_lines(self.axes[1], 3)
        self.mag_lines = self.create_lines(self.axes[2], 3)
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval=100, blit=False)

    def create_lines(self, axis, num = 3):
        return [axis.plot([], [])[0] for i in range(0, num)]

    def draw_lines(self, axis, lines, values):
        xs = list(range(0, len(values)))
        for idx in range(0, 3):
            axis.set_xlim(0, 2*len(xs))
            axis.set_ylim(self.min_value(values), self.max_value(values))
            ys = list(map(lambda value: value[idx], values))
            lines[idx].set_data(xs, ys)

    def min_value(self, values):
        if(len(values) == 0):
            return -1

        return numpy.amin([numpy.amin(value) for value in values])

    def max_value(self, values):
        if(len(values) == 0):
            return 1
        
        return numpy.amax([numpy.amax(value) for value in values])

    def animate(self, i):
        self.draw_lines(self.axes[0], self.accel_lines, self.data.get_acceleration())
        self.draw_lines(self.axes[1], self.gyro_lines, self.data.get_gyro())
        self.draw_lines(self.axes[2], self.mag_lines, self.data.get_mag())
        self.fig.canvas.draw()

    def start(self):
        plt.show()