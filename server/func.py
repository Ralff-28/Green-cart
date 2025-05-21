from google import genai
import json
# Set your OpenAI API Key
client = genai.Client(api_key="AIzaSyC7VmFWi3ZEobk8tvwNl5JFpL76gIaxha8")

def analyze_carbon_footprint(file_path):
    """Reads scraped HTML from a file and generates carbon footprint analysis using OpenAI API."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = json.load(file) 
    users = content.get("users", [])  # Get the "users" list, default to empty list if not found
    last_link = users[-1] if users else None

    prompt = f"""
    You are an environmental expert. Analyze the following HTML product page from Flipkart to estimate its carbon footprint and environmental friendliness.
    
    Consider:
    - Type of product and its material composition.
    - Estimated carbon footprint based on manufacturing, transportation, and disposal.
    - Suggestions for eco-friendly alternatives.
    - A rating for its sustainability (out of 10).
    Here is the product link

    {last_link}

    Provide a well-structured and professional analysis of 100 words.
    """
    response = client.models.generate_content(
        model="gemini-1.5-flash", contents=[prompt]
    )

    return response


# **Read from scraped_data.txt and analyze**
file_path = "data.json"

# Generate AI-powered carbon footprint analysis
carbon_analysis = analyze_carbon_footprint(file_path)
print("\n🌍 Carbon Footprint & Environmental Analysis:\n", carbon_analysis)
