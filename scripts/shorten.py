import sys
import re
import requests
from modules import shared

GRADIO_RE = re.compile(r"(https://[a-zA-Z0-9\-]+\.gradio\.live)")
_printed = False


def shorten_url(url: str) -> str:
    provider = getattr(shared.opts, "gls_provider", "is.gd")

    try:
        if provider == "is.gd":
            r = requests.get(
                "https://is.gd/create.php",
                params={"format": "simple", "url": url},
                timeout=5,
            )
            return r.text.strip()

        elif provider == "tinyurl":
            r = requests.get(
                "https://tinyurl.com/api-create.php",
                params={"url": url},
                timeout=5,
            )
            return r.text.strip()

        elif provider == "shrtco.de":
            r = requests.get(
                "https://api.shrtco.de/v2/shorten",
                params={"url": url},
                timeout=5,
            )
            data = r.json()
            return data["result"]["full_short_link"]

        elif provider == "clck.ru":
            r = requests.get(
                "https://clck.ru/--",
                params={"url": url},
                timeout=5,
            )
            return r.text.strip()

        else:
            return "[unknown provider]"

    except Exception as e:
        return f"[shorten failed: {e}]"


class StdoutInterceptor:
    def __init__(self, original):
        self.original = original

    def write(self, text):
        global _printed
        self.original.write(text)

        if _printed:
            return

        if not getattr(shared.opts, "gls_enabled", True):
            return

        match = GRADIO_RE.search(text)
        if not match:
            return

        long_url = match.group(1)
        short = shorten_url(long_url)
        provider = getattr(shared.opts, "gls_provider", "is.gd")

        self.original.write(
            "\n==============================\n"
            f"[Gradio public URL] {long_url}\n"
            f"[Short URL ({provider})] {short}\n"
            "==============================\n\n"
        )

        _printed = True

    def flush(self):
        self.original.flush()

    def isatty(self):
        return self.original.isatty()

    def __getattr__(self, name):
        return getattr(self.original, name)


# hook
sys.stdout = StdoutInterceptor(sys.stdout)
