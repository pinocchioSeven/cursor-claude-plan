import json
from openai import OpenAI
from .prompts import PLAN_SYSTEM_PROMPT, build_user_prompt

class AIPlanner:
    def __init__(self, api_key: str, base_url: str, model: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url.strip()
        )
        self.model = model

    def generate_plan(self, user_request: str) -> dict:
        messages = [
            {"role": "system", "content": PLAN_SYSTEM_PROMPT},
            {"role": "user", "content": build_user_prompt(user_request)}
        ]

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            response_format={"type": "json_object"},
            temperature=0.0,
            max_tokens=1000
        )

        try:
            plan = json.loads(response.choices[0].message.content)
            return plan
        except json.JSONDecodeError as e:
            raise ValueError(f"LLM returned invalid JSON: {e}")