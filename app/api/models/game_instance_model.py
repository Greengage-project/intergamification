from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field
from .game_schema_model import GameSchema
from .jwt_model import JWT_data


class Action(BaseModel):
    action_name: str
    action_value: str
    action_date: date


class UserData(BaseModel):
    user_id: str
    actions: List[Action]


class Game(BaseModel):
    process_id: str
    schema: GameSchema
    created_by: Optional[JWT_data] = None
    isPublicLeaderboard: Optional[bool] = True
    status: str
    data_game: List[UserData]
