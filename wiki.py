import wikipediaapi
import time
from queue import Queue

user_agent = 'APCSP-Zalea (zaleay@gmail.com)'
wiki = wikipediaapi.Wikipedia(user_agent, 'en')

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    print(f'Working on finding {target_page}...')
    start_time = time.time()

    queue = Queue() # queue for items to check next
    visited = set() # keeps track of visited links
    parent = {}     # dictionary to keep track of parent page

    # add starting page to queue and visited
    queue.put(start_page.title)
    visited.add(start_page.title)

    # keep looping as long as queue is not empty
    while not queue.empty():
        # get next itme in our queue
        current_page_title = queue.get()

        if current_page_title == target_page.title:
            break

        # fetch all links at current page
        current_page = wiki.page(current_page_title)
        links = fetch_links(current_page)

        # go through each of the links and add them to queue
        for link in links:
            # if page hasn't already been visited
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link] = current_page_title

    # reconstruct path from target page to start page
    path = []
    page_title = target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]
    
    path.append(start_page.title)
    path.reverse()

    end_time = time.time()
    print(f"This algorithm took {end_time - start_time} seconds.")
    return path

# start and end pages for our wikipedia game solver
start_page = wiki.page('DNA')
target_page = wiki.page('SARS-CoV-2')
path = wikipedia_game_solver(start_page, target_page)
print(path)