
import json
import unittest
from unittest.mock import MagicMock, patch

import handler


class TestLambdaHandler(unittest.TestCase):

    @patch.dict("os.environ", {"SNS_TOPIC_ARN": "arn:aws:sns:us-east-1:123456789012:test-topic"})
    @patch.object(handler.sns, "publish")
    def test_alarm_notification(self, mock_publish):
        mock_publish.return_value = {"MessageId": "test-message-123"}

        event = {
            "AlarmName": "High-CPU-Usage",
            "NewStateValue": "ALARM",
            "NewStateReason": "CPU utilization exceeded threshold"
        }

        response = handler.lambda_handler(event, None)

        self.assertEqual(response["statusCode"], 200)
        self.assertEqual(
            json.loads(response["body"])["state"],
            "ALARM"
        )
        mock_publish.assert_called_once()

    @patch.dict("os.environ", {}, clear=True)
    def test_missing_sns_topic(self):
        event = {"AlarmName": "TestAlarm"}

        with self.assertRaises(ValueError):
            handler.lambda_handler(event, None)


if __name__ == "__main__":
    unittest.main()
