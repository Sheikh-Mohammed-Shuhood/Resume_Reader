# Resume Reader

## Git Commands to set up repo from CLI
Create a folder and then run the commands in bash
```
git init
gh repo create Resume_Reader --public --source=. --remote=origin
git branch -M main
touch README.md
echo "# Project Title" > README.md
git add README.md
git commit -m "Initial commit"
git push -u origin main
```