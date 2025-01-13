from langchain_openai import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from models.historical_event import ExtractionData, KeyDevelopment
from typing import List
from langchain_core.documents import Document


class EventExtractor:
    def __init__(self, model_name="gpt-4o-mini"):
        self.model = ChatOpenAI(model=model_name, temperature=0)
        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are an expert at identifying key historic developments in text. "
                "Only extract important historic developments with specific dates or years."
            ),
            ("human", "{text}"),
        ])

    def extract_events(self, text: str) -> List[KeyDevelopment]:
        """Extract historical events from the given text."""
        document = Document(page_content=text)
        text_splitter = RecursiveCharacterTextSplitter()
        splits = text_splitter.split_documents([document])

        extractor = self.prompt | self.model.with_structured_output(
            schema=ExtractionData, include_raw=False
        )
        extractions = extractor.batch(
            [{"text": split.page_content} for split in splits],
            {"max_concurrency": 5},
        )

        key_developments = []
        for extraction in extractions:
            key_developments.extend(extraction.key_developments)
        return key_developments
