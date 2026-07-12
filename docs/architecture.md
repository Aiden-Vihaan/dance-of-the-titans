# System Architecture

## Overview

Dance of the Titans is a browser-based real-time visualization of a binary black hole merger built using Three.js and WebGL.

The application follows a modular architecture separating physics simulation, rendering, particle systems, user interface, and post-processing.

---

## Core Components

### Black Hole System

Responsible for:

- Binary orbital motion
- Event horizon positioning
- Merger detection
- Ringdown transition

---

### Particle System

Responsible for:

- Accretion disk particles
- Relativistic particle motion
- Particle lifetime
- Color evolution

---

### Rendering Engine

Built using:

- Three.js
- WebGL
- EffectComposer
- Bloom
- Depth of Field
- Tone Mapping

---

### UI

Interactive observatory controls allow users to modify simulation parameters in real time.

---

## Rendering Pipeline

Scene

↓

Physics Update

↓

Particle Update

↓

Post Processing

↓

Bloom

↓

Tone Mapping

↓

Screen
