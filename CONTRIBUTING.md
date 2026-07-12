# Contributing to Dance of the Titans

First of all, thank you for considering contributing to **Dance of the Titans**.

This project was created as an interactive real-time visualization of a binary black hole merger using modern WebGL technologies. Contributions that improve the simulation, performance, documentation, accessibility, or user experience are always welcome.

---

## Ways to Contribute

You can contribute by:

- Improving rendering quality
- Optimizing performance
- Enhancing particle systems
- Improving gravitational lensing effects
- Adding new visualization modes
- Fixing bugs
- Improving documentation
- Improving accessibility
- Creating educational content
- Adding tests

---

## Getting Started

### 1. Fork the Repository

Click the **Fork** button on GitHub.

### 2. Clone Your Fork

```bash
git clone https://github.com/YOUR_USERNAME/dance-of-the-titans.git
```

### 3. Navigate into the Project

```bash
cd dance-of-the-titans
```

### 4. Start a Local Server

Python:

```bash
python3 -m http.server 8080
```

Open

```
http://localhost:8080
```

---

## Development Guidelines

Please keep the following principles in mind.

### Code Style

- Use meaningful variable names.
- Write modular JavaScript.
- Keep functions focused on one responsibility.
- Document non-obvious algorithms.
- Prefer readability over cleverness.

### Rendering

When modifying rendering:

- Maintain 60 FPS whenever possible.
- Avoid unnecessary allocations inside animation loops.
- Minimize shader complexity.
- Test on multiple browsers.

### Physics

Changes to the simulation should preserve physical plausibility whenever practical.

When introducing approximations:

- Document assumptions.
- Explain mathematical simplifications.
- Keep the visualization educational.

---

## Pull Request Process

Before opening a pull request:

- Test your changes.
- Ensure the application runs correctly.
- Update documentation if needed.
- Keep pull requests focused on a single improvement.
- Write a clear description of what changed.

---

## Reporting Bugs

Please include:

- Browser
- Operating System
- Device
- Steps to reproduce
- Expected behaviour
- Actual behaviour
- Screenshots if applicable

---

## Feature Requests

Feature requests are welcome.

Please describe:

- The problem you're trying to solve
- Your proposed solution
- Why it would improve the project

---

## Community Standards

Please be respectful and constructive.

Everyone is welcome regardless of experience level.

We value:

- Respect
- Collaboration
- Curiosity
- Scientific accuracy
- Helpful feedback

---

## License

By contributing to this repository, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping improve **Dance of the Titans**.
