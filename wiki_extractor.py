import argparse
import wikipedia
import json
 
 
# Initialize parser
parser = argparse.ArgumentParser()

parser.add_argument("--keyword", help = "Enter the search keyword")
parser.add_argument("--num_urls", help = "Enter the search keyword")
parser.add_argument("--output", help = "Enter the search keyword")

args = parser.parse_args()

num_urls = int(args.num_urls)

search_results = wikipedia.search(args.keyword, results = (num_urls + (num_urls//2)))

dicti = {}
results = []
st = ''
for i in search_results:
    
    try:
      text = wikipedia.page(i).content
      for j in text:
       if j.startswith("\n"):
        break
       else:
        st += j
      dicti['url'] = wikipedia.page(i).url
      dicti['paragraph'] = st
      results.append(dicti)
    except :
        continue
    text = ''
    st = ''
    dicti ={}
    
results = results[:num_urls]

with open(args.output, 'w') as outfile:
    json.dump(results, outfile)