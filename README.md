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

## LLM Model Used
Here I wanted to test out the models which are available locally to get response for my prompt.
Seeing my system compability of 8GB RAM and 2GB Graphics, running a Llama 3.2 (3B parameter) model.

Llama 3.2 is fast, uses minimal memory, and works good for short summary.

Intial size of the folder before downloading Ollama - 408KB
The 3B model from ollama that is llama3.2.3b is 2GB.

Run the below command in the powershell if you are using Windows, to download ollama model.
Gives out of memory error while running ollama model. 