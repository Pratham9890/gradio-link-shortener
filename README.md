# Gradio Link Shortener

Stable Diffusion **WebUI extension** that automatically detects Gradio public
share links (`https://*.gradio.live`) printed in the console and outputs a
shortened version using a configurable URL shortening service.



## Features

- Automatically detects Gradio public share URLs
- Prints a shortened link to the console
- Runs only once per WebUI launch
- Configurable from WebUI settings
- Multiple shortener providers supported



## Installation

### Install via WebUI

1. Open **Stable Diffusion WebUI**
2. Go to **Extensions → Install from URL**
3. Paste:
   https://github.com/Pratham9890/gradio-link-shortener
4. Click **Install**
5. Restart WebUI



### Manual Installation

1. Download the repository as a ZIP
2. Extract to:
   stable-diffusion-webui/extensions/gradio-link-shortener
3. Restart WebUI



## Settings

Available in **Settings → Gradio Link Shortener**

- **Enable Gradio link shortener**
  Enable or disable the extension

- **Shortener service**
  Choose one of:
  - is.gd
  - tinyurl
  - shrtco.de
  - clck.ru



## How It Works

- Hooks into sys.stdout
- Scans console output for:
  https://*.gradio.live
- When detected, prints:
  - Original Gradio URL
  - Shortened URL from selected provider
- Only triggers once per session



## Example Output

```
==============================
[Gradio public URL] https://abcd-1234.gradio.live
[Short URL (is.gd)] https://is.gd/xyz123
==============================
```



## Notes

- Internet connection required
- If shortening fails, an error message is shown
- Only the first Gradio link is processed per launch



## License

MIT
