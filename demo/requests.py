import base64
import dotenv
import os
import requests

from typing import Literal


dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def encode_image(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def go_image(
    *,
    image_path: str,
    detail: Literal["low", "high", "auto"],
) -> None:
    _, ext = os.path.splitext(image_path)
    ext = ext.lower()
    base64_image = encode_image(image_path)

    tag: str
    if ext == ".jpg" or ext == ".jpeg":
        tag = "jpeg"
    elif ext == ".png":
        tag = "png"
    else:
        raise Exception("Unsupported image type")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image?",
                    },
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/{tag};base64,{base64_image}",
                            "detail": detail,
                        },
                    },
                ],
            },
        ],
    }

    endpoint = "https://api.openai.com/v1/chat/completions"
    response = requests.post(endpoint, headers=headers, json=payload)

    print(response.json())


def main():
    go_image(
        image_path="data/sample.png",
        detail="auto",
    )


if __name__ == "__main__":
    main()
