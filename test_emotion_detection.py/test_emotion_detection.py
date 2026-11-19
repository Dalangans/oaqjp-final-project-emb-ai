"""Unit tests for the packaged emotion detector."""

import unittest
from unittest.mock import Mock, patch

from Final_project import emotion_detector


class EmotionDetectorTests(unittest.TestCase):
    """Check dominant emotions and the API error response."""

    def test_sample_statements(self):
        """Verify the dominant emotion for the five lab examples."""
        samples = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear",
        }
        for statement, expected_emotion in samples.items():
            with self.subTest(statement=statement):
                result = emotion_detector(statement)
           test_emotion_detection.py     self.assertEqual(result["dominant_emotion"], expected_emotion)
                self.assertEqual(
                    set(result),
                    {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"},
                )

    @patch("Final_project.emotion_detector.requests.post")
    def test_bad_request_returns_empty_scores(self, post_request):
        """Return null emotion values when the service reports HTTP 400."""
        post_request.return_value = Mock(status_code=400)
        result = emotion_detector("")
        self.assertEqual(
            result,
            {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            },
        )


if __name__ == "__main__":
    unittest.main()
