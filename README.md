# Demo of OpenAI API for GPT with Vision

## Setup
https://platform.openai.com/docs/guides/vision
```
npm install openai

pip install --upgrade openai
pip install python-dotenv
```

## Using the "openai" library
```
> node demo/openai.js
{
  id: 'chatcmpl-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  object: 'chat.completion',
  created: 1705263040,
  model: 'gpt-4-1106-vision-preview',
  usage: { prompt_tokens: 782, completion_tokens: 113, total_tokens: 895 },
  choices: [
    {
      message: {
        role: 'assistant',
        content: `The image appears to be a pixelated graphic with a traditional or old-school tattoo style design. It features a heart in the center with green leaves on both sides. Across the heart, there's a banner with the text "September '23" written on it, suggesting a date or event in September 2023. Below the heart, there's additional text that says "OLD SCHOOL," which likely refers to the aesthetic style of the design. The background of the graphic is dark, likely black or dark navy blue, which makes the brightly colored design stand out.`
      },
      finish_reason: 'stop',
      index: 0
    }
  ]
}

> python -m demo.openai
ChatCompletion(id='chatcmpl-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX', choices=[Choice(finish_reason='stop', index=0, message=ChatCompletionMessage(content='This image features a pixelated design with a school or retro theme. In the center, there\'s a large red heart with green leaves on either side. Overlapping the heart is a banner that reads "September \'23" in yellow letters with black outlines. Below the heart, the text "OLD SCHOOL" is visible in red, on a dark background that seems to be navy or black. The overall look has a nostalgic or old-fashioned vibe, perhaps suggesting a school reunion or a throwback event taking place in September 2023.', role='assistant', function_call=None, tool_calls=None))], created=1705263108, model='gpt-4-1106-vision-preview', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=108, prompt_tokens=782, total_tokens=890))
```

## Using the "requests" library
```
> python -m demo.requests
{'id': 'chatcmpl-XXXXXXXXXXXXXXXXXXXXXXXXXXXXX', 'object': 'chat.completion', 'created': 1705263134, 'model': 'gpt-4-1106-vision-preview', 'usage': {'prompt_tokens': 782, 'completion_tokens': 122, 'total_tokens': 904}, 'choices': [{'message': {'role': 'assistant', 'content': 'The image depicts a pixel art design featuring a red heart with a banner across it. The banner reads "SeptembIT \'23" in stylized text, suggesting an event or celebration planned for September 2023, possibly related to the field of information technology (IT). Below the heart and banner, the words "OLD SCHOOL" are written, which may imply a theme or appreciation for retro or traditional styles and values. The heart is adorned with green leaves, adding a classic decorative touch to the design. The overall aesthetic suggests a vintage or nostalgic sentiment, and the design is set against a dark background.'}, 'finish_reason': 'stop', 'index': 0}]}
```
