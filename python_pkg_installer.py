import os

os.system("conda install -y pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia")
os.system("conda install -y -c conda-forge matplotlib pandas opencv scipy cython")
os.system("pip install numpy jupyter transformers nltk tqdm selenium pyperclip openai-whisper copilot deep-translator")
# cppyy, pypy
