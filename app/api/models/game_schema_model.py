from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field
# default_game_schema
from app.api.models.game_schema_default import default_game_schema
class ActionReward(BaseModel):
    action_reward_name: str
    action_reward_description: str
    action_reward_due_date: Optional[date] = Field(None, alias="action_due_date")
    max_reward: Optional[int] = None
    action_reward_formula: str

    class Config:
        json_encoders = {
            date: lambda v: v.isoformat(),
        }


class GameSchema(BaseModel):
    actions_values: List[str] = Field(default_factory=lambda: ["contribution", "moderator_evaluation", "complete_task", "login"])
    actions_rewards: List[ActionReward]
    reward_formula: str
