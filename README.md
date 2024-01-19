# Ollama
Ollama is a tool that allows you to run open-source large language models (LLMs) locally on your machine. It supports a variety of models, including Llama 2, Code Llama, and others. It bundles model weights, configuration, and data into a single package, defined by a Modelfile.

Step 1: Install Ollama (Ubuntu)
```
curl https://ollama.ai/install.sh | sh
```
Step 2: Identify the Model you would like to use in the local:

Reference: https://github.com/jmorganca/ollama

Step 3: Pull & Run the Model in local
```
ollama run mistral
```
Step 4: Pull the Model in local:
```
ollama pull llama2
```
Step 5: Remove the Model from local:
```
ollama rm llama2
```


# Modify the existing Model:

Pull the Model in local:
```
ollama pull llama2
```

Create a Modelfile:

```
FROM llama2

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are Mario from Super Mario Bros. Answer as Mario, the assistant, only.
"""
```
Next, create and run the model:

```
ollama create mario -f ./Modelfile
ollama run mario
>>> hi
Hello! It's your friend Mario.
```

