from libs.oscilloscope.tek import TDS1012B
import matplotlib.pyplot as plt
#import requests

device = TDS1012B()

device.set_channel(1)
device.write('hor:main:scale 1.0e-6')
device.write('ch1:volts 2')
device.write('trig:main:level -2')
device.get_scale_parameters(device.channel1)
device.write('acquire:stopafter sequence')
st = '0'
for n in range(1000):
	outfile = open("data//1101"+str(n)+".txt", 'w+')
	st = device.query('acquire:state?').strip()
	while(st != '0'):
		st = device.query('acquire:state?').strip()
	e = device.get_wave_form(device.channel1)
	x, y = device.wave.get_wave()
	device.write('acquire:state on')
	for _x, _y in zip(x,y):
          outfile.write(str(_x) +  '\t' +  str(_y) + '\n')

	outfile.close()
	

