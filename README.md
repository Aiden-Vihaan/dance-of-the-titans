# 🌌 Dance of the Titans

> **An interactive cinematic simulation of a Binary Black Hole Merger built with Python and Taichi.**

## Overview

Dance of the Titans is a real-time physics simulation that visualizes two black holes orbiting each other, gradually spiraling inward, and merging into a single rotating black hole. The project combines scientifically inspired gravitational dynamics with cinematic particle rendering to create an engaging educational experience.

Built for **Simathon 2026**, this project demonstrates how complex astrophysical phenomena can be explored through interactive simulations.

---

## Features

- 🌌 Binary Black Hole orbital dynamics
- ⚫ Dual event horizons with glowing accretion disks
- ✨ Real-time particle simulation
- 🌠 Temperature-based particle coloring
- 🌊 Gravitational-wave inspired merger visualization
- 🎮 Interactive controls for simulation parameters
- 🚀 Smooth real-time rendering powered by Taichi
- 📚 Educational visualization of black hole physics

---

## Physics

The simulation is inspired by real astrophysical concepts, including:

- Newtonian gravitational attraction
- Orbital mechanics
- Accretion disk dynamics
- Event horizons
- Particle motion around compact massive objects
- Gravitational-wave inspired merger effects

Some visual effects are artistic approximations designed to improve understanding while maintaining scientific integrity.

---

## Controls

| Key | Action |
|------|--------|
| Space | Pause / Resume simulation |
| R | Reset simulation |
| + / - | Increase or decrease simulation speed |
| Mouse | Interact with particles *(planned)* |

---

## Technologies

- Python 3.12
- Taichi
- NumPy
- Git
- GitHub

---

## Project Structure

```
dance-of-the-titans/
│
├── sim.py
├── README.md
├── requirements.txt
├── assets/
├── screenshots/
└── video/
```

---

## Getting Started

Clone the repository

```bash
git clone https://github.com/Aiden-Vihaan/dance-of-the-titans.git
```

Install dependencies

```bash
pip install taichi numpy
```

Run the simulation

```bash
python sim.py
```

If using Python 3.13 or later:

```bash
uv run --python 3.12 --with taichi sim.py
```

---

## Screenshots

*Screenshots will be added after development.*

---

## Demo Video

*A demonstration video will be added before the final submission.*

---

## Future Improvements

- Advanced gravitational lensing
- Kerr black hole approximation
- Improved relativistic effects
- Multiple camera modes
- Educational information overlay
- Performance optimizations

---

## License

This project is licensed under the MIT License.

---

## Author

**Aiden Vihaan**

Built for **Simathon 2026** with the goal of making astrophysics more interactive, immersive, and accessible.
