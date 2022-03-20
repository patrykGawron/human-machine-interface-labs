import time

import pandas as pd
from numpy.fft import fft, fftfreq
from pytrignos.pytrignos import TrignoAdapter

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Scope:
    def __init__(self, ax, maxt=4, dt=0.02):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.01, 0.01)
        self.ax.set_xlim(0, self.maxt)

    def update(self, val, sensors):
        sensors_reading = sensors.sensors_reading()
        print(sensors_reading)
        # sensors_reading.to_hdf("./test.hdf5", key="data")
        if len(sensors_reading) > 0:
            lastt = self.tdata[-1]
            if lastt > self.tdata[0] + self.maxt:  # reset the arrays
                self.tdata = [self.tdata[-1]]
                self.ydata = [self.ydata[-1]]
                self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
                self.ax.figure.canvas.draw()

            t = self.tdata[-1] + (((sensors_reading.index-sensors_reading.index[0]).microseconds)/1e6).values
            self.tdata = fftfreq(len(sensors_reading["EMG"].values), 1)#self.tdata + t.tolist()
            self.ydata = fft(sensors_reading["EMG"].values)# + (sensors_reading['EMG'].values.tolist())
        self.line.set_data(self.tdata, self.ydata)
        return self.line,



# Fixing random state for reproducibility


trigno_sensors = TrignoAdapter()
ip = "150.254.46.55"
id = 6
trigno_sensors.add_sensors(sensors_mode='ORIENTATION', sensors_ids=(id,), sensors_labels=('ORIENTATION1',), host=ip)
trigno_sensors.add_sensors(sensors_mode='EMG', sensors_ids=(id,), sensors_labels=('EMG1',), host=ip)

trigno_sensors.start_acquisition()

time_period = 1.0 #s


fig, ax = plt.subplots()
scope = Scope(ax)

# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, fargs=(trigno_sensors,), interval=1000,
                              blit=True)

plt.show()
trigno_sensors.stop_acquisition()
