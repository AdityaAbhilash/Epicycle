# Epicycle Drawing from SVG Paths

Generate mesmerizing epicycle animations from SVG images using Discrete Fourier Transform (DFT). This project converts vector paths into continuous one-line epicycle drawings, inspired by Fourier Series visualization.

---

## Table of Contents

- [Overview](#-overview)
- [Theory](#-theory)
- [Features](#-features)
- [🛠Requirements](#-requirements)
  - [Install Required Dependencies](#-install-required-dependencies)
- [Examples](#-examples)
  - [Boy Drawing Animation](#-boy-drawing-animation)
  - [More Examples](#-more-examples)

---

## Overview

This project visualizes SVG drawings using rotating vectors, called epicycles, based on their Fourier coefficients. It supports multi-path SVGs and animates each disjoint curve simultaneously. This technique bridges signal processing with artistic visualization.

---

## Theory

Fourier Series allows us to represent any periodic signal as a sum of sinusoids. In our case, we treat an SVG path as a complex signal:

- A point (x, y) is represented as z = x + iy.
- The full path becomes a list of complex numbers sampled over time.
- Using the Discrete Fourier Transform (DFT), we obtain frequency-domain coefficients.
- Each coefficient corresponds to a rotating vector (epicycle).
- By drawing these epicycles over time, we reconstruct the original path dynamically.

This method captures both the frequency and phase information of the signal, making it ideal for smooth and accurate path reconstructions.

---

## Features

- Multi-path SVG support (disjoint continuous paths).
- Fourier Coefficient computation using NumPy FFT.
- Animated epicycle visualization using matplotlib.
- Optional path smoothing and simplification.
- SVG tracing from hand-drawn sketches (optional Kivy interface).
- Save animations as MP4 or GIF.

---

## 🛠Requirements

Ensure you have **Python 3.7+** installed.

---

### Install Required Dependencies

Install all the necessary libraries using the following command:

```bash
pip install numpy matplotlib svgpathtools scipy opencv-python svgwrite

```

## Examples

### Boy Drawing Animation

**Original Sketch**  
![Boy Image](https://github.com/AdityaAbhilash/Epicycle/blob/main/Examples/boy_color/boy.png)

**Epicycle Animation**  
![Boy Animation](https://github.com/AdityaAbhilash/Epicycle/blob/main/Examples/boy_color/boy.gif)

---

### More Examples

Explore more SVG sketches and their animations in the **Examples** folder.

