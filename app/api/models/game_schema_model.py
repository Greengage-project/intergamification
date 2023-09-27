from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, EmailStr
# default_game_schema
from app.api.models.default_data_model import default_game_schema


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


class CreatedBy(BaseModel):
    exp: Optional[datetime] = None
    iat: Optional[datetime] = None
    auth_time: Optional[datetime] = None
    jti: Optional[str] = None
    iss: Optional[str] = None
    aud: Optional[str] = None
    sub: Optional[str] = None
    typ: Optional[str] = None
    azp: Optional[str] = None
    nonce: Optional[str] = None
    session_state: Optional[str] = None
    at_hash: Optional[str] = None
    acr: Optional[str] = None
    sid: Optional[str] = None
    email_verified: Optional[bool] = None
    name: Optional[str] = None
    preferred_username: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    email: Optional[EmailStr] = None


class GameSchema(BaseModel):
    actions_values: List[str] = Field(default_factory=lambda: [
                                      "contribution", "moderator_evaluation", "complete_task", "login"])
    actions_rewards: List[ActionReward]
    reward_formula: str
    recomended: Optional[bool] = False
    created_by: Optional[CreatedBy] = None
