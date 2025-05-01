import re

USERNAME = "Omayer111"

# New dynamic URLs
activity_graph_url = f"https://github-readme-activity-graph.cyclic.app/graph?username={USERNAME}&theme=react-dark"
stats_url = f"https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&theme=radical"
streak_url = f"https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=radical"

# Read the current README.md
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

# Update the URLs using regex
readme_content = re.sub(r'https://github-readme-activity-graph\.cyclic\.app/graph\?username=[^"\s]+',
                        activity_graph_url, readme_content)

readme_content = re.sub(r'https://github-readme-stats\.vercel\.app/api\?username=[^"\s]+',
                        stats_url, readme_content)

readme_content = re.sub(r'https://github-readme-streak-stats\.herokuapp\.com/\?user=[^"\s]+',
                        streak_url, readme_content)

# Write the updated content back to README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)
