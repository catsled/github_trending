from states import State
from langgraph.graph import END


def should_continue(state: State):
    if len(state["messages"]) >= 2:
        # human -> generate -> reflection -> generate
        return END
    return "reflect"