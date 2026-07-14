from langsmith import Client
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

client = Client()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = client.pull_prompt(
    "rlm/rag-prompt",
    include_model=False,
    dangerously_pull_public_prompt=True,
)

generation_chain = prompt | llm | StrOutputParser()

