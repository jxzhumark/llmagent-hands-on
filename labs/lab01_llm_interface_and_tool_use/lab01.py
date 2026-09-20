# lab01.py - LLM Interface and Tool Use

# import libraries
import os # for calling environment variables, e.g. API keys
from openai import OpenAI # for setting up the LLM API client
from typing import Literal # for type hinting, Literal is a type that can be one of the values in the list

# Practice 1: set up the LLM API client (so easy!, see e.g., https://api-docs.deepseek.com/ for reference)
LLM_client = OpenAI(
    base_url = os.getenv("DEEPSEEK_BASE_URL_FOR_OPENAI"), # set model provider's base URL
    api_key = os.getenv("DeepSeek_API_KEY"), # get model provider's API key
)

# test the LLM API client
def test_llm_client_in_one_turn_conversation(use_prompt: str, sys_prompt: str = None, stream: bool = False,
                    thinking_mode_toggle: Literal["enabled", "disabled"] = "disabled",
                    reasoning_effort_control: Literal["low", "high", "max"] = "low") -> object:
    """Test the LLM API client by sending a prompt and returning the response.

    Args:
        use_prompt (str): The prompt to send to the LLM.
        sys_prompt (str, optional): The system prompt to send to the LLM. Defaults to None.
        stream (bool, optional): Whether to stream the response. Defaults to False.
        reasoning_effort (Literal["none"|"low"|"medium"|"high"], optional): The effort to put into reasoning. Defaults to "none".

    Returns:
        str: The LLM's response to the prompt in a structured format, as follows:
        {   
            "reasoning": str,
            "response": str,
        }
        if stream is True, the response will be streamed in real-time.
    """
    response = LLM_client.chat.completions.create(
        model = os.getenv("DEEPSEEK_MODEL"),
        messages = [
            {"role": "system", "content": sys_prompt} if sys_prompt is not None else None,
            {"role": "user", "content": use_prompt}
        ],
        stream = stream,
        reasoning_effort = reasoning_effort_control,
        extra_body = {
            "thinking": {"type": thinking_mode_toggle} # extend the request body to include thinking mode
        }
    )
    return response


if __name__ == "__main__":
    use_prompt = "1 + 3 + 5 + ... + 11 = ?"
    # use_prompt = "who am i"
    sys_prompt = "You are a helpful assistant."
    stream = False
    reasoning_effort_control = "low"
    response = test_llm_client_in_one_turn_conversation(use_prompt = use_prompt, 
                                                        sys_prompt = sys_prompt, 
                                                        stream = stream, 
                                                        thinking_mode_toggle = "enabled",
                                                        reasoning_effort_control = reasoning_effort_control)
    message = response.choices[0].message
    assistant = {
        "reasoning": getattr(message, "reasoning_content", None),
        "response": message.content,
        "sum_of_tokens": response.usage.total_tokens,
    }
    print(f"Enabled Thinking Mode: User: {use_prompt}\nAssistant: {assistant}")
    
    response = test_llm_client_in_one_turn_conversation(use_prompt = use_prompt, 
                                                        sys_prompt = sys_prompt, 
                                                        stream = stream, 
                                                        thinking_mode_toggle = "disabled",
                                                        reasoning_effort_control = reasoning_effort_control)
    message = response.choices[0].message
    assistant = {
        "reasoning": None,
        "response": message.content,
        "sum_of_tokens": response.usage.total_tokens,
    }
    print(f"Disabled Thinking Mode: User: {use_prompt}\nAssistant: {assistant}")