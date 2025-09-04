---

```markdown
# 🎮 Gesture-Based Game Controller

Control PC games like **Hill Climb Racing** using just your **hand gestures** ✋ with the help of a webcam.  
This project combines **Computer Vision** 🧠 and **Gesture Recognition** 📸 to simulate **keyboard arrow keys** for acceleration and braking.

---

## ✨ Features

- 🖐 **Open Palm (5 fingers)** → Accelerate (Right Arrow)
- ✊ **Closed Fist (0 fingers)** → Brake (Left Arrow)
- 🙌 Any other gesture → No control (keys released)
- 🎥 Real-time gesture detection via webcam
- ⚡ Instant key press simulation with no physical input
- 🖥 Works on PC games that support **Arrow Keys**

---

## 🛠 Tech Stack

- 🐍 **Python**
- 🎥 **OpenCV** – Frame capture & processing
- ✋ **MediaPipe** – Hand landmark detection
- 🔢 **NumPy** – Finger counting logic
- 🎮 **PyDirectInput** – Simulates key presses in games

---

## 📂 Project Structure

```

Gesture\_Game\_Controller/
│── gesture\_game\_controller.py   # Main script
│── venv/                        # Virtual environment (optional)
│── README.md                    # Documentation

````

---

## ⚙ How It Works

1. 🎥 **Hand Tracking**  
   Uses **MediaPipe** to detect hand landmarks in real time.

2. ✋ **Finger Counting**  
   - Counts raised fingers from landmarks.  
   - `5 fingers` → Accelerate.  
   - `0 fingers` → Brake.  

3. ⌨ **Key Simulation**  
   - `Right Arrow` pressed/released automatically for acceleration.  
   - `Left Arrow` pressed/released for braking.  

---

## 📥 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Gesture_Game_Controller.git
cd Gesture_Game_Controller
````

2. Install dependencies:

```bash
pip install opencv-python mediapipe numpy pydirectinput
```

3. Run the script:

```bash
python gesture_game_controller.py
```

---

## 🚀 Usage

* 🎥 Make sure your webcam is connected.
* ✋ Show your hand clearly with good lighting.
* 🖐 Open palm (5 fingers) → **Accelerate**
* ✊ Closed fist (0 fingers) → **Brake**
* ❌ Press **ESC** to exit the program.

---

## 📸 Demo

![Gesture Accelerate](https://via.placeholder.com/600x300.png?text=Accelerate+Gesture)

![Gesture Brake](https://via.placeholder.com/600x300.png?text=Brake+Gesture)

---

## 🔮 Future Improvements

* 🎮 Support for more gestures (e.g., 2 fingers = gas + brake together).
* 🕹 Add mapping for other games (WASD, Space, etc.).
* ⚡ Gesture customization via config file.
* 🖐 Multi-hand support.

---

## 👤 Author

**Bhabani S Biswal** – Python & AI/ML Developer
📧 Email: [bhabanibiswalb17@gmail.com](mailto:bhabanibiswalb17@gmail.com)
🔗 GitHub: [Bhabani S Biswal](https://github.com/bhabanisbiswal)

---


