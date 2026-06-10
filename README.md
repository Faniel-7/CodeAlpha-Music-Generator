# 🎵 AI Music Generator

An AI-powered music generation project that learns patterns from MIDI files and creates new musical compositions using LSTM neural networks.

-------------------------------------------

## 📖 Table of Contents

- 🎯 [About The Project](#about-the-project)
- 🛠 [Built With](#built-with)
- 📂 [Project Structure](#project-structure)
- 🚀 [Getting Started](#getting-started)
- ⚙️ [Installation](#installation)
- 🎵 [Usage](#usage)
- 📊 [Results](#results)
- 🗺 [Roadmap](#roadmap)
- 🤝 [Contributing](#contributing)
- 📬 [Contact](#contact)

-------------------------------------------

## 🎯 About The Project

This project uses Deep Learning and LSTM networks to learn musical patterns from MIDI files and generate original music.

### Features

- Extract notes from MIDI files
- Preprocess music data
- Train LSTM neural networks
- Generate new MIDI music
- Save generated songs automatically
- Customizable music generation length

-------------------------------------------

## 🛠 Built With

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Music21](https://img.shields.io/badge/Music21-FF6B35?style=for-the-badge&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

-------------------------------------------

## 📂 Project Structure

```
Music-Generator/
│
├── data/
│   ├── midi/
│   ├── notes.pkl
│   └── sequences.pkl
│
├── models/
│   ├── music_model.keras
│   └── best_model.keras
│
├── output/
│   └── generated_song1.mid
│
├── read_midi.py
├── preprocess.py
├── prepare_sequences.py
├── model.py
├── train.py
├── generate.py
├── requirements.txt
└── README.md
```

-------------------------------------------

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/Faniel-7/Music-Generator.git
cd Music-Generator
```

-------------------------------------------

## ⚙️ Installation

Create virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

-------------------------------------------

## 🎵 Usage

Extract notes:

```bash
python read_midi.py
```

Preprocess data:

```bash
python preprocess.py
```

Prepare sequences:

```bash
python prepare_sequences.py
```

Train model:

```bash
python train.py
```

Generate music:

```bash
python generate.py
```

-------------------------------------------

## 📊 Results

The model learns patterns from MIDI music and generates new musical sequences saved as:

```
output/generated_song1.mid
output/generated_song2.mid
output/generated_song3.mid
```

-------------------------------------------

## 🗺 Roadmap

- [x] Collect MIDI dataset
- [x] Extract notes
- [x] Preprocess data
- [x] Train LSTM model
- [x] Generate MIDI music
- [ ] Improve music quality
- [ ] Add web interface
- [ ] Add multiple instruments
- [ ] Export to WAV/MP3

-------------------------------------------

## 🤝 Contributing

Contributions are welcome.

Fork the project and submit a pull request.



## 📬 Contact

GitHub:
https://github.com/Faniel-7

LinkedIn:

## ⭐ Support

If you found this project useful, give it a star on GitHub.
