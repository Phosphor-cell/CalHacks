import requests
import os
import openai
from dotenv import load_dotenv




# Load environment variables
load_dotenv()
api_key = os.getenv("OPEN_AI_KEY")
openai.api_key = "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"






def queryTwo(pOne, pTwo, pThree):
    emailBackground = [{
            "role": "system",
            "content": f"""
            I need you to give me a search query on google for how to find support for this in Calgary, Alberta. 
            I only want the search query and nothing else. Just what I would put into google to find immigrant support for these in Calgary.
            """
    }]


    #Getting response one:
    emailBackground.append({"role": "user", "content": pOne})
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=emailBackground)
    p1= response.choices[0].message.content
    print(p1)

    #Getting response two:
    emailBackground.append({"role": "user", "content": pTwo})
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=emailBackground)
    p2= response.choices[0].message.content
    print(p2)

    #Getting response three:
    emailBackground.append({"role": "user", "content": pThree})
    response = openai.chat.completions.create(model="gpt-4o-mini", messages=emailBackground)
    p3= response.choices[0].message.content
    print(p3)
    
    
    return p1,p2,p3