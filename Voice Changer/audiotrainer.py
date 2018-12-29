from pyo import *
import wave

audio_serv = Server(duplex=1).boot()
aud_in = Input(chnl=1, mul=.7)

sf2 = aud_in.mix(2).out()

# Sets values for 8 LFO'ed delay lines (you can add more if you want!).
# LFO frequencies.
freqs = [.254, .465, .657, .879, 1.23, 1.342, 1.654, 1.879]
# Center delays in seconds.
cdelay = [.0087, .0102, .0111, .01254, .0134, .01501, .01707, .0178]
# Modulation depths in seconds.
adelay = [.001, .0012, .0013, .0014, .0015, .0016, .002, .0023]

# Create 8 sinusoidal LFOs with center delays "cdelay" and depths "adelay".
lfos = Sine(freqs, mul=adelay, add=cdelay)

# Create 8 modulated delay lines with a little feedback and send the signals
# to the output. Streams 1, 3, 5, 7 to the left and streams 2, 4, 6, 8 to the
# right (default behaviour of the out() method).
delays = Delay(aud_in, lfos, feedback=.5, mul=.5).out()

audio_serv.gui(locals())
