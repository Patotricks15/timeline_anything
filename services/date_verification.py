from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from services.utils import extract_date_from_text
import pandas as pd

class DateVerificationService:
    def __init__(self, model_name="gpt-3.5-turbo-1106", max_results=2):
        """Initialize the Tavily Agent."""
        self.model = ChatOpenAI(model=model_name)
        self.search = TavilySearchResults(max_results=max_results)
        self.agent_executor = create_react_agent(self.model, [self.search])

    def verify_date(self, description: str, date: str) -> str:
        """
        Verifies if the date is true. If false, returns the corrected date.
        :param description: The description of the event.
        :param date: The date to verify.
        :return: Corrected date (if necessary) or the original date.
        """
        query = f"Verify if the following statement is true or false: '{description} happened on {date}'. Provide the correct date if it is false."

        response = self.agent_executor.invoke(
            {
                "messages": [HumanMessage(content=query)]
            }
        )
        response_text = response['messages'][-1].content

        # If false, extract the corrected date; otherwise, keep the original
        if "false" in response_text.lower():
            corrected_date = extract_date_from_text(response_text)
            return corrected_date if corrected_date else date
        return date

    def verify_dates_in_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Applies date verification to a DataFrame.
        :param df: DataFrame with 'description' and 'date' columns.
        :return: Updated DataFrame with corrected dates.
        """
        def verify_row(row):
            return self.verify_date(row['description'], row['date'])

        df["date"] = df.apply(verify_row, axis=1)
        return df
