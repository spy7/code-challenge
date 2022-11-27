from typing import Dict

from pandas import DataFrame


class RecommendationService:
    grades: Dict = {
        "Buy": 1,
        "Neutral": 0,
        "Strong Buy": 1.5,
        "Sell": -1,
        "Strong Sell": -1.5,
        "Positive": 1,
        "Negative": -1,
        "Everything Else": 0,
    }

    def get_scalar(self, grade: str) -> float:
        if grade in self.grades:
            return self.grades[grade]
        return 0

    def add_scalar_to_dataframe(self, dataframe: DataFrame) -> DataFrame:
        df = dataframe.copy()
        df["scalar"] = df.apply(
            lambda row: self.get_scalar(row["toGrade"]), axis=1
        )
        return df

    def transform_scalar_to_average(self, dataframe: DataFrame) -> DataFrame:
        if dataframe.empty:
            return dataframe
        df = self.add_scalar_to_dataframe(dataframe)
        df = DataFrame(df.groupby("date", as_index=False)["scalar"].mean())
        df = df.rename(columns={"scalar": "average"})
        return df
