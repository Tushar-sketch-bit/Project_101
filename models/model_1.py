import ollama

# No API Key needed! It's running on your own PC.
response = ollama.chat(
    model='my-llama2',
 
    messages=[
        {
            'role': 'user',
            'content': 'List all methods that are used in data analysis and data science and a must know for a beginner from numpy, pandas, matplotlib, scikit-learn, libraries that is used in data analysis and data science.'
        }
    ],
)

print(response['message']['content'])


#import ollama
#import requests
#from bs4 import BeautifulSoup

# Step 1: Use Python to fetch the text from a URL
#url = ""
#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'html.parser')
#book_text = soup.get_text()[:5000] # Grabbing the first 5000 characters (context limit)

# Step 2: Pass that text to your local model
#prompt = f"Summarize the following text from this book: {book_text}"

#output = ollama.chat(model='my-llama', messages=[{'role': 'user', 'content': prompt}])
#print(output['message']['content'])


