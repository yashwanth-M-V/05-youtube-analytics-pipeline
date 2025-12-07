import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv()

def extract_video_id(url: str):
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    return query.get("v", [""])[0]
