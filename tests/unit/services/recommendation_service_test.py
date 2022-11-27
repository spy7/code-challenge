from unittest import TestCase
from pandas import DataFrame

from code_challenge.services.recommendation_service import (
    RecommendationService,
)


class RecommendationServiceTestCase(TestCase):
    sample_data = {
        "date": ["2022-11-05", "2022-11-05", "2022-11-05", "2022-11-08"],
        "toGrade": ["Buy", "Strong Buy", "Negative", "Positive"],
    }

    def test_get_scalar(self):
        recommendationService = RecommendationService()
        self.assertEqual(1, recommendationService.get_scalar("Buy"))
        self.assertEqual(0, recommendationService.get_scalar("Neutral"))
        self.assertEqual(1.5, recommendationService.get_scalar("Strong Buy"))
        self.assertEqual(-1, recommendationService.get_scalar("Sell"))
        self.assertEqual(-1.5, recommendationService.get_scalar("Strong Sell"))
        self.assertEqual(1, recommendationService.get_scalar("Positive"))
        self.assertEqual(-1, recommendationService.get_scalar("Negative"))
        self.assertEqual(0, recommendationService.get_scalar("Other"))

    def test_add_scalar_to_dataframe(self):
        df = DataFrame(data=self.sample_data)
        df = RecommendationService().add_scalar_to_dataframe(df)
        self.assertEqual([1.0, 1.5, -1.0, 1.0], list(df["scalar"]))

    def test_transform_average(self):
        df = DataFrame(data=self.sample_data)
        df = RecommendationService().transform_scalar_to_average(df)
        self.assertEqual([0.5, 1.0], list(df["average"]))
