scripts for craeting project 

mkdir my-ml-portfolio
cd my-ml-portfolio
mkdir 01_linear_regression
mkdir 02_logistic_regression
mkdir 03_decision_trees
mkdir datasets
mkdir utils
touch README.md
touch requirements.txt
touch .gitignore


mkdir -p mitra-ml-projects/{01_linear_regression/{data,notebooks,src,models},02_logistic_regression/{data,notebooks,src,models},03_decision_trees/{data,notebooks,src,models},datasets,utils}


#creating files
touch 02_logistic_regression/.gitkeep
touch 03_decision_trees/.gitkeep
touch datasets/.gitkeep
touch 01_linear_regression/data/.gitkeep
touch 01_linear_regression/models/.gitkeep
touch 01_linear_regression/notebooks/.gitkeep

# creating project struct
mkdir -p 02_logistic_regression/{data,notebooks,src,models}
mkdir -p 03_decision_trees/{data,notebooks,src,models}

touch 02_logistic_regression/data/.gitkeep
touch 02_logistic_regression/notebooks/.gitkeep
touch 02_logistic_regression/src/.gitkeep
touch 02_logistic_regression/models/.gitkeep

touch 03_decision_trees/data/.gitkeep
touch 03_decision_trees/notebooks/.gitkeep
touch 03_decision_trees/src/.gitkeep
touch 03_decision_trees/models/.gitkeep

# adding to Git
git add .
git commit -m "Add complete project structure with .gitkeep files"
git push


