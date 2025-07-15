import sys
import requests
import argparse

parser = argparse.ArgumentParser(description="Post stdin data to a URL.")
parser.add_argument(
    "--template", help="These are templates from the Kong AI Template plugin configuration.", default=None
)
parser.add_argument(
    "--ai_gateway_url", help="URL to Kong AI Gateway.", default="http://localhost:8000/convert"
)
args = parser.parse_args()

url = args.ai_gateway_url

data = sys.stdin.read()

try:
    template = args.template or "wsdl"
    rdata = {
        "messages": f"{{template://{template}}}",
        "properties": {args.template: data }
    }
    response = requests.post(url, headers={"x-model": "openai"}, json=rdata)
    print(response.json()["choices"][0]["message"]["content"])
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)