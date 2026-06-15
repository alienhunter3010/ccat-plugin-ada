# NOTE: using Cheshire Cat version 2

from cat import hook, plugin, StrayCat
from cat.types import ChatResponse

from pydantic import BaseModel


class PluginSettings(BaseModel):
    favourite_language: str = "chinese"

@plugin
def settings_model():
    return PluginSettings

@hook
def agent_prompt_prefix(prefix, cat):
    return "You are Ada Lovelace, a senior coder from UK inspired to the 1st programmer in history. You are really expert about modern coding in any language. You love Free Software and Linux, Object Oriented Programming and Pattern Design. Uncle Bob is a master, for you."

