import time
from pytrignos.pytrignos import TrignoAdapter
import sys, signal

def signal_handler(signal, frame):
    trigno_sensors.stop_acquisition()
    sys.exit(0)


if __name__ == "__main__":
    host_ip = "150.254.46.55"
    id = 6
    trigno_sensors = TrignoAdapter()
    trigno_sensors.add_sensors(sensors_mode='EMG', sensors_ids=(id,), sensors_labels=('EMG1',), host=host_ip)
    trigno_sensors.add_sensors(sensors_mode='ORIENTATION', sensors_ids=(id,), sensors_labels=('ORIENTATION1',), host=host_ip)
    trigno_sensors.start_acquisition()

    time_period = 1.0 #s
    signal.signal(signal.SIGINT, signal_handler)

    while(True):
        time.sleep(time_period)
        sensors_reading = trigno_sensors.sensors_reading()
        print(sensors_reading)
    trigno_sensors.stop_acquisition()

    # 150.254.46.55
