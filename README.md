
#  HandTalk Project 🤟

A **real-time sign language translator** using **ESP32-CAM**  and **Computer Vision**. 
This project captures hand gestures through an ESP32-CAM and processes them using computer vision algorithms on a Python-based server. It translates recognized gestures into readable text and can even convert them into speech for better accessibility. HandTalk aims to bridge communication gaps for the hearing and speech impaired, offering an affordable and scalable solution.

## 🔧 Prerequisites

Make sure you have the following installed and ready:

-   Python 3.8+
    
-   Arduino IDE
    
-   ESP32-CAM board with FTDI module
    

----------

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/HandTalk.git
cd HandTalk

```

----------

### 2️⃣ Update IP Configuration

**Step 1:** Find your local IP address

-   🪟 Windows:
    
    ```bash
    ipconfig
    
    ```
    
    _(Look for IPv4 Address)_
    
-   🍎 Linux/Mac:
    
    ```bash
    ifconfig
    
    ```
    
    _(Look for inet)_
    

**Step 2:** Replace the default IP `192.168.40.200` with your **local IP** using **Find & Replace** in VS Code 🔍

----------

### 3️⃣ Arduino IDE Setup

1.  Open Arduino IDE
    
2.  Install ESP32-CAM libraries and open **CameraWebServer** from examples
    
3.  Navigate to your project directory in VS Code:
    
    ```bash
    Programs/Camera Webserver/
    
    ```
    
4.  Replace the following files with project-specific versions:
    
    -   `CameraWebServer.ino` → `main.ino`
        
    -   `camera_pins.h`
        
    -   `camera_index.h`
        
    -   `app_httpd.cpp`
        

----------

### 4️⃣ Python Virtual Environment

Set up a virtual environment for Python dependencies:

```bash
python -m venv handtalk-env

# 🪟 Windows:
handtalk-env\Scripts\activate

# 🐧 Linux/Mac:
source handtalk-env/bin/activate

pip install -r requirements.txt

```

----------

### 5️⃣ Update File Paths 

Change project paths to match your system:

```python
# From this:
BASE_DIR = "/path/to/remote/HandTalk"

# To your local path:
BASE_DIR = "C:/Users/yourname/HandTalk"

```

----------

## ▶️ Usage

1.  **Upload** Arduino sketch to ESP32-CAM
    
2.  **Start Python server**:
    
    ```bash
    python -u "{your_directory}/HandTalk/Programs/Main/main.py"
    
    ```
    
3.  **Open browser** and go to:
    
    ```
    http://{your_replaced_local_ip}
    
    ```
