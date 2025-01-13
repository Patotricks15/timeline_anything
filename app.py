import streamlit as st
from services.wikipedia import WikipediaService
from services.extractor import EventExtractor
from services.date_verification import DateVerificationService
from services.renderer import TimelineRenderer
from services.adjuster import DateAdjuster
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def main():
    st.title("Timeline Anything (Ai powered)")
    st.write("Enter a topic and view its historical timeline with verified dates.")

    # Input for the topic
    topic_input = st.text_input("Enter a topic:", "Colonial Brazil")
    verify_date = st.checkbox("Verify and correct dates using Tavily Search (it will increase the execution time)", value=False)

    if st.button("Generate Timeline"):
        with st.spinner("Fetching information..."):
            # Fetch text from Wikipedia
            wikipedia_service = WikipediaService()
            text = wikipedia_service.fetch_content(topic_input)

            # Extract historical events
            extractor = EventExtractor()
            events = extractor.extract_events(text)

            # Convert events to DataFrame
            data = [{"date": e.date, "description": e.description, "evidence": e.evidence} for e in events]
            df = pd.DataFrame(data)
            adjuster = DateAdjuster()
            df = adjuster.adjust_dates(df=df)
            
            if verify_date:
            # Automatically verify and correct dates
                with st.spinner("Verifying and correcting dates..."):
                    date_verification_service = DateVerificationService()
                    df = date_verification_service.verify_dates_in_dataframe(df)

            # Render HTML timeline
            renderer = TimelineRenderer()
            timeline_html = renderer.render_html(df)

            # Display timeline
            st.components.v1.html(timeline_html, height=800, scrolling=True)

            # Display table of events
            st.write("Historical Events Table:")
            st.dataframe(df)


if __name__ == "__main__":
    main()
