from typing import List
from datetime import date
from pydantic import BaseModel
from .game_schema_model import GameSchema


class Action(BaseModel):
    action_name: str
    action_value: str
    action_date: date


class UserData(BaseModel):
    user_id: str
    actions: List[Action]


class Game(BaseModel):
    game_id: str
    schema: GameSchema
    status: str
    data_game: List[UserData]
