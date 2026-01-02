from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes

import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

#initialize groq model
model = ChatGroq(model="groq/compound-mini", groq_api_key=groq_api_key )

#creating a prompt template
system_template = "Give a response in {language} to the user input."
prompt_template= ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user","{text}")
])

parser = StrOutputParser()

#create a chain
chain = prompt_template | model | parser

# FAstAPI app
app = FastAPI(
    title = "LangChain server",
    version = "1.0",
    description="A FastAPI server for LangChain chains",
)

# adding chain routing 
add_routes(app, chain, path="/chain")

# run server 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

