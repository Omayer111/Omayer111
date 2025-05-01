import requests

# GitHub username
USERNAME = "Omayer111"

# URLs for dynamic content
activity_graph_url = f"https://github-readme-activity-graph.cyclic.app/graph?username={USERNAME}&theme=react-dark"
stats_url = f"https://github-readme-stats.vercel.app/api?username={USERNAME}&show_icons=true&theme=radical"
streak_url = f"https://github-readme-streak-stats.herokuapp.com/?user={USERNAME}&theme=radical"

# Read the current README.md
with open("README.md", "r") as file:
    readme_content = file.read()

# Replace placeholders in the README with updated URLs
updated_content = readme_content
updated_content = updated_content.replace("![GitHub Activity Graph](old_url)", f"![GitHub Activity Graph]({activity_graph_url})")
updated_content = updated_content.replace("![GitHub Stats](old_url)", f"![GitHub Stats]({stats_url})")
updated_content = updated_content.replace("![GitHub Streak](old_url)", f"![GitHub Streak]({streak_url})")

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(updated_content)
