# https://stackskills.com/courses/102831/lectures/1499455

from bs4 import BeautifulSoup
import requests

search = input("Search for:")
params = {"q": search}
r = requests.get('https://www.bing.com/search', params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class" :"b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print("    ", item_href)
        # print("Parent:", item.find("a").parent)
        print("    ", item.find("a").parent.parent.find("p").text)
        print("")
        # for child in item.children:
        #     print("Child:", child)
        # h2 = item.find("h2")
        # print("Next sibling of h2:", h2.next_sibling)