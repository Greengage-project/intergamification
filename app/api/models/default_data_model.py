default_game_schema = {
    "game_schema_id": "1",
    "actions_values": [
        "contribution_score",
        "moderator_evaluation_score",
    ],
    "actions_rewards": [
        {
            "action_reward_name": "contribution_action",
            "action_reward_title": "Contribution",
            "action_reward_description": "contribution to the project by the user ",
            "action_reward_formula": "[contribution_score] * 1 *(complexity_score/100)",
            "max_reward": 1000
        },
        {
            "action_reward_name": "evaluation_by_moderator",
            "action_reward_title": "Evaluation by moderator",
            "action_reward_description": "evaluation by moderator of the contribution to the project",
            "action_reward_formula": "[moderator_evaluation_score] * 1 *(complexity_score/100)",
            "max_reward": None
        }
    ],
    "milestones": [
        {
            "milestone_name": "Become a contributor",
            "milestone_description": "5 contributions",
            "milestone_formula": "[contribution_action] >= 5",
            "rewardPoints": 100,
            "badge": "Beginner contributor"
        },
        {
            "milestone_name": "Become a intermediate contributor",
            "milestone_description": "20 contributions",
            "milestone_formula": "[contribution_action] >= 10",
            "rewardPoints": 200,
            "badge": "Intermediate contributor"
        },
        {
            "milestone_name": "Become a advanced contributor",
            "milestone_description": "50 contributions",
            "milestone_formula": "[contribution_action] >= 15",
            "rewardPoints": 300,
            "badge": "Advanced contributor"
        },
        {
            "milestone_name": "Become a expert contributor",
            "milestone_description": "100 contributions",
            "milestone_formula": "[contribution_action] >= 20",
            "rewardPoints": 400,
            "badge": "Expert contributor"
        }
    ],

    "reward_formula": "[contribution_action] + [evaluation_by_moderator]",
    "title": "Game schema 1",
    "description": "Game schema 1 description",
    "tags": [
        "tag1",
        "tag2"
    ],
}


default_new_game_instance = {
    "processId": "changeThis",
    "gameSchemaId": "changeThis",
    "tasks":   [
        {
            "task_id": "e3a09f07-98f3-4dc4-988f-aee41ebcab1c",
            "variables": [
                {
                    "complexityScore": 100
                }
            ],
        }
    ]
}
