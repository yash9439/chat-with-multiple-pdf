# Chat with your PDF

This project allows you to engage in interactive conversations with your PDF documents using LangChain, ChromaDB, and OpenAI's API. With this powerful combination, you can extract valuable insights and information from your PDFs through dynamic chat-based interactions.

Article - https://medium.com/@yash9439/unleashing-the-power-of-chat-with-multiple-pdfs-a-beginners-guide-fa1b6d4d6b89

## Architecture

The architecture of this project involves several components working together:

- **LangChain**: It serves as the interface for communication with OpenAI's API. LangChain handles rephrasing, retrieves relevant text chunks, and manages the conversation flow.

- **ChromaDB**: A vector database used to store and query high-dimensional vectors. It helps in efficiently searching for and retrieving relevant text chunks during conversations.

- **OpenAI's API**: The API provides access to OpenAI's language models, such as GPT-3.5 Turbo. It processes prompts, generates responses, and incorporates retrieved text chunks to ensure accurate and context-aware conversations.

## Getting Started

To get started with this project, follow the steps below:

### Prerequisites

- Python
- Pipenv

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yash9439/chat-with-multiple-pdf
   ```

2. Navigate to the project directory:

   ```bash
   cd chat-with-multiple-pdf
   ```

3. Install the required dependencies using Pipenv:

   ```bash
   pipenv install
   ```

4. Activate the Pipenv shell:

   ```bash
   pipenv shell
   ```

5. Create a `.env` file and replace `OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX"` with your OpenAI API key:

   ```bash
   echo 'OPENAI_API_KEY="sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX"' > .env
   ```

6. Run merge script to combine all the PDF to chat with them simultaniously:

   ```bash
   python src/merge.py
   ```

7. Run the ingestion script to parse and extract text from the PDF:

   ```bash
   python src/ingest.py
   ```

8. Start the conversation script to interact with the PDF:

   ```bash
   python src/chat-with-multiple-pdf.py
   ```

## Useful Links
- The pdf used here are a AI Development Index report 2023 and a research paper https://www.researchgate.net/publication/323498156_Artificial_Intelligence

- [OpenAI](https://platform.openai.com/): OpenAI's platform provides access to powerful language models and APIs.

- [LangChain](https://python.langchain.com/en/latest/index.html): LangChain is the library used for communication and interaction with OpenAI's API.

- [Chroma DB](https://docs.trychroma.com/): Chroma DB is a vector database used to store and query high-dimensional vectors efficiently.


Feel free to explore this project and enhance it further to suit your needs. Enjoy chatting with your PDFs and extracting valuable insights!
