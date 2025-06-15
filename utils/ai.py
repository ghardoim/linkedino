from langchain.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from os import getenv

load_dotenv()

class AI:
    def think(args:dict, parser:PydanticOutputParser, prompt:str) -> dict:

        LLM = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=getenv("GOOGLE_API_KEY"), temperature=0)
        parser = PydanticOutputParser(pydantic_object=parser)

        chain = PromptTemplate(template=prompt + "\n\n{FMT}") | LLM | parser
        chain.invoke(args | {"FMT": parser.get_format_instructions()})
