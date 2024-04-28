[![Streamlit](https://img.shields.io/badge/Streamlit-Webapp-green)](https://detext.streamlit.app/)

## Identifying AI-Generated Text at a Glance

ChatGPT often uses sophisticated or unfamiliar vocabulary, as do other open-source language models like Mistral. While using AI to generate content is ethical if done responsibly, it can sometimes be difficult to discern AI-written text. For instance, during a science-writing contest for 14-16 year-olds, a judge became suspicious upon encountering the phrase "Labyrinthian mazes," suspecting it was too sophisticated for the age group. Subsequent checks with AI detection tools confirmed that nearly the entire essay was AI-generated, ranging from 90-96%. This highlights the importance of critical thinking in identifying AI-authored texts.

Spotting AI-generated text might involve looking for less commonly used words. For example, a search in the [NOW corpus](https://www.english-corpora.org/now/) for the word "delve" revealed its usage had surged by approximately 200% in 2022, coinciding with the release of ChatGPT. Similar trends were noticed for words like "intricacies" and "unwavering."
![Trend of intricacies and unwavering in [NOW](https://www.english-corpora.org/now/) Corpus (by Fareed Khan)](https://cdn-images-1.medium.com/max/6512/1*EgrevS32vUy4eKx3F__oog.png)

This vocabulary isn't exclusive to AI; humans also use these words, particularly in academic writing. However, AI models like ChatGPT often suggest them. In an analysis of the [arXiv database](https://www.kaggle.com/datasets/Cornell-University/arxiv), the word "delve" appeared significantly in 2023 abstracts, suggesting possible AI usage.

To assist in detecting AI-written content, I've compiled [a list of 180+ words to watch for](ai_words.txt) and created a [web app](https://detext.streamlit.app/) that quickly analyzes texts and documents to determine if they might have been AI-generated or altered.

Enjoy the exploration!
