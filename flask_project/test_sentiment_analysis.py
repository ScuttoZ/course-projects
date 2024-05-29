from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

POSITIVE_LABEL = 'SENT_POSITIVE'
NEGATIVE_LABEL = 'SENT_NEGATIVE'
NEUTRAL_LABEL = 'SENT_NEUTRAL'

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        resp_1 = sentiment_analyzer('I love using this thing')
        self.assertEqual(resp_1['label'], POSITIVE_LABEL)
        resp_2 = sentiment_analyzer('I''m really hating this thing')
        self.assertEqual(resp_2['label'], NEGATIVE_LABEL)
        resp_3 = sentiment_analyzer('I am neutral about this thing')
        self.assertEqual(resp_3['label'], NEUTRAL_LABEL)

unittest.main()

