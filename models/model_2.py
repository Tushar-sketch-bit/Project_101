import requests
from bs4 import BeautifulSoup
import ollama

# Step 1: Download the webpage content
url = "https://medium.com/@jalufirdausi/the-quotes-from-the-things-you-can-see-only-when-you-slow-down-book-6a10bd241535"
response = requests.get(url)

# Step 2: Parse the HTML to get only the article text
soup = BeautifulSoup(response.text, 'html.parser')
# Medium usually keeps the main article content in <p> (paragraph) tags
paragraphs = soup.find_all('p')
article_text = "\n".join([p.get_text() for p in paragraphs])

# Step 3: Send it to your local Llama model
prompt = f"""
I am providing a list of quotes from a book. 
Please summarize the core philosophy of this book in 3 main points:
{article_text[:4000]} # Limit to 4k chars to stay safe with your 8GB RAM
"""

output = ollama.chat(model='my-llama', messages=[{'role': 'user', 'content': prompt}])
print(output['message']['content'])
