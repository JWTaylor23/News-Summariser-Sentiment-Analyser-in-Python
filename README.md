# News Summariser & Sentiment Analyser in Python  

This project demonstrates how to automatically **summarise online news articles** and perform **sentiment analysis** on their content. It uses the `newspaper3k` library for article extraction and summarisation, `TextBlob` for sentiment analysis, and provides a **Tkinter-based graphical interface** for ease of use.  

###Project Structure  

News_Summariser_Sentiment/

├── main.py                 
├── README.md             
└── (optional) venv/     

### Features  

- Loads and processes articles directly from a given **URL**  
- Extracts:  
  - Title  
  - Author(s)  
  - Publication Date  
  - Summary  
- Performs **sentiment analysis** with polarity scoring (Positive, Negative, Neutral)  
- Provides a **desktop GUI** for interaction  
- Includes error handling for invalid or inaccessible articles  

### AI & NLP Overview  

The project applies **Natural Language Processing** techniques for summarisation and sentiment classification.  

**Application Key Concepts:**  
- **Article Parsing:** The `newspaper3k` library downloads and parses articles from the web.  
- **Summarisation:** Extractive summarisation condenses article content into key points.  
- **Sentiment Analysis:** `TextBlob` evaluates the polarity of text and classifies sentiment.  
- **GUI:** A Tkinter interface allows users to input URLs and view results in a structured layout.  

### Why This Approach?  

The use of **pre-built NLP tools** such as `newspaper3k` and `TextBlob` provides a quick yet effective demonstration of applied NLP. It shows how text can be automatically extracted, summarised, and analysed, with results presented to the user in a clear format. 

### Running the Application  

1. Install the dependencies: pip install newspaper3k textblob
3. Run the applications: python summariser.py
4. Enter the URL of a news article into the application’s input field and click **Summarise**

### Future Improvements

- Replace TextBlob with more advanced models such as VADER or transformer-based classifiers.
- Enhance summarisation using BART or T5 from Hugging Face.
- Add keyword extraction and data visualisations (e.g. word clouds).
- Deploy as a web application with Streamlit or Flask.

### Licence

This project is licensed under the MIT Licence.

### Author

Joshua Taylor
taylor.jw21@hotmail.com

Feel free to reach out for collaboration or feedback!


