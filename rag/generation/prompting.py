class PromptManager:
    """Manages the creation of prompts for the LLM."""

    def __init__(self):
        self.system_prompt = (
            "You are a Computer Vision Expert Assistant. "
            "Use the provided context to answer the user's question. "
            "If the answer is not in the context, say you don't know. "
            "Always cite the source and page number in your answer."
        )

    def build_rag_prompt(self, query: str, context_chunks: list[str]) -> str:
        """Combines context and query into a structured prompt."""
        context_text = "\n\n".join(
            [f"--- Context {i+1} ---\n{content}" for i, content in enumerate(context_chunks)]
        )
        
        prompt = (
            f"Context information is below:\n"
            f"{context_text}\n\n"
            f"User Question: {query}\n"
            f"Answer:"
        )
        return prompt