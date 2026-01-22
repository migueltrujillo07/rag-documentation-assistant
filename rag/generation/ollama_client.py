import ollama

class OllamaClient:
    """Client to interact with local LLMs via Ollama."""

    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name

    def generate_response(self, system_message: str, user_message: str) -> str:
        """Sends the prompt to the LLM and gets a response."""
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {'role': 'system', 'content': system_message},
                {'role': 'user', 'content': user_message},
            ]
        )
        return response['message']['content']