import os

os.system("conda install -y pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia")
os.system("conda install -y -c conda-forge matplotlib pandas scipy cppyy pypy cython")
os.system("pip install numpy jupyter transformers nltk tqdm selenium opencv-python pyperclip openai-whisper copilot deep-translator")
