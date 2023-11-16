# Demo of OpenAI API for GPT with Vision

## Setup
https://platform.openai.com/docs/guides/vision
```
pip install --upgrade openai
pip install python-dotenv
```

## Using the "openai" library
```
> python -m demo.openai
ChatCompletion(id='chatcmpl-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX', choices=[Choice(finish_reason=None, index=0, message=ChatCompletionMessage(content='This image features a pixel art style graphic which includes a central red heart with green', role='assistant', function_call=None, tool_calls=None), finish_details={'type': 'max_tokens'})], created=1700150548, model='gpt-4-1106-vision-preview', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=16, prompt_tokens=782, total_tokens=798))
```

## Using the "requests" library
```
> python -m demo.requests
{'id': 'chatcmpl-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'object': 'chat.completion', 'created': 1700150516, 'model': 'gpt-4-1106-vision-preview', 'usage': {'prompt_tokens': 782, 'completion_tokens': 16, 'total_tokens': 798}, 'choices': [{'message': {'role': 'assistant', 'content': 'This is a pixelated image featuring a heart with a ribbon across it. The'}, 'finish_details': {'type': 'max_tokens'}, 'index': 0}]}
```
