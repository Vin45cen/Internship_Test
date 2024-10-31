Great! Here’s the updated README with your GitHub repository link included:

---

# Flask API for LLM Inference using Ollama

This project uses a simple Flask API that employs the Ollama library, specifically the LLaMA 3.2 model, to perform language model inference. 

## Table of Contents
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Example Request and Response](#example-request-and-response)
- [Error Handling](#error-handling)


## Requirements

- **Python 3.10+**
- Download and setup [Ollama installer](https://github.com/ollama/ollama)
   
- Pull the llamma3.2 model from Ollama:
   ```bash
   ollama pull llamma3.2
   ```
- **Flask** - To install Flask, run:
  ```bash
  pip install Flask
  ```
- **ollama** - Ensure you have the `ollama` package and that it's configured. To install, run:
  ```bash
  pip install ollama
  ```

## Project Structure

- **main.py** - Contains the code to create the Flask API and handle requests.

## Installation

1. Clone the repository or download the code files.
   ```bash
   git clone https://github.com/Vin45cen/Internship_Test.git
   ```
2. Navigate into the project directory:
   ```bash
   cd Internship_Test
   ```

3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   ```

4. Install the required libraries:
   ```bash
   pip install Flask ollama
   ```

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

