#If you'd like to install packages that aren't installed by default, uncomment the next two lines
#import sys\n",
#!{sys.executable} -m pip install langchain openai pandas spacy matplotlib wordcloud pinecone-client langchain-community arxiv pymupdf

import openai
import pandas as pd
import spacy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import ArxivLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

# Initialize OpenAI API
openai.api_key = "your_openai_api_key"

# Step 1: Pull a technology topic from recent articles
def fetch_technology_topic():
    # Placeholder: Replace this with API calls to news sources like The Verge
    topics = ["Artificial Intelligence", "Blockchain", "Quantum Computing", "Cybersecurity"]
    return topics[0]  # For this example, we'll use "Artificial Intelligence"

topic = fetch_technology_topic()

# Step 2: Search topic using arxiv and retrieve abstracts
def fetch_arxiv_papers(topic):
    #loader = arxivDigitalLibraryLoader(query=topic) todo: write this loader!
    from langchain_community.document_loaders import ArxivLoader

    # Supports all arguments of `ArxivAPIWrapper`
    loader = ArxivLoader(
        query=topic,
        load_max_docs=2,
        # doc_content_chars_max=1000,
        # load_all_available_meta=False,
    )
    docs = loader.get_summaries_as_docs()
    return [doc.page_content for doc in docs]

papers = fetch_arxiv_papers(topic)

# Step 3: Extract keywords from summaries using spaCy
def extract_keywords(texts, n_top=25):
    nlp = spacy.load("en_core_web_sm")
    all_text = " ".join(texts)
    doc = nlp(all_text)
    keywords = [chunk.text for chunk in doc.noun_chunks]
    keyword_freq = pd.Series(keywords).value_counts()
    return keyword_freq.head(n_top)

keywords = extract_keywords(papers)

# Visualize keywords as a WordCloud for a brief look at the topic
wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(keywords)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# Step 4: Pick a semi-random keyword
chosen_keyword = keywords.index[0]  # Using the top keyword for simplicity todo: incorporate top 10-20
print(f"Chosen Keyword: {chosen_keyword}")

# Step 5: Use RAG (with Pinecone) to retrieve additional context and generate text
# Initialize Pinecone
pinecone.init(api_key="your_pinecone_api_key", environment="your_pinecone_env")
index_name = "rag-index"
embedding_model = OpenAIEmbeddings()

# Load documents into Pinecone for retrieval
vectorstore = Pinecone.from_texts(papers, embedding_model, index_name=index_name)

# Create RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm=openai.ChatCompletion, retriever=vectorstore.as_retriever()
)

# Generate content using GPT-3.5
def generate_blog_post(keyword):
    context = qa_chain.run(f"Write a detailed explanation about {keyword}.")
    response = openai.Completion.create(
        engine="gpt-4o",
        prompt=f"Write a blog post titled 'An Introduction to {keyword}' based on the following context:\n\n{context}",
        max_tokens=500,
    )
    return response["choices"][0]["text"]

blog_post = generate_blog_post(chosen_keyword)
print("\nGenerated Blog Post:\n")
print(blog_post)

# Save the blog post to a file
with open(f"{chosen_keyword}_blog_post.txt", "w") as file:
    file.write(blog_post)
