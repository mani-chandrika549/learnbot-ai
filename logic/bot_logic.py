import json
import re

# Load learning paths once
with open('learning_paths.json', 'r') as file:
    learning_paths = json.load(file)

# Refined keyword map
keyword_map = {
    "java": "java",
    "full stack": "full_stack",
    "ai": "ai",
    "artificial intelligence": "ai",
    "web": "web_development",
    "web dev": "web_development",
    "app": "app_development",
    "mobile": "app_development",
    "dsa": "dsa",
    "data structures": "dsa",
    "cloud": "cloud_devops",
    "devops": "cloud_devops",
    "database": "database",
    "sql": "database",
    "python": "python_foundation",
    "cyber": "cybersecurity",
    "cybersecurity": "cybersecurity",
    "machine learning": "machine_learning",
    "ml": "machine_learning",
    "nlp": "nlp",
    "data science": "data_science",
    "ui": "ui_ux",
    "ux": "ui_ux",
    "design": "ui_ux",
    "blockchain": "blockchain",
    "testing": "software_testing",
    "qa": "software_testing",
    "prompt": "prompt_engineering",
    "iot": "iot",
    "robotics": "robotics",
    "ar": "ar_vr",
    "vr": "ar_vr",
    "generative": "generative_ai",
    "writing": "technical_writing",
    "bi": "business_intelligence",
    "business intelligence": "business_intelligence",
    "nocode": "nocode_dev",
    "no code": "nocode_dev",
    "ui testing": "ui_testing",
    "automation": "ui_testing",
    "game": "game_development"
}

def get_bot_response(user_input):
    user_input = user_input.lower()

    for keyword, path_key in keyword_map.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
            path = learning_paths.get(path_key)
            if path:
                response = f"📚 **{path['title']} Learning Path**:\n"
                for i, step in enumerate(path['steps'], 1):
                    response += f"{i}. {step}\n"
                return response

    suggestions = ', '.join(sorted(set(k.title() for k in keyword_map.keys())))
    return f"❌ Sorry, I couldn't find a matching learning path.\n👉 Try asking about: {suggestions}"
