import numpy as np
import scipy
import matplotlib.pyplot as plt
from IPython.display import audio, display

class AudioEdit

    data=None
    sr  =None
    
    def __init__(self,wav_file) #remember this needs to go inside the class body
        self.sr=sr, self.data= scipy.io.wavfile.read(wav_file)


    def low_pass(self,fr):
        b,a  = scipy.signal.butter(2,fr/(self.sr/2.0),'low')
        edit = scipy.signal.filtfilt(b,a,data)          #apply it to the data in RAM
        self.data = np.asarray(edit,dtype=np.int16)          #convert back into int16
      


    def hi_pass(self,fr):
        b,a  = scipy.signal.butter(2,fr/(self.sr/2.0),'high') #make a fr HZ cutoff hi-pass filter
        edit = scipy.signal.filtfilt(b,a,self.data)           #apply it to the data in RAM
        self.data = np.asarray(edit,dtype=np.int16)           #convert back into int16
        
    def delay(self,ts):
        edit = np.zeros(data.shape,dtype=np.int16)
        edit[:] = self.data[:]
        for s in ts:
            edit[:len(edit)-int(s*sr)] += self.data[int(s*sr):]//2
        self.data=edit
        
    def shifter(self,shift):
        d = scipy.fft.dct(self.data)
        p = scipy.ndimage.shift(d,cval=0.0)
        self.data = scipy.fft.idct(p)

    def save(self, filename):
        scipy.io.wavfile.write(filename, self.sr, self.data)
        
    def play (self):
        display(Audio(self.data, rate= self.sr, autoplay=False))
        
    def plot(self):
        fig,ax= plt.subplots(1,1,figsize=(8,4))
        t=np.linspace(0.,len(edit)/sr,len(edit))
        ax.plot(t,edit,lw=1)
        plt.show

