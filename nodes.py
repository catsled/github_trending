from chains import generate_chain, reflection_chain, translate_chain
from states import State

import re

flags = re.DOTALL

from langchain_core.messages import HumanMessage, AIMessage


def generation_node(state: State) -> State:
    print("=======================generate===============================")
    return {
        "messages": [generate_chain.invoke(state["messages"])]
    }
    

def reflection_node(state: State) -> State:
    # Other messages we need to adjust
    cls_map = {"ai": HumanMessage, "human": AIMessage}
    translated = [state["messages"][0]] + [
        cls_map[msg.type](content=re.sub(r"<think>.*?</think>", "", msg.content, flags=flags)) for msg in state["messages"]
    ]
    
    print("======================reflection=============================")
    res = reflection_chain.invoke(translated)
    
    return {"messages": [HumanMessage(content=res.content)]}

