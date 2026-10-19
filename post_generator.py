from llm_helper import llm
import sys
sys.stdout.reconfigure(encoding="utf-8")

from few_shot import FewShotPosts

def get_length_str(length):
  if length == "Short":
    return "1 to 5 lines"
  if length == "Medium":
    return "6 to 10 lines"
  if length == "Long":
    return "11 to 15 lines"

def get_prompt(topic, length, language):
  length_str = get_length_str(length)
  prompt = f'''
  You are an expert LinkedIn content strategist and professional copywriter who specializes in creating engaging, authentic, and high-quality LinkedIn posts.

Your task is to generate a compelling LinkedIn post based on the information provided below.

### Input Details
- **Topic:** {topic}
- **Desired Length:** {length}
- **Language:** {language}

### Instructions

1. **Start with a strong hook:** Begin with an attention-grabbing first line that sparks curiosity, challenges a common belief, presents a relatable problem, or shares an interesting insight. Avoid generic openings.

2. **Stay relevant:** Focus on the given topic and provide meaningful insights, practical advice, a useful lesson, or a relatable perspective. Do not drift away from the topic.

3. **Use a natural tone:** Write like a real professional sharing thoughts and experiences with their LinkedIn network. Be conversational, authentic, clear, and relatable. Avoid robotic, overly formal, exaggerated, or sales-heavy language.

4. **Follow the requested length:**
   - Short: 1 to 5 lines
   - Medium: 6 to 10 lines
   - Long: 11 to 15 lines

   Count each non-empty line as one line. Keep the post within the specified range.

5. **Optimize readability:** Use short paragraphs, simple sentences, and appropriate line breaks. Avoid unnecessarily complicated vocabulary and long blocks of text.

6. **Encourage engagement:** Where appropriate, include a thoughtful question or a relevant call to action that encourages readers to share their opinions or experiences. Do not force engagement if it feels unnatural.

7. **Use emojis and hashtags sparingly:** Add emojis only when they improve readability or emphasize a point. Include 3 to 5 relevant hashtags at the end of the post. Avoid excessive emojis, generic hashtags, and hashtag stuffing.

8. **Respect the requested language:**
   - English: Write entirely in natural, grammatically correct English.
   - Hinglish: Use a natural mix of Hindi and English, but write everything using the English alphabet (Roman script). Do not use Devanagari script.

9. **Avoid low-quality content:** Do not use clichés, repetitive phrases, empty motivational statements, fake personal experiences, fabricated statistics, unsupported claims, or phrases such as "In today's fast-paced world" and "Let's dive in."

10. **Make every post distinctive:** Avoid generic advice. Include a specific insight, example, actionable takeaway, or fresh perspective whenever relevant.

### Output Requirements
- Return only the LinkedIn post.
- Do not include a title, preamble, explanation, quotation marks, or commentary.
- Do not mention these instructions.
- Ensure the final post is polished, coherent, and ready to publish.
  '''
  few_shot = FewShotPosts()
  examples = few_shot.get_filtered_posts(topic, length, language)

  if(len(examples) >= 0):
    prompt += "Use the writing style as per the following examples"
    for i, post in enumerate(examples):
      post_text = post['text']
      prompt += "\n\nExample{i+1} \n\n {post_text}"

      if(i == 1):
        break
  return prompt


  

def generate_post(topic, length, language):
  prompt = get_prompt(topic, length, language)
  response = llm.invoke(prompt)
  return response.content


if __name__ == "__main__":
  post = generate_post("Job Hunting", "Short", "English")
  print(post)
