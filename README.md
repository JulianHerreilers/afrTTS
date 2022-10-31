# afrTTS - Afrikaans PyTorch-based G2P and text-to-speech synthesis
Please note that this is a direct continuation of the work performed in https://github.com/JulianHerreilers/afrTTS1. As I was finalising my report, I changed the name
and as such lost the ability to push my final code.
please refer to https://github.com/JulianHerreilers/afrTTS1 for the history of work/commits performed throughout the course of the semester. <br />

With this formality addressed, welcome to afrTTS. We implement two systems: <br />
-NaiveTTS uses an existing limited pronunciation dictionary and suffers from misallignment.<br />
-G2PxTTS uses a G2P conversion model to expand this dictionary to create more coherent audio.<br />

Installs <br />
```python
pip install librosa
pip install univoc
pip install tacotron
pip install omegaconf
pip install torch
```

Tacotron
A series 

test


The G2P model can be trained and used to expand the pronuncation dictionary all from the notebook at G2P/G2P_LSTM.ipynb.<br />


##Acknowledegments: <br />
-https://github.com/bshall/Tacotron <br />
-https://github.com/bshall/UniversalVocoding <br />
-Computations were performed using the University of Stellenbosch's HPC1 (Rhasatsha): http://www.sun.ac.za/hpc <br />
