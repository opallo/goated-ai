# Tool: Pull Research Papers from Arxiv API

def pull_research_papers(topic: str) -> List[str]:
    
    # Pulls 5 research papers from Arxiv API based on the given topic.
    
    # Parameters:
    #    topic (str): The topic for which research papers are to be pulled.
    
    # Returns:
    #    List[str]: A list of 5 research paper titles.
    
    # Example Usage:
    # pull_research_papers("AI Blockchain Research")
    
    # CODE HERE

    import requests
    import json

    url = 'http://export.arxiv.org/api/query'
    query = 'search_query=all:' + topic + '&start=0&max_results=5'
    headers = {'Content-Type': 'application/json'}
    
    response = requests.get(url, params=query, headers=headers)
    
    if response.status_code == 200:
        data = response.text
        papers = json.loads(data)
        titles = [paper['title'] for paper in papers['feed']['entry']]
        return titles
    else:
        print("Error: Failed to retrieve research papers.")
        return []