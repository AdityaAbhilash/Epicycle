# 🌀 Epicycle Drawing from SVG Paths

Generate mesmerizing epicycle animations from SVG images using Discrete Fourier Transform (DFT). This project converts vector paths into continuous one-line epicycle drawings, inspired by Fourier Series visualization.

---

## 📚 Table of Contents

- [🎯 Overview](#-overview)
- [🧠 Theory](#-theory)
- [✨ Features](#-features)
- [🛠️ Requirements](#️-requirements)

---

## 🎯 Overview

This project visualizes SVG drawings using rotating vectors, called epicycles, based on their Fourier coefficients. It supports multi-path SVGs and animates each disjoint curve simultaneously. This technique bridges signal processing with artistic visualization.

---

## 🧠 Theory

Fourier Series allows us to represent any periodic signal as a sum of sinusoids. In our case, we treat an SVG path as a complex signal:

- A point (x, y) is represented as z = x + iy.
- The full path becomes a list of complex numbers sampled over time.
- Using the Discrete Fourier Transform (DFT), we obtain frequency-domain coefficients.
- Each coefficient corresponds to a rotating vector (epicycle).
- By drawing these epicycles over time, we reconstruct the original path dynamically.

This method captures both the frequency and phase information of the signal, making it ideal for smooth and accurate path reconstructions.

---

## ✨ Features

- 🔁 Multi-path SVG support (disjoint continuous paths).
- 📈 Fourier Coefficient computation using NumPy FFT.
- 🌀 Animated epicycle visualization using matplotlib.
- 🧹 Optional path smoothing and simplification.
- ✍️ SVG tracing from hand-drawn sketches (optional Kivy interface).
- 🎥 Save animations as MP4 or GIF.

---

## 🛠️ Requirements

Ensure you have Python 3.7+ installed.

Install the required dependencies with:

```bash
pip install numpy matplotlib svgpathtools

### 🔄 Boy Example

![Boy Animation](https://github.com/AdityaAbhilash/Epicycle/blob/main/Examples/boy_color/boy.gif)

🖼️ [boy.png](https://github.com/AdityaAbhilash/Epicycle/blob/main/Examples/boy_color/boy.png)
