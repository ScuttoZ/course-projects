from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector_joy(self):
        resp = emotion_detector('I am glad this happened')
        self.assertEqual(resp['dominant_emotion'], 'joy')

    def test_emotion_detector_anger(self):
        resp = emotion_detector('I am really mad about this')
        self.assertEqual(resp['dominant_emotion'], 'anger')

    def test_emotion_detector_disgust(self):
        resp = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(resp['dominant_emotion'], 'disgust')

    def test_emotion_detector_sadness(self):
        resp = emotion_detector('I am so sad about this')
        self.assertEqual(resp['dominant_emotion'], 'sadness')

    def test_emotion_detector_fear(self):
        resp = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(resp['dominant_emotion'], 'fear')

unittest.main()