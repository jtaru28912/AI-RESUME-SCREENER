from langchain_core.messages import HumanMessage, SystemMessage
from .config_reader import model
from langchain_openai import ChatOpenAI  
from .schema import ResumeSchema
from langchain_core.output_parsers import PydanticOutputParser

from .exceptions import LLMCallFailedError

def make_api_call(job, system_prompt, resume, py_class):
    try:

        # 1. Create LLM
        llm = ChatOpenAI(
                    model=model )
        # 2. Bind structured output (Pydantic / dataclass)

        parser = PydanticOutputParser(pydantic_object=py_class)

        chain = llm | parser 

        #Functionally identical to:

        # structured_llm = llm.with_structured_output(ResumeSchema)
        # result = structured_llm.invoke(messages)

        # 3. Build messages
        
        # Inject format instructions
        format_instructions = parser.get_format_instructions()
        final_system_prompt = f"{system_prompt}\n\n{format_instructions}"

        messages = [
                SystemMessage(content=final_system_prompt),
                HumanMessage(
                    content=f"""
                    Screen the given resume against the given job description.
                    RESUME:{resume}
                    JOB DESCRIPTION: {job}""" )  ]

        result = chain.invoke(messages)
        return result 
    except Exception as e:
        raise LLMCallFailedError('LLM call failed') from e


    




