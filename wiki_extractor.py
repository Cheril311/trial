import argparse
import wikipedia
import json
import wikipediaapi
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

wiki_wiki = wikipediaapi.Wikipedia('en')
 
 
# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("--keyword", help = "Enter the search keyword")
parser.add_argument("--num_urls", help = "Enter the search keyword")
parser.add_argument("--output", help = "Enter the search keyword")

args = parser.parse_args()

num_urls = int(args.num_urls)

search_results = wikipedia.search(args.keyword, results = (num_urls))

dicti = {}
results = []
text = ''
st = ''
for i in search_results:
    
      page_py = wiki_wiki.page(i)
      source = urlopen(page_py.fullurl).read() 
      soup = BeautifulSoup(source,'lxml')
      for paragraph in soup.find_all('p'):
        text += paragraph.text
      for j in text[1:]:
       if j.startswith("\n"):
        break
       else:
        st += j
      st = re.sub(r'\[.*?\]+', '', st)
      st = st.replace('\n', '')
      st = st.replace(u'\xa0', u' ')
      dicti['url'] = page_py.fullurl
      dicti['paragraph'] = st
      results.append(dicti)        
      text = ''
      st = ''
      dicti ={}
    


with open(args.output, 'w') as outfile:
    json.dump(results, outfile)
