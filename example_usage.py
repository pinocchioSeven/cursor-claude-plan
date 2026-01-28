import os
import json
from dotenv import load_dotenv
from src.plan_generator import AIPlanner

load_dotenv()

def main():
    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model_name = os.getenv("MODEL_NAME")

    if not api_key or not base_url or not model_name:
        print("错误：.env文件中缺少API_KEY、BASE_URL或MODEL_NAME")
        return

    print(f"使用模型: {model_name}")
    print(f"API 地址: {base_url.strip()}")

    planner = AIPlanner(
        api_key=api_key,
        base_url=base_url,
        model=model_name
    )

    print("\n请输入编程任务（例如：Add user login API）:")
    user_request = input("> ").strip()

    if not user_request:
        print("未输入任务，程序退出。")
        return

    try:
        print("\n正在生成 Plan...")
        plan = planner.generate_plan(user_request)

        print("\n生成成功！Plan 如下：")
        print(json.dumps(plan, indent=2, ensure_ascii=False))

        with open("plan_output.json", "w", encoding="utf-8") as f:
            json.dump(plan, f, indent=2, ensure_ascii=False)
        print("\n已保存到 plan_output.json")

    except Exception as e:
        print(f"\n执行出错: {e}")

if __name__ == "__main__":
    main()