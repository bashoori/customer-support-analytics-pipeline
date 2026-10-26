from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM


def create_llm():
    """Create the Llama 3 model connection."""
    return OllamaLLM(
        model="llama3",
        temperature=0.1
    )


def analyze_message(message, llama_model):
    """Extract structured information from a customer message."""

    prompt = """
    Analyze this customer support message.

    Return:
    1. Problem: the main issue
    2. Customer request: what the customer wants
    3. Category: choose one of Refund, Delivery, Product,
       Payment, or Exchange.

    Do not invent details.

    Customer message:
    {information}
    """

    prompt_template = ChatPromptTemplate.from_template(prompt)
    chain = prompt_template | llama_model

    return chain.invoke({"information": message})


if __name__ == "__main__":
    model = create_llm()

    test_message = (
        "My order arrived three days late and the box was damaged. "
        "I want a refund."
    )

    result = analyze_message(test_message, model)
    print(result)