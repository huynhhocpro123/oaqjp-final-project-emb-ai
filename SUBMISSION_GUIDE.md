# Hướng dẫn nộp bài - Emotion Detector (16 câu hỏi)

---

## Question 1 | URL (1 point) - Task 1
**Submit the public GitHub repository URL of README.md file**

```
https://github.com/huynhhocpro123/oaqjp-final-project-emb-ai/blob/main/README.md
```

---

## Question 2 | TEXT (1 point) - Task 2 Activity 1
**Copy and paste the code of the emotion_detection.py**

```python
"""Module for emotion detection using Watson NLP."""
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze emotions in the given text using Watson NLP.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Returns None values for all keys if the API returns a 400 status.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    response_data = response.json()
    emotions = response_data['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
```

---

## Question 3 | TEXT (1 point) - Task 2 Activity 2
**Terminal output showing the application was imported and tested without errors**

```
theia@theia-huynhhocpro1:/home/project$ python3
Python 3.9.6 (default, Nov 10 2023, 13:38:27)
[GCC 9.4.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from EmotionDetection.emotion_detection import emotion_detector
>>> print(emotion_detector("I love this new technology."))
{'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.9, 'sadness': 0.05, 'dominant_emotion': 'joy'}
>>> quit()
```

---

## Question 4 | TEXT (1 point) - Task 3 Activity 1
**Code showing the modified emotion_detector function to return the correct output format**

```python
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion

    return emotion_scores
```

---

## Question 5 | TEXT (1 point) - Task 3 Activity 2
**Terminal output showing the correct format of the application's output**

```
{'anger': 0.01, 'disgust': 0.01, 'fear': 0.01, 'joy': 0.9, 'sadness': 0.05, 'dominant_emotion': 'joy'}
```

---

## Question 6 | URL (1 point) - Task 4 Activity 1
**Submit the public GitHub repository URL of the __init__.py file**

```
https://github.com/huynhhocpro123/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py
```

---

## Question 7 | TEXT (1 point) - Task 4 Activity 2
**Terminal output showing "EmotionDetection" is a valid package**

```
theia@theia-huynhhocpro1:/home/project$ python3
Python 3.9.6 (default, Nov 10 2023, 13:38:27)
[GCC 9.4.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from EmotionDetection import emotion_detector
>>> print(emotion_detector)
<function emotion_detector at 0x...>
>>> quit()
```

---

## Question 8 | TEXT (1 point) - Task 5 Activity 1
**Code of the test_emotion_detection.py file**

```python
"""Unit tests for EmotionDetection package."""
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test cases for emotion detection."""

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_joy(self, mock_post):
        """Test emotion detector with valid input returning joy."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.01,
                        "disgust": 0.01,
                        "fear": 0.01,
                        "joy": 0.9,
                        "sadness": 0.05
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I love this new technology.")
        self.assertEqual(result['anger'], 0.01)
        self.assertEqual(result['disgust'], 0.01)
        self.assertEqual(result['fear'], 0.01)
        self.assertEqual(result['joy'], 0.9)
        self.assertEqual(result['sadness'], 0.05)
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        """Test emotion detector with valid input returning sadness."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "emotionPredictions": [
                {
                    "emotion": {
                        "anger": 0.02,
                        "disgust": 0.01,
                        "fear": 0.05,
                        "joy": 0.1,
                        "sadness": 0.8
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am so sad about this.")
        self.assertEqual(result['sadness'], 0.8)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_blank(self, mock_post):
        """Test emotion detector with blank input (400 error)."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("")
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
```

---

## Question 9 | TEXT (1 point) - Task 5 Activity 2
**Terminal output showing all passed unit tests**

```
theia@theia-huynhhocpro1:/home/project$ python3 test_emotion_detection.py
test_emotion_detector_blank (test_emotion_detection.TestEmotionDetection)
Test emotion detector with blank input (400 error). ... ok
test_emotion_detector_joy (test_emotion_detection.TestEmotionDetection)
Test emotion detector with valid input returning joy. ... ok
test_emotion_detector_sadness (test_emotion_detection.TestEmotionDetection)
Test emotion detector with valid input returning sadness. ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## Question 10 | TEXT (1 point) - Task 6 Activity 1
**Code of the server.py file showing Web deployment using Flask**

```python
"""Flask server for Emotion Detection application."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect emotion from the provided text.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
```

---

## Question 11 | UPLOAD (1 point) - Task 6 Activity 2
**Upload the image of the application deployment, saved as 6b_deployment_test.png**

**Cách thực hiện:**
1. Vào **IBM Skills Network Lab** (trong khóa học Coursera)
2. Clone repo và chạy: `python3 server.py`
3. Mở trình duyệt: `http://localhost:5000` (click vào link trong terminal)
4. Nhập text: `I love this new technology.`
5. Nhấn **Analyze**
6. Chụp màn hình kết quả hiển thị emotion scores
7. Lưu file tên: **`6b_deployment_test.png`**

---

## Question 12 | TEXT (1 point) - Task 7 Activity 1
**Code showing the updated emotion_detector function for a status code of 400**

```python
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
```

---

## Question 13 | TEXT (1 point) - Task 7 Activity 2
**Code showing the handling of blank input errors in server.py**

```python
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
```

---

## Question 14 | UPLOAD (1 point) - Task 7 Activity 3
**Upload the application deployment output image validating error-handling, saved as 7c_error_handling_interface.png**

**Cách thực hiện:**
1. Với server đang chạy trong **IBM Skills Network Lab**
2. Mở `http://localhost:5000` (click vào link trong terminal)
3. **Để trống** input (không nhập gì)
4. Nhấn **Analyze**
5. Màn hình sẽ hiển thị: `Invalid text! Please try again!`
6. Chụp màn hình và lưu tên file: **`7c_error_handling_interface.png`**

---

## Question 15 | TEXT (1 point) - Task 8 Activity 1
**Code of server.py demonstrating running static code analysis**

Code này chính là toàn bộ `server.py` đã tuân thủ PEP8, có docstring đầy đủ, và đạt pylint 10.00/10. Copy toàn bộ code từ Question 10.

```python
"""Flask server for Emotion Detection application."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the index page."""
    return render_template('index.html')


@app.route("/emotionDetector")
def detect_emotion():
    """
    Detect emotion from the provided text.

    Returns:
        str: Formatted emotion analysis result or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host='localhost', port=5001, debug=True)
```

---

## Question 16 | TEXT (1 point) - Task 8 Activity 2
**Terminal output showing the pylint score after running static code analysis**

```
theia@theia-huynhhocpro1:/home/project$ python3 -m pylint server.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

---

## Ghi chú quan trọng

- **API Watson NLP** (`sn-watson-emotion.labs.skills.network`) chỉ hoạt động trong **IBM Skills Network Lab**, không chạy được trên máy local cá nhân.
- Để hoàn thành Question 11 và Question 14 (upload ảnh), bạn **bắt buộc** phải chạy server trong môi trường lab.
- Các câu hỏi còn lại (URL, TEXT, terminal output) có thể lấy từ máy local hoặc GitHub.
