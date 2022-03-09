# This project is still a work in progress and might change repeatedly and may not yet be stable or not run at all in some places.

# SMART MIRROR

This is a brief description of how to install and assemble the Smart Mirror. All the hardware parts I need or use are listed in the first step under <a href="#Hardware">Hardware</a>. the assembly is described afterwards under the same tab. Finally, under the <a href="#Software">Software</a> tab, the installation under Windows and Debian and Fedora Linux distributions is described. At the bottom of the document you will find finally used add-ons, previews and the people who worked on the project.

<br>

<div id="Hardware"><h2>Hardware</h2></div>

### Used hardware for testing and for general use:

 - [Mirror](#)
 - [Screen](#)
 - [RaspberryPI 4B 4GB](https://www.amazon.de/Raspberry-Pi-ARM-Cortex-A72-Bluetooth-Micro-HDMI/dp/B07TC2BK1X/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=146QJHPH6580P&dchild=1&keywords=raspberry%2Bpi%2B4%2B4gb&qid=1634766904&sprefix=rasp%2Caps%2C177&sr=8-3&th=1)
 - [Webcam](https://www.amazon.de/Logitech-C922-kostenloser-3-monatiger-XSplit-Lizenz/dp/B01L6L52K4/ref=sr_1_3?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=logitech+g922&qid=1634767096&sr=8-3)



### How to build the smart mirror:

!!! COMMING SOON !!!


<br>

<div id="Software"><h2>Software</h2></div>

### Used Python libraries:

 #### Voice Assistant
 - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
 - [requests](https://pypi.org/project/requests/)
 - [geocoder](https://pypi.org/project/geocoder/)
 - [pyttsx3](https://pypi.org/project/pyttsx3/)

 #### Face Recognition
 - [CMake](https://pypi.org/project/cmake/)
 - [face-recognition](https://pypi.org/project/face-recognition/)
 - [opencv-python](https://pypi.org/project/opencv-python/)
 - [numpy](https://pypi.org/project/numpy/)
 - [pygame](https://pypi.org/project/pygame/)

### Used Software:
 - [Raspbian](https://www.raspbian.org/)
 - [Python 3.10](https://www.python.org/downloads/)

### Installation

Clone the GitHub repository: 
```bash
  git clone https://github.com/rosenguard/smart-mirror.git
```

### Windows

Download the newest graphical installer of [CMake](https://cmake.org/download/) and run the "cmake-XXXXX-windows-x86_64.msi" file.

After that go into the cloned the GitHub repository open the command promt and install the requirements.txt file.

```bash
  pip3 install -r requirements.txt
```

Now you are able to run the ```main.py``` file so you can use the voice assistant, GUI on the screen and the face recognition.

``` bash
  python3 main.py
```

### Linux

Download the newest version of [CMake](https://cmake.org/download/):

#### On Debian:
```bash
  sudo apt install CMake
```

#### On Fedora:
```bash
  sudo dnf install cmake
```

Go into the cloned the GitHub repository open the command promt and install the requirements.txt file.

```bash
  pip3 install -r requirements.txt
```

Now you are able to run the ```main.py``` file so you can use the voice assistant, GUI on the screen and the face recognition.

``` bash
  python3 main.py
```

### Used tools:

[DeepL](https://www.deepl.com)



### A short preview:
!!! COMMING SOON !!!

## Authors

- [@justinrDEV](https://www.github.com/justinrDEV)
