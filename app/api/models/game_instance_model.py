from typing import List, Optional
from datetime import date
from pydantic import BaseModel
from .game_schema_model import GameSchemaBase
from .jwt_model import JWT_data


class TaskVariables(BaseModel):
    complexityScore: int


class task(BaseModel):
    taskId: str
    variables: List[TaskVariables]


class NewGameBody(BaseModel):
    processId: str
    gameSchemaId: str
    tasks: List[dict]


class Action(BaseModel):
    action_name: str
    action_value: str
    action_date: date


class UserData(BaseModel):
    userId: str
    actions: List[Action]


class GameBase(NewGameBody):
    createdBy: Optional[JWT_data] = None
    isPublicLeaderboard: Optional[bool] = True
    status: str
    dataGame: List[UserData]
