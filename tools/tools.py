from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Searches for Linkedin"""
    search = TavilySearchResults()
    res = search.run(f"{name}")
    # Ensure `res` is a list
    return res[0]["url"]
