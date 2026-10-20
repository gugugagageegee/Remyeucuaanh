"""Generate tiny, original cat-like electronic meow effects (no copyrighted samples)."""
from pathlib import Path
import numpy as np
import wave
root=Path(__file__).parent/'assets'/'audio'
root.mkdir(parents=True,exist_ok=True)
SR=24000

def mew(start=550,top=790,end=360,duration=.43):
    n=int(SR*duration)
    t=np.arange(n)/SR
    u=t/duration
    freq=np.piecewise(u,[u<.24,(u>=.24)&(u<.56),u>=.56], [lambda z:start+(top-start)*(z/.24)**1.1,lambda z:top-(top-start)*.28*((z-.24)/.32),lambda z:top-(top-start)*.28-(top-(top-start)*.28-end)*((z-.56)/.44)**.65])
    freq += 14*np.sin(2*np.pi*17*t)*(np.sin(np.pi*u)**2)
    phase=2*np.pi*np.cumsum(freq)/SR
    vocal=(np.sin(phase)+.32*np.sin(2*phase+.4)+.15*np.sin(3*phase+.2)+.065*np.sin(4*phase))
    env=(np.sin(np.pi*np.clip(u,0,1))**.57)*np.minimum(1,t/.029)
    return vocal*env*.37

def make(path,clips):
    pieces=[]
    for args,pause in clips:
        pieces.append(mew(**args));pieces.append(np.zeros(int(SR*pause)))
    a=np.concatenate(pieces)
    a=np.tanh(1.2*a)
    # fade last 15ms
    a[-int(.015*SR):]*=np.linspace(1,0,int(.015*SR))
    pcm=(np.clip(a,-1,1)*32767).astype('<i2')
    with wave.open(str(root/path),'wb') as wf:
        wf.setnchannels(1);wf.setsampwidth(2);wf.setframerate(SR);wf.writeframes(pcm.tobytes())
make('cat-wrong.wav',[({'start':440,'top':660,'end':260,'duration':.59},.03)])
make('cat-correct.wav',[({'start':610,'top':860,'end':520,'duration':.29},.055),({'start':720,'top':1000,'end':610,'duration':.34},.015)])
for p in root.glob('*.wav'):
    print(p.name,p.stat().st_size)
