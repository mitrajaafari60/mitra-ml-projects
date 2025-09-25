# create_project.py
import os

# project structure
project_structure = {
    'my-ml-portfolio': {
        '01_house_price_prediction': ['data', 'notebooks', 'src', 'models'],
        '02_diabetes_classification': ['data', 'notebooks', 'src', 'models'],
        '03_iris_classification': ['data', 'notebooks', 'src', 'models'],
        'datasets': [],
        'utils': [],
        'docs': []
    }
}

def create_project():
    for main_dir, subdirs in project_structure.items():
        os.makedirs(main_dir, exist_ok=True)
        
        for subdir, subsubdirs in subdirs.items():
            path = os.path.join(main_dir, subdir)
            os.makedirs(path, exist_ok=True)
            
            for subsubdir in subsubdirs:
                os.makedirs(os.path.join(path, subsubdir), exist_ok=True)
    
    # create base parts
    files_to_create = [
        'README.md',
        'requirements.txt',
        '.gitignore',
        'setup.py'
    ]
    
    for file in files_to_create:
        with open(os.path.join('my-ml-portfolio', file), 'w') as f:
            if file == 'requirements.txt':
                f.write("numpy\npandas\nscikit-learn\nmatplotlib\njupyter\nseaborn")
            elif file == '.gitignore':
                f.write("__pycache__/\n*.pyc\n.DS_Store\n.env\n.ipynb_checkpoints/")
    
    print("✅ project created!")

if __name__ == "__main__":
    create_project()