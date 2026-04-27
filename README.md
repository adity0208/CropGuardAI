# 🌾 CropGuardAI - Edge-Optimized Wildlife Detection

[![Model Size](https://img.shields.io/badge/Model%20Size-965%20KB-green)](https://github.com/adity0208/CropGuardAI)
[![Accuracy](https://img.shields.io/badge/Accuracy-89.5%25-brightgreen)](https://github.com/adity0208/CropGuardAI)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

## 📋 Overview
CropGuardAI is a lightweight deep learning model designed to detect and classify wildlife species in real-time on edge devices. Built with MobileNetV2 and optimized for deployment on Raspberry Pi, mobile phones, and microcontrollers.

**Detects 7 Classes:**
🦌 Boar | 🐄 Cow | 🐕 Dog | 🐘 Elephant | 👤 Human | 🐒 Monkey | 🦌 Nilgai

## 🎯 Key Features
- **Edge-Optimized:** 965 KB model size
- **High Accuracy:** 89.52% validation accuracy
- **Real-Time:** <100ms inference on Raspberry Pi 4
- **Cross-Platform:** Runs on Android, iOS, Raspberry Pi, ESP32
- **Low Power:** Suitable for battery-powered devices

## 📊 Performance

| Metric | Value |
|--------|-------|
| Architecture | MobileNetV2 (α=0.35) |
| Input Size | 160×160×3 |
| Parameters | 492,647 total (82,439 trainable) |
| Model Size (FP16) | 965 KB |
| Validation Accuracy | 89.52% |
| Training Dataset | 525 images (7 classes) |

### Training Curves
![Training Curves](docs/training_curves.png)

### Confusion Matrix
![Confusion Matrix](docs/confusion_matrix.png)

## 🚀 Quick Start

### Prerequisites
```bash
pip install tflite-runtime numpy pillow
```
## 🌐 Live Demo

[![Open in Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Live%20Demo-blue)](https://huggingface.co/spaces/Adityakushwh/CropGuardAI)
[![Open in Colab](https://img.shields.io/badge/📓%20Colab-Training%20Notebook-orange)](https://colab.research.google.com/github/adity0208/CropGuardAI/blob/main/notebooks/cropguardai_training.ipynb)
