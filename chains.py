from prompts import generate_prompt, translate_prompt, reflection_prompt, formatter_prompt
from llms import get_llm

from langchain_core.output_parsers import StrOutputParser

llm = get_llm()

generate_chain = generate_prompt | llm

reflection_chain = reflection_prompt | llm

translate_chain = translate_prompt | llm | StrOutputParser()

formatter_chain = formatter_prompt | llm | StrOutputParser()
