# make sure your python scripts on on the search path
PYTHONPATH=/home/jvogel/Documents/aiWorkrepo/mnistWork/scripts
export PYTHONPATH

# create virtual python environment for MNIST work
python3 -m venv .venv
.venv/bin/pip install matplotlib
.venv/bin/pip install PyQt6 # to enable plotting in python (without running in vscode...)
# .venv/bin/pip install numpy as np #i think you get this when you pip matplotlib...


#.venv/bin/pip install os
#.venv/bin/pip install tensorflow
#.venv/bin/pip install scikit-learn
#.venv/bin/pip install numpy #tensorflow supercedes this!!!

#.venv/bin/pip install scipy

#.venv/bin/pip install --upgrade pandas

#activate the virtual environment in your shell
source .venv/bin/activate
deactivate

#test install
python3 test.py



