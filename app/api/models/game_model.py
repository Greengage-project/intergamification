from typing import List
from datetime import date
from pydantic import BaseModel
# Importamos GameSchema desde game_schema_model
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

"""
{
  "game_id": "1",
  "schema":{},
  "status": "active",
  "data_game":[
    {
      "user_id": "xxxxxxxxxx",
      "actions": [
        {
          "action_name": "contribution",
          "action_value": "1",
          "action_date": "2023-01-01"
        },
        {
          "action_name": "moderator_evaluation",
          "action_value": "1",
          "action_date": "2023-01-01"
        },
        {
          "action_name": "complete_task",
          "action_value": "1",
          "action_date": "2023-01-01"
        },
        {
          "action_name": "login",
          "action_value": "1",
          "action_date": "2023-01-01"
        }
      ]
    }
  ]
}
"""