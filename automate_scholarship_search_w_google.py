import requests
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

API_KEY = "AIzaSyAKDKxZHwsIoaLYgHKTOzpwuuGoLJe95uw"
CX = "125fb75ba03064de8"
# queries = ["STEM scholarships", "Southern California scholarships", "scholarships for girls"]
queries = input("What do you want to search for? Separate separate queries by commas. \n").split(", ")
results_per_query = 30

scholarship_data = []

def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    scholarship_dicts = []

    if 'scholarships360' in url.lower():
        headings_with_a = soup.find_all(lambda tag: tag.name == "h4" and tag.find("a"))
        # details_divs = soup.find("div", class_="re-scholarship-card-mob_bottom")
        details = []
        # for details_div in details_divs:
        span_names = soup.find_all("span", class_="re-scholarship-card-info_mob-name")
        span_values = soup.find_all("span", class_="re-scholarship-card-info_mob-value")
        for i, span in enumerate(span_values):
            if 'award' in span_names[i].text:
                details.append({'Awards': span_names[i].text + span.text})
            else:
                details.append({span_names[i].text.replace("Expected d", "D"): span.text})
        # Merge every three dictionaries into one
        merged_details = []
        for i in range(0, len(details), 3):  # Process in chunks of 3
            merged_dict = {}
            for d in details[i:i+3]:  # Take the current chunk
                merged_dict.update(d)  # Merge dictionaries
            merged_details.append(merged_dict)

        # Print the result
        # print(merged_details)

        for i, heading in enumerate(headings_with_a):
            text = heading.text
            details_dict = merged_details[i]
            if ('no essay' not in text.lower()) and ('high school' in details_dict['Grade Level'].lower() or 'all' in details_dict['Grade Level'].lower()): 
                a_tag = heading.find("a")  # Get the <a> tag
                if a_tag:
                    link = a_tag["href"] 
                title = text.replace('This scholarship has been verified by the scholarship providing organization.', '')
                details_dict['Title'] = title
                details_dict['Link'] = link
                scholarship_dicts.append(details_dict)
                # print(scholarship_dicts)

                # print(title)
    return scholarship_dicts

    # else:
    #     headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    #     # Print each heading's text
    #     for heading in headings:
    #         if 'Scholar' in heading.text:
    #             print(f"{heading.name}: {heading.text}")

def get_results(query):
    # Base URL for the Google Custom Search JSON API
    BASE_URL = "https://www.googleapis.com/customsearch/v1"

    # Parameters
    results = []
    start_index = 1  # Start from the first result
    while start_index <= results_per_query:  # Google Custom Search API limit is 100 results
        params = {
            "key": API_KEY,
            "cx": CX,
            "q": query,
            "start": start_index,
            "num": 10,  # Number of results per page (max 10)
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        
        # Add results to the list
        if "items" in data:
            results.extend(data["items"])
        else:
            print("No more results or an error occurred.")
            break
        
        # Increment start_index by 10 for the next page
        start_index += 10
    
    return results

for query in queries:
    results = get_results(query)

    # Process the data
    for item in results:
        title = item['title']
        link = item['link']
        snippet = item['snippet']
        if 'scholarships' in title.lower():
            scholarships = extract_data(link)
            if scholarships != []:
                results_df = pd.DataFrame.from_dict(scholarships)
                print(results_df)
        if 'high school' in snippet.lower() or 'hs' in snippet.lower():
            scholarship_data.append({"Title": title, "Link": link, "Snippet": snippet, "query": query})

search_results_df = pd.DataFrame.from_dict(scholarship_data)

print(search_results_df)

'''<script async src="https://cse.google.com/cse.js?cx=125fb75ba03064de8">
</script>
<div class="gcse-search"></div>'''