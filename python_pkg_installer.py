import os

os.system("conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia")
os.system("conda install -c anaconda numpy pandas scipy jupyter")
os.system("conda install -c conda-forge matplotlib cppyy pypy cython")
os.system("pip install transformers tqdm selenium opencv-python whisper copilot deep-translator")
