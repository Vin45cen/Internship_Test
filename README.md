# Flask API for LLM Inference using Ollama

this project use a simple FLASK API that use ollama library such as llama3.2 to perform language model inference.
Here’s the README with a table of contents and refined sections:

## Table of Contents
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Example Request and Response](#example-request-and-response)
- [Error Handling](#error-handling)

## Requirements

- **Python 3.10+**
- **Flask** - To install Flask, run:
  ```bash
  pip install Flask
  ```
- **ollama** - Ensure you have the `ollama` package and that it's configured. To install, run:
  ```bash
  pip install ollama
  ```

- Download and setup [Ollama installer](https://github.com/ollama/ollama)
   
- Pull the llama3.2 model from Ollama:
   ```bash
   ollama pull llama3.2
   ```

## Project Structure

- **main.py** - Contains the code to create the Flask API and handle requests.
  
## Usage

1. **Run the API**:

   Start the API server by running the following command:

   ```bash
   python main.py
   ```

   By default, this will start the server on `http://127.0.0.1:5000`.

2. **Send a Prompt**:

   To get a response from the model, send a POST request to `http://127.0.0.1:5000/inference` with the JSON payload below:

   ```json
   {
       "prompt": "Your prompt here"
   }
   ```

## Example Request and Response

### Example Request (using `curl`)

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"prompt\": \"Explain GPT in 2 sentences\"}" http://127.0.0.1:5000/inference
```

### Example Response

```json
{
  "Response": "GPT stands for Generative Pre-trained Transformer, a type of artificial intelligence model that uses transformer architecture to generate human-like text based on input prompts. It is trained on large amounts of text data and can be fine-tuned for specific tasks such as language translation, question-answering, and text summarization, making it a versatile tool for natural language processing applications."
}
```

## Error Handling

If the `prompt` key is missing from the request JSON, or an error occurs during response generation, an error message is returned.