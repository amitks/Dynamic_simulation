from apm import * # load APMonitor.com files

z = apm_solve('skydiver',7)

import matplotlib.pyplot as plt

plt.figure(1)
plt.subplot(211)
plt.plot(z['time'],z['x'],'r:')
plt.plot(z['time'],z['y'],'b--')
plt.ylabel('Position (m)')
plt.legend(['x','y'])

plt.subplot(212)
plt.plot(z['time'],z['vx'],'r:')
plt.plot(z['time'],z['vy'],'b--')
plt.plot(z['time'],z['v'],'k-')
plt.xlabel('Time (sec)')
plt.ylabel('Velocity (m/s)')
plt.legend(['V_x','V_y','V'])

plt.figure(2)
plt.plot(z['x'],z['y'],'r-')
plt.xlabel('Position (x)')
plt.ylabel('Position (y)')
plt.show()
