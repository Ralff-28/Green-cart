import requests

def test_api():
    url = 'https://real-time-amazon-data.p.rapidapi.com/search'
    headers = {
        'x-rapidapi-host': 'real-time-amazon-data.p.rapidapi.com',
        'x-rapidapi-key': '02bdadea4bmsh5668220f5b32226p172399jsn585f020418b0'
    }
    params = {
        'query': 'Phone',
        'page': 1,
        'country': 'US',
        'sort_by': 'RELEVANCE',
        'product_condition': 'ALL',
        'is_prime': 'false',
        'deals_and_discounts': 'NONE'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print("API Response:", response.json())
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    test_api()