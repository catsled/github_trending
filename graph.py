from langgraph.graph import START, StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from states import State
from edges import should_continue
from nodes import generation_node, reflection_node


graph = StateGraph(State)
graph.add_node("generate", generation_node)
graph.add_node("reflect", reflection_node)

graph.add_edge(START, "generate")

graph.add_conditional_edges("generate", should_continue)

graph.add_edge("reflect", "generate")

memory = MemorySaver()
graph = graph.compile(checkpointer=memory)