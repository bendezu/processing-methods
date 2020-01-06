from src.Canvas import Canvas
from src.IOController import IOController
from src.compositing.ConcatComposite import concat
from src.compositing.MultiplicationComposite import mult, mult_const
from src.drawable.Drawable import Drawable
from src.drawable.cardiogram import ecg
from src.drawable.itoprocess import ito
from src.drawable.wienerprocess import wiener
from src.filter.bandpass import bandpass
from src.filter.bandstop import bandstop
from src.filter.halflowpass import halflowpass
from src.filter.highpass import highpass
from src.filter.lowpass import lowpass
from src.transform.convolution import conv
from src.transform.hammingwindow import window
from src.transform.inversedft import idft
from src.util.buider import const, line, rand, harmonic, dft, sub, fft, absolute, cross

canvas = Canvas()
io = IOController()

rate, wav = io.read_from_wav("my-voice.wav")
lowpassed = conv(wav, lowpass(dt=1/rate, fCut=300))
highpassed = conv(wav, highpass(dt=1/rate, fCut=300))
drawables = enumerate([
    wav, absolute(fft(wav)),
    lowpassed, absolute(fft(lowpassed)),
    highpassed, absolute(fft(highpassed))
])
io.save_to_wav(lowpassed, rate)
io.save_to_wav(highpassed, rate)

for i, drawable in drawables:
    canvas.add_drawable(drawable)
figure = canvas.plot()

io.savePlotToFile(figure, "result")

# TODO fix myrandom
# TODO rename drawable metrics
# TODO dft adjust scale
# TODO suppress spikes by sliding window
