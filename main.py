import tkinter as tk
from textblob import TextBlob
from newspaper import Article


def summarise():
    url = utext.get('1.0', "end").strip()

    if not url:
        return  # Do nothing if URL is empty

    article = Article(url)

    try:
        article.download()
        article.parse()
        article.nlp()
    except Exception as e:
        # Show error message
        title.config(state='normal')
        title.delete('1.0', 'end')
        title.insert('1.0', f"Error: {e}")
        title.config(state='disabled')
        return

    # Enable widgets for updating
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear previous content
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publication.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')

    # Insert new content
    title.insert('1.0', article.title)
    authors_text = ", ".join(article.authors) if article.authors else "N/A"
    author.insert('1.0', authors_text)
    pub_date = article.publish_date.strftime("%Y-%m-%d") if article.publish_date else "N/A"
    publication.insert('1.0', pub_date)
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment_text = (
        f'Polarity: {analysis.polarity:.2f}, '
        f'Sentiment: {"Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"}'
    )
    sentiment.insert('1.0', sentiment_text)

    # Disable widgets again
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


root = tk.Tk()
root.title('News Summariser')
root.geometry('1200x700')

# Title
tlabel = tk.Label(root, text="Title", font=("Arial", 12, "bold"))
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

# Author
alabel = tk.Label(root, text="Author(s)", font=("Arial", 12, "bold"))
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

# publication Date
plabel = tk.Label(root, text="Publishing Date", font=("Arial", 12, "bold"))
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

# Summary
slabel = tk.Label(root, text="Summary", font=("Arial", 12, "bold"))
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

# Sentiment Analysis
selabel = tk.Label(root, text="Sentiment Analysis", font=("Arial", 12, "bold"))
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

# URL input
ulabel = tk.Label(root, text="URL", font=("Arial", 12, "bold"))
ulabel.pack(pady=(10, 0))
utext = tk.Text(root, height=1, width=140)
utext.pack()

# Summarise button
btn = tk.Button(root, text="Summarise", command=summarise, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn.pack(pady=10)

root.mainloop()
