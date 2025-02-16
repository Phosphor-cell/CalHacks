import requests
from test import queryTwo

# Replace with a valid API key
SERPER_API_KEY = "595d63c8890e0cdf623ade0a546fcbc6b36d7d6e"


#EXAMPLE- TAKE FROM ML
threePillars= ["Employment & Credential Recognition", "Housing Stability", "Healthcare & Mental Health Support"]


pOne= threePillars[0]
pTwo= threePillars[1]
pThree= threePillars[2]
Questions= queryTwo(pOne, pTwo, pThree)

def search_serper(query, num_results=10):
    """
    Search Google using Serper API and return a list of results.
    
    :param query: Search query string.
    :param num_results: Number of search results to return.
    :return: List of dictionaries containing title, link, and snippet.
    """
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query,
        "num": num_results
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for non-200 responses

        data = response.json()
        results = data.get("organic", [])
        
        if not results:
            print("No results found. The API might have changed.")
            return []
        
        return [{"title": item["title"], "link": item["link"], "snippet": item.get("snippet", "")} for item in results]
    
    except requests.exceptions.RequestException as e:
        print("Network or API error:", str(e))
        return []



# Example usage
if __name__ == "__main__":
    topic = Questions[0]
    topic= topic.replace("\"", "")

    search_results = search_serper(topic)

    if search_results:
        print("\nSearch Results:")
        for idx, result in enumerate(search_results, 1):
            print(f"{idx}. {result['title']}\n   {result['link']}\n   {result['snippet']}\n")
    else:
        print("No results found or an error occurred.")
