from goose3 import Goose


class WikipediaService:
    @staticmethod
    def fetch_content(topic: str) -> str:
        """Fetch cleaned text content from a Wikipedia page."""
        g = Goose()
        url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
        article = g.extract(url)
        return article.cleaned_text
