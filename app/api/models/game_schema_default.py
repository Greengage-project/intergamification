default_game_schema = {
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
            "action_reward_name": "evaluation_by_moderator",
            "action_reward_description": "moderator evaluation",
            "action_due_date": None,
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
            "action_due_date": None,
            "max_reward": None,
            "action_reward_formula": "[login] * 0.1"
        }
    ],
    "reward_formula": "[contribution_actions] + [evaluation_by_moderator] + [tasks_completed] + [login_times]"
}