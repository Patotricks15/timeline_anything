# Timeline Anything

The **Timeline Anything** is an interactive Streamlit application that generates a historical timeline for any topic using data extracted from Wikipedia. The application is designed to help users understand the historical context and key events of any subject by presenting a visually appealing timeline.

---

## Features

- 📚 Extracts information from Wikipedia for any given topic.
- 🕰️ Automatically identifies key historical events and organizes them into a timeline.
- 🎨 Displays an interactive timeline with dates and descriptions of events.
- 💻 Fully containerized with Docker for ease of deployment.

---

## Getting Started

Follow these steps to set up and run the project locally or with Docker.

### Prerequisites

- **Python 3.9+**
- **Docker** (if running the application in a container)

---

### Running Locally

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/timeline_anything.git
cd timeline_anything
```

2. **Install dependencies:**

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```
3. **Run the application:**

Start the Streamlit app:

```bash
streamlit run app.py
```

4. **Access the application:**

Open your browser and go to:

http://localhost:8501

### Running with Docker

1. **Build the Docker image:**

```bash
docker build -t timeline_anything .
```

2. **Run the container:**

```bash
docker run -p 8501:8501 timeline_anything
```
3. **Access the application:**

Open your browser and go to: http://localhost:8501

4. **Usage:**
Enter a topic in the input field (e.g., "Colonial Brazil").


# Contributing
We welcome contributions to improve the Timeline Anything! Follow these steps to contribute:

Fork the repository on GitHub.

Clone your forked repository:

```bash
Copy code
git clone https://github.com/your-username/timeline_anything.git
```
Create a new branch for your feature or fix:

```bash
git checkout -b feature-name
```

Make your changes and ensure code quality:

Use consistent formatting.

Add comments for clarity.

Write or update tests if applicable.

Test your changes locally.

Commit and push your changes:

```bash
Copy code
git add .
git commit -m "Add feature: description"
git push origin feature-name
```
Open a pull request to the main repository and provide a clear description of your changes.

# Project Structure

```bash
timeline_anything/
│
├── app.py                     # Main Streamlit application
├── Dockerfile                 # Docker configuration
├── requirements.txt           # Python dependencies
├── LICENSE                    # MIT License file
├── services/                  # Service modules
│   ├── wikipedia.py           # Wikipedia extraction service
│   ├── extractor.py           # Event extraction service
│   ├── date_verification.py   # Date verification and correction
│   ├── renderer.py            # Timeline rendering service
│   └── utils.py               # Utility functions
└── models/                    # Models
    └── historical_event.py    # KeyDevelopment model
```
# License
This project is licensed under the MIT License. See the LICENSE file for details.


# Future Improvements
- Add support for other sources beyond Wikipedia.
- Enhance timeline visualization with more customization options.
- Optimize Tavily Search Agent integration for faster date verification.
- Add multi-language support for global users.

# Issues

If you encounter any issues or have questions, please open an issue in the GitHub repository.

