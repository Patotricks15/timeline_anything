from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd


class DateAdjuster:
    def __init__(self, model_name="gpt-4o-mini"):
        self.model = ChatOpenAI(model=model_name, temperature=0)
        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are an expert in historical dates. "
                "If the date refers to a distant past event (e.g., BC or prehistoric), ensure the format is correct. "
                "If no specific day and month are available, return only the year."
                "If a date has day 01 and month 01, return just the year."
                "If there's no data return 'Without year information'.",
            ),
            (
                "human",
                """The current date is {date}.
                Description: {description}.
                Evidence: {evidence}.
                
                What is the correct format of this date? Return the corrected date in ISO format or as a year only."""
            ),
        ])

    def adjust_dates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Adjust the dates in the DataFrame using the LLM."""
        def adjust_date(row):
            prompt = self.prompt.format_messages(
                date=row["date"],
                description=row["description"],
                evidence=row["evidence"]
            )
            response = self.model(prompt)
            return response.content.strip()

        df["date"] = df.apply(adjust_date, axis=1)
        df = df.sort_values(by="date", ascending=True)
        df['date'] = df['date'].apply(lambda x: x.replace("-01-01",""))
        return df
