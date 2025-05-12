from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


generate_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an essay assistant tasked with writing a brief introduction to a given project, and you also should write features of this project(maybe).  You need to make every effort to avoid hallucinations."
         "If the user provides critique, respond with a revised version, do not reply anything else introduction and features."
         "Additionally, you should first get the features from the given project, if there is not, you are allowed to infer it."
         "Meanwhile, all content should fill in the followed format"
         "\n\n"
         "Introduction:\n"
         "the brief introduction to a given project\n"
         "Features:\n"
         "features of this project"),
        MessagesPlaceholder(variable_name="messages")
    ]
)


reflection_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a teacher grading an essay submission. Generate critique and recommendations for the user's submission."
         "the format should only includ brief introduction and features."
         " Provide detailed suggestions including hallucinations, readability."),
        MessagesPlaceholder(variable_name="messages")
    ]
)

translate_system = """You are a translator, you need to translate the language of the given documents to Chinese,
                    you should notion four points, 
                    1. translate like a native chinese speaker;
                    2. keep the correctness.
                    3. Do not translate some specific content, just like title and terms.
                    4. Do not output any irrelevant content."""
                    
translate_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", translate_system),
        ("human", "Here is the content needed to be translate \n\n {docs}")
    ]
)


formatter_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你现在是一个精通格式整理的智能助手，你需要将给定的文字内容整理为简洁美观的格式"),
        ("human", "{docs}")
    ]
)