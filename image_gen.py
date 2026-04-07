import requests
from urllib.parse import quote


def generate_image(prompt: str) -> bytes | None:
    encoded = quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&model=flux"
    response = requests.get(url, timeout=60)
    if response.status_code == 200:
        return response.content
    return None
