# Webscraper AI

A web scraper and content parser built with Python, Selenium, Langchain, and Streamlit. This tool allows users to extract specific information from web pages by describing the data they want.

## Features

- **Web Scraping**: Uses Selenium to load the page and retrieve the full HTML content.
- **Content Extraction**: Cleans and extracts readable content from the web page (removes scripts, styles, etc.).
- **Chunking**: Large text bodies are split into smaller chunks for more efficient processing.
- **Content Parsing**: Uses Langchain's integration with Ollama to parse the content based on user-defined prompts and extract the required information.
- **Streamlit UI**: Provides an interactive and user-friendly interface to input URLs and define parsing requirements.

---

## Tech Stack

- **Python**: Main programming language.
- **Selenium**: Web scraping and browser automation.
- **Langchain**: For building the language model-driven prompt chain for parsing.
- **Streamlit**: For building the web-based user interface.
- **BeautifulSoup**: For cleaning and extracting data from HTML.

---

## Setup

### Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.7 or later**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package installer (comes with Python by default).
- **Google Chrome**: Install the latest version of Chrome from [Google Chrome](https://www.google.com/chrome/).
- **chromedriver**: WebDriver for Chrome (ensure it matches your installed version of Chrome).

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   Open your terminal or command prompt and clone the repository to your local machine:
   ```bash
   git clone https://github.com/Lokeshzz7/webscraper_ai.git
   cd webscraper_ai

2. **Create a virtual environment**:
    In your terminal, create a virtual environment named venv (or any other name you prefer):
    python -m venv venv
    Activate the virtual environment:

    On Windows:

    venv\Scripts\activate

    On MacOS/Linux:

    source venv/bin/activate

3. **Installing Dependencies**:
    
    pip install -r requirements.txt
    
    Make sure the requirements.txt file in your repository contains the necessary dependencies. You can manually create it if it doesn't exist. Example requirements.txt:

    streamlit 
    langchain 
    langchain_ollama
    selenium
    beautifulsoup4
    lxml 
    html5lib
    python-dotenv

4. **Downloading Chromedriver**
    The chromedriver is necessary for Selenium to interact with Google Chrome.
    
    Download Chromedriver:
    Visit the Chromedriver download page and select the version that matches your Google Chrome version.
    
    Place Chromedriver:
    After downloading, place the chromedriver executable in the root of your project directory (where app.py is located). Alternatively, you can update the path in your code to point to wherever you've saved it.

5. **Run the Streamlit app**:

    streamlit run main.py
