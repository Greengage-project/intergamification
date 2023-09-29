from typing import List, Optional
from pydantic import BaseModel, Field
from .jwt_model import JWT_data
# default_game_schema


class ActionReward(BaseModel):
    action_reward_name: str
    action_reward_title: str
    action_reward_description: str
    action_reward_formula: str
    max_reward: Optional[int] = None


class Milestone(BaseModel):
    milestone_name: str
    milestone_description: str
    milestone_formula: str
    rewardPoints: int
    badge: str


class GameSchemaBase(BaseModel):
    actions_values: List[str]
    actions_rewards: List[ActionReward]
    reward_formula: str
    milestones: List[Milestone]
    recomended: Optional[bool] = False
    createdBy: Optional[JWT_data] = None
    title: str
    description: str
    tags: List[str]
