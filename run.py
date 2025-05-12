from utils import clean_trending_html, clean_content_html
from chains import translate_chain, formatter_chain
from graph import graph

from langchain_core.messages import HumanMessage

import requests
import re
import os

import json

from datetime import datetime
from pathlib import Path

flags = re.DOTALL

max_retries = 2

save_dir = Path(__file__).resolve().parent / "records"

os.makedirs(save_dir, exist_ok=True)

dtime = datetime.now()
save_path = os.path.join(str(save_dir), f"{dtime.year}-{dtime.month}-{dtime.day}.json")

print(save_path)


base_url = "https://github.com/trending"


def main():
    response = requests.get(base_url)

    assert int(response.status_code) == 200

    records = clean_trending_html(response.text)
    
    results = []

    for tid, record in enumerate(records, 1):
        config = {"configurable": {"thread_id": f"{tid}"}}
        response = requests.get(record['link'])
        assert int(response.status_code) == 200
        try:
            doc = clean_content_html(response.text)
        except Exception as e:
            continue

        retry_nums = 0

        while retry_nums < max_retries:
            try:
                response = graph.invoke(
                    {"messages": [HumanMessage(content=doc)]},
                    config=config
                )
                break  # 成功执行后退出循环
            except Exception as e:
                print(f"Attempt {retry_nums + 1} failed: {str(e)}")
                # 获取最新的有效配置
                state_history = list(graph.get_state_history(config))
                if state_history:
                    config = state_history[-1].config
                retry_nums += 1
                # 可添加延时逻辑（如 time.sleep）
                if retry_nums == max_retries:
                    raise RuntimeError(f"Failed after {max_retries} attempts")

        print("========================= Translate ===================================")
        translated_response = re.sub(r"<think>.*?</think>", "", translate_chain.invoke({"docs":response['messages'][-1].content}), flags=flags)
        print(translated_response.strip())
        print(record['link'])
        
        results.append(
            {"link": record['link'], "content": translated_response, "title": record['link'].split("/")[-1]}
        )
    
    with open(save_path, "w") as f:
        json.dump(results, f, indent=4)


if __name__ == "__main__":
    main()


