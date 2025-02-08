## **PDF Info Retrieval using LangChain And Google Gemini**

Retrieve information from Multiple PDF Documents. This application allows to ask questions based on the uploaded PDFs using LangChain and Google Gemini.
Multiple PDFs files can be uploaded and user can ask questions.
A web interface built with Streamlit.


## **Installation Steps**

1. **Clone the repository**
   ```bash
   git clone https://github.com/shwetavw/pdf-info-retrieval.git
   cd pdf-info-retrieval
   ```

2. **Create Python env**
   ```bash
   conda create -n {env_name} python=3.10 -y
   conda activate {env_name}
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

## **Features**

- **Upload PDF Files** : Use the interface to upload multiple PDF files.
- **Ask Questions** : Ask questions related to the content of the uploaded PDFs.
- **Get Answers** : Get answers based on the content of the PDF files.

## **Techstack**
- Python
- LangChain
- Google Gemini
- Streamlit
- FAISS library

