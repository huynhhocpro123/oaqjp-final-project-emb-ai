# Final Project

## Emotion Detector

A web-based AI application that detects emotions in text using the Watson NLP library.

## Project Structure

- `EmotionDetection/`: Package containing the emotion detection module
  - `__init__.py`: Package initializer
  - `emotion_detection.py`: Core emotion detection logic using Watson NLP
- `templates/`: HTML templates for Flask
  - `index.html`: Main web interface
- `server.py`: Flask web application
- `test_emotion_detection.py`: Unit tests for the emotion detection module

## Setup

Install dependencies:
```bash
pip install flask requests
```

## Running the Application

```bash
python server.py
```

## Running Tests

```bash
python test_emotion_detection.py
```

## Running Static Code Analysis

```bash
pylint server.py
```
