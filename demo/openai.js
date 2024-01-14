const OpenAI = require("openai");
const fs = require("fs");
const dotenv = require("dotenv");

dotenv.config();

const openai = new OpenAI();

function encodeImage(imagePath) {
  return fs.readFileSync(imagePath, { encoding: "base64" });
}

async function goImage({ imagePath, detail }) {
  const ext = imagePath.split(".").pop().toLowerCase();
  let tag;
  if (ext === "jpg" || ext === "jpeg") {
    tag = "jpeg";
  } else if (ext === "png") {
    tag = "png";
  } else {
    throw new Error("Unsupported image type");
  }

  const base64Image = encodeImage(imagePath);
  const model = "gpt-4-vision-preview";

  const ROLE_SYSTEM = "system";
  const ROLE_USER = "user";

  const response = await openai.chat.completions.create({
    model: model,
    // `maxTokens` affects price even if not used to capacity
    // https://platform.openai.com/docs/guides/rate-limits/reduce-the-max_tokens-to-match-the-size-of-your-completions
    max_tokens: 200,
    messages: [
      {
        role: ROLE_SYSTEM,
        content: [{
          type: "text",
          text: "What's in this image?",
        }],
      },
      {
        role: ROLE_USER,
        content: [{
          type: "image_url",
          image_url: {
            url: `data:image/${tag};base64,${base64Image}`,
            detail: detail,
          },
        }],
      },
    ],
  });

  console.dir(response, { depth: null });
}

async function main() {
  await goImage({
    imagePath: "data/sample.png",
    detail: "auto",
  });
}

main();
