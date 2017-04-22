from bs4 import BeautifulSoup
import requests

r = requests.get("http://python123.io/ws/demo.html")
soup = BeautifulSoup(demo, "html.parser")
