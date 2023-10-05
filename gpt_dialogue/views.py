from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.views.decorators.csrf import csrf_exempt
import requests
from .models import Dialogue
import openai

openai.api_key = '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'

# class Dialogue(models.Model):
#     context = models.TextField()
#     user_input = models.TextField()
#     model_response = models.TextField()

def generate_model_response(context, user_input):
    # 调用 OpenAI GPT-3 API 进行对话生成
    response = openai.Completion.create(
        engine='text-davinci-003',  # 指定使用的 GPT-3 模型引擎
        prompt=context + user_input,  # 拼接 context 和 user_input 作为输入
        max_tokens=2000,  # 生成的最大长度（令牌数）
        temperature=0.7,  # 控制生成文本的多样性，值越大越随机，值越小越保守
        n = 1,  # 生成多个响应的数量
        stop=None,  # 指定停止生成的条件，例如可以使用 'stop=["\n"]' 来在换行符处停止生成
        timeout=10,  # API 超时时间（秒）
    )

    # 提取生成的模型响应
    model_response = response.choices[0].text.strip()

    return model_response


@csrf_exempt
# def dialogue(request):
#     if request.method == 'POST':
#         context = request.POST.get('context', '')  # 获取用户自定义的 context 信息
#         user_input = request.POST.get('user_input', '')  # 获取用户输入的对话内容

#         if user_input:
#             # 调用大语言模型 API 进行对话生成
#             # 将 context 和 user_input 发送给大语言模型 API，获取模型生成的响应
#             # 请在下面的代码中替换为您的大语言模型 API 调用代码
#             model_response = generate_model_response(context, user_input)

#             # 将对话记录保存到数据库
#             dialogue = Dialogue(context=context, user_input=user_input, model_response=model_response)
#             dialogue.save()

#             return render(request, 'dialogue.html', {'model_response': model_response})

#     return render(request, 'dialogue.html')


def dialogue(request):
    if request.method == 'POST':
        context = request.POST.get('context', '')  # 获取用户自定义的 context 信息
        user_input = request.POST.get('user_input', '')  # 获取用户输入的对话内容

        if user_input:
            # 调用大语言模型 API 进行对话生成
            # 将 context 和 user_input 发送给大语言模型 API，获取模型生成的响应
            # 请在下面的代码中替换为您的大语言模型 API 调用代码
            model_response = generate_model_response(context, user_input)

            # 将对话记录保存到数据库
            dialogue = Dialogue(context=context, user_input=user_input, model_response=model_response)
            dialogue.save()

            return render(request, 'dialogue.html', {'model_response': model_response})

    # 如果不是 POST 请求，返回一个空的 HttpResponse
    return HttpResponse()


