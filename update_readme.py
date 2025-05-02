import re

USERNAME = "Omayer111"

# New dynamic URLs
activity_graph_url = f"https://github-readme-stats.vercel.app/api/top-langs/?username=Omayer111&theme=radical&hide_border=true&include_all_commits=true&count_private=true&layout=compact"
stats_url = f"https://github-readme-stats.vercel.app/api?username=Omayer111&show_icons=true&theme=radical" alt="GitHub Stats"
streak_url = f"https://github-readme-streak-stats.herokuapp.com/?user=Omayer111&theme=radical&hide_border=true"

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
