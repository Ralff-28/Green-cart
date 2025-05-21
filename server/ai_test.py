from google import genai

client = genai.Client(api_key="AIzaSyC7VmFWi3ZEobk8tvwNl5JFpL76gIaxha8")
response = client.models.generate_content(
    model="gemini-1.5-flash", contents="Explain how AI works"
)
print(response.text)