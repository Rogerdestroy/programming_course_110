# "411071114 林鈺翔.py"為期末專案  
#### "411071114 林鈺翔.ipynb"為期末作業    
#### 資料來源正在努力更新中 
use Python：Anaconda  conda 4.13.0   
Python 3.6.13   
IDE：spyder   

import numpy as np   
from math import log    
import cv2   
import prettytable as pt    
import random    
import time    
import sys    
import os    
import tkinter as tk    
from tkinter import messagebox    
import tkinter.ttk as ttk   
from selenium import webdriver    
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By  
from tqdm import tqdm  
 
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">Package</th>
    <th class="tg-0pky">Version</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">absl-py</td>
    <td class="tg-0pky">0.15.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">alabaster</td>
    <td class="tg-0pky">0.7.12</td>
  </tr>
  <tr>
    <td class="tg-0pky">appdirs</td>
    <td class="tg-0pky">1.4.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">argh</td>
    <td class="tg-0pky">0.26.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">arrow</td>
    <td class="tg-0pky">1.2.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">astroid</td>
    <td class="tg-0pky">2.6.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">astunparse</td>
    <td class="tg-0pky">1.6.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">async-generator</td>
    <td class="tg-0pky">1.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">atomicwrites</td>
    <td class="tg-0pky">1.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">attrs</td>
    <td class="tg-0pky">21.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">autopep8</td>
    <td class="tg-0pky">1.5.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">Babel</td>
    <td class="tg-0pky">2.9.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">backcall</td>
    <td class="tg-0pky">0.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">bcrypt</td>
    <td class="tg-0pky">3.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">beautifulsoup4</td>
    <td class="tg-0pky">4.11.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">binaryornot</td>
    <td class="tg-0pky">0.4.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">black</td>
    <td class="tg-0pky">19.3b0</td>
  </tr>
  <tr>
    <td class="tg-0pky">bleach</td>
    <td class="tg-0pky">4.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">brotlipy</td>
    <td class="tg-0pky">0.7.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">cached-property</td>
    <td class="tg-0pky">1.5.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">cachetools</td>
    <td class="tg-0pky">4.2.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">certifi</td>
    <td class="tg-0pky">2021.5.30</td>
  </tr>
  <tr>
    <td class="tg-0pky">cffi</td>
    <td class="tg-0pky">1.14.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">chardet</td>
    <td class="tg-0pky">4.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">charset-normalizer</td>
    <td class="tg-0pky">2.0.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">clang</td>
    <td class="tg-0pky">5</td>
  </tr>
  <tr>
    <td class="tg-0pky">click</td>
    <td class="tg-0pky">8.0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">cloudpickle</td>
    <td class="tg-0pky">2.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">cmake</td>
    <td class="tg-0pky">3.22.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">collection</td>
    <td class="tg-0pky">0.1.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">colorama</td>
    <td class="tg-0pky">0.4.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">cookiecutter</td>
    <td class="tg-0pky">1.7.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">cryptography</td>
    <td class="tg-0pky">35.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">cycler</td>
    <td class="tg-0pky">0.11.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">dataclasses</td>
    <td class="tg-0pky">0.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">decorator</td>
    <td class="tg-0pky">4.4.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">defusedxml</td>
    <td class="tg-0pky">0.7.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">demo-package</td>
    <td class="tg-0pky">0.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">diff-match-patch</td>
    <td class="tg-0pky">20200713</td>
  </tr>
  <tr>
    <td class="tg-0pky">dlib</td>
    <td class="tg-0pky">19.22.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">docutils</td>
    <td class="tg-0pky">0.17.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">entrypoints</td>
    <td class="tg-0pky">0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">face-recognition</td>
    <td class="tg-0pky">1.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">flake8</td>
    <td class="tg-0pky">3.9.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">flatbuffers</td>
    <td class="tg-0pky">1.12</td>
  </tr>
  <tr>
    <td class="tg-0pky">future</td>
    <td class="tg-0pky">0.18.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">gast</td>
    <td class="tg-0pky">0.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">GlobalVars</td>
    <td class="tg-0pky">0.0.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">google-auth</td>
    <td class="tg-0pky">1.35.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">google-auth-oauthlib</td>
    <td class="tg-0pky">0.4.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">google-pasta</td>
    <td class="tg-0pky">0.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">grpcio</td>
    <td class="tg-0pky">1.46.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">gym</td>
    <td class="tg-0pky">0.24.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">gym-notices</td>
    <td class="tg-0pky">0.0.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">gym-super-mario-bros</td>
    <td class="tg-0pky">7.3.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">h5py</td>
    <td class="tg-0pky">3.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">idna</td>
    <td class="tg-0pky">3.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">imageio</td>
    <td class="tg-0pky">2.15.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">imageio-ffmpeg</td>
    <td class="tg-0pky">0.4.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">imagesize</td>
    <td class="tg-0pky">1.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">importlib-metadata</td>
    <td class="tg-0pky">4.8.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">importlib-resources</td>
    <td class="tg-0pky">5.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">inflection</td>
    <td class="tg-0pky">0.5.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">intervaltree</td>
    <td class="tg-0pky">3.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">ipykernel</td>
    <td class="tg-0pky">5.3.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">ipython</td>
    <td class="tg-0pky">7.16.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">ipython-genutils</td>
    <td class="tg-0pky">0.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">isort</td>
    <td class="tg-0pky">5.9.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">jedi</td>
    <td class="tg-0pky">0.17.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">Jinja2</td>
    <td class="tg-0pky">3.0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">jinja2-time</td>
    <td class="tg-0pky">0.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">joblib</td>
    <td class="tg-0pky">1.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">jsonschema</td>
    <td class="tg-0pky">3.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">jupyter-client</td>
    <td class="tg-0pky">7.1.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">jupyter-core</td>
    <td class="tg-0pky">4.8.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">jupyterlab-pygments</td>
    <td class="tg-0pky">0.1.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">keras</td>
    <td class="tg-0pky">2.6.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">Keras-Preprocessing</td>
    <td class="tg-0pky">1.1.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">keyring</td>
    <td class="tg-0pky">23.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">Kivy</td>
    <td class="tg-0pky">2.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">kivy-deps.angle</td>
    <td class="tg-0pky">0.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">kivy-deps.glew</td>
    <td class="tg-0pky">0.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">kivy-deps.sdl2</td>
    <td class="tg-0pky">0.3.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">Kivy-Garden</td>
    <td class="tg-0pky">0.1.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">kiwisolver</td>
    <td class="tg-0pky">1.3.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">lazy-object-proxy</td>
    <td class="tg-0pky">1.6.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">Markdown</td>
    <td class="tg-0pky">3.3.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">MarkupSafe</td>
    <td class="tg-0pky">2.0.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">matplotlib</td>
    <td class="tg-0pky">3.3.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">mccabe</td>
    <td class="tg-0pky">0.6.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">mistune</td>
    <td class="tg-0pky">0.8.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">mkl-fft</td>
    <td class="tg-0pky">1.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">mkl-random</td>
    <td class="tg-0pky">1.1.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">mkl-service</td>
    <td class="tg-0pky">2.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">moviepy</td>
    <td class="tg-0pky">1.0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">nbclient</td>
    <td class="tg-0pky">0.5.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">nbconvert</td>
    <td class="tg-0pky">6.0.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">nbformat</td>
    <td class="tg-0pky">5.1.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">nes-py</td>
    <td class="tg-0pky">8.1.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">nest-asyncio</td>
    <td class="tg-0pky">1.5.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">numpy</td>
    <td class="tg-0pky">1.19.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">numpydoc</td>
    <td class="tg-0pky">1.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">oauthlib</td>
    <td class="tg-0pky">3.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">olefile</td>
    <td class="tg-0pky">0.46</td>
  </tr>
  <tr>
    <td class="tg-0pky">opencv-python</td>
    <td class="tg-0pky">4.5.5.64</td>
  </tr>
  <tr>
    <td class="tg-0pky">opt-einsum</td>
    <td class="tg-0pky">3.3.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">packaging</td>
    <td class="tg-0pky">21.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">pandas</td>
    <td class="tg-0pky">1.1.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">pandocfilters</td>
    <td class="tg-0pky">1.5.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">paramiko</td>
    <td class="tg-0pky">2.8.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">parso</td>
    <td class="tg-0pky">0.7.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pexpect</td>
    <td class="tg-0pky">4.8.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pickleshare</td>
    <td class="tg-0pky">0.7.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">Pillow</td>
    <td class="tg-0pky">8.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pip</td>
    <td class="tg-0pky">21.2.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">pluggy</td>
    <td class="tg-0pky">1.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">poyo</td>
    <td class="tg-0pky">0.5.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">prettytable</td>
    <td class="tg-0pky">2.5.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">proglog</td>
    <td class="tg-0pky">0.1.10</td>
  </tr>
  <tr>
    <td class="tg-0pky">prompt-toolkit</td>
    <td class="tg-0pky">3.0.20</td>
  </tr>
  <tr>
    <td class="tg-0pky">protobuf</td>
    <td class="tg-0pky">3.19.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">psutil</td>
    <td class="tg-0pky">5.8.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">ptyprocess</td>
    <td class="tg-0pky">0.7.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyasn1</td>
    <td class="tg-0pky">0.4.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyasn1-modules</td>
    <td class="tg-0pky">0.2.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">pycodestyle</td>
    <td class="tg-0pky">2.6.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pycparser</td>
    <td class="tg-0pky">2.21</td>
  </tr>
  <tr>
    <td class="tg-0pky">pydocstyle</td>
    <td class="tg-0pky">6.1.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyflakes</td>
    <td class="tg-0pky">2.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pygame</td>
    <td class="tg-0pky">2.1.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyglet</td>
    <td class="tg-0pky">1.5.11</td>
  </tr>
  <tr>
    <td class="tg-0pky">Pygments</td>
    <td class="tg-0pky">2.11.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">pylint</td>
    <td class="tg-0pky">2.9.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyls-black</td>
    <td class="tg-0pky">0.4.6</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyls-spyder</td>
    <td class="tg-0pky">0.3.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">PyNaCl</td>
    <td class="tg-0pky">1.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyOpenSSL</td>
    <td class="tg-0pky">22.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyparsing</td>
    <td class="tg-0pky">3.0.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">pypiwin32</td>
    <td class="tg-0pky">223</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyrsistent</td>
    <td class="tg-0pky">0.17.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">PySocks</td>
    <td class="tg-0pky">1.7.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">python-dateutil</td>
    <td class="tg-0pky">2.8.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">python-jsonrpc-server</td>
    <td class="tg-0pky">0.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">python-language-server</td>
    <td class="tg-0pky">0.36.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">python-slugify</td>
    <td class="tg-0pky">5.0.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">pytz</td>
    <td class="tg-0pky">2021.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">pywin32</td>
    <td class="tg-0pky">228</td>
  </tr>
  <tr>
    <td class="tg-0pky">pywin32-ctypes</td>
    <td class="tg-0pky">0.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">PyYAML</td>
    <td class="tg-0pky">5.4.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">pyzmq</td>
    <td class="tg-0pky">22.2.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">QDarkStyle</td>
    <td class="tg-0pky">3.0.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">qstylizer</td>
    <td class="tg-0pky">0.1.10</td>
  </tr>
  <tr>
    <td class="tg-0pky">QtAwesome</td>
    <td class="tg-0pky">1.0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">qtconsole</td>
    <td class="tg-0pky">5.2.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">QtPy</td>
    <td class="tg-0pky">2.0.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">requests</td>
    <td class="tg-0pky">2.27.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">requests-oauthlib</td>
    <td class="tg-0pky">1.3.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">rope</td>
    <td class="tg-0pky">0.22.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">rsa</td>
    <td class="tg-0pky">4.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">Rtree</td>
    <td class="tg-0pky">0.9.7</td>
  </tr>
  <tr>
    <td class="tg-0pky">scikit-learn</td>
    <td class="tg-0pky">0.24.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">scipy</td>
    <td class="tg-0pky">1.5.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">selenium</td>
    <td class="tg-0pky">3.141.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">setuptools</td>
    <td class="tg-0pky">58.0.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">six</td>
    <td class="tg-0pky">1.15.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">snowballstemmer</td>
    <td class="tg-0pky">2.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">sortedcontainers</td>
    <td class="tg-0pky">2.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">soupsieve</td>
    <td class="tg-0pky">2.3.2.post1</td>
  </tr>
  <tr>
    <td class="tg-0pky">Sphinx</td>
    <td class="tg-0pky">4.4.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">sphinxcontrib-applehelp</td>
    <td class="tg-0pky">1.0.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">sphinxcontrib-devhelp</td>
    <td class="tg-0pky">1.0.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">sphinxcontrib-htmlhelp</td>
    <td class="tg-0pky">2.0.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">sphinxcontrib-jsmath</td>
    <td class="tg-0pky">1.0.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">sphinxcontrib-qthelp</td>
    <td class="tg-0pky">1.0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">sphinxcontrib-serializinghtml</td>
    <td class="tg-0pky">1.1.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">spyder</td>
    <td class="tg-0pky">5.0.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">spyder-kernels</td>
    <td class="tg-0pky">2.0.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">tensorboard</td>
    <td class="tg-0pky">2.6.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">tensorboard-data-server</td>
    <td class="tg-0pky">0.6.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">tensorboard-plugin-wit</td>
    <td class="tg-0pky">1.8.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">tensorboardX</td>
    <td class="tg-0pky">2.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">tensorflow</td>
    <td class="tg-0pky">2.6.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">tensorflow-estimator</td>
    <td class="tg-0pky">2.6.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">termcolor</td>
    <td class="tg-0pky">1.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">testpath</td>
    <td class="tg-0pky">0.5.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">text-unidecode</td>
    <td class="tg-0pky">1.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">textdistance</td>
    <td class="tg-0pky">4.2.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">threadpoolctl</td>
    <td class="tg-0pky">3.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">three-merge</td>
    <td class="tg-0pky">0.1.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">tinycss</td>
    <td class="tg-0pky">0.4</td>
  </tr>
  <tr>
    <td class="tg-0pky">toml</td>
    <td class="tg-0pky">0.10.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">torch</td>
    <td class="tg-0pky">1.10.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">torchvision</td>
    <td class="tg-0pky">0.11.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">tornado</td>
    <td class="tg-0pky">6.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">tqdm</td>
    <td class="tg-0pky">4.64.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">traitlets</td>
    <td class="tg-0pky">4.3.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">typed-ast</td>
    <td class="tg-0pky">1.4.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">typing-extensions</td>
    <td class="tg-0pky">3.7.4.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">ujson</td>
    <td class="tg-0pky">4.0.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">Unidecode</td>
    <td class="tg-0pky">1.2.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">urllib3</td>
    <td class="tg-0pky">1.26.8</td>
  </tr>
  <tr>
    <td class="tg-0pky">watchdog</td>
    <td class="tg-0pky">2.1.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">wcwidth</td>
    <td class="tg-0pky">0.2.5</td>
  </tr>
  <tr>
    <td class="tg-0pky">webencodings</td>
    <td class="tg-0pky">0.5.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">Werkzeug</td>
    <td class="tg-0pky">2.0.3</td>
  </tr>
  <tr>
    <td class="tg-0pky">wheel</td>
    <td class="tg-0pky">0.37.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">win-inet-pton</td>
    <td class="tg-0pky">1.1.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">wincertstore</td>
    <td class="tg-0pky">0.2</td>
  </tr>
  <tr>
    <td class="tg-0pky">wrapt</td>
    <td class="tg-0pky">1.12.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">wxPython</td>
    <td class="tg-0pky">4.1.1</td>
  </tr>
  <tr>
    <td class="tg-0pky">yapf</td>
    <td class="tg-0pky">0.31.0</td>
  </tr>
  <tr>
    <td class="tg-0pky">zipp</td>
    <td class="tg-0pky">3.6.0</td>
  </tr>
</tbody>
</table>
