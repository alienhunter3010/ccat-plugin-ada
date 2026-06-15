# NOTE: using Cheshire Cat version 2

from cat import tool, hook, plugin, StrayCat
from cat.types import ChatResponse

from pydantic import BaseModel


class PluginSettings(BaseModel):
    favourite_language: str = "chinese"

@plugin
def settings_model():
    return PluginSettings


@tool
async def get_alphabet(language: str, include_numbers: bool, cat: StrayCat):
    """Get the alphabet for a specific language, optionally including numbers."""

    prompt = f"Provide the alphabet for the language {language}, in a compact format."
    if include_numbers:
        prompt += " Include numbers as well."
    
    alphabet = await cat.llm(prompt)
    return alphabet


@hook
def agent_prompt_prefix(prefix, cat):
    return "You are Ada Lovelace, a senior coder from UK inspired to the 1st programmer in history. You are really expert about modern coding in any language. You love Free Software and Linux, Object Oriented Programming and Pattern Design. Uncle Bob is a master, for you."

