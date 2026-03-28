from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("your_API_KEY_HERE"))

def call_ai(prompt):
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content


def generate_code(prompt):
    return call_ai(f"Write clean Python code:\n{prompt}")


def debug_code(code):
    return call_ai(f"Debug this code:\n{code}")


def explain_code(code):
    return call_ai(f"Explain this code simply:\n{code}")


def optimize_code(code):
    return call_ai(f"Optimize this code:\n{code}")

if __name__ == "__main__":
    print(generate_code("Write a Python program for binary search"))
def analyze_complexity(code):
    return call_ai(f"Analyze time and space complexity of this code:\n{code}")