from typing import List, Optional
from datetime import date
from pydantic import BaseModel, Field

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
    actions_values: List[str]
    actions_rewards: List[ActionReward]
    reward_formula: str


"""
Example of a game schema:
{
  "actions_values":[
    "contribution",
    "moderator_evaluation",
    "complete_task",
    "login"
  ],
  "actions_rewards": [
    {
      "action_reward_name": "contribution_actions",
      "action_reward_description": "contribution to the project",
      "action_reward_due_date": "2023-01-01",
      "max_reward": "100",
      "action_reward_formula": "[contribution] * 0.1"
    },
    {
      "action_action_reward_namename": "evaluation_by_moderator",
      "action_reward_description": "moderator evaluation",
      "action_due_date": null,
      "max_reward": "100",
      "action_reward_formula": "[moderator_evaluation] * 0.5"
    },
    {
      "action_reward_name": "tasks_completed",
      "action_reward_description": "completed task",
      "action_due_date": "2023-01-01",
      "max_reward": "100",
      "action_reward_formula": "[completed_task] * 0.5"
    },
    {
      "action_reward_name": "login_times",
      "action_reward_description": "login",
      "action_due_date": null,
      "max_reward": null,
      "action_reward_formula": "[login] * 0.1"
    }
  ],
  "reward_formula": "[contribution_actions] + [evaluation_by_moderator] + [tasks_completed] + [login_times]"
}
"""
