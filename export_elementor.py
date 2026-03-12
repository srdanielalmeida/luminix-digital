import json
import re

with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

with open("script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Extrair conteúdo de <body>
body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL | re.IGNORECASE)
body_content = body_match.group(1) if body_match else ""

# Remove the script.js include inside the body since we will inline it
body_content = re.sub(r'<script src="script.js"></script>', '', body_content)

# Extrair conteúdo de <head>
head_match = re.search(r'<head[^>]*>(.*?)</head>', html_content, re.DOTALL | re.IGNORECASE)
head_content = head_match.group(1) if head_match else ""

tw_script = re.search(r'(<script src="https://cdn\.tailwindcss\.com.*?</script>)', head_content, re.DOTALL)
tw_config = re.search(r'(<script id="tailwind-config">.*?</script>)', head_content, re.DOTALL)
fonts = re.findall(r'(<link[^>]*fonts\.googleapis\.com[^>]*>)', head_content, re.IGNORECASE)
styles = re.search(r'(<style>.*?</style>)', head_content, re.DOTALL)

fonts_str = "\n".join(fonts)
tw_str = tw_script.group(1) if tw_script else ""
config_str = tw_config.group(1) if tw_config else ""
styles_str = styles.group(1) if styles else ""

combined_html = f"""
{fonts_str}
{tw_str}
{config_str}
{styles_str}

<div class="bg-background-light dark:bg-background-dark text-slate-900 dark:text-slate-100 font-display">
{body_content}
</div>

<script>
{js_content}
</script>
"""

elementor_json = {
    "version": "0.4",
    "title": "Luminix Landing Page",
    "type": "page",
    "content": [
        {
            "id": "section_luminix",
            "elType": "section",
            "settings": {
                "layout": "full_width"
            },
            "elements": [
                {
                    "id": "col_luminix",
                    "elType": "column",
                    "settings": {
                        "_column_size": 100
                    },
                    "elements": [
                        {
                            "id": "html_luminix",
                            "elType": "widget",
                            "widgetType": "html",
                            "settings": {
                                "html": combined_html
                            },
                            "elements": []
                        }
                    ]
                }
            ]
        }
    ]
}

with open("luminix-elementor-template.json", "w", encoding="utf-8") as out:
    json.dump(elementor_json, out, indent=4, ensure_ascii=False)

print("Template exported successfully.")
