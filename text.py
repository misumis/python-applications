from dotenv import load_dotenv
import os
import requests
load_dotenv()

ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}'
r = requests.get(url)
data = r.json()

print(data)

# Write a program that prints the first 10 numbers of the Fibonacci sequence.
# Fibonnaci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b
        
# do it recursively

def fibonacci_recursive(n, a=0, b=1):
    if n == 0:
        return
    print(a)
    fibonacci_recursive(n-1, b, a+b)