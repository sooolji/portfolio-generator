import json
from datetime import UTC, datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

LANGUAGES = [
    {"code": "en", "file": "portfolio-solji-en.json"},
    {"code": "es", "file": "portfolio-solji-es.json"},
]

env = Environment(loader=FileSystemLoader("."), autoescape=True)
index_template = env.get_template("portfolio_template.html")
resume_template = env.get_template("resume_template.html")

for lang in LANGUAGES:
    with Path(lang["file"]).open(encoding="utf-8") as f:
        data = json.load(f)

    data["current_year"] = datetime.now(tz=UTC).year

    if "social_links" in data:
        for link in data["social_links"]:
            if link.get("svg_path"):
                with Path(link["svg_path"]).open(encoding="utf-8") as svg_file:
                    link["svg_data"] = svg_file.read()

    portfolio_html = index_template.render(**data)
    resume_html = resume_template.render(**data)

    with Path(f"portfolio-{lang['code']}.html").open("w", encoding="utf-8") as f:
        f.write(portfolio_html)

    with Path(f"resume-{lang['code']}.html").open("w", encoding="utf-8") as f:
        f.write(resume_html)

print("HTML files generated successfully!")
