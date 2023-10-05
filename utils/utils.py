from pypinyin import pinyin, lazy_pinyin, Style
import openai
from decouple import config
import g4f

def transName(name):
    nameSpell = lazy_pinyin(name,style=Style.NORMAL)
    nameSpell = " ".join(nameSpell)
    return nameSpell


# g4f free openai api
# gpt-3.5-turbo, gpt-4
# def getRecommand(year, sex, name, model="gpt-4"):

#     nameSap = transName(name)

#     response = g4f.ChatCompletion.create(
#         stream=False,
#         model=model,
#         messages=[
#             {
#                 "role": "user", 
#                 "content": "接下來我會給你一個嬰兒的出生年份、它中文姓名的讀音、它的性別，請建議它五個適合的英文名字，這些名字需要與它的名字的中文發音相似，適合它的性別，並且符合它的出生年代，請只輸出5個英文名字，不需要額外其他資訊',"
#             },
#             {
#                 "role": "user",
#                 "content": "2000, male, bo jun"
#             },
#             {
#                 "role": "assistant",
#                 "content": 'Bowen, Bob, Bryan, Johan, Jon'
#             },
#             {
#                 "role": "user",
#                 "content": f"{year}, {sex}, {nameSap}"
#             },
#         ],
#     )
#     print(response)
#     returnContent = list(response.split(", "))

#     return returnContent


def getRecommand(year, sex, name, model="gpt-3.5-turbo"):

    nameSap = transName(name)

    openai.api_key = config('OPENAI_API_KEY')
    openai.api_base = config('OPENAI_API_BASE')

    chat_completion = openai.ChatCompletion.create(
        stream=False,
        model=model,
        messages=[
            {
                "role": "user", 
                "content": "接下來我會給你一個嬰兒的出生年份、它中文姓名的讀音、它的性別，請建議它五個適合的英文名字，這些名字需要與它的名字的中文發音相似，適合它的性別，並且符合它的出生年代，請只輸出5個英文名字，不需要額外其他資訊',"
            },
            {
                "role": "user",
                "content": "2000, male, bo jun"
            },
            {
                "role": "assistant",
                "content": 'Bowen, Bob, Bryan, Johan, Jon'
            },
            {
                "role": "user",
                "content": f"{year}, {sex}, {nameSap}"
            },
        ],
    )

    returnContent = chat_completion['choices'][0]['message']['content']
    returnContent = list(returnContent.split(", "))

    return returnContent