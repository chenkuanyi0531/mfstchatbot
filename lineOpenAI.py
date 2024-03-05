import os  
import openai  
import json  
  
# 讀取模型配置  
with open("model_config.json") as f:  
    model_list = json.load(f)  
  
openai.api_key =os.getenv("AZURE_OPENAI_API_KEY")
openai.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")  # 您的 endpoint 應該類似於 https://YOUR_RESOURCE_NAME.openai.azure.com/  
openai.api_type = 'azure'  
openai.api_version = os.getenv("AZURE_OPENAI_API_VERSION")  # 這可能會在未來變更  
model =os.getenv("AZURE_OPENAI_MODEL")
  
# 初始化一個空的訊息歷史列表  
messages_history = [  
    {"role": "system", "content": "你是一位智能小幫手，協助處理問題，請說繁體中文，數學公式請直接寫純數字"},  
]  
print(messages_history)
  
def GPT_response(text):       
    # 將用戶的請求添加到歷史紀錄中  
    messages_history.append({"role": "user", "content": text})  
      
    response = openai.ChatCompletion.create(  
        engine=model,  
        messages=messages_history,  # 將帶有歷史紀錄的列表發送給模型  
        temperature=0.9,  
        max_tokens=1000,  
        top_p=0.95  
    )  
      
    # 將模型的回應也添加到歷史紀錄中  
    messages_history.append({"role": "assistant", "content": response['choices'][0]['message']['content']})  
    #print(messages_history)
    return response['choices'][0]['message']['content']  
