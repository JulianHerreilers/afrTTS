# afrTTS - Afrikaans PyTorch-based G2P and text-to-speech synthesis
Welcome to afrTTS! We implement two systems: <br />
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

Tacotron <br />
A series pretrained weights are avaible at https://github.com/JulianHerreilers/pantoffel_tacotron_models_storage only the following two should be used: <br />
-NaiveTTS: "https://github.com/JulianHerreilers/pantoffel_tacotron_models_storage/releases/download/v0.190k-210k-230k-beta/model-230000. <br />
-G2PxTTS: "https://github.com/JulianHerreilers/pantoffel_tacotron_models_storage/releases/download/v1.120epoch/model-300000.pt" <br />
<br />
Tacotron can be trained by running the following preprocessing and training commands:<br />
First adjust the first argument in line 32 of utils/jsonmaker.py to metadata_incomplete.csv then run the following commands: <br/>
```python
python utils/jsonmaker.py
python preprocess.py afrZA datasets/afrZA
python train.py afrza afrZA/metadata_incomplete.csv datasets/afrZA
```
<br/>
The G2P model can be trained and used to expand the pronuncation dictionary all from the notebook at G2P/G2P_LSTM.ipynb.<br />
<br/>
A demo notebook afrTTS_demo.pynb can be used to test out the two systems provided that demo_utils.py, g2pmodel.py and the two dictionaries, afr_za_dict.txt and rcrl_apd.1.4.1.txt are in the same directory.<br/>
<br/>
Further datasets and alogrithms are available in utils/: <br/>

-split_num_letters.py converts all numbers in a sequence to their word equivalents. <br/>
-demo_sample_randomizer.ipynb was used to sort the demo samples for the subjective evaluation. <br/>
-check_valid_entries complete.py returns the remainder of the dataset that remains in the selected dictionary, whether afr_za_dict.txt or rcrl_apd.1.4.1.txt. <br/>

Acknowledegments: <br />
-https://github.com/bshall/Tacotron <br />
-https://github.com/bshall/UniversalVocoding <br />
-Computations were performed using the University of Stellenbosch's HPC1 (Rhasatsha): http://www.sun.ac.za/hpc <br />
