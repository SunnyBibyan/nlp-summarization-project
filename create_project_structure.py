import os

# Define the project structure
project_structure = {
    "nlp-text-summarization": {
        ".gitignore": "",
        "README.md": "# NLP Text Summarization\n",
        "requirements.txt": "transformers\nflask\npandas\nscikit-learn\n",  # Add required packages
        "setup.py": "",
        "data": {
            "raw": {},
            "processed": {}
        },
        "models": {
            "t5_finetuned": {},
            "checkpoints": {}
        },
        "notebooks": {
            "data_exploration.ipynb": "",
            "model_training.ipynb": ""
        },
        "src": {
            "__init__.py": "",
            "preprocess.py": "",
            "train.py": "",
            "app.py": "",
            "utils.py": ""
        },
        "tests": {
            "__init__.py": "",
            "test_app.py": ""
        }
    }
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # Recursive call for directories
        else:
            with open(path, 'w') as f:
                f.write(content)  # Write content to file

# Create the project structure
create_structure(".", project_structure)
