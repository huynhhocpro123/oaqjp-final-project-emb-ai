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
