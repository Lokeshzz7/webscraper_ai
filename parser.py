from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = (
    "You are tasked with extracting specific information from the following text content: {domc}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parsed}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

model = OllamaLLM(model = "llama3")

def parse_content(chunks,parsed):
    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    results = []

    for i,chunk in enumerate(chunks,start=1):

        response = chain.invoke({"domc":chunk,"parsed":parsed})


        print(f"Parsed {i} of {len(chunks)}")

        results.append(response)

    return "\n".join(results)