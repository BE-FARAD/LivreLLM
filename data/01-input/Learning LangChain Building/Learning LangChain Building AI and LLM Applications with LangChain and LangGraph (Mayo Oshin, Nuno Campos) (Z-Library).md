![](_page_0_Picture_0.jpeg)

![](_page_0_Picture_3.jpeg)

## Praise for *Learning LangChain*

*With clear explanations and actionable techniques, this is the go-to resource for anyone looking to harness LangChain's power for production-ready generative AI and agents. A must-read for developers aiming to push the boundaries of this platform.*

—Tom Taulli, IT consultant and author of *AI-Assisted Programming*

*This comprehensive guide on LangChain covers everything from document retrieval and indexing to deploying and monitoring AI agents in production. With engaging examples, intuitive illustrations, and hands-on code, this book made learning LangChain interesting and fun!*

—Rajat K. Goel, senior software engineer, IBM

*This book is a comprehensive LLM guide covering fundamentals to production, packed with technical insights, practical strategies, and robust AI patterns.*

—Gourav Singh Bais, senior data scientist and senior technical content writer, Allianz Services

*Prototyping generative AI apps is easy—shipping them is hard. The strategies and tools in Learning LangChain make it possible to turn ideas into modern, production-ready applications.*

> —James Spiteri, director of product management for security, Elastic

*Learning LangChain provides a clear path for transforming how you build AI-powered applications. By breaking down flexible architectures and robust checkpointing, it offers a strong foundation for creating reliable, production-ready AI agents at scale.*

—David O'Regan, engineering manager for AI/ML, GitLab

*Learning LangChain helped us skip the boilerplate for debugging and monitoring. The many helpful patterns and tooling insights allowed us to move fast and deploy AI apps with confidence.*

—Chris Focke, chief AI scientist, AppFolio

*Teaching LangChain through clear, actionable examples, this book is a gateway to agentic applications that are as inspiring as Asimov's sci-fi novels.*

— Ilya Meyzin, SVP head of data science, Dun & Bradstreet

## Learning LangChain

Building AI and LLM Applications with LangChain and LangGraph

Mayo Oshin and Nuno Campos

![](_page_4_Picture_3.jpeg)

## Learning LangChain

by Mayo Oshin and Nuno Campos

Copyright © 2025 Olumayowa "Mayo" Olufemi Oshin. All rights reserved.

Printed in the United States of America.

Published by O'Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.

O'Reilly books may be purchased for educational, business, or sales promotional use. Online editions are also available for most titles (*[http://oreilly.com](http://oreilly.com/)*). For more information, contact our corporate/institutional sales department: 800-998-9938 or *corporate@oreilly.com*.

- Acquisitions Editor: Nicole Butterfield
- Development Editor: Corbin Collins
- Production Editor: Clare Laylock
- Copyeditor: nSight, Inc.
- Proofreader: Helena Stirling
- Indexer: Judith McConville
- Interior Designer: David Futato
- Cover Designer: Karen Montgomery
- Illustrator: Kate Dullea
- February 2025: First Edition

## Revision History for the First Edition

2024-02-13: First Release

See *<http://oreilly.com/catalog/errata.csp?isbn=9781098167288>* for release details.

The O'Reilly logo is a registered trademark of O'Reilly Media, Inc. *Learning LangChain*, the cover image, and related trade dress are trademarks of O'Reilly Media, Inc.

The views expressed in this work are those of the authors and do not represent the publisher's views. While the publisher and the authors have used good faith efforts to ensure that the information and instructions contained in this work are accurate, the publisher and the authors disclaim all responsibility for errors or omissions, including without limitation responsibility for damages resulting from the use of

or reliance on this work. Use of the information and instructions contained in this work is at your own risk. If any code samples or other technology this work contains or describes is subject to open source licenses or the intellectual property rights of others, it is your responsibility to ensure that your use thereof complies with such licenses and/or rights.

978-1-098-16728-8

[LSI]

## <span id="page-8-0"></span>Preface

<span id="page-8-3"></span><span id="page-8-1"></span>On November 30, 2022, San Francisco–based firm OpenAI publicly released [ChatGPT](https://oreil.ly/uAnsr)—the viral AI chatbot that can generate content, answer questions, and solve problems like a human. Within two months of its launch, ChatGPT attracted over 100 million [monthly](https://oreil.ly/ATsLe) active users, the fastest adoption rate of a new consumer technology application (so far). ChatGPT is a chatbot experience powered by an instruction and dialoguetuned version of OpenAI's GPT-3.5 family of large language models (LLMs). We'll get to definitions of these concepts very shortly.

#### **NOTE**

<span id="page-8-4"></span><span id="page-8-2"></span>Building LLM applications with or without LangChain requires the use of an LLM. In this book we will be making use of the OpenAI API as the LLM provider we use in the code examples (pricing is listed on its [platform\)](https://oreil.ly/-YYoR). One of the benefits of working with LangChain is that you can follow along with all of these examples using either OpenAI or alternative commercial or open source LLM providers.

Three months later, OpenAI released the [ChatGPT](https://oreil.ly/DwU7R) API, giving developers access to the chat and speech-to-text capabilities. This kickstarted an uncountable number of new applications

<span id="page-9-1"></span>and technical developments under the loose umbrella term of *generative AI*.

<span id="page-9-3"></span><span id="page-9-0"></span>Before we define generative AI and LLMs, let's touch on the concept of *machine learning* (ML). Some computer *algorithms* (imagine a repeatable recipe for achievement of some predefined task, such as sorting a deck of cards) are directly written by a software engineer. Other computer algorithms are instead *learned* from vast amounts of training examples—the job of the software engineer shifts from writing the algorithm itself to writing the training logic that creates the algorithm. A lot of attention in the ML field went into developing algorithms for predicting any number of things, from tomorrow's weather to the most efficient delivery route for an Amazon driver.

<span id="page-9-4"></span>With the advent of LLMs and other generative models (such as diffusion models for generating images, which we don't cover in this book), those same ML techniques are now applied to the problem of generating new content, such as a new paragraph of text or drawing, that is at the same time unique and informed by examples in the training data. LLMs in particular are generative models dedicated to generating text.

<span id="page-9-2"></span>LLMs have two other differences from previous ML algorithms:

- They are trained on much larger amounts of data; training one of these models from scratch would be very costly.
- They are more versatile.

The same text generation model can be used for summarization, translation, classification, and so forth, whereas previous ML models were usually trained and used for a specific task.

These two differences conspire to make the job of the software engineer shift once more, with increasing amounts of time dedicated to working out how to get an LLM to work for their use case. And that's what LangChain is all about.

<span id="page-10-4"></span><span id="page-10-3"></span><span id="page-10-1"></span><span id="page-10-0"></span>By the end of 2023, competing LLMs emerged, including Anthropic's Claude and Google's Bard (later renamed Gemini), providing even wider access to these new capabilities. And subsequently, thousands of successful startups and major enterprises have incorporated generative AI APIs to build applications for various use cases, ranging from customer support chatbots to writing and debugging code.

<span id="page-10-2"></span>On October 22, 2022, Harrison Chase [published](https://oreil.ly/mCdYZ) the first commit on GitHub for the LangChain open source library. LangChain started from the realization that the most interesting LLM

applications needed to use LLMs together with "other sources of computation or [knowledge". For](https://oreil.ly/uXiPi) instance, you can try to get an LLM to generate the answer to this question:

How many balls are left after splitting 1,234 bal

You'll likely be disappointed by its math prowess. However, if you pair it up with a calculator function, you can instead instruct the LLM to reword the question into an input that a calculator could handle:

1,234 % 123

Then you can pass that to a calculator function and get an accurate answer to your original question. LangChain was the first (and, at the time of writing, the largest) library to provide such building blocks and the tooling to reliably combine them into larger applications. Before discussing what it takes to build compelling applications with these new tools, let's get more familiar with LLMs and LangChain.

## <span id="page-11-0"></span>Brief Primer on LLMs

<span id="page-12-6"></span><span id="page-12-3"></span><span id="page-12-1"></span>In layman's terms, LLMs are trained algorithms that receive text input and predict and generate humanlike text output. Essentially, they behave like the familiar autocomplete feature found on many smartphones, but taken to an extreme.

Let's break down the term *large language model*:

- <span id="page-12-7"></span><span id="page-12-4"></span><span id="page-12-0"></span>*Large* refers to the size of these models in terms of training data and parameters used during the learning process. For example, OpenAI's GPT-3 model contains 175 billion *parameters*, which were learned from training on 45 terabytes of text data. *Parameters* in a neural network model are made up of the numbers that control the output of each *neuron* and the relative weight of its connections with its neighboring neurons. (Exactly which neurons are connected to which other neurons varies for each neural network architecture and is beyond the scope of this book.) **[1](#page-43-0)**
- <span id="page-12-5"></span><span id="page-12-2"></span>*Language model* refers to a computer algorithm trained to receive written text (in English or other languages) and produce output also as written text (in the same language or a different one). These are *neural networks*, a type of ML model which resembles a stylized conception of the human brain, with the final output resulting from the combination of the individual outputs of many simple mathematical functions, called *neurons*, and their interconnections. If many

of these neurons are organized in specific ways, with the right training process and the right training data, this produces a model that is capable of interpreting the meaning of individual words and sentences, which makes it possible to use them for generating plausible, readable, written text.

<span id="page-13-2"></span><span id="page-13-1"></span>Because of the prevalence of English in the training data, most models are better at English than they are at other languages with a smaller number of speakers. By "better" we mean it is easier to get them to produce desired outputs in English. There are LLMs designed for multilingual output, such as [BLOOM,](https://oreil.ly/Nq7w0) that use a larger proportion of training data in other languages. Curiously, the difference in performance between languages isn't as large as might be expected, even in LLMs trained on a predominantly English training corpus. Researchers have found that LLMs are able to transfer some of their semantic understanding to other languages. **[2](#page-43-1)**

<span id="page-13-0"></span>Put together, *large language models* are instances of big, general-purpose language models that are trained on vast amounts of text. In other words, these models have learned from patterns in large datasets of text—books, articles, forums, and other publicly available sources—to perform general textrelated tasks. These tasks include text generation, summarization, translation, classification, and more.

Let's say we instruct an LLM to complete the following sentence:

The capital of England is \_\_\_\_\_\_\_.

The LLM will take that input text and predict the correct output answer as London . This looks like magic, but it's not. Under the hood, the LLM estimates the probability of a sequence of word(s) given a previous sequence of words.

**TIP**

Technically speaking, the model makes predictions based on tokens, not words. A *token* represents an atomic unit of text. Tokens can represent individual characters, words, subwords, or even larger linguistic units, depending on the specific tokenization approach used. For example, using GPT-3.5's tokenizer (called cl100k ), the phrase *good morning dearest friend* would consist of five [tokens](https://oreil.ly/dU83b) (using \_ to show the space character):

*Good*

<span id="page-15-0"></span>With token ID 19045

*\_morning*

With token ID 6693

*\_de*

With token ID 409

*arest*

With token ID 15795

*\_friend*

With token ID 4333

Usually tokenizers are trained with the objective of having the most common words encoded into a single token, for example, the word *morning* is encoded as the token 6693 . Less common words, or words in other languages (usually tokenizers are trained on English text), require several tokens to encode them. For example, the word *dearest* is encoded as tokens 409, 15795 . One token spans on average four characters of text for common English text, or roughly three quarters of a word.

<span id="page-16-2"></span><span id="page-16-1"></span><span id="page-16-0"></span>The driving engine behind LLMs' predictive power is known as the *transformer neural network architecture*. The transformer architecture enables models to handle sequences of data, such as sentences or lines of code, and make predictions about the likeliest next word(s) in the sequence. Transformers are designed to understand the context of each word in a sentence by considering it in relation to every other word. This allows the model to build a comprehensive understanding of the meaning of a sentence, paragraph, and so on (in other words, a sequence of words) as the joint meaning of its parts in relation to each other. **[3](#page-43-2)**

So, when the model sees the sequence of words *the capital of England is*, it makes a prediction based on similar examples it saw during its training. In the model's training corpus the word *England* (or the token(s) that represent it) would have often shown up in sentences in similar places to words like *France*, *United States*, *China*. The word *capital* would figure in the training data in many sentences also containing words like *England*, *France*, and *US*, and words like *London*, *Paris*, *Washington*. This repetition during the model's training resulted in the capacity to correctly predict that the next word in the sequence should be *London*.

<span id="page-17-5"></span><span id="page-17-4"></span>The instructions and input text you provide to the model is called a *prompt*. Prompting can have a significant impact on the quality of output from the LLM. There are several best practices for *prompt design* or *prompt engineering*, including providing clear and concise instructions with contextual examples, which we discuss later in this book. Before we go further into prompting, let's look at some different types of LLMs available for you to use.

<span id="page-17-3"></span><span id="page-17-2"></span><span id="page-17-1"></span>The base type, from which all the others derive, is commonly known as a *pretrained LLM*: it has been trained on very large amounts of text (found on the internet and in books, newspapers, code, video transcripts, and so forth) in a selfsupervised fashion. This means that—unlike in supervised ML, where prior to training the researcher needs to assemble a dataset of pairs of *input* to *expected output*—for LLMs those pairs are inferred from the training data. In fact, the only feasible way to use datasets that are so large is to assemble those pairs from the training data automatically. Two techniques to do this involve having the model do the following:

#### <span id="page-17-0"></span>*Predict the next word*

Remove the last word from each sentence in the training data, and that yields a pair of *input* and *expected output*, such as *The capital of England is \_\_\_* and *London*.

#### *Predict a missing word*

Similarly, if you take each sentence and omit a word from the middle, you now have other pairs of input and expected output, such as *The \_\_\_ of England is London* and *capital*.

These models are quite difficult to use as is, they require you to prime the response with a suitable prefix. For instance, if you want to know the capital of England, you might get a response by prompting the model with *The capital of England is*, but not with the more natural *What is the capital of England?*

### **Instruction-Tuned LLMs**

<span id="page-18-1"></span>[Researchers](https://oreil.ly/lP6hr) have made pretrained LLMs easier to use by further training (additional training applied on top of the long and costly training described in the previous section), also known as *fine-tuning* them on the following:

#### *Task-specific datasets*

<span id="page-18-0"></span>These are datasets of pairs of questions/answers manually assembled by researchers, providing examples of desirable responses to common questions that end users might prompt the model with. For example, the dataset might contain the following pair: *Q: What is the capital of*

*England? A: The capital of England is London.* Unlike the pretraining datasets, these are manually assembled, so they are by necessity much smaller:

*Reinforcement learning from human feedback (RLHF)*

<span id="page-19-1"></span>Through the use of RLHF [methods,](https://oreil.ly/lrlAK) those manually assembled datasets are augmented with user feedback received on output produced by the model. For example, user A preferred *The capital of England is London* to *London is the capital of England* as an answer to the earlier question.

Instruction-tuning has been key to broadening the number of people who can build applications with LLMs, as they can now be prompted with *instructions*, often in the form of questions such as, *What is the capital of England?*, as opposed to *The capital of England is*.

### **Dialogue-Tuned LLMs**

<span id="page-19-0"></span>Models tailored for dialogue or chat purposes are a further enhancement of [instruction-tuned](https://oreil.ly/1DxW6) LLMs. Different providers of LLMs use different techniques, so this is not necessarily true of all *chat models*, but usually this is done via the following:

#### *Dialogue datasets*

<span id="page-20-2"></span><span id="page-20-1"></span>The manually assembled *fine-tuning* datasets are extended to include more examples of multiturn dialogue interactions, that is, sequences of prompt-reply pairs.

#### *Chat format*

<span id="page-20-8"></span><span id="page-20-7"></span><span id="page-20-6"></span><span id="page-20-5"></span><span id="page-20-3"></span><span id="page-20-0"></span>The input and output formats of the model are given a layer of structure over freeform text, which divides text into parts associated with a role (and optionally other metadata like a name). Usually, the roles available are *system* (for instructions and framing of the task), *user* (the actual task or question), and *assistant* (for the outputs of the [model\). This](https://oreil.ly/dINx0) method evolved from early prompt engineering techniques and makes it easier to tailor the model's output while making it harder for models to confuse user input with instructions. Confusing user input with prior instructions is also known as *jailbreaking*, which can, for instance, lead to carefully crafted prompts, possibly including trade secrets, being exposed to end users.

### <span id="page-20-4"></span>**Fine-Tuned LLMs**

<span id="page-21-0"></span>Fine-tuned LLMs are created by taking base LLMs and further training them on a proprietary dataset for a specific task. Technically, instruction-tuned and dialogue-tuned LLMs are fine-tuned LLMs, but the term "fine-tuned LLM" is usually used to describe LLMs that are tuned by the developer for their specific task. For example, a model can be fine-tuned to accurately extract the sentiment, risk factors, and key financial figures from a public company's annual report. Usually, finetuned models have improved performance on the chosen task at the expense of a loss of generality. That is, they become less capable of answering queries on unrelated tasks.

Throughout the rest of this book, when we use the term *LLM*, we mean instruction-tuned LLMs, and for *chat model* we mean dialogue-instructed LLMs, as defined earlier in this section. These should be your workhorses when using LLMs—the first tools you reach for when starting a new LLM application.

<span id="page-21-1"></span>Now let's quickly discuss some common LLM prompting techniques before diving into LangChain.

## Brief Primer on Prompting

<span id="page-22-3"></span>As we touched on earlier, the main task of the software engineer working with LLMs is not to train an LLM, or even to fine-tune one (usually), but rather to take an existing LLM and work out how to get it to accomplish the task you need for your application. There are commercial providers of LLMs, like OpenAI, Anthropic, and Google, as well as open source LLMs [\(Llama,](https://oreil.ly/ld3Fu) [Gemma](https://oreil.ly/RGKfi), and others), released free-of-charge for others to build upon. Adapting an existing LLM for your task is called *prompt engineering*.

<span id="page-22-0"></span>Many prompting techniques have been developed in the past two years, and in a broad sense, this is a book about how to do prompt engineering with LangChain—how to use LangChain to get LLMs to do what you have in mind. But before we get into LangChain proper, it helps to go over some of these techniques first (and we apologize in advance if your favorite [prompting](https://oreil.ly/8uGK_) technique isn't listed here; there are too many to cover).

<span id="page-22-2"></span>To follow along with this section we recommend copying these prompts to the OpenAI Playground to try them yourself:

<span id="page-22-1"></span>1. Create an account for the OpenAI API at *[http://platform.openai.com](http://platform.openai.com/)*, which will let you use OpenAI LLMs programmatically, that is, using the API from your Python or JavaScript code. It will also give you access to the OpenAI Playground, where you can experiment with prompts from your web browser.

- 2. If necessary, add payment details for your new OpenAI account. OpenAI is a commercial provider of LLMs and charges a fee for each time you use their models through OpenAI's API or through Playground. You can find the latest pricing on their [website.](https://oreil.ly/MiKRD) Over the past two years, the price for using OpenAI's models has come down significantly as new capabilities and optimizations are introduced.
- 3. Head on over to the OpenAI [Playground](https://oreil.ly/rxiAG) and you're ready to try out the following prompts for yourself. We'll make use of the OpenAI API throughout this book.
- 4. Once you've navigated to the Playground, you will see a panel of presets on the right side of the screen, including your model of choice. If you look further down the panel, you will see Temperature under the "Model configuration" title. Move the Temperature toggle from middle to left until the number shows 0.00. Essentially, temperature controls the randomness of LLM output. The lower the temperature, the more deterministic the model output.

<span id="page-23-0"></span>Now on to the prompts!

### **Zero-Shot Prompting**

<span id="page-24-0"></span>The first and most straightforward prompting technique consists of simply instructing the LLM to perform the desired task:

How old was the 30th president of the United Stat

This is typically what you should try first, and it will usually work for simple questions, especially when the answer to it was likely present in some of the training data. If we prompt OpenAI's gpt-3.5-turbo with the preceding prompt, the following is returned:

The 30th president of the United States, Calvin C his wife's mother passed away in 1926.

#### **NOTE**

You may get a different result from what we get. There is an element of randomness to how LLMs generate responses, and OpenAI may have updated the model by the time you try it.

While the model did correctly identify the 30th president, the answer isn't quite right. Often you'll have to iterate on prompts and responses to get a reliable system. The next sections expand on how.

### **Chain-of-Thought**

<span id="page-25-1"></span><span id="page-25-0"></span>A very useful iteration is to further instruct the model to take the time to *think*. This [technique](https://oreil.ly/8xWcs) has been found to increase performance on a variety of tasks. Curiously, a more recent paper suggests that this technique can also reduce LLM performance on tasks where thinking reduces human performance. Called chain-of-thought (CoT) prompting, this is usually done by prepending the prompt with instructions for the LLM to describe how it could arrive at the answer: **[4](#page-43-3)**

```
Think step by step.
```
How old was the 30th president of the United Stat

And now let's see what the same model produces for this new prompt:

1. First, find out who the 30th president of the done by researching a list of US presidents or by of the United States" online. You will find that Coolidge.

2. Next, find out the year when Calvin Coolidge w

be found by researching online or in a history bo the president from 1923-1929.

3. Now, you need to determine the year when Calvi This can be done by researching the life and deat Coolidge. You will find that she lived from 1879-

4. Calculate the age of Calvin Coolidge's wife's 78 years old.

5. Determine the age of Calvin Coolidge when his the year of his birth, 1872, from the year his mo means that Calvin Coolidge was 85 years old when

Notice how the only change in the prompt was the addition of Think step by step , and how much of a difference that made in the model's output. Now the model outputs a sequence of steps you could go through when trying to answer this question. Unfortunately, while the steps are very reasonable,

the final output is still incorrect, given it got some facts wrong, namely it listed the wrong birth and death years for President Coolidge's wife's mother. Let's see how to improve on this.

### **Retrieval-Augmented Generation**

<span id="page-27-1"></span><span id="page-27-0"></span>*Retrieval-augmented generation* (RAG) consists of finding relevant pieces of text, also known as *context*, such as facts you'd find in an encyclopedia and including that context in the prompt. The RAG technique can (and in real applications should) be combined with CoT, but for simplicity we'll use these techniques one at a time here. Here's the prompt including RAG:

Context:

- Calvin Coolidge (born John Calvin Coolidge Jr.; January 5, 1933) was an American attorney and pol 30th president of the United States from 1923 to

- Grace Anna Coolidge (née Goodhue; January 3, 18 wife of the 30th president of the United States,

- Grace Anna Goodhue was born on January 3, 1879, only child of Andrew Issachar Goodhue and Lemira

- Lemira A. Goodhue (Barrett) ; Birthdate: April Burlington, Chittenden County, VT, United States

How old was the 30th president of the United Stat

And the output from the model:

The 30th president of the United States, Calvin C his wife's mother, Lemira A. Goodhue, died on Oct

Now we're a lot closer to the correct answer, but as we touched on earlier, LLMs aren't great at out-of-the-box math. In this case, the final result of 54 years old is off by 3. Let's see how we can improve on this.

### **Tool Calling**

<span id="page-28-0"></span>The *tool calling* technique consists of prepending the prompt with a list of external functions the LLM can make use of, along with descriptions of what each is good for and instructions on how to signal in the output that it *wants* to use one (or more) of

these functions. Finally, you—the developer of the application should parse the output and call the appropriate functions. Here's one way to do this:

```
Tools:
- calculator: This tool accepts math expressions 
- search: This tool accepts search engine queries
result.
If you want to use tools to arrive at the answer,
inputs in CSV format, with this header row `tool,
How old was the 30th president of the United Stat
```
And this is the output you might get:

tool,input

calculator,2023-1892

search,"What age was Calvin Coolidge when his mot

<span id="page-30-0"></span>While the LLM correctly followed the output format instructions, the tools and inputs selected aren't the most appropriate for this question. This gets at one of the most important things to keep in mind when prompting LLMs: *each prompting technique is most useful when used in combination with (some of) the others*. For instance, here we could improve on this by combining tool calling, chain-of-thought, and RAG into a prompt that uses all three. Let's see what that looks like:

Context:

- Calvin Coolidge (born John Calvin Coolidge Jr.; January 5, 1933) was an American attorney and pol president of the United States from 1923 to 1929

- Grace Anna Coolidge (née Goodhue; January 3, 18 of the 30th president of the United States, Calvi

- Grace Anna Goodhue was born on January 3, 1879, only child of Andrew Issachar Goodhue and Lemira

- Lemira A. Goodhue (Barrett) ; Birthdate: April Burlington, Chittenden County, VT, United States

Tools:

- calculator: This tool accepts math expressions If you want to use tools to arrive at the answer, inputs in CSV format, with this header row `tool, Think step by step. How old was the 30th president of the United Stat

And with this prompt, maybe after a few tries, we might get this output:

tool,input

calculator,1929 - 1872

If we parse that CSV output, and have a calculator function execute the operation 1929 - 1827 , we finally get the right answer: 57 years.

As per the previous example, by combining RAG with chain-ofthought and tool calling, you can retrieve the most relevant

data to ground your model's output, then guide it step by step to ensure it uses that context effectively.

### **Few-Shot Prompting**

<span id="page-32-1"></span>Finally, we come to another very useful prompting technique: *few-shot prompting*. This consists of providing the LLM with examples of other questions and the correct answers, which enables the LLM to *learn* how to perform a new task without going through additional training or fine-tuning. When compared to fine-tuning, few-shot prompting is more flexible you can do it on the fly at query time—but less powerful, and you might achieve better performance with fine-tuning. That said, you should usually always try few-shot prompting before fine-tuning:

#### *Static few-shot prompting*

<span id="page-32-2"></span>The most basic version of few-shot prompting is to assemble a predetermined list of a small number of examples that you include in the prompt.

#### *Dynamic few-shot prompting*

<span id="page-32-0"></span>If you assemble a dataset of many examples, you can instead pick the most relevant examples for each new

#### <span id="page-33-3"></span>query.

The next section covers using LangChain to build applications using LLMs and these prompting techniques.

## LangChain and Why It's Important

<span id="page-33-1"></span>LangChain was one of the earliest open source libraries to provide LLM and prompting building blocks and the tooling to reliably combine them into larger applications. As of writing, LangChain has amassed over 28 million monthly [downloads](https://oreil.ly/8OKbf), 99,000 [GitHub](https://oreil.ly/bF5pc) stars, and the largest developer community in generative AI ([72,000+](https://oreil.ly/PNWL3) strong). It has enabled software engineers who don't have an ML background to utilize the power of LLMs to build a variety of apps, ranging from AI chatbots to AI agents that can reason and take action responsibly.

<span id="page-33-2"></span><span id="page-33-0"></span>LangChain builds on the idea stressed in the preceding section: that prompting techniques are most useful when used together. To make that easier, LangChain provides simple *abstractions* for each major prompting technique. By abstraction we mean Python and JavaScript functions and classes that encapsulate the ideas of those techniques into easy-to-use wrappers. These

abstractions are designed to play well together and to be combined into a larger LLM application.

<span id="page-34-1"></span><span id="page-34-0"></span>First of all, LangChain provides integrations with the major LLM providers, both commercial [\(OpenAI](https://oreil.ly/TTLXA), [Anthropic](https://oreil.ly/O4UXw), [Google,](https://oreil.ly/12g3Z) and more) and open source ([Llama,](https://oreil.ly/5WAVi) [Gemma,](https://oreil.ly/-40Ne) and others). These integrations share a common interface, making it very easy to try out new LLMs as they're announced and letting you avoid being locked-in to a single provider. We'll use these in [Chapter](#page-44-0) 1.

<span id="page-34-2"></span>LangChain also provides *prompt template* abstractions, which enable you to reuse prompts more than once, separating static text in the prompt from placeholders that will be different for each time you send it to the LLM to get a completion generated. We'll talk more about these also in [Chapter](#page-44-0) 1. LangChain prompts can also be stored in the LangChain Hub for sharing with teammates.

<span id="page-34-4"></span><span id="page-34-3"></span>LangChain contains many integrations with third-party services (such as Google Sheets, Wolfram Alpha, Zapier, just to name a few) exposed as *tools*, which is a standard interface for functions to be used in the tool-calling technique.

<span id="page-35-6"></span><span id="page-35-4"></span>For RAG, LangChain provides integrations with the major *embedding models* (language models designed to output a numeric representation, the *embedding*, of the meaning of a sentence, paragraph, and so on), *vector stores* (databases dedicated to storing embeddings), and *vector indexes* (regular databases with vector-storing capabilities). You'll learn a lot more about these in Chapters [2](#page-93-0) and [3](#page-163-0).

<span id="page-35-5"></span><span id="page-35-2"></span><span id="page-35-1"></span><span id="page-35-0"></span>For CoT, LangChain (through the LangGraph library) provides *agent* abstractions that combine chain-of-thought reasoning and tool calling, first popularized by the ReAct [paper.](https://oreil.ly/27BIC) This enables building LLM applications that do the following:

- 1. Reason about the steps to take.
- 2. Translate those steps into external tool calls.
- 3. Receive the output of those tool calls.
- 4. Repeat until the task is accomplished.

We cover these in Chapters [5](#page-277-0) through [8.](#page-385-0)

<span id="page-35-3"></span>For chatbot use cases, it becomes useful to keep track of previous interactions and use them when generating the response to a future interaction. This is called *memory*, and [Chapter](#page-237-0) 4 discusses using it in LangChain.

Finally, LangChain provides the tools to compose these building blocks into cohesive applications. Chapters [1](#page-44-0) through [6](#page-315-0) talk more about this.

In addition to this library, LangChain provides [LangSmith—](https://oreil.ly/geRgx)a platform to help debug, test, deploy, and monitor AI workflows —and LangGraph Platform—a platform for deploying and scaling LangGraph agents. We cover these in Chapters [9](#page-424-0) and [10](#page-469-0).

## What to Expect from This Book

With this book, we hope to convey the excitement and possibility of adding LLMs to your software engineering toolbelt.

We got into programming because we like building things, getting to the end of a project, looking at the final product and realizing there's something new out there, and we built it. Programming with LLMs is so exciting to us because it expands the set of things we can build, it makes previously hard things easy (for example, extracting relevant numbers from a long text) and previously impossible things possible—try building an automated assistant a year ago and you end up with the *phone*

*tree hell* we all know and love from calling up customer support numbers.

Now with LLMs and LangChain, you can actually build pleasant assistants (or myriad other applications) that chat with you and understand your intent to a very reasonable degree. The difference is night and day! If that sounds exciting to you (as it does to us) then you've come to the right place.

In this Preface, we've given you a refresher on what makes LLMs tick and why exactly that gives you "thing-building" superpowers. Having these very large ML models that understand language and can output answers written in conversational English (or some other language) gives you a *programmable* (through prompt engineering), versatile language-generation tool. By the end of the book, we hope you'll see just how powerful that can be.

<span id="page-37-0"></span>We'll begin with an AI chatbot customized by, for the most part, plain English instructions. That alone should be an eye-opener: you can now "program" part of the behavior of your application without code.

Then comes the next capability: giving your chatbot access to your own documents, which takes it from a generic assistant to one that's knowledgeable about any area of human knowledge for which you can find a library of written text. This will allow you to have the chatbot answer questions or summarize documents you wrote, for instance.

After that, we'll make the chatbot remember your previous conversations. This will improve it in two ways: It will feel a lot more natural to have a conversation with a chatbot that remembers what you have previously chatted about, and over time the chatbot can be personalized to the preferences of each of its users individually.

Next, we'll use chain-of-thought and tool-calling techniques to give the chatbot the ability to plan and act on those plans, iteratively. This will enable it to work toward more complicated requests, such as writing a research report about a subject of your choice.

As you use your chatbot for more complicated tasks, you'll feel the need to give it the tools to collaborate with you. This encompasses both giving you the ability to interrupt or authorize actions before they are taken, as well as providing the chatbot with the ability to ask for more information or clarification before acting.

Finally, we'll show you how to deploy your chatbot to production and discuss what you need to consider before and after taking that step, including latency, reliability, and security. Then we'll show you how to monitor your chatbot in production and continue to improve it as it is used.

Along the way, we'll teach you the ins and outs of each of these techniques, so that when you finish the book, you will have truly added a new tool (or two) to your software engineering toolbelt.

## Conventions Used in This Book

The following typographical conventions are used in this book:

*Italic*

Indicates new terms, URLs, email addresses, filenames, and file extensions.

#### *Constant width*

Used for program listings, as well as within paragraphs to refer to program elements such as variable or function names, databases, data types, environment variables, statements, and keywords.

#### **TIP**

This element signifies a tip or suggestion.

#### **NOTE**

This element signifies a general note.

## Using Code Examples

<span id="page-40-0"></span>Supplemental material (code examples, exercises, etc.) is available for download at *https://oreil.ly/supp-[LearningLangChain](https://oreil.ly/supp-LearningLangChain)*.

If you have a technical question or a problem using the code examples, please send email to *[support@oreilly.com](mailto:support@oreilly.com)*.

This book is here to help you get your job done. In general, if example code is offered with this book, you may use it in your programs and documentation. You do not need to contact us for permission unless you're reproducing a significant portion of the code. For example, writing a program that uses several chunks of code from this book does not require permission. Selling or distributing examples from O'Reilly books does require permission. Answering a question by citing this book

and quoting example code does not require permission. Incorporating a significant amount of example code from this book into your product's documentation does require permission.

We appreciate, but generally do not require, attribution. An attribution usually includes the title, author, publisher, and ISBN. For example: "*Learning LangChain* by Mayo Oshin and Nuno Campos (O'Reilly). Copyright 2025 Olumayowa "Mayo" Olufemi Oshin, 978-1-098-16728-8."

If you feel your use of code examples falls outside fair use or the permission given above, feel free to contact us at *[permissions@oreilly.com](mailto:permissions@oreilly.com)*.

## O'Reilly Online Learning

#### **NOTE**

For more than 40 years, *[O'Reilly](https://oreilly.com/) Media* has provided technology and business training, knowledge, and insight to help companies succeed.

Our unique network of experts and innovators share their knowledge and expertise through books, articles, and our online learning platform. O'Reilly's online learning platform gives you on-demand access to live training courses, in-depth learning paths, interactive coding environments, and a vast collection of text and video from O'Reilly and 200+ other publishers. For more information, visit *[https://oreilly.com](https://oreilly.com/)*.

## How to Contact Us

<span id="page-42-0"></span>Please address comments and questions concerning this book to the publisher:

O'Reilly Media, Inc.

1005 Gravenstein Highway North

Sebastopol, CA 95472

800-889-8969 (in the United States or Canada)

707-827-7019 (international or local)

707-829-0104 (fax)

*[support@oreilly.com](mailto:support@oreilly.com)*

*<https://oreilly.com/about/contact.html>*

We have a web page for this book, where we list errata, examples, and any additional information. You can access this page at *<https://oreil.ly/learning-langchain>*.

For news and information about our books and courses, visit *[https://oreilly.com](https://oreilly.com/)*.

Find us on LinkedIn: *<https://linkedin.com/company/oreilly-media>*.

Watch us on YouTube: *<https://youtube.com/oreillymedia>*.

## Acknowledgments

We would like to express our gratitude and appreciation to the reviewers—Rajat Kant Goel, Douglas Bailley, Tom Taulli, Gourav Bais, and Jacob Lee—for providing valuable technical feedback on improving this book.

<span id="page-43-0"></span>Tom B. Brown et al., ["Language](https://oreil.ly/1qoM6) Models Are Few-Shot Learners", arXiv, July 22, 2020. **[1](#page-12-0)**

<span id="page-43-1"></span>Xiang Zhang et al., "Don't Trust ChatGPT When Your Question Is Not in English: A Study of [Multilingual](https://oreil.ly/u5Cy1) Abilities and Types of LLMs", Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, December 6–10, 2023. **[2](#page-13-0)**

<span id="page-43-2"></span>For more information, see Ashish Vaswani et al., ["Attention](https://oreil.ly/Frtul) Is All You Need ", arXiv, June 12, 2017. **[3](#page-16-0)**

<span id="page-43-3"></span>Ryan Liu et al. "Mind Your Step (by Step): [Chain-of-Thought](https://oreil.ly/UHFp9) Can Reduce Performance on Tasks Where Thinking Makes Humans Worse", arXiv, November 8, 2024. **[4](#page-25-0)**

# <span id="page-44-0"></span>Chapter 1. LLM Fundamentals with LangChain

<span id="page-44-2"></span>The [Preface](#page-8-0) gave you a taste of the power of LLM prompting, where we saw firsthand the impact that different prompting techniques can have on what you get out of LLMs, especially when judiciously combined. The challenge in building good LLM applications is, in fact, in how to effectively construct the prompt sent to the model and process the model's prediction to return an accurate output (see [Figure](#page-44-1) 1-1).

<span id="page-44-1"></span>![](_page_44_Figure_2.jpeg)

Figure 1-1. The challenge in making LLMs a useful part of your application

If you can solve this problem, you are well on your way to building LLM applications, simple and complex alike. In this chapter, you'll learn more about how LangChain's building blocks map to LLM concepts and how, when combined effectively, they enable you to build LLM applications. But first, the sidebar "Why [LangChain?"](#page-46-0) is a brief primer on why we think it useful to use LangChain to build LLM applications.

#### <span id="page-46-0"></span>**WHY LANGCHAIN?**

<span id="page-46-1"></span>You can of course build LLM applications without LangChain. The most obvious alternative is to use the software development kit (SDK)—the package exposing the methods of their HTTP API as functions in the programming language of your choice—of the LLM provider you tried first (for example, OpenAI). We think learning LangChain will pay off in the short term and over the long run because of the following factors:

#### *Prebuilt common patterns*

LangChain comes with reference implementations of the most common LLM application patterns (we mentioned some of these in the [Preface](#page-8-0): chain-of-thought, tool calling, and others). This is the quickest way to get started with LLMs and might often be all you need. We'd suggest starting any new application from these and checking whether the results out of the box are good enough for your use case. If not, then see the next item for the other half of the LangChain libraries.

#### *Interchangeable building blocks*

These are components that can be easily swapped out for alternatives. Every component (an LLM, chat model, output parser, and so on—more on these shortly) follows a shared specification, which makes your application future-proof. As new capabilities are released by model providers and as your needs change, you can evolve your application without rewriting it each time.

Throughout this book we make use of the following major components in the code examples:

- LLM/chat model: OpenAI
- Embeddings: OpenAI
- Vector store: PGVector

You can swap out each of these for any of the alternatives listed on the following pages:

#### *Chat models*

<span id="page-47-5"></span><span id="page-47-4"></span><span id="page-47-1"></span><span id="page-47-0"></span>See the LangChain [documentation](https://oreil.ly/8Qlnb). If you don't want to use OpenAI (a commercial API) we suggest [Anthropic](https://oreil.ly/XdGfD) as a commercial alternative or [Ollama](https://oreil.ly/eKy6-) as an open source one.

#### *Embeddings*

<span id="page-47-3"></span><span id="page-47-2"></span>See the LangChain [documentation](https://oreil.ly/sKpfM). If you don't want to use OpenAI (a commercial API) we suggest [Cohere](https://oreil.ly/o1D0C) as a commercial alternative or [Ollama](https://oreil.ly/FarfL) as an open source one.

*Vector stores*

<span id="page-48-3"></span><span id="page-48-2"></span><span id="page-48-0"></span>See the LangChain [documentation](https://oreil.ly/q3RF1). If you don't want to use PGVector (an open source extension to the popular SQL database Postgres) we suggest using either [Weaviate](https://oreil.ly/XqlYa) (a dedicated vector store) or [OpenSearch](https://oreil.ly/1s357) (vector search features that are part of a popular search database).

This effort goes beyond, for instance, all LLMs having the same methods, with similar arguments and return values. Let's look at the example of chat models and two popular LLM providers, OpenAI and Anthropic. Both have a chat API which receives *chat messages* (loosely defined as objects with a type string and a content string) and returns a new message generated by the model. But if you try to use both models in the same conversation, you'll immediately run into issues, as their chat message formats are subtly incompatible. LangChain abstracts away these differences to enable building applications that are truly independent of a particular provider. For instance, with LangChain, a chatbot conversation where you use both OpenAI and Anthropic models works.

<span id="page-48-1"></span>Finally, as you build out your LLM applications with several of these components, we've found it useful to have the *orchestration* capabilities of LangChain:

- All major components are instrumented by the callbacks system for observability (more on this in [Chapter](#page-385-0) 8).
- All major components implement the same interface (more on this toward the end of this chapter).
- <span id="page-49-0"></span>Long-running LLM applications can be interrupted, resumed, or retried (more on this in [Chapter](#page-315-0) 6).

## Getting Set Up with LangChain

<span id="page-49-1"></span>To follow along with the rest of the chapter, and the chapters to come, we recommend setting up LangChain on your computer first.

<span id="page-49-2"></span>See the instructions in the [Preface](#page-8-0) regarding setting up an OpenAI account and complete these if you haven't yet. If you prefer using a different LLM provider, see "Why [LangChain?"](#page-46-0) for alternatives.

Then head over to the API Keys [page](https://oreil.ly/BKrtV) on the OpenAI website (after logging in to your OpenAI account), create an API key, and save it—you'll need it soon.

#### **NOTE**

In this book, we'll show code examples in both Python and JavaScript (JS). LangChain offers the same functionality in both languages, so just pick the one you're most comfortable with and follow the respective code snippets throughout the book (the code examples for each language are equivalent).

<span id="page-50-0"></span>First, some setup instructions for readers using Python:

- 1. Ensure that you have Python [installed. See](https://oreil.ly/20K9l) the instructions for your operating system.
- 2. Install Jupyter if you want to run the examples in a notebook environment. You can do this by running pip install notebook in your terminal.
- 3. Install the LangChain library by running the following commands in your terminal:

pip install langchain langchain-openai langchai pip install langchain-text-splitters langchain-

4. Take the OpenAI API key you generated at the beginning of this section and make it available in your terminal environment. You can do this by running the following:

```
export OPENAI_API_KEY=your-key
```
- 5. Don't forget to replace your-key with the API key you generated previously.
- 6. Open a Jupyter notebook by running this command:

<span id="page-51-0"></span>jupyter notebook

You're now ready to follow along with the Python code examples.

Here are the instructions for readers using JavaScript:

1. Take the OpenAI API key you generated at the beginning of this section and make it available in your terminal environment. You can do this by running the following:

```
export OPENAI_API_KEY=your-key
```
2. Don't forget to replace your-key with the API key you generated previously.

- 3. If you want to run the examples as Node.js scripts, install Node by following the [instructions](https://oreil.ly/5gjiO).
- 4. Install the LangChain libraries by running the following commands in your terminal:

npm install langchain @langchain/openai @langch npm install @langchain/core pg

5. Take each example, save it as a *.js* file and run it with node ./file.js .

## Using LLMs in LangChain

<span id="page-52-1"></span><span id="page-52-0"></span>To recap, LLMs are the driving engine behind most generative AI applications. LangChain provides two simple interfaces to interact with any LLM API provider:

- Chat models
- LLMs

The LLM interface simply takes a string prompt as input, sends the input to the model provider, and then returns the model prediction as output.

<span id="page-53-0"></span>Let's import LangChain's OpenAI LLM wrapper to invoke a model prediction using a simple prompt:

<span id="page-53-2"></span>*Python*

```
from langchain_openai.llms import OpenAI
```

```
model = OpenAI(model="gpt-3.5-turbo")
```

```
model.invoke("The sky is")
```
*JavaScript*

```
import { OpenAI } from "@langchain/openai";
const model = new OpenAI({ model: "gpt-3.5-turbo"
await model.invoke("The sky is");
```
*The output:*

Blue!

#### **TIP**

<span id="page-54-2"></span>Notice the parameter model passed to OpenAI . This is the most common parameter to configure when using an LLM or chat model, the underlying model to use, as most providers offer several models with different trade-offs in capability and cost (usually larger models are more capable, but also more expensive and slower). See OpenAI's [overview](https://oreil.ly/dM886) of the models they offer.

Other useful parameters to configure include the following, offered by most providers.

#### *temperature*

<span id="page-54-4"></span><span id="page-54-3"></span>This controls the sampling algorithm used to generate output. Lower values produce more predictable outputs (for example, 0.1), while higher values generate more creative, or unexpected, results (such as 0.9). Different tasks will need different values for this parameter. For instance, producing structured output usually benefits from a lower temperature, whereas creative writing tasks do better with a higher value:

#### *max\_tokens*

<span id="page-54-1"></span>This limits the size (and cost) of the output. A lower value may cause the LLM to stop generating the output before getting to a natural end, so it may appear to have been truncated.

Beyond these, each provider exposes a different set of parameters. We recommend looking at the documentation for the one you choose. For an example, refer to [OpenAI's](https://oreil.ly/5O1RW) platform.

<span id="page-54-0"></span>Alternatively, the chat model interface enables back and forth conversations between the user and model. The reason why it's a separate interface is because popular LLM providers like OpenAI differentiate messages sent to and from the model into *user*, *assistant*, and *system* roles (here *role* denotes the type of content the message contains):

#### *System role*

<span id="page-55-3"></span><span id="page-55-2"></span>Used for instructions the model should use to answer a user question

#### *User role*

<span id="page-55-4"></span>Used for the user's query and any other content produced by the user

#### *Assistant role*

<span id="page-55-0"></span>Used for content generated by the model

The chat model's interface makes it easier to configure and manage conversions in your AI chatbot application. Here's an example utilizing LangChain's ChatOpenAI model:

<span id="page-55-1"></span>*Python*

from langchain\_openai.chat\_models import ChatOpen from langchain\_core.messages import HumanMessage

```
model = ChatOpenAI()
prompt = [HumanMessage("What is the capital of Fr
model.invoke(prompt)
```
<span id="page-56-1"></span>*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
import { HumanMessage } from '@langchain/core/mes
const model = new ChatOpenAI()
const prompt = [new HumanMessage('What is the cap
await model.invoke(prompt)
```
*The output:*

```
AIMessage(content='The capital of France is Paris
```
<span id="page-56-0"></span>Instead of a single prompt string, chat models make use of different types of chat message interfaces associated with each role mentioned previously. These include the following:

*HumanMessage*

<span id="page-57-2"></span>A message sent from the perspective of the human, with the user role

#### *AIMessage*

<span id="page-57-0"></span>A message sent from the perspective of the AI that the human is interacting with, with the assistant role

#### *SystemMessage*

<span id="page-57-4"></span>A message setting the instructions the AI should follow, with the system role

*ChatMessage*

<span id="page-57-1"></span>A message allowing for arbitrary setting of role

Let's incorporate a SystemMessage instruction in our example:

#### <span id="page-57-3"></span>*Python*

```
from langchain_core.messages import HumanMessage,
from langchain_openai.chat_models import ChatOpen
model = ChatOpenAI()
system_msg = SystemMessage(
```

```
 '''You are a helpful assistant that responds 
 exclamation marks.'''
)
human_msg = HumanMessage('What is the capital of 
model.invoke([system_msg, human_msg])
```
<span id="page-58-0"></span>*JavaScript*

```
import { ChatOpenAI } from "@langchain/openai";
import { HumanMessage, SystemMessage } from "@lan
const model = new ChatOpenAI();
const prompt = [
 new SystemMessage(
 `You are a helpful assistant that responds to
 exclamation marks.`,
 ),
 new HumanMessage("What is the capital of France
];
await model.invoke(prompt);
```
*The output:*

```
AIMessage('Paris!!!')
```
As you can see, the model obeyed the instruction provided in the SystemMessage even though it wasn't present in the user's question. This enables you to preconfigure your AI application to respond in a relatively predictable manner based on the user's input.

## <span id="page-59-1"></span>Making LLM Prompts Reusable

<span id="page-59-0"></span>The previous section showed how the prompt instruction significantly influences the model's output. Prompts help the model understand context and generate relevant answers to queries.

<span id="page-59-2"></span>Here is an example of a detailed prompt:

Answer the question based on the context below. I answered using the information provided, answer w

Context: The most recent advancements in NLP are Models (LLMs). These models outperform their smal become invaluable for developers who are creating

biliti D l t i t th d l

```
capabilities. Developers can tap into these model
`transformers` library, or by utilizing OpenAI an
the `openai` and `cohere` libraries, respectively
Question: Which model providers offer LLMs?
Answer:
```
Although the prompt looks like a simple string, the challenge is figuring out what the text should contain and how it should vary based on the user's input. In this example, the Context and Question values are hardcoded, but what if we wanted to pass these in dynamically?

<span id="page-60-0"></span>Fortunately, LangChain provides prompt template interfaces that make it easy to construct prompts with dynamic inputs:

<span id="page-60-1"></span>*Python*

```
from langchain_core.prompts import PromptTemplate
template = PromptTemplate.from_template("""Answer
 context below. If the question cannot be answ
 provided, answer with "I don't know".
```
Context: {context}

```
Question: {question}
Answer: """)
template.invoke({
 "context": """The most recent advancements in
 Language Models (LLMs). These models outp
 counterparts and have become invaluable f
 applications with NLP capabilities. Devel
 models through Hugging Face's `transforme
 OpenAI and Cohere's offerings through the
 libraries, respectively.""",
 "question": "Which model providers offer LLMs
})
```
<span id="page-61-0"></span>*JavaScript*

```
import { PromptTemplate } from '@langchain/core/p
```
const template = PromptTemplate.fromTemplate(`Ans context below. If the question cannot be answer provided, answer with "I don't know".

```
Context: {context}
Question: {question}
Answer: `)
await template.invoke({
 context: `The most recent advancements in NLP a
 Language Models (LLMs). These models outperfo
 counterparts and have become invaluable for d
 applications with NLP capabilities. Developer
 through Hugging Face's \`transformers\` libra
 and Cohere's offerings through the \`openai\`
 respectively.`,
 question: "Which model providers offer LLMs?"
})
```
#### *The output:*

StringPromptValue(text='Answer the question based question cannot be answered using the informa don\'t know".\n\nContext: The most recent adv driven by Large Language Models (LLMs). These smaller counterparts and have become invaluab creating applications with NLP capabilities. models through Hugging Face\'s `transformers` OpenAI and Cohere\'s offerings through the `o

 OpenAI and Cohere\ s offerings through the o respectively.\n\nQuestion: Which model provid

This example takes the static prompt from the previous block and makes it dynamic. The template contains the structure of the final prompt alongside the definition of where the dynamic inputs will be inserted.

As such, the template can be used as a recipe to build multiple static, specific prompts. When you format the prompt with some specific values—in this case, context and question you get a static prompt ready to be passed in to an LLM.

<span id="page-63-3"></span><span id="page-63-1"></span><span id="page-63-0"></span>As you can see, the question argument is passed dynamically via the invoke function. By default, LangChain prompts follow Python's f-string syntax for defining dynamic parameters any word surrounded by curly braces, such as {question} , are placeholders for values passed in at runtime. In the previous example, {question} was replaced by "Which model providers offer LLMs?"

Let's see how we'd feed this into an LLM OpenAI model using LangChain:

<span id="page-63-2"></span>*Python*

```
from langchain_openai.llms import OpenAI
from langchain_core.prompts import PromptTemplate
```

```
# both `template` and `model` can be reused many
```

```
template = PromptTemplate.from_template("""Answer
 context below. If the question cannot be answ
 provided, answer with "I don't know".
```
Context: {context}

Question: {question}

Answer: """)

model = OpenAI()

# `prompt` and `completion` are the results of us

prompt = template.invoke({

 "context": """The most recent advancements in Language Models (LLMs). These models outp counterparts and have become invaluable f applications with NLP capabilities. Devel models through Hugging Face's `transforme OpenAI and Cohere's offerings through the libraries, respectively.""",

"question": "Which model providers offer LLMs

```
 question : Which model providers offer LLMs
})
completion = model.invoke(prompt)
```
#### <span id="page-65-0"></span>*JavaScript*

```
import { PromptTemplate } from '@langchain/core/p
import { OpenAI } from '@langchain/openai'
const model = new OpenAI()
const template = PromptTemplate.fromTemplate(`Ans
 context below. If the question cannot be answer
 provided, answer with "I don't know".
Context: {context}
Question: {question}
Answer: `)
const prompt = await template.invoke({
 context: `The most recent advancements in NLP a
 Language Models (LLMs). These models outperfo
 counterparts and have become invaluable for d
 applications with NLP capabilities. Developer
 through Hugging Face's \`transformers\` libra
```

```
 and Cohere's offerings through the \`openai\`
 respectively.`,
 question: "Which model providers offer LLMs?"
})
await model.invoke(prompt)
```
*The output:*

```
Hugging Face's `transformers` library, OpenAI usi
Cohere using the `cohere` library offer LLMs.
```
If you're looking to build an AI chat application, the ChatPromptTemplate can be used instead to provide dynamic inputs based on the role of the chat message:

<span id="page-66-1"></span>*Python*

```
from langchain_core.prompts import ChatPromptTemp
template = ChatPromptTemplate.from_messages([
 ('system', '''Answer the question based on th
 question cannot be answered using the inf
 "I don\'t know".'''),
   ('human' 'Context: {context}')
```

```
 ( human , Context: {context} ),
 ('human', 'Question: {question}'),
])
template.invoke({
 "context": """The most recent advancements in
 Language Models (LLMs). These models outp
 counterparts and have become invaluable f
 applications with NLP capabilities. Devel
 models through Hugging Face's `transforme
 OpenAI and Cohere's offerings through the
 libraries, respectively.""",
 "question": "Which model providers offer LLMs
})
```
#### <span id="page-67-0"></span>*JavaScript*

```
import { ChatPromptTemplate } from '@langchain/co
const template = ChatPromptTemplate.fromMessages(
 ['system', `Answer the question based on the co
 cannot be answered using the information prov
 don\'t know".`],
 ['human', 'Context: {context}'],
 ['human', 'Question: {question}'],
])
```
![](_page_68_Picture_0.jpeg)

#### *The output:*

ChatPromptValue(messages=[SystemMessage(content= the context below. If the question cannot be provided, answer with "I don\'t know".'), Hum The most recent advancements in NLP are being Models (LLMs). These models outperform their become invaluable for developers who are crea capabilities. Developers can tap into these m `transformers` library, or by utilizing OpenA

 through the `openai` and `cohere` libraries, (content='Question: Which model providers off

Notice how the prompt contains instructions in a SystemMessage and two instances of HumanMessage that contain dynamic context and question variables. You can still format the template in the same way and get back a static prompt that you can pass to a large language model for a prediction output:

#### *Python*

```
from langchain_openai.chat_models import ChatOpen
from langchain_core.prompts import ChatPromptTemp
# both `template` and `model` can be reused many 
template = ChatPromptTemplate.from_messages([
 ('system', '''Answer the question based on th
 question cannot be answered using the inf
 with "I don\'t know".'''),
 ('human', 'Context: {context}'),
 ('human', 'Question: {question}'),
])
model = ChatOpenAI()
# `prompt` and `completion` are the results of us
prompt = template invoke({
```

```
prompt = template.invoke({
 "context": """The most recent advancements in
 Large Language Models (LLMs). These model
 counterparts and have become invaluable f
 applications with NLP capabilities. Devel
 models through Hugging Face's `transforme
 OpenAI and Cohere's offerings through the
 libraries, respectively.""",
 "question": "Which model providers offer LLMs
})
model.invoke(prompt)
```
*JavaScript*

```
import { ChatPromptTemplate } from '@langchain/co
import { ChatOpenAI } from '@langchain/openai'
const model = new ChatOpenAI()
const template = ChatPromptTemplate.fromMessages(
 ['system', `Answer the question based on the co
 cannot be answered using the information prov
 don\'t know".`],
 ['human', 'Context: {context}'],
 ['human', 'Question: {question}'],
])
```

```
const prompt = await template.invoke({
 context: `The most recent advancements in NLP a
 Language Models (LLMs). These models outperfo
 counterparts and have become invaluable for d
 applications with NLP capabilities. Developer
 through Hugging Face's \`transformers\` libra
 and Cohere's offerings through the \`openai\`
 respectively.`,
 question: "Which model providers offer LLMs?"
})
await model.invoke(prompt)
```
*The output:*

AIMessage(content="Hugging Face's `transformers` `openai` library, and Cohere using the `coher

## Getting Specific Formats out of LLMs

<span id="page-71-1"></span><span id="page-71-0"></span>Plain text outputs are useful, but there may be use cases where you need the LLM to generate a *structured* output—that is, output in a machine-readable format, such as JSON, XML, CSV,

or even in a programming language such as Python or JavaScript. This is very useful when you intend to hand that output off to some other piece of code, making an LLM play a part in your larger application.

### **JSON Output**

<span id="page-72-0"></span>The most common format to generate with LLMs is JSON. JSON outputs can (for example) be sent over the wire to your frontend code or be saved to a database.

When generating JSON, the first task is to define the schema you want the LLM to respect when producing the output. Then, you should include that schema in the prompt, along with the text you want to use as the source. Let's see an example:

#### <span id="page-72-1"></span>*Python*

```
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel
class AnswerWithJustification(BaseModel):
 '''An answer to the user's question along wit
 answer.'''
 answer: str
 '''The answer to the user's question'''
```

```
 justification: str
 '''Justification for the answer'''
```

```
llm = ChatOpenAI(model="gpt-3.5-turbo", temperatu
structured_llm = llm.with_structured_output(Answe
```

```
structured_llm.invoke("""What weighs more, a poun
 of feathers""")
```
*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
import { z } from "zod";
const answerSchema = z
 .object({
 answer: z.string().describe("The answer to th
 justification: z.string().describe(`Justifica
 answer`),
 })
 .describe(`An answer to the user's question alo
 the answer.`);
const model = new ChatOpenAI({
 model: "gpt-3.5-turbo",
 temperature: 0,
}) withStructuredOutput(answerSchema)
```

```
}).withStructuredOutput(answerSchema)
await model.invoke("What weighs more, a pound of
```
*The output:*

```
{
 answer: "They weigh the same",
 justification: "Both a pound of bricks and a po
 The weight is the same, but the volu"... 42 m
}
```
<span id="page-74-1"></span><span id="page-74-0"></span>So, first define a schema. In Python, this is easiest to do with Pydantic (a library used for validating data against schemas). In JS, this is easiest to do with Zod (an equivalent library). The method with\_structured\_output will use that schema for two things:

- The schema will be converted to a JSONSchema object (a JSON format used to describe the shape [types, names, descriptions] of JSON data), which will be sent to the LLM. For each LLM, LangChain picks the best method to do this, usually function calling or prompting.
- The schema will also be used to validate the output returned by the LLM before returning it; this ensures the output

produced respects the schema you passed in exactly.

### **Other Machine-Readable Formats with Output Parsers**

<span id="page-75-3"></span><span id="page-75-2"></span><span id="page-75-0"></span>You can also use an LLM or chat model to produce output in other formats, such as CSV or XML. This is where output parsers come in handy. *Output parsers* are classes that help you structure large language model responses. They serve two functions:

#### *Providing format instructions*

<span id="page-75-1"></span>Output parsers can be used to inject some additional instructions in the prompt that will help guide the LLM to output text in the format it knows how to parse.

#### *Validating and parsing output*

The main function is to take the textual output of the LLM or chat model and render it to a more structured format, such as a list, XML, or other format. This can include removing extraneous information, correcting incomplete output, and validating the parsed values.

Here's an example of how an output parser works:

#### <span id="page-76-2"></span>*Python*

```
from langchain_core.output_parsers import CommaSe
parser = CommaSeparatedListOutputParser()
items = parser.invoke("apple, banana, cherry")
```
<span id="page-76-1"></span>*JavaScript*

```
import { CommaSeparatedListOutputParser } from '@
const parser = new CommaSeparatedListOutputParser
await parser.invoke("apple, banana, cherry")
```
*The output:*

```
['apple', 'banana', 'cherry']
```
LangChain provides a variety of output parsers for various use cases, including CSV, XML, and more. We'll see how to combine output parsers with models and prompts in the next section.

# Assembling the Many Pieces of an LLM Application

<span id="page-77-2"></span>The key components you've learned about so far are essential building blocks of the LangChain framework. Which brings us to the critical question: How do you combine them effectively to build your LLM application?

### **Using the Runnable Interface**

<span id="page-77-3"></span><span id="page-77-1"></span>As you may have noticed, all the code examples used so far utilize a similar interface and the invoke() method to generate outputs from the model (or prompt template, or output parser). All components have the following:

- <span id="page-77-0"></span>There is a common interface with these methods:
	- invoke : transforms a single input into an output
	- batch : efficiently transforms multiple inputs into multiple outputs
	- stream : streams output from a single input as it's produced
- There are built-in utilities for retries, fallbacks, schemas, and runtime configurability.

In Python, each of the three methods have asyncio equivalents.

As such, all components behave the same way, and the interface learned for one of them applies to all:

<span id="page-78-1"></span>*Python*

```
from langchain_openai.llms import ChatOpenAI
model = ChatOpenAI()
completion = model.invoke('Hi there!')
# Hi!
completions = model.batch(['Hi there!', 'Bye!'])
# ['Hi!', 'See you!']
for token in model.stream('Bye!'):
 print(token)
 # Good
 # bye
 # !
```
<span id="page-78-0"></span>*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
const model = new ChatOpenAI()
const completion = await model.invoke('Hi there!
// Hi!
const completions = await model.batch(['Hi there
// ['Hi!', 'See you!']
for await (const token of await model.stream('Bye
 console.log(token)
 // Good
 // bye
 // !
}
```
In this example, you see how the three main methods work:

- invoke() takes a single input and returns a single output.
- batch() takes a list of outputs and returns a list of outputs.
- stream() takes a single input and returns an iterator of parts of the output as they become available.

In some cases, where the underlying component doesn't support iterative output, there will be a single part containing all output.

You can combine these components in two ways:

#### *Imperative*

```
Call your components directly, for example, with
model.invoke(...)
```
*Declarative*

<span id="page-80-1"></span>Use LangChain Expression Language (LCEL), as covered in an upcoming section

<span id="page-80-0"></span>[Table](#page-81-0) 1-1 summarizes their differences, and we'll see each in action next.

|                       | Imperative                                                                               | Declarative |
|-----------------------|------------------------------------------------------------------------------------------|-------------|
| Syntax                | All<br>of<br>Python<br>or<br>JavaScript                                                  | LCEL        |
| Parallel<br>execution | Python:<br>with<br>threads<br>or<br>coroutines<br>JavaScript:<br>with<br>Promise.al<br>l | Automatic   |
| Streaming             | With<br>yield<br>keyword                                                                 | Automatic   |
| Async<br>execution    | With<br>async<br>functions                                                               | Automatic   |

<span id="page-81-0"></span>Table 1-1. The main differences between imperative and declarative composition.

### **Imperative Composition**

<span id="page-81-1"></span>*Imperative composition* is just a fancy name for writing the code you're used to writing, composing these components into functions and classes. Here's an example combining prompts, models, and output parsers:

<span id="page-81-2"></span>*Python*

from langchain\_openai.chat\_models import ChatOpen from langchain core.prompts import ChatPromptTemp

```
from langchain_core.runnables import chain
# the building blocks
template = ChatPromptTemplate.from_messages([
 ('system', 'You are a helpful assistant.'),
 ('human',
              '{question}'),
])
model = ChatOpenAI()
# combine them in a function
# @chain decorator adds the same Runnable interfa
@chain
def chatbot(values):
 prompt = template.invoke(values)
 return model.invoke(prompt)
# use it
chatbot.invoke({"question": "Which model provider
```
o a gc a \_co e p o pts po t C at o pt e p

<span id="page-82-0"></span>*JavaScript*

import {ChatOpenAI} from '@langchain/openai'

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
import {RunnableLambda} from '@langchain/core/run
// the building blocks
const template = ChatPromptTemplate.fromMessages(
 ['system', 'You are a helpful assistant.'],
 ['human', '{question}'],
])
const model = new ChatOpenAI()
// combine them in a function
// RunnableLambda adds the same Runnable interfac
const chatbot = RunnableLambda.from(async values
 const prompt = await template.invoke(values)
 return await model.invoke(prompt)
})
// use it
await chatbot.invoke({
 "question": "Which model providers offer LLMs?"
})
```
*The output:*

```
AIMessage(content="Hugging Face's `transformers` 
 `openai` library, and Cohere using the `coher
```
The preceding is a complete example of a chatbot, using a prompt and chat model. As you can see, it uses familiar Python syntax and supports any custom logic you might want to add in that function.

On the other hand, if you want to enable streaming or async support, you'd have to modify your function to support it. For example, streaming support can be added as follows:

<span id="page-84-0"></span>*Python*

```
@chain
def chatbot(values):
 prompt = template.invoke(values)
 for token in model.stream(prompt):
 yield token
for part in chatbot.stream({
 "question": "Which model providers offer LLMs
```

```
}):
 print(part)
```
<span id="page-85-0"></span>*JavaScript*

```
const chatbot = RunnableLambda.from(async functio
 const prompt = await template.invoke(values)
 for await (const token of await model.stream(pr
 yield token
 }
})
for await (const token of await chatbot.stream({
 "question": "Which model providers offer LLMs?"
})) {
 console.log(token)
}
```
*The output:*

```
AIMessageChunk(content="Hugging")
AIMessageChunk(content=" Face's")
```

```
AIMessageChunk(content=" `transformers`")
...
```
So, either in JS or Python, you can enable streaming for your custom function by yielding the values you want to stream and then calling it with stream .

<span id="page-86-0"></span>For asynchronous execution, you'd rewrite your function like this:

<span id="page-86-3"></span>*Python*

```
@chain
async def chatbot(values):
 prompt = await template.ainvoke(values)
 return await model.ainvoke(prompt)
await chatbot.ainvoke({"question": "Which model p
# > AIMessage(content="""Hugging Face's `transfor
 the `openai` library, and Cohere using the `c
```
<span id="page-86-2"></span><span id="page-86-1"></span>This one applies to Python only, as asynchronous execution is the only option in JavaScript.

### **Declarative Composition**

<span id="page-87-1"></span><span id="page-87-0"></span>LCEL is a *declarative language* for composing LangChain components. LangChain compiles LCEL compositions to an *optimized execution plan*, with automatic parallelization, streaming, tracing, and async support.

Let's see the same example using LCEL:

<span id="page-87-2"></span>*Python*

```
from langchain_openai.chat_models import ChatOpen
from langchain_core.prompts import ChatPromptTemp
# the building blocks
template = ChatPromptTemplate.from_messages([
 ('system', 'You are a helpful assistant.'),
 ('human',
              '{question}'),
])
model = ChatOpenAI()
# combine them with the | operator
chatbot = template | model
```

```
# use it
```
chatbot.invoke({"question": "Which model provider

#### <span id="page-88-0"></span>*JavaScript*

```
import { ChatOpenAI } from '@langchain/openai'
import { ChatPromptTemplate } from '@langchain/co
import { RunnableLambda } from '@langchain/core/r
// the building blocks
const template = ChatPromptTemplate.fromMessages(
 ['system', 'You are a helpful assistant.'],
 ['human', '{question}'],
])
const model = new ChatOpenAI()
// combine them in a function
const chatbot = template.pipe(model)
// use it
```

```
await chatbot.invoke({
 "question": "Which model providers offer LLMs?"
})
```
*The output:*

```
AIMessage(content="Hugging Face's `transformers` 
 `openai` library, and Cohere using the `coher
```
Crucially, the last line is the same between the two examples that is, you use the function and the LCEL sequence in the same way, with invoke/stream/batch . And in this version, you don't need to do anything else to use streaming:

<span id="page-89-0"></span>*Python*

```
chatbot = template | model
for part in chatbot.stream({
 "question": "Which model providers offer LLMs
}):
 print(part)
 # > AIMessageChunk(content="Hugging")
```
![](_page_90_Figure_0.jpeg)

<span id="page-90-0"></span>*JavaScript*

```
const chatbot = template.pipe(model)
for await (const token of await chatbot.stream({
 "question": "Which model providers offer LLMs?"
})) {
 console.log(token)
}
```
And, for Python only, it's the same for using asynchronous methods:

*Python*

```
chatbot = template | model
await chatbot.ainvoke({
 "question": "Which model providers offer LLMs
})
```
## Summary

<span id="page-91-1"></span>In this chapter, you've learned about the building blocks and key components necessary to build LLM applications using LangChain. LLM applications are essentially a chain consisting of the large language model to make predictions, the prompt instruction(s) to guide the model toward a desired output, and an optional output parser to transform the format of the model's output.

<span id="page-91-0"></span>All LangChain components share the same interface with invoke , stream , and batch methods to handle various inputs and outputs. They can either be combined and executed imperatively by calling them directly or declaratively using LCEL.

<span id="page-91-2"></span>The imperative approach is useful if you intend to write a lot of custom logic, whereas the declarative approach is useful for simply assembling existing components with limited customization.

In [Chapter](#page-93-0) 2, you'll learn how to provide external data to your AI chatbot as *context* so that you can build an LLM application

that enables you to "chat" with your data.

## <span id="page-93-0"></span>Chapter 2. RAG Part I: Indexing Your Data

In the previous chapter, you learned about the important building blocks used to create an LLM application using LangChain. You also built a simple AI chatbot consisting of a prompt sent to the model and the output generated by the model. But there are major limitations to this simple chatbot.

<span id="page-93-1"></span>What if your use case requires knowledge that the model wasn't trained on? For example, let's say you want to use AI to ask questions about a company, but the information is contained in a private PDF or other type of document. While we've seen model providers enriching their training datasets to include more and more of the world's public information (no matter what format it is stored in), two major limitations continue to exist in LLM's knowledge corpus:

#### *Private data*

<span id="page-93-3"></span><span id="page-93-2"></span>Information that isn't publicly available is, by definition, not included in the training data of LLMs.

*Current events*

<span id="page-94-0"></span>Training an LLM is a costly and time-consuming process that can span multiple years, with data-gathering being one of the first steps. This results in what is called the knowledge cutoff, or a date beyond which the LLM has no knowledge of real-world events; usually this would be the date the training set was finalized. This can be anywhere from a few months to a few years into the past, depending on the model in question.

<span id="page-94-3"></span><span id="page-94-2"></span>In either case, the model will most likely hallucinate (find misleading or false information) and respond with inaccurate information. Adapting the prompt won't resolve the issue either because it relies on the model's current knowledge.

## The Goal: Picking Relevant Context for LLMs

<span id="page-94-1"></span>If the only private/current data you needed for your LLM use case was one to two pages of text, this chapter would be a lot shorter: all you'd need to make that information available to the LLM is to include that entire text in every single prompt you sent to the model.

The challenge in making data available to LLMs is first and foremost a quantity problem. You have more information than can fit in each prompt you send to the LLM. Which small subset of your large collection of text do you include each time you call the model? Or in other words, how do you pick (with the aid of the model) which text is most relevant to answer each question?

In this chapter and the next, you'll learn how to overcome this challenge in two steps:

- 1. *Indexing* your documents, that is, preprocessing them in a way where your application can easily find the most relevant ones for each question
- <span id="page-95-3"></span><span id="page-95-2"></span><span id="page-95-0"></span>2. *Retrieving* this external data from the index and using it as *context* for the LLM to generate an accurate output based on your data

<span id="page-95-4"></span><span id="page-95-1"></span>This chapter focuses on indexing, the first step, which involves preprocessing your documents into a format that can be understood and searched with LLMs. This technique is called *retrieval-augmented generation* (RAG). But before we begin, let's discuss *why* your documents require preprocessing.

Let's assume you would like to use LLMs to analyze the financial performance and risks in Tesla's 2022 [annual](https://oreil.ly/Bp51E) report, which is stored as text in PDF format. Your goal is to be able to ask a question like "What key risks did Tesla face in 2022?" and get a humanlike response based on context from the risk factors section of the document.

Breaking it down, there are four key steps (shown in [Figure](#page-96-0) 2-1) that you'd need to take in order to achieve this goal:

- 1. Extract the text from the document.
- 2. Split the text into manageable chunks.
- 3. Convert the text into numbers that computers can understand.
- 4. Store these number representations of your text somewhere that makes it easy and fast to retrieve the relevant sections of your document to answer a given question.

<span id="page-96-0"></span>![](_page_96_Figure_6.jpeg)

Figure 2-1. Four key steps to preprocess your documents for LLM usage

<span id="page-97-3"></span><span id="page-97-2"></span>[Figure](#page-96-0) 2-1 illustrates the flow of this preprocessing and transformation of your documents, a process known as ingestion. *Ingestion* is simply the process of converting your documents into numbers that computers can understand and analyze, and storing them in a special type of database for efficient retrieval. These numbers are formally known as *embeddings*, and this special type of database is known as a *vector store.* Let's look a little more closely at what embeddings are and why they're important, starting with something simpler than LLM-powered embeddings.

# <span id="page-97-4"></span>Embeddings: Converting Text to Numbers

<span id="page-97-0"></span>*Embedding* refers to representing text as a (long) sequence of numbers. This is a lossy representation—that is, you can't recover the original text from these number sequences, so you usually store both the original text and this numeric representation.

<span id="page-97-1"></span>So, why bother? Because you gain the flexibility and power that comes with working with numbers: you can do math on words! Let's see why that's exciting.

### **Embeddings Before LLMs**

<span id="page-98-0"></span>Long before LLMs, computer scientists were using embeddings —for instance, to enable full-text search capabilities in websites or to classify emails as spam. Let's see an example:

- 1. Take these three sentences:
	- What a sunny day.
	- Such bright skies today.
	- I haven't seen a sunny day in weeks.
- 2. List all unique words in them: *what*, *a*, *sunny*, *day*, *such*, *bright*, and so on.
- 3. For each sentence, go word by word and assign the number 0 if not present, 1 if used once in the sentence, 2 if present twice, and so on.

[Table](#page-99-0) 2-1 shows the result.

| Word    | What<br>a<br>sunny<br>day. | Such<br>bright<br>skies<br>today. | I<br>haven't<br>seen<br>a<br>sunny<br>day<br>in<br>weeks. |
|---------|----------------------------|-----------------------------------|-----------------------------------------------------------|
| what    | 1                          | 0                                 | 0                                                         |
| a       | 1                          | 0                                 | 1                                                         |
| sunny   | 1                          | 0                                 | 1                                                         |
| day     | 1                          | 0                                 | 1                                                         |
| such    | 0                          | 1                                 | 0                                                         |
| bright  | 0                          | 1                                 | 0                                                         |
| skies   | 0                          | 1                                 | 0                                                         |
| today   | 0                          | 1                                 | 0                                                         |
| I       | 0                          | 0                                 | 1                                                         |
| haven't | 0                          | 0                                 | 1                                                         |
| seen    | 0                          | 0                                 | 1                                                         |
| in      | 0                          | 0                                 | 1                                                         |

<span id="page-99-0"></span>Table 2-1. Word embeddings for three sentences

| Word  | What<br>a<br>sunny<br>day. | Such<br>bright<br>skies<br>today. | I<br>haven't<br>seen<br>a<br>sunny<br>day<br>in<br>weeks. |
|-------|----------------------------|-----------------------------------|-----------------------------------------------------------|
| weeks | 0                          | 0                                 | 1                                                         |

<span id="page-100-3"></span><span id="page-100-0"></span>In this model, the embedding for *I haven't seen a sunny day in weeks* is the sequence of numbers *0 1 1 1 0 0 0 0 1 1 1 1 1*. This is called the *bag-of-words* model, and these embeddings are also called *sparse embeddings* (or sparse vectors—*vector* is another word for a sequence of numbers), because a lot of the numbers will be 0. Most English sentences use only a very small subset of all existing English words.

You can successfully use this model for:

#### *Keyword search*

<span id="page-100-2"></span>You can find which documents contain a given word or words.

#### *Classification of documents*

<span id="page-100-1"></span>You can calculate embeddings for a collection of examples previously labeled as email spam or not spam, average them out, and obtain average word frequencies for each of the classes (spam or not spam). Then, each new

document is compared to those averages and classified accordingly.

The limitation here is that the model has no awareness of meaning, only of the actual words used. For instance, the embeddings for *sunny day* and *bright skies* look very different. In fact they have no words in common, even though we know they have similar meaning. Or, in the email classification problem, a would-be spammer can trick the filter by replacing common "spam words" with their synonyms.

In the next section, we'll see how semantic embeddings address this limitation by using numbers to represent the meaning of the text, instead of the exact words found in the text.

### **LLM-Based Embeddings**

<span id="page-101-0"></span>We're going to skip over all the ML developments that came in between and jump straight to LLM-based embeddings. Just know that there was a gradual evolution from the simple method outlined in the previous section to the sophisticated method described in this one.

You can think of embedding models as an offshoot from the training process of LLMs. If you remember from the [Preface](#page-8-0), the LLM training process (learning from vast amounts of written text) enables LLMs to complete a prompt (or input) with the most appropriate continuation (output). This capability stems from an understanding of the meaning of words and sentences in the context of the surrounding text, learned from how words are used together in the training texts. This *understanding* of the meaning (or semantics) of the prompt can be extracted as a numeric representation (or embedding) of the input text, and can be used directly for some very interesting use cases too.

In practice, most embedding models are trained for that purpose alone, following somewhat similar architectures and training processes as LLMs, as that is more efficient and results in higher-quality embeddings. **[1](#page-161-0)**

<span id="page-102-3"></span><span id="page-102-2"></span><span id="page-102-1"></span><span id="page-102-0"></span>An *embedding model* then is an algorithm that takes a piece of text and outputs a numerical representation of its meaning technically, a long list of floating-point (decimal) numbers, usually somewhere between 100 and 2,000 numbers, or *dimensions*. These are also called *dense* embeddings, as opposed to the *sparse* embeddings of the previous section, as here usually all dimensions are different from 0.

#### **TIP**

Different models produce different numbers and different sizes of lists. All of these are specific to each model; that is, even if the size of the lists matches, you cannot compare embeddings from different models. Combining embeddings from different models should always be avoided.

### **Semantic Embeddings Explained**

<span id="page-103-0"></span>Consider these three words: *lion*, *pet*, and *dog*. Intuitively, which pair of these words share similar characteristics to each other at first glance? The obvious answer is *pet* and *dog*. But computers do not have the ability to tap into this intuition or nuanced understanding of the English language. In order for a computer to differentiate between a lion, pet, or dog, you need to be able to translate them into the language of computers, which is numbers*.*

[Figure](#page-104-0) 2-2 illustrates converting each word into hypothetical number representations that retain their meaning.

<span id="page-104-0"></span>![](_page_104_Figure_0.jpeg)

Figure 2-2. Semantic representations of words

<span id="page-104-1"></span>[Figure](#page-104-0) 2-2 shows each word alongside its corresponding semantic embedding. Note that the numbers themselves have no particular meaning, but instead the sequences of numbers for two words (or sentences) that are close in meaning should be *closer* than those of unrelated words. As you can see, each number is a *floating-point value*, and each of them represents a semantic *dimension*. Let's see what we mean by *closer*:

If we plot these vectors in a three-dimensional space, it could look like [Figure](#page-105-0) 2-3.

<span id="page-105-0"></span>![](_page_105_Figure_1.jpeg)

Figure 2-3. Plot of word vectors in a multidimensional space

[Figure](#page-105-0) 2-3 shows the *pet* and *dog* vectors are closer to each other in distance than the *lion* plot. We can also observe that the angles between each plot varies depending on how similar they are. For example, the words *pet* and *lion* have a wider angle between one another than the *pet* and *dog* do, indicating more similarities shared by the latter word pairs. The narrower the angle or shorter the distance between two vectors, the closer their similarities.

<span id="page-106-0"></span>One effective way to calculate the degree of similarity between two vectors in a multidimensional space is called cosine similarity. *Cosine similarity* computes the dot product of vectors and divides it by the product of their magnitudes to output a number between –1 and 1, where 0 means the vectors share no correlation, –1 means they are absolutely dissimilar, and 1 means they are absolutely similar. So, in the case of our three words here, the cosine similarity between *pet* and *dog* could be 0.75, but between *pet* and *lion* it might be 0.1.

<span id="page-106-1"></span>The ability to convert sentences into embeddings that capture semantic meaning and then perform calculations to find semantic similarities between different sentences enables us to get an LLM to find the most relevant documents to answer questions about a large body of text like our Tesla PDF document. Now that you understand the big picture, let's revisit the first step (indexing) of preprocessing your document.

#### **OTHER USES FOR EMBEDDINGS**

<span id="page-107-0"></span>These sequences of numbers and vectors have a number of interesting properties:

- As you learned earlier, if you think of a vector as describing a point in high-dimensional space, points that are closer together have more similar meanings, so a distance function can be used to measure similarity.
- Groups of points close together can be said to be related; therefore, a clustering algorithm can be used to identify topics (or clusters of points) and classify new inputs into one of those topics.
- If you average out multiple embeddings, the average embedding can be said to represent the overall meaning of that group; that is, you can embed a long document (for instance, this book) by:
	- 1. Embedding each page separately
	- 2. Taking the average of the embeddings of all pages as the book embedding
- You can "travel" the "meaning" space by using the elementary math operations of addition and subtraction: for instance, the operation *king – man + woman = queen.* If you take the meaning (or semantic embedding) of *king*, subtract the meaning of *man*, presumably you arrive at the more

abstract meaning of *monarch*, at which point, if you add the meaning of *woman*, you've arrived close to the meaning (or embedding) of the word *queen*.

There are models that can produce embeddings for nontext content, for instance, images, videos, and sounds, in addition to text. This enables, for instance, finding images that are most similar or relevant for a given sentence.

We won't explore all of these attributes in this book, but it's useful to know they can be used for a number of [applications](https://oreil.ly/PU2C8) such as:

#### *Search*

Finding the most relevant documents for a new query

#### *Clustering*

Given a body of documents, dividing them into groups (for instance, topics)

#### *Classification*

Assigning a new document to a previously identified group or label (for instance, a topic)

#### *Recommendation*

Given a document, surfacing similar documents

*Detecting anomalies*

Identifying documents that are very dissimilar from previously seen ones

We hope this leaves you with some intuition that embeddings are quite versatile and can be put to good use in your future projects.

## Converting Your Documents into Text

<span id="page-109-0"></span>As mentioned at the beginning of the chapter, the first step in preprocessing your document is to convert it to text. In order to achieve this, you would need to build logic to parse and extract the document with minimal loss of quality. Fortunately, LangChain provides *document loaders* that handle the parsing logic and enable you to "load" data from various sources into a Document class that consists of text and associated metadata.

<span id="page-109-1"></span>For example, consider a simple *.txt* file. You can simply import a LangChain TextLoader class to extract the text, like this:

*Python*

```
from langchain_community.document_loaders import
```

```
loader = TextLoader("./test.txt")
loader.load()
```
#### *JavaScript*

```
import { TextLoader } from "langchain/document_lo
const loader = new TextLoader("./test.txt");
const docs = await loader.load();
```
#### *The output:*

```
[Document(page_content='text content \n', metadat
 './test.txt'})]
```
The previous code block assumes that you have a file named test.txt in your current directory. Usage of all LangChain document loaders follows a similar pattern:

- 1. Start by picking the loader for your type of document from the long list of [integrations](https://oreil.ly/iLJ33).
- 2. Create an instance of the loader in question, along with any parameters to configure it, including the location of your documents (usually a filesystem path or web address).
- 3. Load the documents by calling load() , which returns a list of documents ready to pass to the next stage (more on that soon).

Aside from *.txt* files, LangChain provides document loaders for other popular file types including *.csv*, *.json*, and Markdown, alongside integrations with popular platforms such as Slack and Notion.

For example, you can use WebBaseLoader to load HTML from web URLs and parse it to text.

Install the beautifulsoup4 package:

pip install beautifulsoup4

<span id="page-111-0"></span>*Python*

from langchain\_community.document\_loaders import

```
loader = WebBaseLoader("https://www.langchain.com
loader.load()
```
#### <span id="page-112-0"></span>*JavaScript*

```
// install cheerio: npm install cheerio
import {
 CheerioWebBaseLoader
} from "@langchain/community/document_loaders/web
const loader = new CheerioWebBaseLoader("https://
const docs = await loader.load();
```
In the case of our Tesla PDF use case, we can utilize LangChain's PDFLoader to extract text from the PDF document:

#### <span id="page-112-1"></span>*Python*

```
# install the pdf parsing library
# pip install pypdf
```
from langchain\_community.document\_loaders import

```
loader = PyPDFLoader("./test.pdf")
pages = loader.load()
```
#### <span id="page-113-1"></span>*JavaScript*

```
// install the pdf parsing library: npm install p
import { PDFLoader } from "langchain/document_loa
const loader = new PDFLoader("./test.pdf");
const docs = await loader.load();
```
<span id="page-113-0"></span>The text has been extracted from the PDF document and stored in the Document class. But there's a problem. The loaded document is over 100,000 characters long, so it won't fit into the context window of the vast majority of LLMs or embedding models. In order to overcome this limitation, we need to split the Document into manageable chunks of text that we can later convert into embeddings and semantically search, bringing us to the second step (retrieving).

#### **TIP**

LLMs and embedding models are designed with a hard limit on the size of input and output tokens they can handle. This limit is usually called *context window*, and usually applies to the combination of input and output; that is, if the context window is 100 (we'll talk about units in a second), and your input measures 90, the output can be at most of length 10. Context windows are usually measured in number of tokens, for instance 8,192 tokens. Tokens, as mentioned in the [Preface](#page-8-0), are a representation of text as numbers, with each token usually covering between three and four characters of English text.

## <span id="page-114-0"></span>Splitting Your Text into Chunks

<span id="page-114-2"></span><span id="page-114-1"></span>At first glance it may seem straightforward to split a large body of text into chunks, but keeping *semantically* related (related by meaning) chunks of text together is a complex process. To make it easier to split large documents into small, but still meaningful, pieces of text, LangChain provides RecursiveCharacterTextSplitter , which does the following:

- 1. Take a list of separators, in order of importance. By default these are:
	- a. The paragraph separator: \n\n
	- b. The line separator: \n
	- c. The word separator: space character
- 2. To respect the given chunk size, for instance, 1,000 characters, start by splitting up paragraphs.
- 3. For any paragraph longer than the desired chunk size, split by the next separator: lines. Continue until all chunks are smaller than the desired length, or there are no additional separators to try.
- 4. Emit each chunk as a Document , with the metadata of the original document passed in and additional information about the position in the original document.

Let's see an example:

#### <span id="page-115-0"></span>*Python*

```
from langchain_text_splitters import RecursiveCha
loader = TextLoader("./test.txt") # or any other 
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
 chunk_size=1000,
 chunk_overlap=200,
)
splitted_docs = splitter.split_documents(docs)
```
#### <span id="page-116-0"></span>*JavaScript*

```
import { TextLoader } from "langchain/document_lo
import { RecursiveCharacterTextSplitter } from "@
const loader = new TextLoader("./test.txt"); // o
const docs = await loader.load();
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 1000,
 chunkOverlap: 200,
});
const splittedDocs = await splitter.splitDocument
```
In the preceding code, the documents created by the document loader are split into chunks of 1,000 characters each, with some overlap between chunks of 200 characters to maintain some context. The result is also a list of documents, where each document is up to 1,000 characters in length, split along the natural divisions of written text—paragraphs, new lines and finally, words. This uses the structure of the text to keep each chunk a consistent, readable snippet of text.

RecursiveCharacterTextSplitter can also be used to split code languages and Markdown into semantic chunks. This is done by using keywords specific to each language as the separators, which ensures, for instance, the body of each function is kept in the same chunk, instead of split between several. Usually, as programming languages have more structure than written text, there's less need to use overlap between the chunks. LangChain contains separators for a number of popular languages, such as Python, JS, Markdown, HTML, and many more. Here's an example:

*Python*

```
from langchain_text_splitters import (
 Language,
 RecursiveCharacterTextSplitter,
)
PYTHON_CODE = """
def hello_world():
 print("Hello, World!")
# Call the function
hello_world()
"""
```

```
python_splitter = RecursiveCharacterTextSplitter
 language=Language.PYTHON, chunk_size=50, chun
)
python_docs = python_splitter.create_documents([P
```
#### *JavaScript*

```
import { RecursiveCharacterTextSplitter } from "@
const PYTHON_CODE = `
def hello_world():
 print("Hello, World!")
# Call the function
hello_world()
`;
const pythonSplitter = RecursiveCharacterTextSpli
 chunkSize: 50,
 chunkOverlap: 0,
});
const pythonDocs = await pythonSplitter.createDoc
```
*The output:*

[Document(page\_content='def hello\_world():\n p Document(page\_content='# Call the function\nh

#### Notice how we're still using

RecursiveCharacterTextSplitter as before, but now we're creating an instance of it for a specific language, using the from\_language method. This one accepts the name of the language, and the usual parameters for chunk size, and so on. Also notice we are now using the method create\_documents , which accepts a list of strings, rather than the list of documents we had before. This method is useful when the text you want to split doesn't come from a document loader, so you have only the raw text strings.

You can also use the optional second argument to create\_documents in order to pass a list of metadata to associate with each text string. This metadata list should have the same length as the list of strings and will be used to populate the metadata field of each Document returned.

Let's see an example for Markdown text, using the metadata argument as well:

#### *Python*

```
markdown_text = """
# LangChain
⚡ Building applications with LLMs through compos
## Quick Install
```bash
pip install langchain
```
As an open source project in a rapidly developing
 to contributions.
"""
md_splitter = RecursiveCharacterTextSplitter.from
 language=Language.MARKDOWN, chunk_size=60, ch
)
md_docs = md_splitter.create_documents([markdown_
 [{"source": "https://www.langchain.com"}])
```
*JavaScript*

```
const markdownText = `
# LangChain
```

```
⚡ Building applications with LLMs through compos
## Quick Install
\`\`\`bash
pip install langchain
\`\`\`
As an open source project in a rapidly developing
 open to contributions.
`;
const mdSplitter = RecursiveCharacterTextSplitter
 chunkSize: 60,
 chunkOverlap: 0,
});
const mdDocs = await mdSplitter.createDocuments([
 [{"source": "https://www.langchain.com"}]);
```
#### *The output:*

```
[Document(page_content='# LangChain', 
 metadata={"source": "https://www.langchain.co
 Document(page_content='⚡ Building applications 
   ⚡', metadata={"source": "https://www.langcha
```
 ⚡ , metadata { source : https://www.langcha Document(page\_content='## Quick Install\n\n```ba metadata={"source": "https://www.langchain.co Document(page\_content='pip install langchain', metadata={"source": "https://www.langchain.co Document(page\_content='```', metadata={"source" Document(page\_content='As an open source project we', metadata={"source": "https://www.langcha Document(page\_content='are extremely open to con metadata={"source": "https://www.langchain.co

Notice two things:

- The text is split along the natural stopping points in the Markdown document; for instance, the heading goes into one chunk, the line of text under it in a separate chunk, and so on.
- The metadata we passed in the second argument is attached to each resulting document, which allows you to track, for instance, where the document came from and where you can go to see the original.

## <span id="page-122-2"></span>Generating Text Embeddings

<span id="page-122-4"></span><span id="page-122-3"></span><span id="page-122-1"></span><span id="page-122-0"></span>LangChain also has an Embeddings class designed to interface with text embedding models—including OpenAI, Cohere, and

Hugging Face—and generate vector representations of text. This class provides two methods: one for embedding documents and one for embedding a query. The former takes a list of text strings as input, while the latter takes a single text string.

Here's an example of [embedding](https://oreil.ly/9tnzQ) a document using OpenAI's embedding model:

#### <span id="page-123-1"></span>*Python*

```
from langchain_openai import OpenAIEmbeddings
model = OpenAIEmbeddings()
embeddings = model.embed_documents([
 "Hi there!",
 "Oh, hello!",
 "What's your name?",
 "My friends call me World",
 "Hello World!"
])
```
#### <span id="page-123-0"></span>*JavaScript*

import { OpenAIEmbeddings } from "@langchain/open

```
const model = new OpenAIEmbeddings();
const embeddings = await embeddings.embedDocument
 "Hi there!",
 "Oh, hello!",
 "What' s your name?",
 "My friends call me World",
 "Hello World!"
]);
```
#### *The output:*

```
[
 [
 -0.004845875, 0.004899438, -0.016358767, -0.0
 0.012571548, -0.019156644, 0.009036391, -0
 0.022861943, 0.010321903, -0.023479493, -0
 0.0026371893, 0.025206111, -0.012048521, 0.01
 -0.010580265, -0.003509951, 0.004070787, 0.00
 ... 1511 more items
 ]
 [
 -0.009446913, -0.013253193, 0.013174579, 0
 0.0077763423, -0.0260478, -0.0114384955, -0
 0.041797023, 0.01787183, 0.00552271, -0.004
     -0 01542166 0 033752076 0 006112323 0 02
```

```
 -0.01542166, 0.033752076, 0.006112323, 0.02
 -0.006623321, 0.016116094, -0.0061090477, -
 ... 1511 more items
 ]
 ... 3 more items
]
```
Notice that you can embed multiple documents at the same time; you should prefer this to embedding them one at a time, as it will be more efficient (due to how these models are constructed). You get back a list containing multiple lists of numbers—each inner list is a vector or embedding, as explained in an earlier section.

<span id="page-125-1"></span><span id="page-125-0"></span>Now let's see an end-to-end example using the three capabilities we've seen so far:

- Document loaders, to convert any document to plain text
- Text splitters, to split each large document into many smaller ones
- Embeddings models, to create a numeric representation of the meaning of each split

Here's the code:

<span id="page-125-2"></span>*Python*

```
from langchain_community.document_loaders import
from langchain_text_splitters import RecursiveCha
from langchain_openai import OpenAIEmbeddings
```

```
## Load the document
```

```
loader = TextLoader("./test.txt")
doc = loader.load()
```
"""

[

```
 Document(page_content='Document loaders\n\nUs
 from a source as `Document`\'s. A `Docume
 associated metadata. For example, there a
 loading a simple `.txt` file, for loading
 page, or even for loading a transcript of
 document loader exposes two methods:\n1. 
 the configured source\n2. "Load and split
 configured source and split them using th
 splitter\n\nThey optionally implement:\n\
 documents into memory lazily\n', metadata
```
] """

```
## Split the document
```
h k i 1000

text\_splitter = RecursiveCharacterTextSplitter(

```
 chunk_size=1000,
 chunk_overlap=20,
)
chunks = text_splitter.split_documents(doc)
## Generate embeddings
embeddings_model = OpenAIEmbeddings()
embeddings = embeddings_model.embed_documents(
 [chunk.page_content for chunk in chunks]
)
"""
[[0.0053587136790156364,
 -0.0004999046213924885,
 0.038883671164512634,
 -0.003001077566295862,
 -0.00900818221271038, ...], ...]
"""
```
#### <span id="page-127-0"></span>*JavaScript*

```
import { TextLoader } from "langchain/document_lo
import { RecursiveCharacterTextSplitter } from "@
import { OpenAIEmbeddings } from "@langchain/open
// Load the document
```

```
const loader = new TextLoader("./test.txt");
const docs = await loader.load();
// Split the document
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 1000,
 chunkOverlap: 200,
});
const chunks = await splitter.splitDocuments(docs
// Generate embeddings
const model = new OpenAIEmbeddings();
await embeddings.embedDocuments(chunks.map(c => c
```
<span id="page-128-0"></span>Once you've generated embeddings from your documents, the next step is to store them in a special database known as a vector store.

## Storing Embeddings in a Vector Store

<span id="page-128-1"></span>Earlier in this chapter, we discussed the cosine similarity calculation to measure the similarity between vectors in a vector space. A vector store is a database designed to store vectors and perform complex calculations, like cosine similarity, efficiently and quickly.

Unlike traditional databases that specialize in storing structured data (such as JSON documents or data conforming to the schema of a relational database), vector stores handle unstructured data, including text and images. Like traditional databases, vector stores are capable of performing create, read, update, delete (CRUD), and search operations.

<span id="page-129-1"></span>Vector stores unlock a wide variety of use cases, including scalable applications that utilize AI to answer questions about large documents, as illustrated in [Figure](#page-129-0) 2-4.

<span id="page-129-0"></span>![](_page_129_Figure_3.jpeg)

Figure 2-4. Loading, embedding, storing, and retrieving relevant docs from a vector store

[Figure](#page-129-0) 2-4 illustrates how document embeddings are inserted into the vector store and how later, when a query is sent, similar embeddings are retrieved from the vector store.

Currently, there is an abundance of vector store providers to choose from, each specializing in different capabilities. Your selection should depend on the critical requirements of your

application, including multitenancy, metadata filtering capabilities, performance, cost, and scalability.

Although vector stores are niche databases built to manage vector data, there are a few disadvantages working with them:

- Most vector stores are relatively new and may not stand the test of time.
- Managing and optimizing vector stores can present a relatively steep learning curve.
- Managing a separate database adds complexity to your application and may drain valuable resources.

Fortunately, vector store capabilities have recently been extended to PostgreSQL (a popular open source relational database) via the pgvector extension. This enables you to use the same database you're already familiar with and to power both your transactional tables (for instance your users table) as well as your vector search tables.

### <span id="page-130-0"></span>**Getting Set Up with PGVector**

<span id="page-130-1"></span>To use Postgres and PGVector you'll need to follow a few setup steps:

- 1. Ensure you have Docker installed on your computer, following the [instructions](https://oreil.ly/Gn28O) for your operating system.
- 2. Run the following command in your terminal; it will launch a Postgres instance in your computer running on port 6024:

```
docker run \
 --name pgvector-container \
 -e POSTGRES_USER=langchain \
 -e POSTGRES_PASSWORD=langchain \
 -e POSTGRES_DB=langchain \
 -p 6024:5432 \
 -d pgvector/pgvector:pg16
```
Open your docker dashboard containers and you should see a green running status next to pgvector-container .

3. Save the connection string to use in your code; we'll need it later:

postgresql+psycopg://langchain:langchain@localh

### **Working with Vector Stores**

Picking up where we left off in the previous section on embeddings, now let's see an example of loading, splitting, embedding, and storing a document in PGVector:

#### <span id="page-132-0"></span>*Python*

```
# first, pip install langchain-postgres
from langchain_community.document_loaders import
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCha
from langchain_postgres.vectorstores import PGVec
from langchain_core.documents import Document
import uuid
```

```
# Load the document, split it into chunks
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(ch
```

```
 chunk_overlap=200)
documents = text_splitter.split_documents(raw_doc
```

```
# embed each chunk and insert it into the vector 
embeddings_model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:lang
db = PGVector.from_documents(documents, embedding
```
#### <span id="page-133-0"></span>*JavaScript*

```
import { TextLoader } from "langchain/document_lo
import { RecursiveCharacterTextSplitter } from "@
import { OpenAIEmbeddings } from "@langchain/open
import { PGVectorStore } from "@langchain/communi
import { v4 as uuidv4 } from 'uuid';
// Load the document, split it into chunks
const loader = new TextLoader("./test.txt");
const raw_docs = await loader.load();
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 1000,
 chunkOverlap: 200,
});
const docs = await splitter.splitDocuments(docs)
// embed each chunk and insert it into the vector
const embeddings_model = new OpenAIEmbeddings();
const db = await PGVectorStore.fromDocuments(docs
 postgresConnectionOptions: {
 connectionString: 'postgresql://langchain:lan
 }
})
```
Notice how we reuse the code from the previous sections to first load the documents with the loader and then split them into smaller chunks. Then, we instantiate the embeddings model we want to use—in this case, OpenAI's. Note that you could use any other embeddings model supported by LangChain here.

Next, we have a new line of code, which creates a vector store given documents, the embeddings model, and a connection string. This will do a few things:

- Establish a connection to the Postgres instance running in your computer (see "Getting Set Up with [PGVector"](#page-130-0).)
- Run any setup necessary, such as creating tables to hold your documents and vectors, if this is the first time you're running it.
- Create embeddings for each document you passed in, using the model you chose.
- Store the embeddings, the document's metadata, and the document's text content in Postgres, ready to be searched.

Let's see what it looks like to search documents:

*Python*

```
db.similarity_search("query", k=4)
```
*JavaScript*

await pgvectorStore.similaritySearch("query", 4);

This method will find the most relevant documents (which you previously indexed), by following this process:

- The search query—in this case, the word query —will be sent to the embeddings model to retrieve its embedding.
- Then, it will run a query on Postgres to find the N (in this case 4) previously stored embeddings that are most similar to your query.
- Finally, it will fetch the text content and metadata that relates to each of those embeddings.
- The model can now return a list of Document sorted by how similar they are to the query—the most similar first, the second most similar after, and so on.

You can also add more documents to an existing database. Let's see an example:

*Python*

```
ids = [str(uuid.uuid4()), str(uuid.uuid4())]
db.add_documents(
 [
 Document(
 page_content="there are cats in the p
 metadata={"location": "pond", "topic"
 ),
 Document(
 page_content="ducks are also found in
 metadata={"location": "pond", "topic"
 ),
 ],
 ids=ids,
)
```
*JavaScript*

```
const ids = [uuidv4(), uuidv4()];
await db.addDocuments(
 [
 {
 pageContent: "there are cats in the pond",
 metadata: {location: "pond", topic: "animal
 },
 {
```

```
{
 pageContent: "ducks are also found in the p
 metadata: {location: "pond", topic: "animal
 },
 ],
 {ids}
);
```
The add\_documents method we're using here will follow a similar process to fromDocuments :

- Create embeddings for each document you passed in, using the model you chose.
- Store the embeddings, the document's metadata, and the document's text content in Postgres, ready to be searched.

In this example, we are using the optional ids argument to assign identifiers to each document, which allows us to update or delete them later.

Here's an example of the delete operation:

*Python*

db.delete(ids=[1])

*JavaScript*

```
await db.delete({ ids: [ids[1]] })
```
This removes the second document inserted by using its Universally Unique Identifier (UUID). Now let's see how to do this in a more systematic way.

## Tracking Changes to Your Documents

<span id="page-138-1"></span>One of the key challenges with working with vector stores is working with data that regularly changes, because changes mean re-indexing. And re-indexing can lead to costly recomputations of embeddings and duplications of preexisting content.

<span id="page-138-2"></span>Fortunately, LangChain provides an indexing API to make it easy to keep your documents in sync with your vector store. The API utilizes a class ( RecordManager ) to keep track of document writes into the vector store. When indexing content, hashes are computed for each document and the following information is stored in RecordManager :

- The document hash (hash of both page content and metadata)
- Write time
- The source ID (each document should include information in its metadata to determine the ultimate source of this document).

<span id="page-139-0"></span>In addition, the indexing API provides cleanup modes to help you decide how to delete existing documents in the vector store. For example, If you've made changes to how documents are processed before insertion or if source documents have changed, you may want to remove any existing documents that come from the same source as the new documents being indexed. If some source documents have been deleted, you'll want to delete all existing documents in the vector store and replace them with the re-indexed documents.

The modes are as follows:

- None mode does not do any automatic cleanup, allowing the user to manually do cleanup of old content.
- Incremental and full modes delete previous versions of the content if the content of the source document or derived documents has changed.

Full mode will additionally delete any documents not included in documents currently being indexed.

Here's an example of the use of the indexing API with Postgres database set up as a record manager:

#### <span id="page-140-0"></span>*Python*

```
from langchain.indexes import SQLRecordManager, i
from langchain_postgres.vectorstores import PGVec
from langchain_openai import OpenAIEmbeddings
from langchain.docstore.document import Document
connection = "postgresql+psycopg://langchain:lang
collection_name = "my_docs"
embeddings_model = OpenAIEmbeddings(model="text-e
namespace = "my_docs_namespace"
vectorstore = PGVector(
 embeddings=embeddings_model,
 collection_name=collection_name,
 connection=connection,
 use_jsonb=True,
)
record_manager = SQLRecordManager(
 namespace,
```

```
 db_url="postgresql+psycopg://langchain:langch
)
# Create the schema if it doesn't exist
record_manager.create_schema()
# Create documents
docs = [
 Document(page_content='there are cats in the 
 "id": 1, "source": "cats.txt"}),
 Document(page_content='ducks are also found i
 "id": 2, "source": "ducks.txt"}),
]
# Index the documents
index_1 = index(
 docs,
 record_manager,
 vectorstore,
 cleanup="incremental", # prevent duplicate d
 source_id_key="source", # use the source fie
)
print("Index attempt 1:", index_1)
# second time you attempt to index, it will not a
index_2 = index(
 docs,
 record manager,
```

```
 vectorstore,
 cleanup="incremental",
 source_id_key="source",
)
print("Index attempt 2:", index_2)
# If we mutate a document, the new version will b
# versions sharing the same source will be delete
docs[0].page_content = "I just modified this docu
index_3 = index(
 docs,
 record_manager,
 vectorstore,
 cleanup="incremental",
 source_id_key="source",
)
print("Index attempt 3:", index_3)
```
\_ g ,

<span id="page-142-0"></span>*JavaScript*

/\*\* 1 Ensure docker is installed and running (https 1. Ensure docker is installed and running (https 2. Run the following command to start the postgre

```
docker run \
```
--name pgvector-container \

-e POSTGRES\_USER=langchain \

- -e POSTGRES\_PASSWORD=langchain \
- -e POSTGRES\_DB=langchain \
- -p 6024:5432 \

-d pgvector/pgvector:pg16

```
3. Use the connection string below for the postgr
*/
```

```
import { PostgresRecordManager } from '@langchain
import { index } from 'langchain/indexes';
import { OpenAIEmbeddings } from '@langchain/open
import { PGVectorStore } from '@langchain/communi
import { v4 as uuidv4 } from 'uuid';
```

```
const tableName = 'test_langchain';
const connectionString =
```
 'postgresql://langchain:langchain@localhost:602 // Load the document, split it into chunks

```
const config = {
 postgresConnectionOptions: {
 connectionString,
 },
 tableName: tableName
```

```
 tableName: tableName,
 columns: {
 idColumnName: 'id',
 vectorColumnName: 'vector',
 contentColumnName: 'content',
 metadataColumnName: 'metadata',
 },
};
const vectorStore = await PGVectorStore.initializ
 new OpenAIEmbeddings(),
 config
);
// Create a new record manager
const recordManagerConfig = {
 postgresConnectionOptions: {
 connectionString,
 },
 tableName: 'upsertion_records',
};
const recordManager = new PostgresRecordManager(
 'test_namespace',
 recordManagerConfig
);
// Create the schema if it doesn't exist
await recordManager.createSchema();
```

```
const docs = [
 {
 pageContent: 'there are cats in the pond',
 metadata: { id: uuidv4(), source: 'cats.txt'
 },
 {
 pageContent: 'ducks are also found in the pon
 metadata: { id: uuidv4(), source: 'ducks.txt
 },
];
// the first attempt will index both documents
const index_attempt_1 = await index({
 docsSource: docs,
 recordManager,
 vectorStore,
 options: {
 // prevent duplicate documents by id from bei
 cleanup: 'incremental',
 // the key in the metadata that will be used 
 sourceIdKey: 'source',
 },
});
console.log(index_attempt_1);
// the second attempt will skip indexing because 
// already exist
```

```
// already exist
const index_attempt_2 = await index({
 docsSource: docs,
 recordManager,
 vectorStore,
 options: {
 cleanup: 'incremental',
 sourceIdKey: 'source',
 },
});
console.log(index_attempt_2);
// If we mutate a document, the new version will 
// versions sharing the same source will be delet
docs[0].pageContent = 'I modified the first docum
const index_attempt_3 = await index({
 docsSource: docs,
 recordManager,
 vectorStore,
 options: {
 cleanup: 'incremental',
 sourceIdKey: 'source',
 },
});
console.log(index_attempt_3);
```
First, you create a record manager, which keeps track of which documents have been indexed before. Then you use the index function to synchronize your vector store with the new list of documents. In this example, we're using the incremental mode, so any documents that have the same ID as previous ones will be replaced with the new version.

## <span id="page-147-1"></span>Indexing Optimization

<span id="page-147-0"></span>A basic RAG indexing stage involves naive text splitting and embedding of chunks of a given document. However, this basic approach leads to inconsistent retrieval results and a relatively high occurrence of hallucinations, especially when the data source contains images and tables.

There are various strategies to enhance the accuracy and performance of the indexing stage. We will cover three of them in the next sections: MultiVectorRetriever, RAPTOR, and ColBERT.

### **MultiVectorRetriever**

<span id="page-147-2"></span>A document that contains a mixture of text and tables cannot be simply split by text into chunks and embedded as context: the entire table can be easily lost. To solve this problem, we can decouple documents that we want to use for answer synthesis, from a reference that we want to use for the [retriever. Figure](#page-148-0) 2- 5 illustrates how.

<span id="page-148-0"></span>![](_page_148_Figure_1.jpeg)

Figure 2-5. Indexing multiple representations of a single document

For example, in the case of a document that contains tables, we can first generate and embed summaries of table elements, ensuring each summary contains an id reference to the full raw table. Next, we store the raw referenced tables in a separate docstore. Finally, when a user's query retrieves a table summary, we pass the entire referenced raw table as context to the final prompt sent to the LLM for answer synthesis. This approach enables us to provide the model with the full context of information required to answer the question.

Here's an example. First, let's use the LLM to generate summaries of the documents:

#### <span id="page-149-0"></span>*Python*

from langchain\_community.document\_loaders import from langchain\_text\_splitters import RecursiveCha from langchain\_openai import OpenAIEmbeddings from langchain\_postgres.vectorstores import PGVec from langchain\_core.output\_parsers import StrOutp from langchain\_core.prompts import ChatPromptTemp from pydantic import BaseModel from langchain\_core.runnables import RunnablePass from langchain\_openai import ChatOpenAI from langchain\_core.documents import Document from langchain.retrievers.multi\_vector import Mul from langchain.storage import InMemoryStore import uuid connection = "postgresql+psycopg://langchain:lang collection\_name = "summaries" embeddings\_model = OpenAIEmbeddings() # Load the document loader = TextLoader("./test.txt", encoding="utf-8 docs = loader.load()

print("length of loaded docs: ", len(docs[0].page

```
# Split the document
splitter = RecursiveCharacterTextSplitter(chunk_s
chunks = splitter.split_documents(docs)
# The rest of your code remains the same, startin
prompt_text = "Summarize the following document:\
prompt = ChatPromptTemplate.from_template(prompt_
llm = ChatOpenAI(temperature=0, model="gpt-3.5-tu
summarize_chain = {
 "doc": lambda x: x.page_content} | prompt | l
# batch the chain across the chunks
summaries = summarize_chain.batch(chunks, {"max_c
```
Next, let's define the vector store and docstore to store the raw summaries and their embeddings:

#### <span id="page-150-0"></span>*Python*

)

```
# The vectorstore to use to index the child chunk
vectorstore = PGVector(
 embeddings=embeddings_model,
 collection_name=collection_name,
 connection=connection,
 use_jsonb=True,
```

```
)
# The storage layer for the parent documents
store = InMemoryStore()
id_key = "doc_id"
# indexing the summaries in our vector store, whi
# documents in our document store:
retriever = MultiVectorRetriever(
 vectorstore=vectorstore,
 docstore=store,
 id_key=id_key,
)
# Changed from summaries to chunks since we need 
doc_ids = [str(uuid.uuid4()) for _ in chunks]
# Each summary is linked to the original document
summary_docs = [
 Document(page_content=s, metadata={id_key: do
 for i, s in enumerate(summaries)
]
# Add the document summaries to the vector store 
retriever.vectorstore.add_documents(summary_docs)
# Store the original documents in the document st
# via doc_ids
# This allows us to first search summaries effici
# docs when needed
```
retriever.docstore.mset(list(zip(doc\_ids, chunks)

```
# vector store retrieves the summaries
sub_docs = retriever.vectorstore.similarity_searc
 "chapter on philosophy", k=2)
```
Finally, let's retrieve the relevant full context document based on a query:

<span id="page-152-1"></span>*Python*

```
# Whereas the retriever will return the larger so
retrieved_docs = retriever.invoke("chapter on phi
```
Here's the full implementation in JavaScript:

<span id="page-152-0"></span>*JavaScript*

```
import * as uuid from 'uuid';
import { MultiVectorRetriever } from 'langchain/r
import { OpenAIEmbeddings } from '@langchain/open
import { RecursiveCharacterTextSplitter } from '@
```

```
import { InMemoryStore } from '@langchain/core/st
import { TextLoader } from 'langchain/document_lo
import { Document } from '@langchain/core/documen
import { PGVectorStore } from '@langchain/communi
import { ChatOpenAI } from '@langchain/openai';
import { PromptTemplate } from '@langchain/core/p
import { RunnableSequence } from '@langchain/core
import { StringOutputParser } from '@langchain/co
const connectionString =
 'postgresql://langchain:langchain@localhost:602
const collectionName = 'summaries';
const textLoader = new TextLoader('./test.txt');
const parentDocuments = await textLoader.load();
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 10000,
 chunkOverlap: 20,
});
const docs = await splitter.splitDocuments(parent
const prompt = PromptTemplate.fromTemplate(
 `Summarize the following document:\n\n{doc}`
);
const llm = new ChatOpenAI({ modelName: 'gpt-3.5-
const chain = RunnableSequence.from([
```

```
 { doc: (doc) => doc.pageContent },
 prompt,
 llm,
 new StringOutputParser(),
]);
// batch summarization chain across the chunks
const summaries = await chain.batch(docs, {
 maxConcurrency: 5,
});
const idKey = 'doc_id';
const docIds = docs.map((_) => uuid.v4());
// create summary docs with metadata linking to t
const summaryDocs = summaries.map((summary, i) =>
 const summaryDoc = new Document({
 pageContent: summary,
 metadata: {
 [idKey]: docIds[i],
 },
 });
 return summaryDoc;
});
// The byteStore to use to store the original chu
const byteStore = new InMemoryStore();
```
// vector store for the summaries

```
const vectorStore = await PGVectorStore.fromDocum
 docs,
 new OpenAIEmbeddings(),
 {
 postgresConnectionOptions: {
 connectionString,
 },
 }
);
const retriever = new MultiVectorRetriever({
 vectorstore: vectorStore,
 byteStore,
 idKey,
});
const keyValuePairs = docs.map((originalDoc, i) =
// Use the retriever to add the original chunks t
await retriever.docstore.mset(keyValuePairs);
// Vectorstore alone retrieves the small chunks
const vectorstoreResult = await retriever.vectors
 'chapter on philosophy',
 2
);
console.log(`summary: ${vectorstoreResult[0].page
console.log(
```

```
 `summary retrieved length: ${vectorstoreResult[
);
// Retriever returns larger chunk result
const retrieverResult = await retriever.invoke('c
console.log(
 `multi-vector retrieved chunk length: ${retriev
);
```
### **RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval**

<span id="page-156-2"></span><span id="page-156-1"></span>RAG systems need to handle lower-level questions that reference specific facts found in a single document or higherlevel questions that distill ideas that span many documents. Handling both types of questions can be a challenge with typical k-nearest neighbors (k-NN) retrieval over document chunks.

<span id="page-156-3"></span><span id="page-156-0"></span>*Recursive abstractive processing for tree-organized retrieval* (RAPTOR) is an effective strategy that involves creating document summaries that capture higher-level concepts, embedding and clustering those documents, and then [summarizing](https://oreil.ly/VdIpJ) each cluster. This is done recursively, producing a tree of summaries with increasingly high-level concepts. The **[2](#page-162-0)**

summaries and initial documents are then indexed together, giving coverage across lower-to-higher-level user questions. [Figure](#page-157-0) 2-6 illustrates.

<span id="page-157-0"></span>![](_page_157_Figure_1.jpeg)

Figure 2-6. Recursively summarizing documents

### **ColBERT: Optimizing Embeddings**

<span id="page-157-1"></span>One of the challenges of using embeddings models during the indexing stage is that they compress text into fixed-length (vector) representations that capture the semantic content of the document. Although this compression is useful for retrieval, <span id="page-158-1"></span>embedding irrelevant or redundant content may lead to hallucinations in the final LLM output.

One solution to this problem is to do the following:

- 1. Generate contextual embeddings for each token in the document and query.
- 2. Calculate and score similarity between each query token and all document tokens.
- 3. Sum the maximum similarity score of each query embedding to any of the document embeddings to get a score for each document.

<span id="page-158-0"></span>This results in a granular and effective embedding approach for better retrieval. Fortunately, the embedding model called ColBERT embodies the solution to this problem. **[3](#page-162-1)**

Here's how we can utilize ColBERT for optimal embedding of our data:

#### <span id="page-158-2"></span>*Python*

# RAGatouille is a library that makes it simple t #! pip install -U ragatouille

from ragatouille import RAGPretrainedModel

```
RAG = RAGPretrainedModel.from_pretrained("colbert
```

```
import requests
```
g p

data = response.json()

```
def get_wikipedia_page(title: str):
 """
 Retrieve the full text content of a Wikipedia
 :param title: str - Title of the Wikipedia pa
 :return: str - Full text content of the page 
 """
 # Wikipedia API endpoint
 URL = "https://en.wikipedia.org/w/api.php"
 # Parameters for the API request
 params = {
 "action": "query",
 "format": "json",
 "titles": title,
 "prop": "extracts",
 "explaintext": True,
 }
 # Custom User-Agent header to comply with Wik
 headers = {"User-Agent": "RAGatouille_tutoria
 response = requests.get(URL, params=params, h
```

```
 # Extracting page content
 page = next(iter(data["query"]["pages"].value
 return page["extract"] if "extract" in page e
full_document = get_wikipedia_page("Hayao_Miyazak
## Create an index
RAG.index(
 collection=[full_document],
 index_name="Miyazaki-123",
 max_document_length=180,
 split_documents=True,
)
#query
results = RAG.search(query="What animation studio
results
#utilize langchain retriever
retriever = RAG.as_langchain_retriever(k=3)
retriever.invoke("What animation studio did Miyaz
```
p j ()

By using ColBERT, you can improve the relevancy of retrieved documents used as context by the LLM.

## Summary

<span id="page-161-1"></span>In this chapter, you've learned how to prepare and preprocess your documents for your LLM application using various LangChain's modules. The document loaders enable you to extract text from your data source, the text splitters help you split your document into semantically similar chunks, and the embeddings models convert your text into vector representations of their meaning.

Separately, vector stores allow you to perform CRUD operations on these embeddings alongside complex calculations to compute semantically similar chunks of text. Finally, indexing optimization strategies enable your AI app to improve the quality of embeddings and perform accurate retrieval of documents that contain semistructured data including tables.

In [Chapter](#page-163-0) 3, you'll learn how to efficiently retrieve the most similar chunks of documents from your vector store based on your query, provide it as context the model can see, and then generate an accurate output.

<span id="page-161-0"></span>Arvind Neelakantan et al., "Text and Code Embeddings by Contrastive [Pre-Training"](https://oreil.ly/YOVmh), arXiv, January 21, 2022. **[1](#page-102-0)**

<span id="page-162-0"></span>Parth Sarthi et al., "RAPTOR: Recursive Abstractive Processing for [Tree-Organized](https://oreil.ly/hS4NB) Retrieval", arXiv, January 31, 2024. Paper published at ICLR 2024. **[2](#page-156-0)**

<span id="page-162-1"></span>Keshav Santhanam et al., "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late [Interaction",](https://oreil.ly/9spW2) arXiv, December 2, 2021. **[3](#page-158-0)**

## <span id="page-163-0"></span>Chapter 3. RAG Part II: Chatting with Your Data

In the previous chapter, you learned how to process your data and create and store embeddings in a vector store. In this chapter, you'll learn how to efficiently retrieve the most relevant embeddings and chunks of documents based on a user's query. This enables you to construct a prompt that contains relevant documents as context, improving the accuracy of the LLM's final output.

This process—which involves embedding a user's query, retrieving similar documents from a data source, and then passing them as context to the prompt sent to the LLM—is formally known as *retrieval-augmented generation* (RAG).

<span id="page-163-1"></span>RAG is an essential component of building chat-enabled LLM apps that are accurate, efficient, and up-to-date. In this chapter, you'll progress from basics to advanced strategies to build an effective RAG system for various data sources (such as vector stores and databases) and data structures (structured and unstructured).

But first, let's define RAG and discuss its benefits.

# Introducing Retrieval-Augmented Generation

<span id="page-164-2"></span>RAG is a technique used to enhance the accuracy of outputs generated by LLMs by providing context from external sources. The term was originally coined in a paper by Meta AI researchers who discovered that RAG-enabled models are more factual and specific than non-RAG models. **[1](#page-235-0)**

<span id="page-164-0"></span>Without RAG, the LLM relies solely on its pretrained data, which may be outdated. For example, let's ask ChatGPT a question about a current event and see its response:

#### <span id="page-164-1"></span>*Input*

Which country is the latest winner of the men's F

#### *Output*

The most recent FIFA World Cup winner was France,

The response by the LLM is factually incorrect and outdated. The latest winner at the time of this book's publication is Argentina, who won the World Cup in 2022. While this example question may be trivial, LLM hallucination can have disastrous consequences if its answers are relied upon for fact-checking or important decision making.

<span id="page-165-1"></span>To combat this problem, we need to provide the LLM with factual, up-to-date information from which it can formulate an accurate response. Continuing on from the previous example, let's go over to Wikipedia's page for the FIFA [World](https://oreil.ly/LpLOV) Cup, copy the introduction paragraph, and then append it as *context* to our prompt to ChatGPT:

<span id="page-165-0"></span>Which country is the latest winner of the men's F

See context below.

The FIFA World Cup, often called the World Cup, i football competition among the senior men's natio the Fédération Internationale de Football Associa global governing body. The tournament has been he inaugural tournament in 1930, with the exception Second World War. The reigning champions are Arge title at the 2022 tournament.

Note that the last sentence contains the necessary context the LLM can use to provide an accurate answer. Here's the response from the LLM:

The latest winner of the men's FIFA World Cup is title at the 2022 tournament.

Because of the up-to-date additional context provided, the LLM was able to generate an accurate response to the prompt. But copying and pasting relevant information as context isn't practical nor scalable for a production AI application. We need an automated system to fetch relevant information based on a user's query, append it as context to the prompt, and then execute the generation request to the LLM.

### **Retrieving Relevant Documents**

<span id="page-166-2"></span>A RAG system for an AI app typically follows three core stages:

*Indexing*

<span id="page-166-3"></span><span id="page-166-1"></span><span id="page-166-0"></span>This stage involves preprocessing the external data source and storing embeddings that represent the data in a

vector store where they can be easily retrieved.

#### *Retrieval*

This stage involves retrieving the relevant embeddings and data stored in the vector store based on a user's query.

#### *Generation*

This stage involves synthesizing the original prompt with the retrieved relevant documents as one final prompt sent to the model for a prediction.

The three basic stages look like [Figure](#page-167-0) 3-1.

<span id="page-167-0"></span>![](_page_167_Figure_6.jpeg)

Figure 3-1. The key stages of RAG

The indexing stage of this process was covered extensively in [Chapter](#page-93-0) 2, where you learned how to use document loaders,

text splitters, embeddings, and vector stores.

Let's run through an example from scratch again, starting with the indexing stage:

<span id="page-168-1"></span>*Python*

```
from langchain_community.document_loaders import
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCha
from langchain_postgres.vectorstores import PGVec
```

```
# Load the document, split it into chunks
raw_documents = TextLoader('./test.txt').load()
text_splitter = RecursiveCharacterTextSplitter(ch
 chunk_overlap=200)
documents = text_splitter.split_documents(raw_doc
```

```
# embed each chunk and insert it into the vector 
model = OpenAIEmbeddings()
connection = 'postgresql+psycopg://langchain:lang
db = PGVector.from_documents(documents, model, co
```
<span id="page-168-0"></span>*JavaScript*

```
import { TextLoader } from "langchain/document_lo
import { RecursiveCharacterTextSplitter } from "@
import { OpenAIEmbeddings } from "@langchain/open
import { PGVectorStore } from "@langchain/communi
// Load the document, split it into chunks
const loader = new TextLoader("./test.txt");
const raw_docs = await loader.load();
const splitter = new RecursiveCharacterTextSplitt
 chunkSize: 1000,
 chunkOverlap: 200,
});
const docs = await splitter.splitDocuments(docs)
// embed each chunk and insert it into the vector
const model = new OpenAIEmbeddings();
const db = await PGVectorStore.fromDocuments(docs
 postgresConnectionOptions: {
 connectionString: 'postgresql://langchain:lan
 }
})
```
[Chapter](#page-93-0) 2 has more details on the indexing stage.

<span id="page-169-0"></span>The indexing stage is now complete. In order to execute the retrieval stage, we need to perform similarity search calculations—such as cosine similarity—between the user's

query and our stored embeddings, so relevant chunks of our indexed document are retrieved (see [Figure](#page-171-0) 3-2).

<span id="page-171-0"></span>![](_page_171_Figure_0.jpeg)

Figure 3-2. An example flow of indexing documents alongside retrieval of relevant documents from a vector store; the Hierarchical Navigable Small World (HNSW) box depicts calculating similarity of documents against the user's query

<span id="page-172-0"></span>[Figure](#page-171-0) 3-2 illustrates the steps in the retrieval process:

- 1. Convert the user's query into embeddings.
- 2. Calculate the embeddings in the vector store that are most similar to the user's query.
- 3. Retrieve the relevant document embeddings and their corresponding text chunk.

We can represent these steps programmatically using LangChain as follows:

#### <span id="page-172-2"></span>*Python*

```
# create retriever
retriever = db.as_retriever()
# fetch relevant documents
docs = retriever.invoke("""Who are the key figure
 history of philosophy?""")
```
#### <span id="page-172-1"></span>*JavaScript*

```
// create retriever
const retriever = db.asRetriever()
```

```
// fetch relevant documents
const docs = await retriever.invoke(`Who are the 
 greek history of philosophy?`)
```
Note that we are using a vector store method you haven't seen before: as\_retriever . This function abstracts the logic of embedding the user's query and the underlying similarity search calculations performed by the vector store to retrieve the relevant documents.

<span id="page-173-0"></span>There is also an argument k , which determines the number of relevant documents to fetch from the vector store. For example:

*Python*

```
# create retriever with k=2
retriever = db.as_retriever(search_kwargs={"k": 2
# fetch the 2 most relevant documents
docs = retriever.invoke("""Who are the key figure
 of philosophy?""")
```
*JavaScript*

```
// create retriever with k=2
const retriever = db.asRetriever({k: 2})
// fetch the 2 most relevant documents
const docs = await retriever.invoke(`Who are the 
 greek history of philosophy?`)
```
In this example, the argument k is specified as 2. This tells the vector store to return the two most relevant documents based on the user's query.

It may seem counterintuitive to use a low k value, but retrieving more documents is not always better. The more documents are retrieved, the slower your application will perform, the larger the prompt (and associated cost of generation) will be, and the greater the likelihood of retrieving chunks of text that contain irrelevant information, which will cause the LLM to hallucinate.

<span id="page-174-0"></span>Now that we've completed the retrieval stage of the RAG system, let's move on to the final generation stage.

### **Generating LLM Predictions Using Relevant Documents**

<span id="page-175-1"></span>Once we've retrieved the relevant documents based on the user's query, the final step is to add them to the original prompt as context and then invoke the model to generate a final output [\(Figure](#page-175-0) 3-3).

<span id="page-175-0"></span>![](_page_175_Figure_1.jpeg)

Figure 3-3. An example flow demonstrating indexing documents, retrieval of relevant documents from a vector store, and inclusion of retrieved documents as context in the LLM prompt

Here's a code example continuing on from our previous example:

<span id="page-176-0"></span>*Python*

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemp
retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answ
 the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temp
chain = prompt | llm
# fetch relevant documents 
docs = retriever.get_relevant_documents("""Who ar
 ancient greek history of philosophy?""")
# run
```
h i i k ({" t t" d " ti " """Wh

```
chain.invoke({"context": docs,"question": """Who 
 ancient greek history of philosophy?"""})
```
<span id="page-177-0"></span>*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
const retriever = db.asRetriever()
const prompt = ChatPromptTemplate.fromTemplate(`A
 on the following context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0, model
const chain = prompt.pipe(llm)
// fetch relevant documents
const docs = await retriever.invoke(`Who are the 
 greek history of philosophy?`)
await chain.invoke({context: docs, question: `Who
 ancient greek history of philosophy?`})
```
![](_page_178_Picture_0.jpeg)

Note the following changes:

- We implement dynamic context and question variables into our prompt, which allows us to define a ChatPromptTemplate the model can use to generate a response.
- We define a ChatOpenAI interface to act as our LLM. Temperature is set to 0 to eliminate the creativity in outputs from the model.
- We create a chain to compose the prompt and LLM. A reminder: the | operator (or pipe method in JS) takes the output of prompt and uses it as the input to llm .
- We invoke the chain passing in the context variable (our retrieved relevant docs) and the user's question to generate a final output.

We can encapsulate this retrieval logic in a single function:

#### *Python*

from langchain\_openai import ChatOpenAI from langchain\_core.prompts import ChatPromptTemp from langchain\_core.runnables import chain

```
retriever = db.as_retriever()
prompt = ChatPromptTemplate.from_template("""Answ
 the following context:
{context}
Question: {question}
""")
llm = ChatOpenAI(model="gpt-3.5-turbo", temperatu
@chain
def qa(input):
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(input
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                              "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
# run
qa.invoke("Who are the key figures in the ancient
```
*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
import {RunnableLambda} from '@langchain/core/run
const retriever = db.asRetriever()
const prompt = ChatPromptTemplate.fromTemplate(`A
 on the following context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0, model
```

```
const qa = RunnableLambda.from(async input => {
 // fetch relevant documents
 const docs = await retriever.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
```
await qa.invoke(`Who are the key figures in the a philosophy?`)

| p<br>p<br>y<br>) |  |
|------------------|--|
|                  |  |
|                  |  |
|                  |  |

Notice how we now have a new runnable qa function that can be called with just a question and takes care to first fetch the relevant docs for context, format them into the prompt, and finally generate the answer. In the Python code, the @chain decorator turns the function into a runnable chain. This notion of encapsulating multiple steps into a single function will be key to building interesting apps with LLMs.

You can also return the retrieved documents for further inspection:

#### *Python*

```
@chain
def qa(input):
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(input
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                             "
 # generate answer
 answer = llm.invoke(formatted)
 return {"answer": answer, "docs": docs}
```
#### *JavaScript*

```
const qa = RunnableLambda.from(async input => {
 // fetch relevant documents
 const docs = await retriever.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return {answer, docs}
})
```
Congratulations! You've now built a basic RAG system to power an AI app for personal use.

<span id="page-182-0"></span>However, a production-ready AI app used by multiple users requires a more advanced RAG system. In order to build a robust RAG system, we need to answer the following questions effectively:

- How do we handle the variability in the quality of a user's input?
- How do we route queries to retrieve relevant data from a variety of data sources?
- How do we transform natural language to the query language of the target data source?
- How do we optimize our indexing process, i.e., embedding, text splitting?

Next we'll discuss the latest research-backed strategies to answer these questions and build a production-ready RAG system. These strategies can be summarized in [Figure](#page-183-0) 3-4.

<span id="page-183-0"></span>![](_page_183_Figure_3.jpeg)

Figure 3-4. Effective strategies to optimize the accuracy of your RAG system

#### **NOTE**

<span id="page-184-0"></span>All code blocks in the rest of this chapter use the vector store we set up at the beginning of the chapter.

## Query Transformation

<span id="page-184-1"></span>One of the major problems with a basic RAG system is that it relies too heavily on the quality of a user's query to generate an accurate output. In a production setting, a user is likely to construct their query in an incomplete, ambiguous, or poorly worded manner that leads to model hallucination.

<span id="page-184-3"></span><span id="page-184-2"></span>*Query transformation* is a subset of strategies designed to modify the user's input to answer the first RAG problem question: How do we handle the variability in the quality of a user's input? [Figure](#page-185-0) 3-5 illustrates the range of query transformation strategies, ranging from those that make a user's input more or less abstract in order to generate an accurate LLM output. The next section begins with a middle ground strategy.

<span id="page-185-0"></span>![](_page_185_Figure_0.jpeg)

Figure 3-5. Various methods to transform a user's query based on the abstraction level

### **Rewrite-Retrieve-Read**

<span id="page-185-2"></span><span id="page-185-1"></span>The Rewrite-Retrieve-Read strategy proposed by a Microsoft Research team simply prompts the LLM to rewrite the user's query before performing retrieval. To illustrate, let's return to the chain we built in the previous section, this time invoked with a poorly worded user query: **[2](#page-235-1)**

*Python*

```
@chain
def qa(input):
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(input
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                             "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
qa.invoke("""Today I woke up and brushed my teeth
```

```
 news. But then I forgot the food on the cooke
 the ancient greek history of philosophy?""")
```
#### *JavaScript*

```
const qa = RunnableLambda.from(async input => {
 // fetch relevant documents
 const docs = await retriever.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
```
it i k (`T d I k d b h d t

```
await qa.invoke(`Today I woke up and brushed my t
 the news. But then I forgot the food on the coo
 in the ancient greek history of philosophy?`)
```
*The output* (remember: if you rerun it, your output might be different from this):

```
Based on the given context, there is no informati
```
The model failed to answer the question because it was distracted by the irrelevant information provided in the user's query.

Now let's implement the Rewrite-Retrieve-Read prompt:

<span id="page-187-0"></span>*Python*

```
rewrite_prompt = ChatPromptTemplate.from_template
 query for web search engine to answer the giv
 with '**'. Question: {x} Answer:""")
def parse_rewriter_output(message):
 return message.content.strip('"').strip("**")
```

```
rewriter = rewrite_prompt | llm | parse_rewriter_
@chain
def qa_rrr(input):
 # rewrite the query
 new_query = rewriter.invoke(input)
 # fetch relevant documents 
 docs = retriever.get_relevant_documents(new_q
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                             "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
# run
qa_rrr.invoke("""Today I woke up and brushed my t
 the news. But then I forgot the food on the c
 figures in the ancient greek history of philo
```
<span id="page-188-0"></span>*JavaScript*

const rewritePrompt = ChatPromptTemplate.fromTemp query for web search engine to answer the given with '\*\*'. Question: {question} Answer:`)

const rewriter = rewritePrompt pipe(llm) pipe(mes

```
const rewriter = rewritePrompt.pipe(llm).pipe(mes
 return message.content.replaceAll('"'
                                       ,
                                         '').repl
})
const qa = RunnableLambda.from(async input => {
 const newQuery = await rewriter.invoke({questio
 // fetch relevant documents
 const docs = await retriever.invoke(newQuery)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
await qa.invoke(`Today I woke up and brushed my t
 the news. But then I forgot the food on the coo
 figures in the ancient greek history of philoso
```
*The output:*

Based on the given context, some key figures in t philosophy include: Themistocles (an Athenian sta

Notice that we have had an LLM rewrite the user's initial distracted query into a much clearer one, and it is that more focused query that is passed to the retriever to fetch the most relevant documents. Note: this technique can be used with any retrieval method, be that a vector store such as we have here or, for instance, a web search tool. The downside of this approach is that it introduces additional latency into your chain, because now we need to perform two LLM calls in sequence.

### <span id="page-190-1"></span>**Multi-Query Retrieval**

<span id="page-190-0"></span>A user's single query can be insufficient to capture the full scope of information required to answer the query comprehensively. The multi-query retrieval strategy resolves this problem by instructing an LLM to generate multiple queries based on a user's initial query, executing a parallel retrieval of each query from the data source and then inserting the retrieved results as prompt context to generate a final model output. [Figure](#page-191-0) 3-6 illustrates.

<span id="page-191-0"></span>![](_page_191_Figure_0.jpeg)

Figure 3-6. Demonstration of the multi-query retrieval strategy

This strategy is particularly useful for use cases where a single question may rely on multiple perspectives to provide a comprehensive answer.

Here's a code example of multi-query retrieval in action:

<span id="page-191-1"></span>*Python*

![](_page_191_Picture_5.jpeg)

 similarity search. Provide these alternative newlines. Original question: {question}""")

```
def parse_queries_output(message):
 return message.content.split('\n')
```

```
query_gen = perspectives_prompt | llm | parse_que
```
<span id="page-192-0"></span>*JavaScript*

```
const perspectivesPrompt = ChatPromptTemplate.fro
 language model assistant. Your task is to gener
 of the given user question to retrieve relevant
 database. By generating multiple perspectives o
 goal is to help the user overcome some of the l
 distance-based similarity search. Provide these
 separated by newlines. Original question: {ques
const queryGen = perspectivesPrompt.pipe(llm).pip
 return message.content.split('\n')
})
```
Note that the prompt template is designed to generate variations of questions based on the user's initial query. Next we take the list of generated queries, retrieve the most relevant docs for each of them in parallel, and then combine to get the unique union of all the retrieved relevant documents:

*Python*

```
def get_unique_union(document_lists):
 # Flatten list of lists, and dedupe them
 deduped_docs = {
 doc.page_content: doc
 for sublist in document_lists for doc in
 }
 # return a flat list of unique docs
 return list(deduped_docs.values())
retrieval_chain = query_gen | retriever.batch | g
```
*JavaScript*

```
const retrievalChain = queryGen
 .pipe(retriever.batch.bind(retriever))
 .pipe(documentLists => {
 const dedupedDocs = {}
 documentLists.flat().forEach(doc => {
```

```
 dedupedDocs[doc.pageContent] = doc
 })
 return Object.values(dedupedDocs)
 })
```
Because we're retrieving documents from the same retriever with multiple (related) queries, it's likely at least some of them are repeated. Before using them as context to answer the question, we need to deduplicate them, to end up with a single instance of each. Here we dedupe docs by using their content (a string) as the key in a dictionary (or object in JS), because a dictionary can only contain one entry for each key. After we've iterated through all docs, we simply get all the dictionary values, which is now free of duplicates.

Notice our use as well of .batch , which runs all generated queries in parallel and returns a list of the results—in this case, a list of lists of documents, which we then flatten and dedupe as described earlier.

This final step is to construct a prompt, including the user's question and combined retrieved relevant documents, and a model interface to generate the prediction:

*Python*

```
prompt = ChatPromptTemplate.from_template("""Answ
 on this context:
{context}
Question: {question}
""")
@chain
def multi_query_qa(input):
 # fetch relevant documents 
 docs = retrieval_chain.invoke(input)
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                              "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
# run
multi_query_qa.invoke("""Who are some key figures
 of philosophy?""")
```
*JavaScript*

const prompt = ChatPromptTemplate.fromTemplate(`A

```
 question based on this context:
{context}
Question: {question}
`)
const multiQueryQa = RunnableLambda.from(async in
 // fetch relevant documents
 const docs = await retrievalChain.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
await multiQueryQa.invoke(`Who are some key figur
 history of philosophy?`)
```
<span id="page-196-0"></span>Notice how this isn't that different from our previous QA chains, as all the new logic for multi-query retrieval is contained in retrieval\_chain . This is key to making good use of these techniques—implementing each technique as a standalone chain (in this case, retrieval\_chain ), which makes it easy to adopt them and even to combine them.

### **RAG-Fusion**

<span id="page-197-2"></span><span id="page-197-0"></span>The RAG-Fusion strategy shares similarities with the multiquery retrieval strategy, except we will apply a final reranking step to all the retrieved documents. This reranking step makes use of the *reciprocal rank fusion* (RRF) algorithm, which involves combining the ranks of different search results to produce a single, unified ranking. By combining ranks from different queries, we pull the most relevant documents to the top of the final list. RRF is well-suited for combining results from queries that might have different scales or distributions of scores. **[3](#page-235-2)**

Let's demonstrate RAG-Fusion in code. First, we craft a prompt similar to the multi-query retrieval strategy to generate a list of queries based on the user query:

#### <span id="page-197-1"></span>*Python*

from langchain.prompts import ChatPromptTemplate from langchain\_openai import ChatOpenAI

```
prompt_rag_fusion = ChatPromptTemplate.from_templ
 assistant that generates multiple search quer
 query. \n
```
Generate multiple search queries related to:

```
 Generate multiple search queries related to: 
 Output (4 queries):""")
def parse_queries_output(message):
 return message.content.split('\n')
llm = ChatOpenAI(temperature=0)
query_gen = prompt_rag_fusion | llm | parse_queri
```
#### <span id="page-198-0"></span>*JavaScript*

```
import {ChatPromptTemplate} from '@langchain/core
import {ChatOpenAI} from '@langchain/openai';
import {RunnableLambda} from '@langchain/core/run
const perspectivesPrompt = ChatPromptTemplate.fro
 assistant that generates multiple search querie
 query. \n
 Generate multiple search queries related to: {q
 Output (4 queries):`)
const queryGen = perspectivesPrompt.pipe(llm).pip
```

```
 return message.content.split('\n')
})
```
Once we've generated our queries, we fetch relevant documents for each query and pass them into a function to *rerank* (that is, *reorder* according to relevancy) the final list of relevant documents.

The function reciprocal\_rank\_fusion takes a list of the search results of each query, so a list of lists of documents, where each inner list of documents is sorted by their relevance to that query. The RRF algorithm then calculates a new score for each document based on its ranks (or positions) in the different lists and sorts them to create a final reranked list.

After calculating the fused scores, the function sorts the documents in descending order of these scores to get the final reranked list, which is then returned:

*Python*

def reciprocal\_rank\_fusion(results: list[list], k """reciprocal rank fusion on multiple lists o and an optional parameter k used in the RR """

```
 # Initialize a dictionary to hold fused score
 # Documents will be keyed by their contents t
 fused_scores = {}
 documents = {}
```

```
 # Iterate through each list of ranked documen
 for docs in results:
 # Iterate through each document in the li
 # with its rank (position in the list)
 for rank, doc in enumerate(docs):
 # Use the document contents as the ke
 doc_str = doc.page_content
 # If the document hasn't been seen ye
 # - initialize score to 0
 # - save it for later
 if doc_str not in fused_scores:
 fused_scores[doc_str] = 0
 documents[doc_str] = doc
 # Update the score of the document us
 # 1 / (rank + k)
 fused_scores[doc_str] += 1 / (rank +
 # Sort the documents based on their fused sco
 # to get the final reranked results
 reranked_doc_strs = sorted(
```

```
 fused_scores, key=lambda d: fused_scores[
```
# retrieve the corresponding doc for each doc

```
 )
```

```
 # retrieve the corresponding doc for each doc
 return [
 documents[doc_str]
 for doc_str in reranked_doc_strs
 ]
retrieval_chain = generate_queries | retriever.ba
```
#### *JavaScript*

```
function reciprocalRankFusion(results, k = 60) {
 // Initialize a dictionary to hold fused scores
 // Documents will be keyed by their contents to
 const fusedScores = {}
 const documents = {}
 results.forEach(docs => {
 docs.forEach((doc, rank) => {
 // Use the document contents as the key for
 const key = doc.pageContent
 // If the document hasn't been seen yet,
 // - initialize score to 0
 // - save it for later
 if (!(key in fusedScores)) {
 fusedScores[key] = 0
```
d t [k ] 0

```
 documents[key] = 0
 }
 // Update the score of the document using t
 // 1 / (rank + k)
 fusedScores[key] += 1 / (rank + k)
 })
 })
 // Sort the documents based on their fused scor
 // to get the final reranked results
 const sorted = Object.entries(fusedScores).sort
 // retrieve the corresponding doc for each key
 return sorted.map(([key]) => documents[key])
}
const retrievalChain = queryGen
 .pipe(retriever.batch.bind(retriever))
 .pipe(reciprocalRankFusion)
```
<span id="page-202-0"></span>Notice that the function also takes a k parameter, which determines how much influence documents in each query's result sets have over the final list of documents. A higher value indicates that lower-ranked documents have more influence.

Finally, we combine our new retrieval chain (now using RRF) with the full chain we've seen before:

*Python*

```
prompt = ChatPromptTemplate.from_template("""Answ
 on this context:
{context}
Question: {question}
""")
llm = ChatOpenAI(temperature=0)
@chain
def multi_query_qa(input):
 # fetch relevant documents 
 docs = retrieval_chain.invoke(input)
 # format prompt
 formatted = prompt.invoke({"context": docs,
                                              "
 # generate answer
 answer = llm.invoke(formatted)
 return answer
multi_query_qa.invoke("""Who are some key figures
 of philosophy?""")
```
#### *JavaScript*

```
const rewritePrompt = ChatPromptTemplate.fromTemp
 question based on this context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0})
const multiQueryQa = RunnableLambda.from(async in
 // fetch relevant documents
 const docs = await retrievalChain.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
```
await multiQueryQa.invoke(`Who are some key figur history of philosophy?`)

RAG-Fusion's strength lies in its ability to capture the user's intended expression, navigate complex queries, and broaden the scope of retrieved documents, enabling serendipitous discovery.

### <span id="page-205-2"></span>**Hypothetical Document Embeddings**

<span id="page-205-1"></span><span id="page-205-0"></span>*Hypothetical Document Embeddings* (HyDE) is a strategy that involves creating a hypothetical document based on the user's query, embedding the document, and retrieving relevant documents based on vector similarity. The intuition behind HyDE is that an LLM-generated hypothetical document will be more similar to the most relevant documents than the original query, as shown in [Figure](#page-206-0) 3-7. **[4](#page-236-0)**

<span id="page-206-0"></span>![](_page_206_Figure_0.jpeg)

Figure 3-7. An illustration of HyDE closer in the vector space to the document embeddings than the plain query embeddings

First, define a prompt to generate a hypothetical document:

#### <span id="page-206-1"></span>*Python*

```
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutp
from langchain_openai import ChatOpenAI
prompt_hyde = ChatPromptTemplate.from_template(""
 answer the question.\n Question: {question} \n
```
generate\_doc = (

```
 prompt_hyde | ChatOpenAI(temperature=0) | Str
)
```
#### <span id="page-207-0"></span>*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {ChatPromptTemplate} from '@langchain/core
import {RunnableLambda} from '@langchain/core/run
const prompt = ChatPromptTemplate.fromTemplate(`P
 answer the question
Question: {question}
Passage:`)
const llm = new ChatOpenAI({temperature: 0})
const generateDoc = prompt.pipe(llm).pipe(msg =>
```
Next, we take the hypothetical document and use it as input to the retriever , which will generate its embedding and search for similar documents in the vector store:

*Python*

retrieval\_chain **=** generate\_doc **|** retriever

*JavaScript*

```
const retrievalChain = generateDoc.pipe(retriever
```
Finally, we take the retrieved documents, pass them as context to the final prompt, and instruct the model to generate an output:

*Python*

@chain

```
prompt = ChatPromptTemplate.from_template("""Answ
 on this context:
{context}
Question: {question}
""")
llm = ChatOpenAI(temperature=0)
```

```
@chain
def qa(input):
 # fetch relevant documents from the hyde retrie
 docs = retrieval_chain.invoke(input)
 # format prompt
 formatted = prompt.invoke({"context": docs, "qu
 # generate answer
 answer = llm.invoke(formatted)
 return answer
qa.invoke("""Who are some key figures in the anci
 philosophy?""")
```
*JavaScript*

```
const prompt = ChatPromptTemplate.fromTemplate(`A
 question based on this context:
{context}
Question: {question}
`)
const llm = new ChatOpenAI({temperature: 0})
const qa = RunnableLambda.from(async input => {
  // fetch relevant documents from the hyde retri
```

```
 // fetch relevant documents from the hyde retri
 const docs = await retrievalChain.invoke(input)
 // format prompt
 const formatted = await prompt.invoke({context
 // generate answer
 const answer = await llm.invoke(formatted)
 return answer
})
await qa.invoke(`Who are some key figures in the 
 philosophy?`)
```
To recap what we covered in this section, query transformation consists of taking the user's original query and doing the following:

- Rewriting into one or more queries
- Combining the results of those queries into a single set of the most relevant results

Rewriting the query can take many forms, but it's usually done in a similar fashion: take the user's original query—a prompt you wrote—and ask an LLM to write a new query or queries. Some examples of typical changes made are:

Removing irrelevant/unrelated text from the query.

- Grounding the query with past conversation history. For instance, to make sense of a query such as *and what about in LA,* we need to combine it with a hypothetical past question about the weather in SF, to arrive at a useful query such as *weather in LA*.
- Casting a wider net for relevant documents by also fetching documents for related queries.
- Decomposing a complex question into multiple, simpler questions and then including results for all of them in the final prompt to generate an answer.

The right rewriting strategy to use will depend on your use case.

Now that we've covered the main query transformation strategies, let's discuss the second major question to answer in order to build a robust RAG system: How do we route queries to retrieve relevant data from multiple data sources?

## <span id="page-211-1"></span>Query Routing

<span id="page-211-0"></span>Although using a single vector store is useful, the required data may live in a variety of data sources, including relational databases or other vector stores.

For example, you may have two vector stores: one for LangChain Python documentation and another for LangChain JS documentation. Given a user's question, we would like to *route* the query to the appropriate inferred data source to retrieve relevant docs. *Query routing* is a strategy used to forward a user's query to the relevant data source.

### <span id="page-212-2"></span>**Logical Routing**

<span id="page-212-1"></span>In *logical routing*, we give the LLM knowledge of the various data sources at our disposal and then let the LLM reason which data source to apply based on the user's query, as shown in [Figure](#page-212-0) 3-8.

<span id="page-212-0"></span>![](_page_212_Figure_3.jpeg)

Figure 3-8. Query routing to relevant data sources

<span id="page-213-0"></span>In order to achieve this, we make use of function-calling models like GPT-3.5 Turbo to help classify each query into one of the available routes. A *function call* involves defining a schema that the model can use to generate arguments of a function based on the query. This enables us to generate structured outputs that can be used to run other functions. The following Python code defines the schema for our router based on three docs for different languages:

<span id="page-213-1"></span>*Python*

)

```
from typing import Literal
from langchain_core.prompts import ChatPromptTemp
from langchain_core.pydantic_v1 import BaseModel,
from langchain_openai import ChatOpenAI
# Data model
class RouteQuery(BaseModel):
 """Route a user query to the most relevant da
 datasource: Literal["python_docs"
                                   ,
                                    "js_docs"]
 ...,
 description="""Given a user question, cho
 most relevant for answering their que
```

```
 )
# LLM with function call 
llm = ChatOpenAI(model="gpt-3.5-turbo"
                                    , temperatu
structured_llm = llm.with_structured_output(Route
# Prompt 
system = """You are an expert at routing a user q
 source.
Based on the programming language the question is
 relevant data source."""
prompt = ChatPromptTemplate.from_messages(
 [
 ("system"
                , system),
 ("human"
               ,
                 "{question}"),
 ]
)
# Define router 
router = prompt | structured_llm
```
<span id="page-214-0"></span>*JavaScript*

```
import { ChatOpenAI } from "@langchain/openai";
import { z } from "zod";
```

```
const routeQuery = z.object({
 datasource: z.enum(["python_docs", "js_docs"])
 question, choose which datasource would be mo
 their question`),
}).describe("Route a user query to the most relev
const llm = new ChatOpenAI({model: "gpt-3.5-turbo
const structuredLlm = llm.withStructuredOutput(ro
const prompt = ChatPromptTemplate.fromMessages([
 ['system', `You are an expert at routing a user
 data source.
Based on the programming language the question is
```
Now we invoke the LLM to extract the data source based on the predefined schema:

const router = prompt.pipe(structuredLlm)

the relevant data source.`],

['human', '{question}']

*Python*

])

```
question = """Why doesn't the following code work
from langchain_core.prompts import ChatPromptTemp
prompt = ChatPromptTemplate.from_messages(["human
prompt.invoke("french")
"""
result = router.invoke({"question": question})
result.datasource
# "python_docs"
```
*JavaScript*

```
const question = `Why doesn't the following code 
from langchain_core.prompts import ChatPromptTemp
prompt = ChatPromptTemplate.from_messages(["human
prompt.invoke("french")
`
```
await router.invoke({ question })

*The output:*

```
{
 datasource: "python_docs"
}
```
Notice how the LLM produced JSON output, conforming to the schema we defined earlier. This will be useful in many other tasks.

Once we've extracted the relevant data source, we can pass the value into another function to execute additional logic as required:

*Python*

```
def choose_route(result):
 if "python_docs" in result.datasource.lower()
 ### Logic here 
 return "chain for python_docs"
 else:
```
![](_page_218_Figure_0.jpeg)

#### *JavaScript*

```
function chooseRoute(result) {
 if (result.datasource.toLowerCase().includes('p
 return 'chain for python_docs';
 } else {
 return 'chain for js_docs';
 }
}
const fullChain = router.pipe(chooseRoute)
```
Notice how we don't do an exact string comparison but instead first turn the generated output to lowercase, and then do a substring match. This makes our chain more resilient to the LLM going off script and producing output that doesn't quite conform to the schema we asked for.

Resilience to the random nature of LLM outputs is an important theme to keep in mind when building your LLM applications.

Logical routing is most suitable when you have a defined list of data sources from which relevant data can be retrieved and utilized by the LLM to generate an accurate output. These can range from vector stores to databases and even APIs.

### <span id="page-219-1"></span>**Semantic Routing**

<span id="page-219-3"></span><span id="page-219-2"></span>Unlike logical routing, *semantic routing* involves embedding various prompts that represent various data sources alongside the user's query and then performing vector similarity search to retrieve the most similar prompt. [Figure](#page-219-0) 3-9 illustrates.

<span id="page-219-0"></span>![](_page_219_Figure_4.jpeg)

Figure 3-9. Semantic routing to improve the accuracy of retrieved documents

#### **TIP**

The following is an example of semantic routing:

<span id="page-220-0"></span>*Python*

```
from langchain.utils.math import cosine_similarit
from langchain_core.output_parsers import StrOutp
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import chain
from langchain_openai import ChatOpenAI, OpenAIEm
# Two prompts
physics_template = """You are a very smart physic
 answering questions about physics in a concis
 When you don't know the answer to a question,
Here is a question:
{query}"""
math_template = """You are a very good mathematic
 math questions. You are so good because you a
 problems into their component parts, answer t
 put them together to answer the broader quest
Here is a question:
{query}"""
```
# Embed prompts

```
embeddings = OpenAIEmbeddings()
prompt_templates = [physics_template, math_templa
prompt_embeddings = embeddings.embed_documents(pr
# Route question to prompt
@chain
def prompt_router(query):
 # Embed question
 query_embedding = embeddings.embed_query(quer
 # Compute similarity
 similarity = cosine_similarity([query_embeddi
 # Pick the prompt most similar to the input q
 most_similar = prompt_templates[similarity.ar
 return PromptTemplate.from_template(most_simi
semantic_router = (
 prompt_router
 | ChatOpenAI()
 | StrOutputParser()
)
print(semantic_router.invoke("What's a black hole
```
<span id="page-221-0"></span>*JavaScript*

import {cosineSimilarity} from '@langchain/core/u

```
import {ChatOpenAI, OpenAIEmbeddings} from '@lang
import {PromptTemplate} from '@langchain/core/pro
import {RunnableLambda} from '@langchain/core/run
```
import {cosineSimilarity} from @langchain/core/u

```
const physicsTemplate = `You are a very smart phy
 at answering questions about physics in a conci
 manner. When you don't know the answer to a que
 don't know.
```

```
Here is a question:
{query}`
```

```
const mathTemplate = `You are a very good mathema
 answering math questions. You are so good becau
 hard problems into their component parts, answe
 then put them together to answer the broader qu
```

```
Here is a question:
{query}`
```

```
const embeddings = new OpenAIEmbeddings()
```

```
const promptTemplates = [physicsTemplate, mathTem
const promptEmbeddings = await embeddings.embedDo
```

```
const promptRouter = RunnableLambda.from(query =>
 // Embed question
 const queryEmbedding = await embeddings.embedQu
```

```
 // Compute similarity
 const similarities = cosineSimilarity([queryEmb
 // Pick the prompt most similar to the input qu
 const mostSimilar = similarities[0] > similarit
 ? promptTemplates[0]
 : promptTemplates[1]
 return PromptTemplate.fromTemplate(mostSimilar)
})
const semanticRouter = promptRouter.pipe(new Chat
await semanticRouter.invoke("What's a black hole"
```
Now that you've seen how to route a user's query to the relevant data source, let's discuss the third major question when building a robust RAG system: "How do we transform natural language to the query language of the target data source?"

## <span id="page-223-0"></span>Query Construction

<span id="page-224-1"></span>As discussed earlier, RAG is an effective strategy to embed and retrieve relevant unstructured data from a vector store based on a query. But most data available for use in production apps is structured and typically stored in relational databases. In addition, unstructured data embedded in a vector store also contains structured metadata that possesses important information.

<span id="page-224-2"></span>*Query construction* is the process of transforming a natural language query into the query language of the database or data source you are interacting with. See [Figure](#page-224-0) 3-10.

<span id="page-224-0"></span>![](_page_224_Figure_2.jpeg)

Figure 3-10. Illustration of query languages for various data sources

For example, consider the query: *What are movies about aliens in the year 1980?* This question contains an unstructured topic that can be retrieved via embeddings (*aliens*), but it also contains potential structured components (*year == 1980*).

The following sections dive deeper into the various forms of query construction.

### **Text-to-Metadata Filter**

<span id="page-225-1"></span>Most vector stores provide the ability to limit your vector search based on metadata. During the embedding process, we can attach metadata key-value pairs to vectors in an index and then later specify filter expressions when you query the index.

LangChain provides a SelfQueryRetriever that abstracts this logic and makes it easier to translate natural language queries into structured queries for various data sources. The self-querying utilizes an LLM to extract and execute the relevant metadata filters based on a user's query and predefined metadata schema:

#### <span id="page-225-0"></span>*Python*

```
from langchain.chains.query_constructor.base impo
from langchain.retrievers.self_query.base import
from langchain_openai import ChatOpenAI
fields = [
 AttributeInfo(
 name="genre",
```

```
 description="The genre of the movie",
 type="string or list[string]",
 ),
 AttributeInfo(
 name="year",
 description="The year the movie was relea
 type="integer",
 ),
 AttributeInfo(
 name="director",
 description="The name of the movie direct
 type="string",
 ),
 AttributeInfo(
 name="rating", description="A 1-10 rating
 ),
]
description = "Brief summary of a movie"
llm = ChatOpenAI(temperature=0)
retriever = SelfQueryRetriever.from_llm(
 llm, db, description, fields,
)
print(retriever.invoke(
 "What's a highly rated (above 8.5) science fi
```
g ,

#### <span id="page-227-0"></span>*JavaScript*

```
import { ChatOpenAI } from "@langchain/openai";
import { SelfQueryRetriever } from "langchain/ret
import { FunctionalTranslator } from "@langchain/
/**
 * First, we define the attributes we want to be 
 * in this case, we want to be able to query on t
 * rating, and length of the movie.
 * We also provide a description of each attribut
 * This is used to generate the query prompts.
 */
const fields = [
 {
 name: "genre",
 description: "The genre of the movie",
 type: "string or array of strings",
 },
 {
 name: "year",
 description: "The year the movie was released
 type: "number",
 },
 {
 name: "director",
 description: "The director of the movie",
   type: "string"
```

```
 type: "string",
 },
 {
 name: "rating",
 description: "The rating of the movie (1-10)"
 type: "number",
 },
 {
 name: "length",
 description: "The length of the movie in minu
 type: "number",
 },
];
const description = "Brief summary of a movie";
const llm = new ChatOpenAI();
const attributeInfos = fields.map((field) => new
 field.description, field.type));

const selfQueryRetriever = SelfQueryRetriever.fro
 llm,
 db,
 description,
 attributeInfo: attributeInfos,
 /**
 * We need to use a translator that translates 
 * filter format that the vector store can unde
 * here.
  */
```

```
 structuredQueryTranslator: new FunctionalTransl
});
await selfQueryRetriever.invoke(
 "What's a highly rated (above 8.5) science fict
);
```
/

This results in a retriever that will take a user query, and split it into:

- A filter to apply on the metadata of each document first
- A query to use for semantic search on the documents

To do this, we have to describe which fields the metadata of our documents contain; that description will be included in the prompt. The retriever will then do the following:

- 1. Send the query generation prompt to the LLM.
- 2. Parse metadata filter and rewritten search query from the LLM output.
- 3. Convert the metadata filter generated by the LLM to the format appropriate for our vector store.
- 4. Issue a similarity search against the vector store, filtered to only match documents whose metadata passes the generated

<span id="page-230-3"></span>filter.

### **Text-to-SQL**

<span id="page-230-4"></span>SQL and relational databases are important sources of structured data, but they don't interact directly with natural language. Although we can simply use the LLM to translate a user's query to SQL queries, there is little margin for error.

Here are some useful strategies for effective text to SQL translations:

#### *Database description*

<span id="page-230-1"></span>To ground SQL queries, an LLM must be provided with an accurate description of the database. One common text-to-SQL prompt employs an idea reported in this paper and others: provide the LLM with a CREATE TABLE description for each table, including column names and types. We can also provide a few (for instance, three) example rows from the table. **[5](#page-236-1)**

#### <span id="page-230-0"></span>*Few-shot examples*

<span id="page-230-2"></span>Feeding the prompt with few-shot examples of questionquery matches can improve the query generation accuracy. This can be achieved by simply appending

standard static examples in the prompt to guide the agent on how it should build queries based on questions.

<span id="page-231-0"></span>![](_page_231_Figure_1.jpeg)

See [Figure](#page-231-0) 3-11 for a visual of the process.

Figure 3-11. A user's query transformed to a SQL query

Here's a full code example:

#### <span id="page-231-1"></span>*Python*

from langchain\_community.tools import QuerySQLDat from langchain\_community.utilities import SQLData from langchain.chains import create\_sql\_query\_cha from langchain\_openai import ChatOpenAI

```
# replace this with the connection details of you
db = SQLDatabase.from_uri("sqlite:///Chinook.db")
llm = ChatOpenAI(model="gpt-4", temperature=0)
```

```
# convert question to sql query
write_query = create_sql_query_chain(llm, db)
# Execute SQL query
execute_query = QuerySQLDatabaseTool(db=db)
# combined
chain = write_query | execute_query
# invoke the chain
chain.invoke('How many employees are there?');
```
<span id="page-232-0"></span>*JavaScript*

```
import { ChatOpenAI } from "@langchain/openai";
import { createSqlQueryChain } from "langchain/ch
import { SqlDatabase } from "langchain/sql_db";
import { DataSource } from "typeorm";
import { QuerySqlTool } from "langchain/tools/sql
const datasource = new DataSource({
 type: "sqlite",
 database: "./Chinook.db", // here should be the
});
const db = await SqlDatabase.fromDataSourceParams
```

```
 appDataSource: datasource,
});
const llm = new ChatOpenAI({ model: "gpt-4", temp
// convert question to sql query
const writeQuery = await createSqlQueryChain({ ll
// execute query
const executeQuery = new QuerySqlTool(db);
// combined
const chain = writeQuery.pipe(executeQuery);
// invoke the chain
await chain.invoke('How many employees are there?
```
We first convert the user's query to a SQL query appropriate to the dialect of our database. Then we execute that query on our database. Note that executing arbitrary SQL queries on your database generated by an LLM from user input is dangerous in a production application. To use these ideas in production, you need to consider a number of security measures to reduce the risk of unintended queries being run in your database. Here are some examples:

- Run the queries on your database with a user with read-only permissions.
- The database user running the queries should have access only to the tables you wish to make available for querying.
- Add a time-out to the queries run by this application; this would ensure that even if an expensive query is generated, it is canceled before taking up too many of your database resources.

This is not an exhaustive list of security considerations. Security of LLM applications is an area currently in development, with more security measures being added to the recommendations as new vulnerabilities are discovered.

## <span id="page-234-0"></span>Summary

This chapter discussed various state-of-the-art strategies to efficiently retrieve the most relevant documents based on a user's query and synthesize them with your prompt to aid the LLM to generate an accurate, up-to-date output.

As discussed, a robust, production-ready RAG system requires a wide range of effective strategies that can execute query

transformation, query construction, routing, and indexing optimization.

<span id="page-235-4"></span><span id="page-235-3"></span>Query transformation enables your AI app to transform an ambiguous or malformed user query into a representative query that's optimal for retrieval. Query construction enables your AI app to convert the user's query into the syntax of the query language of the database or data source where structured data lives. Routing enables your AI app to dynamically route the user's query to retrieve relevant information from the relevant data source.

In [Chapter](#page-237-0) 4, we'll build on this knowledge to add memory to your AI chatbot so that it can remember and learn from each interaction. This will enable users to "chat" with the application in multiturn conversations like ChatGPT.

<span id="page-235-0"></span>Patrick Lewis et al., ["Retrieval-Augmented](https://oreil.ly/Qzd2K) Generation for Knowledge-Intensive NLP Tasks", arXiv, April 12, 2021. **[1](#page-164-0)**

<span id="page-235-1"></span>Xinbei Ma et al., "Query Rewriting for [Retrieval-Augmented](https://oreil.ly/zyw5E) Large Language Models", arXiv, October 23, 2023. Research commissioned by Microsoft Research Asia. **[2](#page-185-1)**

<span id="page-235-2"></span>Zackary Rackauckas, "RAG-Fusion: A New Take on [Retrieval-Augmented](https://oreil.ly/k7TTY) Generation", arXiv, February 21, 2024. From the *International Journal on Natural Language Computing*, vol. 13, no. 1 (February 2024). **[3](#page-197-0)**

- <span id="page-236-0"></span>Luyu Gao et al., "Precise Zero-Shot Dense Retrieval Without [Relevance](https://oreil.ly/7aTnS) Labels", arXiv, December 20, 2022. **[4](#page-205-0)**
- <span id="page-236-1"></span>Nitarshan Rajkumar et al., ["Evaluating](https://oreil.ly/WOrzt) the Text-to-SQL Capabilities of Large Language Models", arXiv, March 15, 2022. **[5](#page-230-0)**

# <span id="page-237-0"></span>Chapter 4. Using LangGraph to Add Memory to Your Chatbot

In [Chapter](#page-163-0) 3, you learned how to provide your AI chatbot application with up-to-date and relevant context. This enables your chatbot to generate accurate responses based on the user's input. But that's not enough to build a production-ready application. How can you enable your application to actually "chat" back and forth with the user, while remembering prior conversations and relevant context?

<span id="page-237-2"></span><span id="page-237-1"></span>Large language models are *stateless*, which means that each time the model is prompted to generate a new response it has no memory of the prior prompt or model response. In order to provide this historical information to the model, we need a robust memory system that will keep track of previous conversations and context. This historical information can then be included in the final prompt sent to the LLM, thus giving it "memory." [Figure](#page-238-0) 4-1 illustrates this.

<span id="page-238-0"></span>![](_page_238_Figure_0.jpeg)

Figure 4-1. Memory and retrieval used to generate context-aware answers from an LLM

In this chapter, you'll learn how to build this essential memory system using LangChain's built-in modules to make this development process easier.

## Building a Chatbot Memory System

<span id="page-238-1"></span>There are two core design decisions behind any robust memory system:

- How state is stored
- How state is queried

A simple way to build a chatbot memory system that incorporates effective solutions to these design decisions is to store and reuse the history of all chat interactions between the user and the model. The state of this memory system can be:

- Stored as a list of messages (refer to [Chapter](#page-44-0) 1 to learn more about messages)
- Updated by appending recent messages after each turn
- Appended into the prompt by inserting the messages into the prompt

[Figure](#page-239-0) 4-2 illustrates this simple memory system.

<span id="page-239-0"></span>![](_page_239_Figure_4.jpeg)

Figure 4-2. A simple memory system utilizing chat history in prompts to generate model answers

Here's a code example that illustrates a simple version of this memory system using LangChain:

<span id="page-239-1"></span>*Python*

from langchain\_core.prompts import ChatPromptTemp from langchain\_openai import ChatOpenAI

prompt = ChatPromptTemplate from messages([

```
prompt = ChatPromptTemplate.from_messages([
 ("system", """You are a helpful assistant. An
 of your ability."""),
 ("placeholder",
                 "{messages}"),
])
model = ChatOpenAI()
chain = prompt | model
chain.invoke({
 "messages": [
 ("human","""Translate this sentence from 
 programming."""),
 ("ai", "J'adore programmer."),
 ("human", "What did you just say?"),
 ],
})
```
<span id="page-240-0"></span>*JavaScript*

import {ChatPromptTemplate} from '@langchain/core import {ChatOpenAI} from '@langchain/openai' const prompt = ChatPromptTemplate.fromMessages([

```
 ["system", `You are a helpful assistant. Answer
 of your ability.`],
 ["placeholder", "{messages}"],
])
const model = new ChatOpenAI()
const chain = prompt.pipe(model)
await chain.invoke({
 "messages": [
 ["human",`Translate this sentence from Englis
 programming.`],
 ["ai", "J'adore programmer."],
 ["human", "What did you just say?"],
 ],
})
```
#### *The output:*

I said, "J'adore programmer," which means "I love

Note how the incorporation of the previous conversation in the chain enabled the model to answer the follow-up question in a context-aware manner.

While this is simple and it works, when taking your application to production, you'll face some more challenges related to managing memory at scale, such as:

- You'll need to update the memory after every interaction, atomically (i.e., don't record only the question or only the answer in the case of failure).
- You'll want to store these memories in durable storage, such as a relational database.
- You'll want to control how many and which messages are stored for later, and how many of these are used for new interactions.
- You'll want to inspect and modify this state (for now, just a list of messages) outside a call to an LLM.

<span id="page-242-0"></span>We'll now introduce some better tooling, which will help with this and all later chapters.

# Introducing LangGraph

<span id="page-243-4"></span><span id="page-243-3"></span><span id="page-243-2"></span>For the remainder of this chapter and the following chapters, we'll start to make use of [LangGraph,](https://oreil.ly/TKCb6) an open source library authored by LangChain. LangGraph was designed to enable developers to implement multiactor, multistep, stateful cognitive architectures, called *graphs*. That's a lot of words packed into a short sentence; let's take them one at a time. [Figure](#page-243-0) 4-3 illustrates the multiactor aspect.

<span id="page-243-1"></span><span id="page-243-0"></span>![](_page_243_Figure_1.jpeg)

Figure 4-3. From single-actor applications to multiactor applications

A team of specialists can build something together that none of them could build alone. The same is true of LLM applications: an LLM prompt (great for answer generation and task planning <span id="page-244-0"></span>and many more things) is much more powerful when paired up with a search engine (best at finding current facts), or even when paired with different LLM prompts. We have seen developers build some amazing applications, like [Perplexity](https://oreil.ly/bVlu7) or Arc [Search](https://oreil.ly/NPOlF), when they combine those two building blocks (and others) in novel ways.

And just as a human team needs more coordination than one person working by themselves, an application with multiple actors needs a coordination layer to do these things:

- Define the actors involved (the nodes in a graph) and how they hand off work to each other (the edges in that graph).
- Schedule execution of each actor at the appropriate time—in parallel if needed—with deterministic results.

[Figure](#page-245-0) 4-4 illustrates the multistep dimension.

<span id="page-245-0"></span>![](_page_245_Figure_0.jpeg)

Figure 4-4. From multiactor to multistep applications

As each actor hands off work to another (for example, an LLM prompt asking a search tool for the results of a given search query), we need to make sense of the back-and-forth between multiple actors. We need to know what order it happens in,

how many times each actor is called, and so on. To do this, we can model the interaction between the actors as happening across multiple discrete steps in time. When one actor hands off work to another actor, it results in the scheduling of the next step of the computation, and so on, until no more actors hand off work to others, and the final result is reached.

[Figure](#page-246-0) 4-5 illustrates the stateful aspect.

<span id="page-246-0"></span>![](_page_246_Figure_2.jpeg)

Figure 4-5. From multistep to stateful applications

Communication across steps requires tracking some state otherwise, when you call the LLM actor the second time, you'd get the same result as the first time. It is very helpful to pull this state out of each of the actors and have all actors collaborate on updating a single central state. With a single central state, we can:

- Snapshot and store the central state during or after each computation.
- Pause and resume execution, which makes it easy to recover from errors.
- Implement human-in-the-loop controls (more on this in [Chapter](#page-385-0) 8).

Each *graph* is then made up of the following:

#### *State*

<span id="page-247-1"></span>The data received from outside the application, modified and produced by the application while it's running.

#### *Nodes*

<span id="page-247-0"></span>Each step to be taken. Nodes are simply Python/JS functions, which receive the current state as input and can return an update to that state (that is, they can add to it and modify or remove existing data).

#### *Edges*

<span id="page-248-0"></span>The connections between nodes. Edges determine the path taken from the first node to the last, and they can be fixed (that is, after Node B, always visit node D) or conditional (evaluate a function to decide the next node to visit after node C).

LangGraph offers utilities to visualize these graphs and numerous features to debug their workings while in development. These graphs can then easily be deployed to serve production workloads at high scale.

<span id="page-248-2"></span>If you followed the instructions in [Chapter](#page-44-0) 1, you'll already have LangGraph installed. If not, you can install it by running one of the following commands in your terminal:

#### <span id="page-248-3"></span>*Python*

<span id="page-248-1"></span>pip install langgraph

*JavaScript*

npm i @langchain/langgraph

To help get you familiar with using LangGraph, we'll create a simple chatbot using LangGraph, which is a great example of the LLM call architecture with a single use of an LLM. This chatbot will respond directly to user messages. Though simple, it does illustrate the core concepts of building with LangGraph.

## <span id="page-249-0"></span>Creating a StateGraph

<span id="page-249-1"></span>Start by creating a StateGraph . We'll add a node to represent the LLM call:

#### <span id="page-249-2"></span>*Python*

from typing import Annotated, TypedDict

from langgraph.graph import StateGraph, START, EN from langgraph.graph.message import add\_messages

#### class State(TypedDict):

# Messages have the type "list". The `add\_mes

- # function in the annotation defines how this
- # be updated (in this case, it appends new me
- # list, rather than replacing the previous me messages: Annotated[list, add\_messages]

```
builder = StateGraph(State)
```

```
JavaScript
```

```
import {
 StateGraph,
 StateType,
 Annotation,
 messagesStateReducer,
 START, END
} from '@langchain/langgraph'
const State = {
 /**
 * The State defines three things:
 * 1. The structure of the graph's state (which 
 * read/write)
 * 2. The default values for the state's channel
 * 3. The reducers for the state's channels. Red
 * determine how to apply updates to the state. 
 * appended to the messages array.
 */
 messages: Annotation({
 reducer: messagesStateReducer,
 default: () => []
 })
```
# }), } const builder = new StateGraph(State)

#### **NOTE**

<span id="page-251-1"></span>The first thing you do when you define a graph is define the state of the graph. The *state* consists of the shape, or schema, of the graph state, as well as reducer functions that specify how to apply updates to the state. In this example, the state is a dictionary with a single key: messages . The messages key is annotated with the add\_messages reducer function, which tells LangGraph to append new messages to the existing list, rather than overwrite it. State keys without an annotation will be overwritten by each update, storing the most recent value. You can write your own reducer functions, which are simply functions that receive as arguments—argument 1 is the current state, and argument 2 is the next value being written to the state and should return the next state, that is, the result of merging the current state with the new value. The simplest example is a function that appends the next value to a list and returns that list.

So now our graph knows two things:

- Every node we define will receive the current State as input and return a value that updates that state.
- <span id="page-251-0"></span>messages will be *appended* to the current list, rather than directly overwritten. This is communicated via the prebuilt [add\\_messages](https://oreil.ly/sK-Ry) function in the Annotated syntax in the

Python example or the reducer function for the JavaScript example.

Next, add the chatbot node. Nodes represent units of work. They are typically just functions:

<span id="page-252-1"></span>*Python*

```
from langchain_openai import ChatOpenAI
model = ChatOpenAI()
def chatbot(state: State):
 answer = model.invoke(state["messages"])
 return {"messages": [answer]}
# The first argument is the unique node name
# The second argument is the function or Runnable
builder.add_node("chatbot", chatbot)
```
<span id="page-252-0"></span>*JavaScript*

```
import {ChatOpenAI} from '@langchain/openai'
import {
 AIMessage,
```

```
 SystemMessage,
 HumanMessage
} from "@langchain/core/messages";
const model = new ChatOpenAI()
async function chatbot(state) {
 const answer = await model.invoke(state.message
 return {"messages": answer}
}
builder = builder.addNode('chatbot', chatbot)
```
This node receives the current state, does one LLM call, and then returns an update to the state containing the new message produced by the LLM. The add\_messages reducer appends this message to the messages already in the state.

And finally let's add the edges:

g

<span id="page-253-0"></span>*Python*

```
builder.add_edge(START, 'chatbot')
builder.add_edge('chatbot', END)
```

```
graph = builder.compile()
```
*JavaScript*

```
builder = builder
 .addEdge(START, 'chatbot')
 .addEdge('chatbot', END)
let graph = builder.compile()
```
This does a few things:

- It tells the graph where to start its work each time you run it.
- This instructs the graph where it should exit (this is optional, as LangGraph will stop execution once there's no more nodes to run).
- It compiles the graph into a runnable object, with the familiar invoke and stream methods.

We can also draw a visual representation of the graph:

<span id="page-254-1"></span>*Python*

<span id="page-255-1"></span>graph.get\_graph().draw\_mermaid\_png()

*JavaScript*

await graph.getGraph().drawMermaidPng()

<span id="page-255-0"></span>The graph we just made looks like [Figure](#page-255-0) 4-6.

![](_page_255_Figure_4.jpeg)

Figure 4-6. A simple chatbot

You can run it with the familiar stream() method you've seen in earlier chapters:

*Python*

```
input = {"messages": [HumanMessage('hi!)]}
for chunk in graph.stream(input):
 print(chunk)
```
*JavaScript*

```
const input = {messages: [new HumanMessage('hi!)]
for await (const chunk of await graph.stream(inpu
 console.log(chunk)
}
```
*The output:*

```
{ "chatbot": { "messages": [AIMessage("How can I
```
Notice how the input to the graph was in the same shape as the State object we defined earlier; that is, we sent in a list of

<span id="page-257-3"></span>messages in the messages key of a dictionary. In addition, the stream function streams the full value of the state after each step of the graph.

## <span id="page-257-0"></span>Adding Memory to StateGraph

<span id="page-257-4"></span><span id="page-257-2"></span><span id="page-257-1"></span>LangGraph has built-in persistence, which is used in the same way for the simplest graph to the most complex. Let's see what it looks like to apply it to this first architecture. We'll recompile our graph, now attaching a *checkpointer*, which is a storage adapter for LangGraph. LangGraph ships with a base class that any user can subclass to create an adapter for their favorite database; at the time of writing, LangGraph ships with several adapters maintained by LangChain:

- An in-memory adapter, which we'll use for our examples here
- A SQLite adapter, using the popular in-process database, appropriate for local apps and testing
- A Postgres adapter, optimized for the popular relational database and appropriate for large-scale applications.

Many developers have written adapters for other database systems, such as Redis or MySQL:

```
from langgraph.checkpoint.memory import MemorySav
graph = builder.compile(checkpointer=MemorySaver(
```
<span id="page-258-0"></span>*JavaScript*

```
import {MemorySaver} from '@langchain/langgraph'
const graph = builder.compile({ checkpointer: new
```
This returns a runnable object with the same methods as the one used in the previous code block. But now, it stores the state at the end of each step, so every invocation after the first doesn't start from a blank slate. Any time the graph is called, it starts by using the checkpointer to fetch the most recent saved state, if any, and combines the new input with the previous state. And only then does it execute the first nodes.

Let's see the difference in action:

#### *Python*

```
thread1 = {"configurable": {"thread_id": "1"}}
result_1 = graph.invoke(
 { "messages": [HumanMessage("hi, my name is J
 thread1
)
// { "chatbot": { "messages": [AIMessage("How can
result_2 = graph.invoke(
 { "messages": [HumanMessage("what is my name?
 thread1
)
// { "chatbot": { "messages": [AIMessage("Your na
```
*JavaScript*

```
const thread1 = {configurable: {thread_id: '1'}}
const result_1 = await graph.invoke(
 { "messages": [new HumanMessage("hi, my name is
 thread1
)
// { "chatbot": { "messages": [AIMessage("How can
```
const result 2 = await graph invoke(

```
const result_2 = await graph.invoke(
 { "messages": [new HumanMessage("what is my nam
 thread1
)
// { "chatbot": { "messages": [AIMessage("Your na
```
<span id="page-260-1"></span><span id="page-260-0"></span>Notice the object thread1 , which identifies the current interaction as belonging to a particular history of interactions which are called *threads* in LangGraph. Threads are created automatically when first used. Any string is a valid identifier for a thread (usually, Universally Unique Identifiers [UUIDs] are used). The existence of threads helps you achieve an important milestone in your LLM application; it can now be used by multiple users with independent conversations that are never mixed up.

As before, the chatbot node is first called with a single message (the one we just passed in) and returns another message, both of which are then saved in the state.

The second time we execute the graph on the same thread, the chatbot node is called with three messages, the two saved from the first execution, and the next question from the user. This is the essence of memory: the previous state is still there, which makes it possible, for instance, to answer questions

about something said before (and do many more interesting things, of which we will see more later).

You can also inspect and update the state directly; let's see how:

<span id="page-261-1"></span>*Python*

<span id="page-261-0"></span>graph.get\_state(thread1)

*JavaScript*

await graph.getState(thread1)

This returns the current state of this thread.

And you can update the state like this:

*Python*

graph.update\_state(thread1, [HumanMessage('I like

*JavaScript*

await graph.updateState(thread1, [new HumanMessag

<span id="page-262-0"></span>This would add one more message to the list of messages in the state, to be used the next time you invoke the graph on this thread.

## Modifying Chat History

<span id="page-262-1"></span>In many cases, the chat history messages aren't in the best state or format to generate an accurate response from the model. To overcome this problem, we can modify the chat history in three main ways: trimming, filtering, and merging messages.

### **Trimming Messages**

<span id="page-262-3"></span><span id="page-262-2"></span>LLMs have limited *context windows*; in other words, there is a maximum number of tokens that LLMs can receive as a prompt. As such, the final prompt sent to the model shouldn't exceed that limit (particular to each mode), as models will either refuse an overly long prompt or truncate it. In addition, excessive prompt information can distract the model and lead to hallucination.

An effective solution to this problem is to limit the number of messages that are retrieved from chat history and appended to the prompt. In practice, we need only to load and store the most recent messages. Let's use an example chat history with some preloaded messages.

Fortunately, LangChain provides the built-in trim\_messages helper that incorporates various strategies to meet these requirements. For example, the trimmer helper enables specifying how many tokens we want to keep or remove from chat history.

Here's an example that retrieves the last max\_tokens in the list of messages by setting a strategy parameter to "last" :

<span id="page-263-0"></span>*Python*

```
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
trimmer = trim_messages(
 max_tokens=65,
 strategy="last",
 token_counter=ChatOpenAI(model="gpt-4o"),
 include_system=True,
```
![](_page_264_Figure_0.jpeg)

#### <span id="page-264-0"></span>*JavaScript*

import { AIMessage, HumanMessage,

```
 SystemMessage,
 trimMessages,
} from "@langchain/core/messages";
import { ChatOpenAI } from "@langchain/openai";
const trimmer = trimMessages({
 maxTokens: 65,
 strategy: "last",
 tokenCounter: new ChatOpenAI({ modelName: "gpt-
 includeSystem: true,
 allowPartial: false,
 startOn: "human",
});
const messages = [
 new SystemMessage("you're a good assistant"),
 new HumanMessage("hi! I'm bob"),
 new AIMessage("hi!"),
 new HumanMessage("I like vanilla ice cream"),
 new AIMessage("nice"),
 new HumanMessage("what's 2 + 2"),
 new AIMessage("4"),
 new HumanMessage("thanks"),
 new AIMessage("no problem!"),
 new HumanMessage("having fun?"),
 new AIMessage("yes!"),
```
]

```
const trimmed = await trimmer.invoke(messages);
```
#### *The output:*

```
[SystemMessage(content="you're a good assistant")
 HumanMessage(content='what's 2 + 2'),
 AIMessage(content='4'),
 HumanMessage(content='thanks'),
 AIMessage(content='no problem!'),
 HumanMessage(content='having fun?'),
 AIMessage(content='yes!')]
```
#### Note the following:

- The parameter strategy controls whether to start from the beginning or the end of the list. Usually, you'll want to prioritize the most recent messages and cut older messages if they don't fit. That is, start from the end of the list. For this behavior, choose the value last . The other available option is first , which would prioritize the oldest messages and cut more recent messages if they don't fit.
- The token\_counter is an LLM or chat model, which will be used to count tokens using the tokenizer appropriate to that

model.

- We can add the parameter include\_system=True to ensure that the trimmer keeps the system message.
- The parameter allow\_partial determines whether to cut the last message's content to fit within the limit. In our example, we set this to false , which completely removes the message that would send the total over the limit.
- The parameter start\_on="human" ensures that we never remove an AIMessage (that is, a response from the model) without also removing a corresponding HumanMessage (the question for that response).

### <span id="page-267-1"></span>**Filtering Messages**

<span id="page-267-0"></span>As the list of chat history messages grows, a wider variety of types, subchains, and models may be utilized. LangChain's filter\_messages helper makes it easier to filter the chat history messages by type, ID, or name.

Here's an example where we filter for human messages:

<span id="page-267-2"></span>*Python*

from langchain\_core.messages import ( AIMessage,

```
 HumanMessage,
 SystemMessage,
 filter_messages,
)
messages = [
 SystemMessage("you are a good assistant", id=
 HumanMessage("example input", id="2", name="e
 AIMessage("example output", id="3", name="exa
 HumanMessage("real input", id="4", name="bob"
 AIMessage("real output", id="5", name="alice"
]
filter_messages(messages, include_types="human")
```
g

<span id="page-268-0"></span>*JavaScript*

```
import {
 HumanMessage,
 SystemMessage,
 AIMessage,
 filterMessages,
} from "@langchain/core/messages";
const messages = [
 new SystemMessage({content: "you are a good ass
```

```
 new HumanMessage({content: "example input", id
 new AIMessage({content: "example output", id: "
 new HumanMessage({content: "real input", id: "4
 new AIMessage({content: "real output", id: "5",
];
filterMessages(messages, { includeTypes: ["human"
```
*The output:*

```
[HumanMessage(content='example input', name='exam
 HumanMessage(content='real input', name='bob', i
```
Let's try another example where we filter to exclude users and IDs, and include message types:

*Python*

```
filter_messages(messages, exclude_names=["example
"""
[SystemMessage(content='you are a good assistant
HumanMessage(content='real input', name='bob', id
```

```
AIMessage(content='real output', name='alice', id
"""
filter_messages(
 messages,
 include_types=[HumanMessage, AIMessage],
 exclude_ids=["3"]
)
"""
[HumanMessage(content='example input', name='exam
 HumanMessage(content='real input', name='bob', i
 AIMessage(content='real output', name='alice', i
"""
```
*JavaScript*

```
filterMessages(
 messages,
 { excludeNames: ["example_user",
 "example_assistant"] }
);
```
/\*

```
[SystemMessage(content='you are a good assistant
HumanMessage(content='real input', name='bob', id
```

```
AIMessage(content='real output', name='alice', id
*/
filterMessages(messages, { includeTypes: ["human"
/*
[HumanMessage(content='example input', name='exam
 HumanMessage(content='real input', name='bob', i
 AIMessage(content='real output', name='alice', i
*/
```
The filter\_messages helper can also be used imperatively or declaratively, making it easy to compose with other components in a chain:

*Python*

```
model = ChatOpenAI()
filter_ = filter_messages(exclude_names=["example
chain = filter_ | model
```
#### *JavaScript*

```
const model = new ChatOpenAI()
const filter = filterMessages({
 excludeNames: ["example_user", "example_assista
})
const chain = filter.pipe(model)
```
### **Merging Consecutive Messages**

<span id="page-272-0"></span>Certain models don't support inputs, including consecutive messages of the same type (for instance, Anthropic chat models). LangChain's merge\_message\_runs utility makes it easy to merge consecutive messages of the same type:

<span id="page-272-1"></span>*Python*

from langchain\_core.messages import ( AIMessage, HumanMessage, SystemMessage, merge\_message\_runs,

```
messages = [
 SystemMessage("you're a good assistant."),
 SystemMessage("you always respond with a joke
 HumanMessage(
 [{"type": "text", "text": "i wonder why i
 ),
 HumanMessage("and who is harrison chasing any
 AIMessage(
 '''Well, I guess they thought "WordRope" 
 didn\'t have the same ring to it!'''
 ),
 AIMessage("""Why, he's probably chasing after
 office!"""),
]
merge_message_runs(messages)
```
<span id="page-273-0"></span>*JavaScript*

)

import { HumanMessage, SystemMessage, AIMessage, mergeMessageRuns,

} from "@langchain/core/messages";

```
const messages = [
 new SystemMessage("you're a good assistant."),
 new SystemMessage("you always respond with a jo
 new HumanMessage({
 content: [{ type: "text", text: "i wonder why
 }),
 new HumanMessage("and who is harrison chasing a
 new AIMessage(
 `Well, I guess they thought "WordRope" and "S
 have the same ring to it!`
 ),
 new AIMessage(
 "Why, he's probably chasing after the last cu
 ),
];
mergeMessageRuns(messages);
```
} o @ a gc a /co e/ essages ;

#### *The output:*

[SystemMessage(content="you're a good assistant.\ joke."), HumanMessage(content=[{'type': 'text', 'text': " langchain"}, 'and who is harrison chasing any AIMessage(content='Well, I guess they thought "W

j did \' h h i i \ h

 just didn\'t have the same ring to it!\nWhy, the last cup of coffee in the office!')]

Notice that if the contents of one of the messages to merge is a list of content blocks, then the merged message will have a list of content blocks. And if both messages to merge have string contents, then those are concatenated with a newline character.

The merge\_message\_runs helper can be used imperatively or declaratively, making it easy to compose with other components in a chain:

*Python*

```
model = ChatOpenAI()
merger = merge_message_runs()
chain = merger | model
```
*JavaScript*

```
const model = new ChatOpenAI()
const merger = mergeMessageRuns()
const chain = merger.pipe(model)
```
## Summary

<span id="page-276-0"></span>This chapter covered the fundamentals of building a simple memory system that enables your AI chatbot to remember its conversations with a user. We discussed how to automate the storage and updating of chat history using LangGraph to make this easier. We also discussed the importance of modifying chat history and explored various strategies to trim, filter, and summarize chat messages.

In [Chapter](#page-277-0) 5, you'll learn how to enable your AI chatbot to do more than just chat back: for instance, your new model will be able to make decisions, pick actions, and reflect on its past outputs.

# <span id="page-277-0"></span>Chapter 5. Cognitive Architectures with LangGraph

<span id="page-277-2"></span>So far, we've looked at the most common features of LLM applications:

- Prompting techniques in the [Preface](#page-8-0) and [Chapter](#page-44-0) 1
- RAG in Chapters [2](#page-93-0) and [3](#page-163-0)
- Memory in [Chapter](#page-237-0) 4

<span id="page-277-1"></span>The next question should be: How do we assemble these pieces into a coherent application that achieves the goal we set out to solve? To draw a parallel with the world of bricks and mortar, a swimming pool and a one-story house are built of the same materials, but obviously serve very different purposes. What makes them uniquely suited to their different purposes is the plan for how those materials are combined—that is, their architecture. The same is true when building LLM applications. The most important decisions you have to make are how to assemble the different components you have at your disposal (such as RAG, prompting techniques, memory) into something that achieves your purpose.

Before we look at specific architectures, let's walk through an example. Any LLM application you might build will start from a purpose: what the app is designed to do. Let's say you want to build an email assistant—an LLM application that reads your emails before you do and aims to reduce the amount of emails you need to look at. The application might do this by archiving a few uninteresting ones, directly replying to some, and marking others as deserving of your attention later.

You probably also would want the app to be bound by some constraints in its action. Listing those constraints helps tremendously, as they will help inform the search for the right architecture. [Chapter](#page-385-0) 8 covers these constraints in more detail and how to work with them. For this hypothetical email assistant, let's say we'd like it to do the following:

- Minimize the number of times it interrupts you (after all, the whole point is to save time).
- Avoid having your email correspondents receive a reply that you'd never have sent yourself.

<span id="page-278-2"></span><span id="page-278-1"></span><span id="page-278-0"></span>This hints at the key trade-off often faced when building LLM apps: the trade-off between *agency* (or the capacity to act autonomously) and *reliability* (or the degree to which you can trust its outputs). Intuitively, the email assistant will be more

useful if it takes more actions without your involvement, but if you take it too far, it will inevitably send emails you wish it hadn't.

<span id="page-279-0"></span>One way to describe the degree of autonomy of an LLM application is to evaluate how much of the behavior of the application is determined by an LLM (versus code):

- Have an LLM decide the output of a step (for instance, write a draft reply to an email).
- Have an LLM decide the next step to take (for instance, for a new email, decide between the three actions it can take on an email: archive, reply, or mark for review).
- Have an LLM decide what steps are available to take (for instance, have the LLM write code that executes a dynamic action you didn't preprogram into the application).

<span id="page-279-1"></span>We can classify a number of popular *recipes* for building LLM applications based on where they fall in this spectrum of autonomy, that is, which of the three tasks just mentioned are handled by an LLM and which remain in the hands of the developer or user. These recipes can be called *cognitive architectures*. In the artificial intelligence field, the term *cognitive architecture* has long been used to denote models of human reasoning (and their implementations in computers).

<span id="page-280-1"></span>An LLM cognitive architecture (the term was first applied to LLMs, to our knowledge, in a paper ) can be defined as a recipe for the steps to be taken by an LLM application (see [Figure](#page-280-0) 5-1). A *step* is, for instance, retrieval of relevant documents (RAG), or calling an LLM with a chain-of-thought prompt. **[1](#page-314-0)**

<span id="page-280-0"></span>![](_page_280_Figure_1.jpeg)

<span id="page-280-2"></span>Figure 5-1. Cognitive architectures for LLM applications

Now let's look at each of the major architectures, or recipes, that you can use when building your application (as shown in [Figure](#page-280-0) 5-1):

#### *0: Code*

This is not an LLM cognitive architecture (hence we numbered it **0**), as it doesn't use LLMs at all. You can think of this as regular software you're used to writing. The first interesting architecture (for this book, at any rate) is actually the next one.

#### *1: LLM call*

This is the majority of the examples we've seen in the book so far, with one LLM call only. This is useful mostly when it's part of a larger application that makes use of an LLM for achieving a specific task, such as translating or summarizing a piece of text.

#### *2: Chain*

The next level up, so to speak, comes with the use of multiple LLM calls in a predefined sequence. For instance, a text-to-SQL application (which receives as input from the user a natural language description of some calculation to make over a database) could make use of two LLM calls in sequence:

One LLM call to generate a SQL query, from the natural language query, provided by the user, and a description of the database contents, provided by the developer.

And another LLM call to write an explanation of the query appropriate for a nontechnical user, given the

query generated in the previous call. This one could then be used to enable the user to check if the generated query matches his request.

#### *3: Router*

This next step comes from using the LLM to define the sequence of steps to take. That is, whereas the chain architecture always executes a static sequence of steps (however many) determined by the developer, the router architecture is characterized by using an LLM to choose between certain predefined steps. An example would be a RAG application with multiple indexes of documents from different domains, with the following steps:

- 1. An LLM call to pick which of the available indexes to use, given the user-supplied query and the developersupplied description of the indexes.
- 2. A retrieval step that queries the chosen index for the most relevant documents for the user query.
- 3. Another LLM call to generate an answer, given the user-supplied query and the list of relevant documents fetched from the index.

That's as far as we'll go in this chapter. We will talk about each of these architectures in turn. The next chapters discuss the agentic architectures, which make even more use of LLMs. But first let's talk about some better tooling to help us on this journey.

## <span id="page-283-1"></span>Architecture #1: LLM Call

<span id="page-283-0"></span>As an example of the LLM call architecture, we'll return to the chatbot we created in [Chapter](#page-237-0) 4. This chatbot will respond directly to user messages.

Start by creating a StateGraph , to which we'll add a node to represent the LLM call:

<span id="page-283-2"></span>*Python*

```
from typing import Annotated, TypedDict
```
from langgraph.graph import StateGraph, START, EN from langgraph.graph.message import add\_messages from langchain\_openai import ChatOpenAI

```
model = ChatOpenAI()
```

```
class State(TypedDict):
 # Messages have the type "list". The `add_mes
 # function in the annotation defines how this
 # be updated (in this case, it appends new me
 # list, rather than replacing the previous me
 messages: Annotated[list, add_messages]
def chatbot(state: State):
 answer = model.invoke(state["messages"])
 return {"messages": [answer]}
builder = StateGraph(State)
builder.add_node("chatbot", chatbot)
builder.add_edge(START, 'chatbot')
builder.add_edge('chatbot', END)
```

```
graph = builder.compile()
```
<span id="page-284-0"></span>*JavaScript*

import { StateGraph, Annotation, messagesStateReducer, START, END

```
} from '@langchain/langgraph'
import {ChatOpenAI} from '@langchain/openai'
const model = new ChatOpenAI()
const State = {
 /**
 * The State defines three things:
 * 1. The structure of the graph's state (which 
 * read/write)
 * 2. The default values for the state's channel
 * 3. The reducers for the state's channels. Red
 * determine how to apply updates to the state. 
 * appended to the messages array.
 */
 messages: Annotation({
 reducer: messagesStateReducer,
 default: () => []
 }),
}
async function chatbot(state) {
 const answer = await model.invoke(state.message
 return {"messages": answer}
}
const builder = new StateGraph(State)
 .addNode('chatbot', chatbot)
 .addEdge(START, 'chatbot')
```

```
 .addEdge(START, chatbot )
 .addEdge('chatbot', END)
```

```
const graph = builder.compile()
```
We can also draw a visual representation of the graph:

*Python*

graph.get\_graph().draw\_mermaid\_png()

*JavaScript*

await graph.getGraph().drawMermaidPng()

The graph we just made looks like [Figure](#page-287-0) 5-2.

<span id="page-287-0"></span>![](_page_287_Figure_0.jpeg)

Figure 5-2. The LLM call architecture

You can run it with the familiar stream() method you've seen in earlier chapters:

#### *Python*

```
input = {"messages": [HumanMessage('hi!)]}
for chunk in graph.stream(input):
 print(chunk)
```
#### *JavaScript*

```
const input = {messages: [new HumanMessage('hi!)]
for await (const chunk of await graph.stream(inpu
 console.log(chunk)
}
```
*The output:*

```
{ "chatbot": { "messages": [AIMessage("How can I
```
Notice how the input to the graph was in the same shape as the State object we defined earlier; that is, we sent in a list of messages in the messages key of a dictionary.

This is the simplest possible architecture for using an LLM, which is not to say that it should never be used. Here are some examples of where you might see it in action in popular products, among many others:

AI-powered features such as summarize and translate (such as you can find in Notion, a popular writing software) can be powered by a single LLM call.

<span id="page-289-2"></span>Simple SQL query generation can be powered by a single LLM call, depending on the UX and target user the developer has in mind.

### Architecture #2: Chain

<span id="page-289-1"></span>This next architecture extends on all that by using multiple LLM calls, in a predefined sequence (that is, different invocations of the application do the same sequence of LLM calls, albeit with different inputs and results).

Let's take as an example a text-to-SQL application, which receives as input from the user a natural language description of some calculation to make over a database. We mentioned earlier that this could be achieved with a single LLM call, to generate a SQL query, but we can create a more sophisticated application by making use of multiple LLM calls in sequence. Some authors call this architecture *flow engineering*. **[2](#page-314-1)**

<span id="page-289-3"></span><span id="page-289-0"></span>First let's describe the flow in words:

1. One LLM call to generate a SQL query from the natural language query, provided by the user, and a description of the database contents, provided by the developer.

2. Another LLM call to write an explanation of the query appropriate for a nontechnical user, given the query generated in the previous call. This one could then be used to enable the user to check if the generated query matches his request.

You could also extend this even further (but we won't do that here) with additional steps to be taken after the preceding two:

- 3. Executes the query against the database, which returns a two-dimensional table.
- 4. Uses a third LLM call to summarize the query results into a textual answer to the original user question.

And now let's implement this with LangGraph:

<span id="page-290-0"></span>*Python*

```
from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage,
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGrap
from langgraph.graph.message import add_messages
```

```
# useful to generate SQL query
model_low_temp = ChatOpenAI(temperature=0.1)
# useful to generate natural language outputs
model_high_temp = ChatOpenAI(temperature=0.7)
class State(TypedDict):
 # to track conversation history
 messages: Annotated[list, add_messages]
 # input
 user_query: str
 # output
 sql_query: str
 sql_explanation: str
class Input(TypedDict):
 user_query: str
class Output(TypedDict):
 sql_query: str
 sql_explanation: str
generate_prompt = SystemMessage(
```

```
 """You are a helpful data analyst who generat
 on their questions."""
```
)

```
def generate_sql(state: State) -> State:
 user_message = HumanMessage(state["user_query
   messages = [generate prompt *state["messages
```

```
 messages = [generate_prompt, state[ messages
 res = model_low_temp.invoke(messages)
 return {
 "sql_query": res.content,
 # update conversation history
 "messages": [user_message, res],
 }
explain_prompt = SystemMessage(
 "You are a helpful data analyst who explains 
)
def explain_sql(state: State) -> State:
 messages = [
 explain_prompt,
 # contains user's query and SQL query fro
 *state["messages"],
 ]
 res = model_high_temp.invoke(messages)
 return {
 "sql_explanation": res.content,
 # update conversation history
 "messages": res,
 }
builder = StateGraph(State, input=Input, output=O
builder.add_node("generate_sql", generate_sql)
builder.add_node("explain_sql", explain_sql)
```
builder add edge(START "generate sql")

```
builder.add_edge(START, generate_sql )
builder.add_edge("generate_sql", "explain_sql")
builder.add_edge("explain_sql", END)
```

```
graph = builder.compile()
```

```
JavaScript
```

```
import {
 HumanMessage,
 SystemMessage
} from "@langchain/core/messages";
import { ChatOpenAI } from "@langchain/openai";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
 END,
} from "@langchain/langgraph";
// useful to generate SQL query
const modelLowTemp = new ChatOpenAI({ temperature
// useful to generate natural language outputs
const modelHighTemp = new ChatOpenAI({ temperatur
const annotation = Annotation.Root({
```

```
const annotation Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
 user_query: Annotation(),
 sql_query: Annotation(),
 sql_explanation: Annotation(),
});
const generatePrompt = new SystemMessage(
 `You are a helpful data analyst who generates S
 their questions.`
);
async function generateSql(state) {
 const userMessage = new HumanMessage(state.user
 const messages = [generatePrompt, ...state.mess
 const res = await modelLowTemp.invoke(messages)
 return {
 sql_query: res.content as string,
 // update conversation history
 messages: [userMessage, res],
 };
}
const explainPrompt = new SystemMessage(
 "You are a helpful data analyst who explains SQ
);
async function explainSql(state) {
 const messages = [explainPrompt, ...state.messa
```

```
 const messages [explainPrompt, ...state.messa
 const res = await modelHighTemp.invoke(messages
 return {
 sql_explanation: res.content as string,
 // update conversation history
 messages: res,
 };
}
const builder = new StateGraph(annotation)
 .addNode("generate_sql", generateSql)
 .addNode("explain_sql", explainSql)
 .addEdge(START, "generate_sql")
 .addEdge("generate_sql", "explain_sql")
 .addEdge("explain_sql", END);
const graph = builder.compile();
```
The visual representation of the graph is shown in [Figure](#page-296-0) 5-3.

<span id="page-296-0"></span>![](_page_296_Figure_0.jpeg)

![](_page_296_Figure_1.jpeg)

Here's an example of inputs and outputs:

*Python*

graph.invoke({

```
 "user_query": "What is the total sales for each
})
```
*JavaScript*

```
await graph.invoke({
 user_query: "What is the total sales for each p
})
```
*The output:*

```
{
 "sql_query": "SELECT product_name, SUM(sales_am
 sales\nGROUP BY product_name;",
 "sql_explanation": "This query will retrieve th
 by summing up the sales_amount column for e
 results by product_name.",
}
```
First, the generate\_sql node is executed, which populates the sql\_query key in the state (which will be part of the final output) and updates the messages key with the new messages.

Then the explain\_sql node runs, taking the SQL query generated in the previous step and populating the sql\_explanation key in the state. At this point, the graph finishes running, and the output is returned to the caller.

Note also the use of separate input and output schemas when creating the StateGraph . This lets you customize which parts of the state are accepted as input from the user and which are returned as the final output. The remaining state keys are used by the graph nodes internally to keep intermediate state and are made available to the user as part of the streaming output produced by stream() .

### <span id="page-298-1"></span>Architecture #3: Router

<span id="page-298-0"></span>This next architecture moves up the autonomy ladder by assigning to LLMs the next of the responsibilities we outlined before: deciding the next step to take. That is, whereas the chain architecture always executes a static sequence of steps (however many), the router architecture is characterized by using an LLM to choose between certain predefined steps.

Let's use the example of a RAG application with access to multiple indexes of documents from different domains (refer to [Chapter](#page-93-0) 2 for more on indexing). Usually you can extract better performance from LLMs by avoiding the inclusion of irrelevant information in the prompt. Therefore, in building this application, we should try to pick the right index to use for each query and use only that one. The key development in this architecture is to use an LLM to make this decision, effectively using an LLM to evaluate each incoming query and decide which index it should use for that *particular* query.

#### **NOTE**

Before the advent of LLMs, the usual way of solving this problem would be to build a classifier model using ML techniques and a dataset mapping example user queries to the right index. This could prove quite challenging, as it requires the following:

- Assembling that dataset by hand
- Generating enough *features* (quantitative attributes) from each user query to enable training a classifier for the task

LLMs, given their encoding of human language, can effectively serve as this classifier with zero, or very few, examples or additional training.

First, let's describe the flow in words:

1. An LLM call to pick which of the available indexes to use, given the user-supplied query, and the developer-supplied description of the indexes

- 2. A retrieval step that queries the chosen index for the most relevant documents for the user query
- 3. Another LLM call to generate an answer, given the usersupplied query and the list of relevant documents fetched from the index

And now let's implement it with LangGraph:

#### <span id="page-300-0"></span>*Python*

```
from typing import Annotated, Literal, TypedDict
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage,
from langchain_core.vectorstores.in_memory import
from langchain_openai import ChatOpenAI, OpenAIEm
from langgraph.graph import END, START, StateGrap
from langgraph.graph.message import add_messages
embeddings = OpenAIEmbeddings()
# useful to generate SQL query
model_low_temp = ChatOpenAI(temperature=0.1)
# useful to generate natural language outputs
model_high_temp = ChatOpenAI(temperature=0.7)
class State(TypedDict):
```

```
 # to track conversation history
 messages: Annotated[list, add_messages]
 # input
```
( yp )

```
 user_query: str
 # output
 domain: Literal["records", "insurance"]
 documents: list[Document]
 answer: str
```

```
class Input(TypedDict):
 user_query: str
```

```
class Output(TypedDict):
 documents: list[Document]
 answer: str
```
# refer to Chapter 2 on how to fill a vector stor medical\_records\_store = InMemoryVectorStore.from\_ medical\_records\_retriever = medical\_records\_store

```
insurance_faqs_store = InMemoryVectorStore.from_d
insurance_faqs_retriever = insurance_faqs_store.a
```

```
router_prompt = SystemMessage(
 """You need to decide which domain to route t
 domains to choose from:
 - records: contains medical records of 
         diagnosis, treatment, and prescriptions
```

```
 d ag os s, t eat e t, a d p esc pt o s
 - insurance: contains frequently asked 
 policies, claims, and coverage.
Output only the domain name."""
)
def router_node(state: State) -> State:
 user_message = HumanMessage(state["user_query
 messages = [router_prompt,
                           *state["messages"]
 res = model_low_temp.invoke(messages)
 return {
 "domain": res.content,
 # update conversation history
 "messages": [user_message, res],
 }
def pick_retriever(
 state: State,
) -> Literal["retrieve_medical_records", "retriev
 if state["domain"] == "records":
 return "retrieve_medical_records"
 else:
 return "retrieve_insurance_faqs"
def retrieve_medical_records(state: State) -> Sta
 documents = medical_records_retriever.invoke(
 return {
 "documents": documents,
```

```
 }
def retrieve_insurance_faqs(state: State) -> Stat
 documents = insurance_faqs_retriever.invoke(s
 return {
 "documents": documents,
 }
medical_records_prompt = SystemMessage(
 """You are a helpful medical chatbot who answ
 patient's medical records, such as diagno
 prescriptions."""
)
insurance_faqs_prompt = SystemMessage(
 """You are a helpful medical insurance chatbo
 questions about insurance policies, claim
)
def generate_answer(state: State) -> State:
 if state["domain"] == "records":
 prompt = medical_records_prompt
 else:
 prompt = insurance_faqs_prompt
 messages = [
 prompt,
 *state["messages"],
 HumanMessage(f"Documents: {state["documen
```
docu e ts docu e ts,

```
 ]
 res = model_high_temp.invoke(messages)
 return {
 "answer": res.content,
 # update conversation history
 "messages": res,
 }
```
u a essage( ocu e ts {state[ docu e

```
builder = StateGraph(State, input=Input, output=O
builder.add_node("router", router_node)
builder.add_node("retrieve_medical_records", retr
builder.add_node("retrieve_insurance_faqs", retri
builder.add_node("generate_answer", generate_answ
builder.add_edge(START, "router")
builder.add_conditional_edges("router", pick_retr
builder.add_edge("retrieve_medical_records", "gen
builder.add_edge("retrieve_insurance_faqs", "gene
builder.add_edge("generate_answer", END)
```

```
graph = builder.compile()
```
<span id="page-304-0"></span>*JavaScript*

```
import {
 HumanMessage,
  SystemMessage
```

```
 SystemMessage
} from "@langchain/core/messages";
import {
 ChatOpenAI,
 OpenAIEmbeddings
} from "@langchain/openai";
import {
 MemoryVectorStore
} from "langchain/vectorstores/memory";
import {
 DocumentInterface
} from "@langchain/core/documents";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
 END,
} from "@langchain/langgraph";
const embeddings = new OpenAIEmbeddings();
// useful to generate SQL query
const modelLowTemp = new ChatOpenAI({ temperature
// useful to generate natural language outputs
const modelHighTemp = new ChatOpenAI({ temperatur
const annotation = Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
 user_query: Annotation(),
```
d i i ()

```
 domain: Annotation(),
 documents: Annotation(),
 answer: Annotation(),
});
// refer to Chapter 2 on how to fill a vector sto
const medicalRecordsStore = await MemoryVectorSto
 [],
 embeddings
);
const medicalRecordsRetriever = medicalRecordsSto
const insuranceFaqsStore = await MemoryVectorStor
 [],
 embeddings
);
const insuranceFaqsRetriever = insuranceFaqsStore
const routerPrompt = new SystemMessage(
 `You need to decide which domain to route the u
 domains to choose from:
 - records: contains medical records of th
 treatment, and prescriptions.
 - insurance: contains frequently asked qu
 policies, claims, and coverage.
Output only the domain name.`
);
```

```
async function routerNode(state) {
 const userMessage = new HumanMessage(state.user
 const messages = [routerPrompt, ...state.messag
 const res = await modelLowTemp.invoke(messages)
 return {
 domain: res.content as "records" | "insurance
 // update conversation history
 messages: [userMessage, res],
 };
}
function pickRetriever(state) {
 if (state.domain === "records") {
 return "retrieve_medical_records";
 } else {
 return "retrieve_insurance_faqs";
 }
}
async function retrieveMedicalRecords(state) {
 const documents = await medicalRecordsRetriever
 return {
 documents,
 };
}
async function retrieveInsuranceFaqs(state) {
```
d i i i

```
 const documents = await insuranceFaqsRetriever
 return {
 documents,
 };
}
const medicalRecordsPrompt = new SystemMessage(
 `You are a helpful medical chatbot who answers 
 patient's medical records, such as diagnosis,
 prescriptions.`
);
const insuranceFaqsPrompt = new SystemMessage(
 `You are a helpful medical insurance chatbot wh
 questions about insurance policies, claims, a
);
async function generateAnswer(state) {
 const prompt =
 state.domain === "records" ? medicalRecordsPr
 const messages = [
 prompt,
 ...state.messages,
 new HumanMessage(`Documents: ${state.document
 ];
 const res = await modelHighTemp.invoke(messages
 return {
 answer: res.content as string,
```
// d i hi

```
 // update conversation history
 messages: res,
 };
}
const builder = new StateGraph(annotation)
 .addNode("router", routerNode)
 .addNode("retrieve_medical_records", retrieveMe
 .addNode("retrieve_insurance_faqs", retrieveIns
 .addNode("generate_answer", generateAnswer)
 .addEdge(START, "router")
 .addConditionalEdges("router", pickRetriever)
 .addEdge("retrieve_medical_records", "generate_
 .addEdge("retrieve_insurance_faqs", "generate_a
 .addEdge("generate_answer", END);
const graph = builder.compile();
```
The visual representation is shown in [Figure](#page-310-0) 5-4.

<span id="page-310-0"></span>![](_page_310_Figure_0.jpeg)

Figure 5-4. The router architecture

Notice how this is now starting to become more useful, as it shows the two possible paths through the graph, through retrieve\_medical\_records or through retrieve\_insurance\_faqs , and that for both of those, we first visit the router node and finish by visiting the generate\_answer node. These two possible paths were implemented through the use of a conditional edge, implemented in the function pick\_retriever , which maps the domain picked by the LLM to one of the two nodes mentioned earlier. The conditional edge is shown in [Figure](#page-310-0) 5-4 as dotted lines from the source node to the destination nodes.

And now for example inputs and outputs, this time with streaming output:

*Python*

```
input = {
 "user_query": "Am I covered for COVID-19 trea
}
for c in graph.stream(input):
 print(c)
```
*JavaScript*

```
const input = {
 user_query: "Am I covered for COVID-19 treatmen
}
for await (const chunk of await graph.stream(inpu
console.log(chunk)
}
```
*The output* (the actual answer is not shown, since it would depend on your documents):

```
{
 "router": {
 "messages": [
 HumanMessage(content="Am I covered fo
 AIMessage(content="insurance"),
 ],
 "domain": "insurance",
 }
}
{
 "retrieve_insurance_faqs": {
 "documents": [...]
 }
}
{
 "generate_answer": {
 "messages": AIMessage(
 content="...",
 ),
 "answer": "...",
 }
}
```
This output stream contains the values returned by each node that ran during this execution of the graph. Let's take it one at a time. The top-level key in each dictionary is the name of the node, and the value for that key is what that node returned:

- 1. The router node returned an update to messages (this would allow us to easily continue this conversation using the memory technique described earlier), and the domain the LLM picked for this user's query, in this case insurance .
- 2. Then the pick\_retriever function ran and returned the name of the next node to run, based on the domain identified by the LLM call in the previous step.
- 3. Then the retrieve\_insurance\_faqs node ran, returning a set of relevant documents from that index. This means that on the drawing of the graph seen earlier, we took the left path, as decided by the LLM.
- 4. Finally, the generate\_answer node ran, which took those documents and the original user query and produced an answer to the question, which was written to the state (along with a final update to the messages key).

### <span id="page-313-0"></span>Summary

This chapter talked about the key trade-off when building LLM applications: agency versus oversight. The more autonomous an LLM application is, the more it can do—but that raises the

need for more mechanisms of control over its actions. We moved on to different cognitive architectures that strike different balances between agency and oversight.

[Chapter](#page-315-0) 6 talks about the most powerful of the cognitive architectures we've seen so far: the agent architecture.

<span id="page-314-0"></span>Theodore R. Sumers et al., "Cognitive [Architectures](https://oreil.ly/cuQnT) for Language Agents", arXiv, September 5, 2023, updated March 15, 2024. **[1](#page-280-1)**

<span id="page-314-1"></span>Tal Ridnik et al., "Code Generation with [AlphaCodium:](https://oreil.ly/0wHX4) From Prompt Engineering to Flow Engineering", arXiv, January 16, 2024. **[2](#page-289-0)**

## <span id="page-315-0"></span>Chapter 6. Agent Architecture

Building on the architectures described in [Chapter](#page-277-0) 5, this chapter will cover what is perhaps the most important of all current LLM architectures, the agent architecture. First, we introduce what makes LLM agents unique, then we show how to build them and how to extend them for common use cases.

<span id="page-315-3"></span><span id="page-315-1"></span>In the artificial intelligence field, there is a long history of creating (intelligent) agents, which can be most simply defined as "something that acts," in the words of Stuart Russell and Peter Norvig in their *Artificial Intelligence* (Pearson, 2020) textbook. The word *acts* actually carries a little more meaning than meets the eye:

- Acting requires some capacity for deciding what to do.
- Deciding what to do implies having access to more than one possible course of action. After all, a decision without options is no decision at all.
- In order to decide, the agent also needs access to information about the external environment (anything outside of the agent itself).

<span id="page-315-2"></span>So an *agentic* LLM application must be one that uses an LLM to pick from one or more possible courses of action, given some

context about the current state of the world or some desired next state. These attributes are usually implemented by mixing two prompting techniques we first met in the [Preface:](#page-8-0)

#### *Tool calling*

<span id="page-316-1"></span>Include a list of external functions that the LLM can make use of in your prompt (that is, the actions it can decide to take) and provide instructions on how to format its choice in the output it generates. You'll see in a moment what this looks like in the prompt.

#### *Chain-of-thought*

<span id="page-316-0"></span>Researchers have found that LLMs "make better decisions" when given instructions to reason about complex problems by breaking them down into granular steps to be taken in sequence. This is usually done either by adding instructions along the lines of "think step by step" or including examples of questions and their decomposition into several steps/actions.

Here's an example prompt using both tool calling and chain-ofthought:

h thi t l t b h d

Tools:

search: this tool accepts a web search query and calculator: this tool accepts math expressions an

If you want to use tools to arrive at the answer, inputs in CSV format, with the header row: tool,i

Think step by step; if you need to make multiple answer, return only the first one.

How old was the 30th president of the United Stat

tool,input

And the output, when run against gpt-3.5-turbo at temperature 0 (to ensure the LLM follows the desired output format, CSV) and newline as the stop sequence (which instructs the LLM to stop producing output when it reaches this character). This makes the LLM produce a single action (as expected, given the prompt asked for this):

search,30th president of the United States

The most recent LLMs and chat models have been fine-tuned to improve their performance for tool-calling and chain-ofthought applications, removing the need for adding specific instructions to the prompt:

add example prompt and output for tool-calling mo

## The Plan-Do Loop

<span id="page-318-0"></span>What makes the agent architecture different from the architectures discussed in [Chapter](#page-277-0) 5 is a concept we haven't covered yet: the LLM-driven loop.

<span id="page-318-2"></span><span id="page-318-1"></span>Every programmer has encountered loops in their code before. By *loop*, we mean running the same code multiple times until a stop condition is hit. The key to the agent architecture is to have an LLM control the stop condition—that is, decide when to stop looping.

What we'll run in this loop will be some variation of the following:

- Planning an action or actions
- Executing said action(s)

Picking up on the example in the previous section, we'll next run the search tool with the input 30th president of the United States , which produces this output:

Calvin Coolidge (born John Calvin Coolidge Jr.; / 5, 1933) was an American attorney and politician of the United States from 1923 to 1929. John Calv

And then we'll rerun the prompt, with a small addition:

Tools: search: this tool accepts a web search query and calculator: this tool accepts math expressions an output: this tool ends the interaction. Use it wh If you want to use tools to arrive at the answer, inputs in CSV format, with this header row: tool, Think step by step; if you need to make multiple the answer, return only the first one. How old was the 30th president of the United Stat tool,input

search,30th president of the United States

search: Calvin Coolidge (born John Calvin Coolidg January 5, 1933) was an American attorney and pol president of the United States from 1923 to 1929

tool,input

And the output:

calculator,1933 - 1872

Notice we added two things:

- An "output" tool—which the LLM should use when it has found the final answer, and which we'd use as the signal to stop the loop.
- The result of the tool call from the preceding iteration, simply with the name of the tool and its (text) output. This is included in order to allow the LLM to move on to the next step in the interaction. In other words, we're telling the LLM, "Hey, we got the results you asked for, what do you want to do next?"

Let's continue with a third iteration:

Tools: search: this tool accepts a web search query and calculator: this tool accepts math expressions an

If you want to use tools to arrive at the answer, inputs in CSV format, with this header row: tool, output: this tool ends the interaction. Use it wh

Think step by step; if you need to make multiple the answer, return only the first one.

How old was the 30th president of the United Stat

tool,input

search,30th president of the United States

search: Calvin Coolidge (born John Calvin Coolidg January 5, 1933) was an American attorney and pol president of the United States from 1923 to 1929 tool,input

calculator,1933-1872

calculator: 61

tool, input

And the output:

output, 61

With the result from the calculator tool, the LLM now has enough information to provide the final answer, so it picked the output tool and chose "61" as the final answer.

<span id="page-322-0"></span>This is what makes the agent architecture so useful—the LLM is given the agency to decide. The next step is to arrive at an answer and decide how many steps to take—that is, when to stop.

<span id="page-322-3"></span><span id="page-322-2"></span>This architecture, called [ReAct,](https://oreil.ly/M7hF-) was first proposed by Shunyu Yao et al. The rest of this chapter explores how to improve the performance of the agent architecture, motivated by the email assistant example from [Chapter](#page-277-0) 5.

<span id="page-322-1"></span>But first, let's see what it looks like to implement the basic agent architecture using a chat model and LangGraph.

## Building a LangGraph Agent

<span id="page-323-1"></span><span id="page-323-0"></span>For this example, we need to install additional dependencies for the search tool we chose to use, DuckDuckGo. To install it for Python:

*Python*

pip install duckduckgo-search

And for JS, we also need to install a dependency for the calculator tool:

*JavaScript*

npm i duck-duck-scrape expr-eval

With that complete, let's get into the actual code to implement the agent architecture:

<span id="page-323-2"></span>*Python*

```
import ast
from typing import Annotated, TypedDict
```

```
from langchain_community.tools import DuckDuckGoS
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
```
from langgraph.graph import START, StateGraph from langgraph.graph.message import add\_messages from langgraph.prebuilt import ToolNode, tools\_co

```
@tool
```

```
def calculator(query: str) -> str:
 """A simple calculator tool. Input should be 
 return ast.literal_eval(query)
```

```
search = DuckDuckGoSearchRun()
tools = [search, calculator]
model = ChatOpenAI(temperature=0.1).bind_tools(to
```

```
class State(TypedDict):
 messages: Annotated[list, add_messages]
```

```
def model_node(state: State) -> State:
 res = model.invoke(state["messages"])
 return {"messages": res}
```

```
builder = StateGraph(State)
builder.add_node("model", model_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "model")
builder.add_conditional_edges("model", tools_cond
builder.add_edge("tools", "model")
graph = builder.compile()
```
#### <span id="page-325-0"></span>*JavaScript*

```
import {
 DuckDuckGoSearch
} from "@langchain/community/tools/duckduckgo_sea
import {
 Calculator
} from "@langchain/community/tools/calculator";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
} from "@langchain/langgraph";
import {
 ToolNode,
 toolsCondition
```
} from "@langchain/langgraph/prebuilt";

```
const search = new DuckDuckGoSearch();
const calculator = new Calculator();
const tools = [search, calculator];
const model = new ChatOpenAI({
 temperature: 0.1
}).bindTools(tools);
const annotation = Annotation.Root({
 messages: Annotation({
 reducer: messagesStateReducer,
 default: () => []
 }),
});
async function modelNode(state) {
 const res = await model.invoke(state.messages);
 return { messages: res };
}
const builder = new StateGraph(annotation)
 .addNode("model", modelNode)
 .addNode("tools", new ToolNode(tools))
 .addEdge(START, "model")
 .addConditionalEdges("model", toolsCondition)
 .addEdge("tools", "model");
```

```
const graph = builder.compile();
```
The visual representation is shown in [Figure](#page-327-0) 6-1.

<span id="page-327-0"></span>![](_page_327_Figure_2.jpeg)

Figure 6-1. The agent architecture

A few things to notice here:

We're using two tools in this example: a search tool and a calculator tool, but you could easily add more or replace the ones we used. In the Python example, you also see an example of creating a custom tool.

- We've used two convenience functions that ship with LangGraph. ToolNode serves as a node in our graph; it executes the tool calls requested in the latest AI message found in the state and returns a ToolMessage with the results of each. ToolNode also handles exceptions raised by tools—using the error message to build a ToolMessage that is then passed to the LLM—which may decide what to do with the error.
- tools\_condition serves as a conditional edge function that looks at the latest AI message in the state and routes to the tools node if there are any tools to execute. Otherwise, it ends the graph.
- Finally, notice that this graph loops between the model and tools nodes. That is, the model itself is in charge of deciding when to end the computation, which is a key attribute of the agent architecture. Whenever we code a loop in LangGraph, we'll likely want to use a conditional edge, as that allows you to define the *stop condition* when the graph should exit the loop and stop executing.

Now let's see how it does in the previous example:

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
for c in graph.stream(input):
 print(c)
```
*JavaScript*

```
const input = {
 messages: [
 HumanMessage(`How old was the 30th president 
 died?`)
 ]
}
for await (const c of await graph.stream(input))
 console.log(c)
}
```
*The output:*

{

```
 "model": {
 "messages": AIMessage(
 content="",
 tool_calls=[
 {
 "name": "duckduckgo_search",
 "args": {
 "query": "30th president 
 death"
 },
 "id": "call_ZWRbPmjvo0fYkwyo4
 "type": "tool_call",
 }
 ],
 )
 }
}
{
 "tools": {
 "messages": [
 ToolMessage(
 content="Calvin Coolidge (born Ju
 U.S.—died January 5, 1933, No
 the 30th president of the Uni
 acceded to the presidency aft
 Warren G. Harding, just as th
```

```
 to light....",
 name="duckduckgo_search",
 tool_call_id="call_ZWRbPmjvo0fYkw
 )
 ]
 }
}
{
 "model": {
 "messages": AIMessage(
 content="Calvin Coolidge, the 30th pr
 died on January 5, 1933, at the a
 )
 }
}
```
Walking through this output:

- 1. First the model node executed and decided to call the duckduckgo\_search tool, which led the conditional edge to route us to the tools node after.
- 2. The ToolNode executed the search tool and got the search results printed above, which actually contain the answer "Age and Year of Death . January 5, 1933 (aged 60)".
- 3. The model tool was called again, this time with the search results as the latest message, and produced the final answer

<span id="page-332-1"></span>(with no more tool calls); therefore, the conditional edge ended the graph.

Next, let's look at a few useful extensions to this basic agent architecture, customizing both planning and tool calling.

## Always Calling a Tool First

<span id="page-332-0"></span>In the standard agent architecture, the LLM is always called upon to decide what tool to call next. This arrangement has a clear advantage: it gives the LLM ultimate flexibility to adapt the behavior of the application to each user query that comes in. But this flexibility comes at a cost: unpredictability. If, for instance, you, the developer of the application, know that the search tool should always be called first, that can actually be beneficial to your application:

- 1. It will reduce overall latency, as it will skip the first LLM call that would generate that request to call the search tool.
- 2. It will prevent the LLM from erroneously deciding it doesn't need to call the search tool for some user queries.

On the other hand, if your application doesn't have a clear rule of the kind "you should always call this tool first," introducing such a constraint would actually make your application worse.

Let's see what it looks like to do this:

#### <span id="page-333-0"></span>*Python*

```
import ast
from typing import Annotated, TypedDict
from uuid import uuid4
from langchain_community.tools import DuckDuckGoS
from langchain_core.messages import AIMessage, Hu
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_co
@tool
def calculator(query: str) -> str:
 """A simple calculator tool. Input should be 
 return ast.literal_eval(query)
search = DuckDuckGoSearchRun()
tools = [search, calculator]
model = ChatOpenAI(temperature=0.1).bind_tools(to
class State(TypedDict):
    messages: Annotated[list add messages]
```

```
def model_node(state: State) -> State:
 res = model.invoke(state["messages"])
 return {"messages": res}
```

```
def first_model(state: State) -> State:
 query = state["messages"][-1].content
 search_tool_call = ToolCall(
 name="duckduckgo_search", args={"query":
 )
 return {"messages": AIMessage(content=""
                                         , too
```

```
builder = StateGraph(State)
builder.add_node("first_model", first_model)
builder.add_node("model", model_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "first_model")
builder.add_edge("first_model", "tools")
builder.add_conditional_edges("model", tools_cond
builder.add_edge("tools", "model")
```

```
graph = builder.compile()
```
<span id="page-334-0"></span>*JavaScript*

```
import {
 DuckDuckGoSearch
} from "@langchain/community/tools/duckduckgo_sea
import {
 Calculator
} from "@langchain/community/tools/calculator";
import {
 AIMessage,
} from "@langchain/core/messages";
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
} from "@langchain/langgraph";
import {
 ToolNode,
 toolsCondition
} from "@langchain/langgraph/prebuilt";
const search = new DuckDuckGoSearch();
const calculator = new Calculator();
const tools = [search, calculator];
const model = new ChatOpenAI({ temperature: 0.1 }
const annotation = Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
});
```

```
async function firstModelNode(state) {
 const query = state.messages[state.messages.len
 const searchToolCall = {
 name: "duckduckgo_search",
 args: { query },
 id: Math.random().toString(),
 };
 return {
 messages: [new AIMessage({ content: ""
                                         , tool_
 };
}
async function modelNode(state) {
 const res = await model.invoke(state.messages);
 return { messages: res };
}
const builder = new StateGraph(annotation)
 .addNode("first_model", firstModelNode)
 .addNode("model", modelNode)
 .addNode("tools", new ToolNode(tools))
 .addEdge(START, "first_model")
 .addEdge("first_model", "tools")
 .addEdge("tools", "model")
 .addConditionalEdges("model", toolsCondition);
```

```
const graph = builder.compile();
```
The visual representation is shown in [Figure](#page-338-0) 6-2.

<span id="page-338-0"></span>![](_page_338_Figure_0.jpeg)

Figure 6-2. Modifying the agent architecture to always call a specific tool first

Notice the differences compared to the previous section:

- Now, we start all invocations by calling first\_model , which doesn't call an LLM at all. It just creates a tool call for the search tool, using the user's message verbatim as the search query. The previous architecture would have the LLM generate this tool call (or some other response it deemed better).
- After that, we proceed to tools , which is identical to the previous example, and from there we proceed to the agent node as before.

Now let's see some example output, for the same query as before:

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
for c in graph.stream(input):
print(c)
```
#### *JavaScript*

```
const input = {
 messages: [
 HumanMessage(`How old was the 30th president 
 died?`)
 ]
}
for await (const c of await graph.stream(input))
 console.log(c)
}
```
*The output:*

```
{
 "first_model": {
 "messages": AIMessage(
 content="",
 tool_calls=[
 {
 "name": "duckduckgo_search",
 "args": {
 "query": "How old was the
                 States when he died?"
```

```
 States when he died?"
 },
 "id": "9ed4328dcdea4904b1b544
 "type": "tool_call",
 }
 ],
 )
 }
}
{
 "tools": {
 "messages": [
 ToolMessage(
 content="Calvin Coolidge (born Ju
 U.S.—died January 5, 1933, No
 the 30th president of the Uni
 acceded to the presidency aft
 Warren G. Harding, just as th
 to light....",
 name="duckduckgo_search",
 tool_call_id="9ed4328dcdea4904b1b
 )
 ]
 }
}
{
 "model": {
 "messages": AIMessage(
       content="Calvin Coolidge the 30th pr
```

```
 content= Calvin Coolidge, the 30th pr
 was born on July 4, 1872, and die
 calculate his age at the time of 
 birth year from his death year. \
 Birth year\nAge at death = 1933 -
 years\n\nCalvin Coolidge was 61 y
 )
 }
}
```
This time, we skipped the initial LLM call. We first went to first\_model node, which directly returned a tool call for the search tool. From there we went to the previous flow—that is, we executed the search tool and finally went back to the model node to generate the final answer.

<span id="page-342-1"></span>Next let's go over what you can do when you have many tools you want to make available to the LLM.

## <span id="page-342-0"></span>Dealing with Many Tools

<span id="page-342-2"></span>LLMs are far from perfect, and they currently struggle more when given multiple choices or excessive information in a prompt. These limitations also extend to the planning of the next action to take. When given many tools (say, more than 10) the planning performance (that is, the LLM's ability to choose the right tool) starts to suffer. The solution to this problem is to reduce the number of tools the LLM can choose from. But what if you do have many tools you want to see used for different user queries?

One elegant solution is to use a RAG step to preselect the most relevant tools for the current query and then feed the LLM only that subset of tools instead of the entire arsenal. This can also help to reduce the cost of calling the LLM (commercial LLMs usually charge based on the length of the prompt and outputs). On the other hand, this RAG step introduces additional latency to your application, so should only be taken when you see performance decreasing after adding more tools.

Let's see how to do this:

#### <span id="page-343-0"></span>*Python*

```
import ast
from typing import Annotated, TypedDict
from langchain_community.tools import DuckDuckGoS
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
```
f l h i t l i t t l

```
from langchain_core.tools import tool
from langchain_core.vectorstores.in_memory import
from langchain_openai import ChatOpenAI, OpenAIEm
```
from langgraph.graph import START, StateGraph from langgraph.graph.message import add\_messages from langgraph.prebuilt import ToolNode, tools\_co

```
@tool
```

```
def calculator(query: str) -> str:
 """A simple calculator tool. Input should be 
 return ast.literal_eval(query)
```

```
search = DuckDuckGoSearchRun()
tools = [search, calculator]
```

```
embeddings = OpenAIEmbeddings()
model = ChatOpenAI(temperature=0.1)
```

```
tools_retriever = InMemoryVectorStore.from_docume
 [Document(tool.description, metadata={"name"
 embeddings,
```

```
).as_retriever()
```

```
class State(TypedDict):
 messages: Annotated[list, add_messages]
 selected_tools: list[str]
```
d f d l d ( t t St t ) > St t

```
def model_node(state: State) -> State:
 selected_tools = [
 tool for tool in tools if tool.name in st
 ]
 res = model.bind_tools(selected_tools).invoke
 return {"messages": res}
def select_tools(state: State) -> State:
 query = state["messages"][-1].content
 tool_docs = tools_retriever.invoke(query)
 return {"selected_tools": [doc.metadata["name
builder = StateGraph(State)
builder.add_node("select_tools", select_tools)
builder.add_node("model", model_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "select_tools")
builder.add_edge("select_tools", "model")
builder.add_conditional_edges("model", tools_cond
builder.add_edge("tools", "model")
graph = builder.compile()
```
<span id="page-345-0"></span>*JavaScript*

import { DuckDuckGoSearch } from "@langchain/comm import { Calculator } from "@langchain/community/

```
import { ChatOpenAI } from "@langchain/openai";
import { OpenAIEmbeddings } from "@langchain/open
import { Document } from "@langchain/core/documen
import { MemoryVectorStore } from "langchain/vect
import {
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
} from "@langchain/langgraph";
import { ToolNode, toolsCondition } from "@langch
import { HumanMessage } from "@langchain/core/mes

const search = new DuckDuckGoSearch();
const calculator = new Calculator();
const tools = [search, calculator];
const embeddings = new OpenAIEmbeddings();
const model = new ChatOpenAI({ temperature: 0.1 }
const toolsStore = await MemoryVectorStore.fromDo
 tools.map(
 (tool) =>
 new Document({
 pageContent: tool.description,
 metadata: { name: tool.constructor.name }
 })
 ),
```
embeddings

```
);
const toolsRetriever = toolsStore.asRetriever();
const annotation = Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
 selected_tools: Annotation(),
});
async function modelNode(state) {
 const selectedTools = tools.filter((tool) =>
 state.selected_tools.includes(tool.constructo
 );
 const res = await model.bindTools(selectedTools
 return { messages: res };
}
async function selectTools(state) {
 const query = state.messages[state.messages.len
 const toolDocs = await toolsRetriever.invoke(qu
 return {
 selected_tools: toolDocs.map((doc) => doc.met
 };
}
const builder = new StateGraph(annotation)
 .addNode("select_tools", selectTools)
 .addNode("model", modelNode)
```
![](_page_348_Figure_0.jpeg)

You can see the visual representation in [Figure](#page-348-0) 6-3.

<span id="page-348-0"></span>![](_page_348_Figure_2.jpeg)

Figure 6-3. Modifying the agent architecture to deal with many tools

#### **NOTE**

This is very similar to the regular agent architecture. The only difference is that we stop by the select\_tools node before entering the actual agent loop. After that, it works just as the regular agent architecture we've seen before.

Now let's see some example output for the same query as before:

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th presiden
 he died?""")
 ]
}
for c in graph.stream(input):
print(c)
```
*JavaScript*

```
const input = {
 messages: [
```

```
 HumanMessage(`How old was the 30th president 
 died?`)
 ]
}
for await (const c of await graph.stream(input))
 console.log(c)
}
```
#### *The output:*

```
{
 "select_tools": {
 "selected_tools': ['duckduckgo_search', 
 }
}
{
 "model": {
 "messages": AIMessage(
 content="",
 tool_calls=[
 {
 "name": "duckduckgo_search",
 "args": {
 "query": "30th president 
 },
 "id": "9ed4328dcdea4904b1b544
            "type": "tool call"
```

```
 type : tool_call ,
 }
 ],
 )
 }
}
{
 "tools": {
 "messages": [
 ToolMessage(
 content="Calvin Coolidge (born Ju
 U.S.—died January 5, 1933, No
 the 30th president of the Uni
 acceded to the presidency aft
 Warren G. Harding, just as th
 to light....",
 name="duckduckgo_search",
 tool_call_id="9ed4328dcdea4904b1b
 )
 ]
 }
}
{
 "model": {
 "messages": AIMessage(
 content="Calvin Coolidge, the 30th pr
 was born on July 4, 1872, and die
 calculate his age at the time of 
 birth year from his death year. \
```
![](_page_352_Figure_0.jpeg)

<span id="page-352-0"></span>Notice how the first thing we did was query the retriever to get the most relevant tools for the current user query. Then, we proceeded to the regular agent architecture.

## Summary

This chapter introduced the concept of *agency* and discussed what it takes to make an LLM application *agentic*: giving the LLM the ability to decide between multiple options by using external information.

We walked through the standard agent architecture built with LangGraph and looked at two useful extensions: how to always call a specific tool first and how to deal with many tools.

[Chapter](#page-353-0) 7 looks at additional extensions to the agent architecture.

## <span id="page-353-0"></span>Chapter 7. Agents II

[Chapter](#page-315-0) 6 introduced the *agent* architecture, the most powerful of the LLM architectures we have seen up until now. It is hard to overstate the potential of this combination of chain-ofthought prompting, tool use, and looping.

This chapter discusses two extensions to the agent architecture that improve performance for some use cases:

#### *Reflection*

Taking another page out of the repertoire of human thought patterns, this is about giving your LLM app the opportunity to analyze its past output and choices, together with the ability to remember reflections from past iterations.

#### *Multi-agent*

Much the same way as a team can accomplish more than a single person, there are problems that can be best tackled by teams of LLM agents.

Let's start with reflection.

## Reflection

<span id="page-354-2"></span><span id="page-354-0"></span>One prompting technique we haven't covered yet is *reflection* (also known as *self-critique*). *Reflection* is the creation of a loop between a creator prompt and a reviser prompt. This mirrors the creation process for many human-created artifacts, such as this chapter you're reading now, which is the result of a back and forth between the authors, reviewers, and editor until all are happy with the final product.

As with many of the prompting techniques we have seen so far, reflection can be combined with other techniques, such as chain-of-thought and tool calling. In this section, we'll look at reflection in isolation.

<span id="page-354-1"></span>A parallel can be drawn to the modes of human thinking known as *System 1* (reactive or instinctive) and *System 2* (methodical and reflective), first introduced by Daniel Kahneman in the book *Thinking, Fast and Slow* (Farrar, Straus and Giroux, 2011). When applied correctly, self-critique can help LLM applications get closer to something that resembles System 2 behavior [\(Figure](#page-355-0) 7-1).

<span id="page-355-0"></span>![](_page_355_Figure_0.jpeg)

Figure 7-1. System 1 and System 2 thinking

We'll implement reflection as a graph with two nodes: generate and reflect . This graph will be tasked with writing three-paragraph essays, with the generate node writing or revising drafts of the essay, and reflect writing a critique to inform the next revision. We'll run the loop a fixed number of times, but a variation on this technique would be to have the reflect node decide when to finish. Let's see what it looks like:

<span id="page-356-0"></span>*Python*

```
from typing import Annotated, TypedDict
from langchain_core.messages import (
 AIMessage,
 BaseMessage,
 HumanMessage,
 SystemMessage,
)
from langchain_openai import ChatOpenAI
from langgraph.graph import END, START, StateGrap
from langgraph.graph.message import add_messages
model = ChatOpenAI()
class State(TypedDict):
 messages: Annotated[list[BaseMessage], add_me
generate_prompt = SystemMessage(
 """You are an essay assistant tasked with wri
 essays."""
 "Generate the best essay possible for the use
```

```
 """If the user provides critique, respond wit
 previous attempts."""
)
def generate(state: State) -> State:
 answer = model.invoke([generate_prompt] + sta
 return {"messages": [answer]}
reflection_prompt = SystemMessage(
 """You are a teacher grading an essay submiss
 recommendations for the user's submission
 """Provide detailed recommendations, includin
 style, etc."""
)
def reflect(state: State) -> State:
 # Invert the messages to get the LLM to refle
 cls_map = {AIMessage: HumanMessage, HumanMess
 # First message is the original user request
 # We hold it the same for all nodes
 translated = [reflection_prompt, state["messa
 cls_map[msg.__class__](content=msg.conten
 for msg in state["messages"][1:]
 ]
 answer = model.invoke(translated)
 # We treat the output of this as human feedba
 return {"messages": [HumanMessage(content=ans
```

```
def should_continue(state: State):
 if len(state["messages"]) > 6:
 # End after 3 iterations, each with 2 mes
 return END
 else:
 return "reflect"
builder = StateGraph(State)
builder.add_node("generate", generate)
builder.add_node("reflect", reflect)
builder.add_edge(START, "generate")
builder.add_conditional_edges("generate", should_
builder.add_edge("reflect", "generate")
```

```
graph = builder.compile()
```
<span id="page-358-0"></span>*JavaScript*

```
import {
 AIMessage,
 BaseMessage,
 SystemMessage,
 HumanMessage,
} from "@langchain/core/messages";
import { ChatOpenAI } from "@langchain/openai";
import {
```

```
 StateGraph,
 Annotation,
 messagesStateReducer,
 START,
 END,
} from "@langchain/langgraph";
const model = new ChatOpenAI();
const annotation = Annotation.Root({
 messages: Annotation({ reducer: messagesStateRe
});
// fix multiline string
const generatePrompt = new SystemMessage(
 `You are an essay assistant tasked with writing
 Generate the best essay possible for the user's
 If the user provides critique, respond with a r
 previous attempts.`
);
async function generate(state) {
 const answer = await model.invoke([generateProm
 return { messages: [answer] };
}
const reflectionPrompt = new SystemMessage(
 `You are a teacher grading an essay submission
```

```
 recommendations for the user's submission.
 Provide detailed recommendations, including req
 style, etc.`
);
async function reflect(state) {
 // Invert the messages to get the LLM to reflec
 const clsMap: { [key: string]: new (content: st
 ai: HumanMessage,
 human: AIMessage,
 };
 // First message is the original user request. 
 // We hold it the same for all nodes
 const translated = [
 reflectionPrompt,
 state.messages[0],
 ...state.messages
 .slice(1)
 .map((msg) => new clsMap[msg._getType()](ms
 ];
 const answer = await model.invoke(translated);
 // We treat the output of this as human feedbac
 return { messages: [new HumanMessage({ content
}
function shouldContinue(state) {
 if (state.messages.length > 6) {
 // End after 3 iterations, each with 2 messag
```

```
 return END;
 } else {
 return "reflect";
 }
}
const builder = new StateGraph(annotation)
 .addNode("generate", generate)
 .addNode("reflect", reflect)
 .addEdge(START, "generate")
 .addConditionalEdges("generate", shouldContinue
 .addEdge("reflect", "generate");
const graph = builder.compile();
```
The visual representation of the graph is shown in [Figure](#page-362-0) 7-2.

<span id="page-362-0"></span>![](_page_362_Figure_0.jpeg)

Figure 7-2. The reflection architecture

Notice how the reflect node tricks the LLM into thinking it is critiquing essays written by the user. And in tandem, the generate node is made to think that the critique comes from the user. This subterfuge is required because dialogue-tuned LLMs are trained on pairs of human-AI messages, so a sequence of many messages from the same participant would result in poor performance.

One more thing to note: you might, at first glance, expect the end to come after a revise step, but in this architecture we have <span id="page-363-0"></span>a fixed number of iterations of the generate-reflect loop; therefore we terminate after generate (so that the last set of revisions requested are dealt with). A variation on this architecture would instead have the reflect step make the decision to end the process (once it had no more comments).

Let's see what one of the critiques looks like:

```
 'messages': [
```
{

 HumanMessage(content='Your essay on the t and its message in modern life is wel have effectively highlighted the endu themes and its importance in today\'s few areas where you could enhance you While you touch upon the themes of ch nurturing connections, and understand consider delving deeper into each of examples from the book to support you themes manifest in contemporary life analyzing how the book\'s messages ca societal issues or personal experienc discuss how the Little Prince\'s pers to consumer culture or explore how hi can inform interpersonal dynamics in \*\*Length\*\*: Expand on your ideas by a

```
 discussing counterarguments, or explo
 "The Little Prince" in different part
 enrich the depth of your analysis and
 understanding of the book\'s relevanc
 is clear and well-structured. To enha
 readers, consider incorporating quote
 key points or including anecdotes to 
 \n\n5. **Conclusion**: Conclude your 
 enduring significance of "The Little 
 can inspire positive change in modern
 broader implications of the book\'s t
 with a lasting impression.\n\nBy expa
 incorporating more examples, and deep
 book\'s messages, you can create a mo
 compelling essay on the topicality of
 life. Well done on your thoughtful an
 work!', id='70c22b1d-ec96-4dc3-9fd0-d
```
#### And the final output:

],

}

```
{
 'messages': [
 AIMessage(content='"The Little Prince" by
 stands as a timeless masterpiece that
```

```
 insights into human relationships and
 readers across generations. The narra
 travels and encounters with a myriad 
 tapestry of allegorical representatio
 {'token_usage': {'completion_tokens'
 'total_tokens': 2921}, 'model_name': 
 'system_fingerprint': None, 'finish_r
 None}, id='run-2e8f9f13-f625-4820-9c8
 usage_metadata={'input_tokens': 2501,
 'total_tokens': 2921}),
 ],
}
```
This simple type of reflection can sometimes improve performance by giving the LLM multiple attempts at refining its output and by letting the reflection node adopt a different persona while critiquing the output.

There are several possible variations of this architecture. For one, we could combine the reflection step with the agent architecture of [Chapter](#page-315-0) 6, adding it as the last node right before sending output to the user. This would make the critique appear to come from the user, and give the application a chance to improve its final output without direct user intervention. Obviously this approach would come at the expense of higher latency.

In certain use cases, it could be helpful to ground the critique with external information. For instance, if you were writing a code-generation agent, you could have a step before reflect that would run the code through a linter or compiler and report any errors as input to reflect .

#### **TIP**

<span id="page-366-0"></span>Whenever this approach is possible, we strongly recommend giving it a try, as it's likely to increase the quality of the final output.

## Subgraphs in LangGraph

<span id="page-366-1"></span>Before we dive into multi-agent architectures, let's look at an important technical concept in LangGraph that enables it. *Subgraphs* are graphs that are used as part of another graph. Here are some use cases for subgraphs:

- Building multi-agent systems (discussed in the next section).
- When you want to reuse a set of nodes in multiple graphs, you can define them once in a subgraph and then use them in multiple parent graphs.
- When you want different teams to work on different parts of the graph independently, you can define each part as a

subgraph, and as long as the subgraph interface (the input and output schemas) is respected, the parent graph can be built without knowing any details of the subgraph.

<span id="page-367-0"></span>There are two ways to add subgraph nodes to a parent graph:

*Add a node that calls the subgraph directly*

This is useful when the parent graph and the subgraph share state keys, and you don't need to transform state on the way in or out.

*Add a node with a function that invokes the subgraph*

This is useful when the parent graph and the subgraph have different state schemas, and you need to transform state before or after calling the subgraph.

Let's look at each in turn.

### **Calling a Subgraph Directly**

<span id="page-367-1"></span>The simplest way to create subgraph nodes is to attach a subgraph directly as a node. When doing so, it is important that the parent graph and the subgraph share state keys, because those shared keys will be used to communicate. (If your graph and subgraph do not share any keys, see the next section.)

#### **NOTE**

If you pass extra keys to the subgraph node (that is, in addition to the shared keys), they will be ignored by the subgraph node. Similarly, if you return extra keys from the subgraph, they will be ignored by the parent graph.

Let's see what it looks like in action:

#### <span id="page-368-0"></span>*Python*

```
from langgraph.graph import START, StateGraph
from typing import TypedDict
class State(TypedDict):
 foo: str # this key is shared with the subgra
class SubgraphState(TypedDict):
 foo: str # this key is shared with the parent
 bar: str
# Define subgraph
def subgraph_node(state: SubgraphState):
 # note that this subgraph node can communicat
 # via the shared "foo" key
 return {"foo": state["foo"] + "bar"}
subgraph_builder = StateGraph(SubgraphState)
subgraph builder add node(subgraph node)
```

```
subgraph_builder.add_node(subgraph_node)
...
subgraph = subgraph_builder.compile()
# Define parent graph
builder = StateGraph(State)
builder.add_node("subgraph", subgraph)
...
graph = builder.compile()
```
<span id="page-369-0"></span>*JavaScript*

```
import { StateGraph, Annotation, START } from "@l
const StateAnnotation = Annotation.Root({
 foo: Annotation(),
});
const SubgraphStateAnnotation = Annotation.Root({
 // note that this key is shared with the parent
 foo: Annotation(),
 bar: Annotation(),
});
// Define subgraph
const subgraphNode = async (state) => {
 // note that this subgraph node can communicate
```

```
 // the parent graph via the shared "foo" key
 return { foo: state.foo + "bar" };
};
const subgraph = new StateGraph(SubgraphStateAnno
 .addNode("subgraph", subgraphNode);
 ...
 .compile();
// Define parent graph
const parentGraph = new StateGraph(StateAnnotatio
 .addNode("subgraph", subgraph)
 .addEdge(START, "subgraph")
 // Additional parent graph setup would go here
 .compile();
```
### **Calling a Subgraph with a Function**

<span id="page-370-0"></span>You might want to define a subgraph with a completely different schema. In that case, you can create a node with a function that invokes the subgraph. This function will need to transform the input (parent) state to the subgraph state before invoking the subgraph and transform the results back to the parent state before returning the state update from the node.

Let's see what it looks like:

#### <span id="page-371-0"></span>*Python*

```
class State(TypedDict):
 foo: str
class SubgraphState(TypedDict):
 # none of these keys are shared with the pare
 bar: str
 baz: str
# Define subgraph
def subgraph_node(state: SubgraphState):
 return {"bar": state["bar"] + "baz"}
subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(subgraph_node)
...
subgraph = subgraph_builder.compile()
# Define parent graph
def node(state: State):
 # transform the state to the subgraph state
 response = subgraph.invoke({"bar": state["foo
 # transform response back to the parent state
 return {"foo": response["bar"]}
builder = StateGraph(State)
```
# t th t i ` d ` f ti i t d

```
# note that we are using `node` function instead 
builder.add_node(node)
...
graph = builder.compile()
```
#### <span id="page-372-0"></span>*JavaScript*

```
import { StateGraph, START, Annotation } from "@l
const StateAnnotation = Annotation.Root({
 foo: Annotation(),
});
const SubgraphStateAnnotation = Annotation.Root({
 // note that none of these keys are shared with
 bar: Annotation(),
 baz: Annotation(),
});
// Define subgraph
const subgraphNode = async (state) => {
 return { bar: state.bar + "baz" };
};
```

```
const subgraph = new StateGraph(SubgraphStateAnno
 .addNode("subgraph", subgraphNode);
 ...
 .compile();
// Define parent graph
const subgraphWrapperNode = async (state) => {
 // transform the state to the subgraph state
 const response = await subgraph.invoke({
 bar: state.foo,
 });
 // transform response back to the parent state
 return {
 foo: response.bar,
 };
}
const parentGraph = new StateGraph(StateAnnotatio
 .addNode("subgraph", subgraphWrapperNode)
 .addEdge(START, "subgraph")
 // Additional parent graph setup would go here
 .compile();
```
<span id="page-373-0"></span>Now that we know how to use subgraphs, let's take a look at one of the big use cases for them: multi-agent architectures.

## Multi-Agent Architectures

<span id="page-374-0"></span>As LLM agents grow in size, scope, or complexity, several issues can show up and impact their performance, such as the following:

- <span id="page-374-4"></span>The agent is given too many tools to choose from and makes poor decisions about which tool to call next [\(Chapter](#page-315-0) 6 discussed some approaches to this problem).
- <span id="page-374-1"></span>The context grows too complex for a single agent to keep track of; that is, the size of the prompts and the number of things they mention grows beyond the capability of the model you're using.
- <span id="page-374-3"></span>You want to use a specialized subsystem for a particular area, for instance, planning, research, solving math problems, and so on.

<span id="page-374-2"></span>To tackle these problems, you might consider breaking your application into multiple smaller, independent agents and composing them into a multi-agent system. These independent agents can be as simple as a prompt and an LLM call or as complex as a ReAct agent (introduced in [Chapter](#page-315-0) 6). [Figure](#page-375-0) 7-3 illustrates several ways to connect agents in a multi-agent system.

<span id="page-375-0"></span>![](_page_375_Figure_0.jpeg)

Figure 7-3. Multiple strategies for coordinating multiple agents

Let's look at [Figure](#page-375-0) 7-3 in more detail:

*Network*

Each agent can communicate with every other agent. Any agent can decide which other agent is to be executed next.

*Supervisor*

<span id="page-376-0"></span>Each agent communicates with a single agent, called the *supervisor*. The supervisor agent makes decisions on which agent (or agents) should be called next. A special case of this architecture implements the supervisor agent as an LLM call with tools, as covered in [Chapter](#page-315-0) 6.

#### *Hierarchical*

You can define a multi-agent system with a supervisor of supervisors. This is a generalization of the supervisor architecture and allows for more complex control flows.

#### *Custom multi-agent workflow*

Each agent communicates with only a subset of agents. Parts of the flow are deterministic, and only select agents can decide which other agents to call next.

The next section dives deeper into the supervisor architecture, which we think has a good balance of capability and ease of use.

### **Supervisor Architecture**

In this architecture, we add each agent to the graph as a node and also add a supervisor node, which decides which agents should be called next. We use conditional edges to route

execution to the appropriate agent node based on the supervisor's decision. Refer back to [Chapter](#page-277-0) 5 for an introduction to LangGraph, which goes over the concepts of nodes, edges, and more.

Let's first see what the supervisor node looks like:

<span id="page-377-0"></span>*Python*

```
from typing import Literal
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
```

```
class SupervisorDecision(BaseModel):
 next: Literal["researcher", "coder", "FINISH"
```

```
model = ChatOpenAI(model="gpt-4o", temperature=0)
model = model.with_structured_output(SupervisorDe
```

```
agents = ["researcher", "coder"]
```

```
system_prompt_part_1 = f"""You are a supervisor t
conversation between the following workers: {agen
request, respond with the worker to act next. Eac
task and respond with their results and status. W
respond with FINISH."""
```

```
system_prompt_part_2 = f"""Given the conversation
 should we FINISH? Select one of: {', '.join(a
def supervisor(state):
 messages = [
 ("system", system_prompt_part_1),
 *state["messages"],
 ("system", system_prompt_part_2)
 ]
 return model.invoke(messages)
```
<span id="page-378-0"></span>*JavaScript*

```
import { ChatOpenAI } from 'langchain-openai';
import { z } from 'zod';
const SupervisorDecision = z.object({
 next: z.enum(['researcher', 'coder', 'FINISH'])
});
const model = new ChatOpenAI({ model: 'gpt-4o', t
const modelWithStructuredOutput = model.withStruc
const agents = ['researcher', 'coder'];
```

```
const systemPromptPart1 = `You are a supervisor t
 conversation between the following workers: ${a
 following user request, respond with the worker
 will perform a task and respond with their resu
 finished, respond with FINISH.`;
```

```
const systemPromptPart2 = `Given the conversation
 should we FINISH? Select one of: ${agents.join(
```

```
const supervisor = async (state) => {
 const messages = [
 { role: 'system', content: systemPromptPart1
 ...state.messages,
 { role: 'system', content: systemPromptPart2
 ];
 return await modelWithStructuredOutput.invoke({
};
```
#### **NOTE**

<span id="page-379-0"></span>The code in the prompt requires the names of your subagents to be self-explanatory and distinct. For instance, if they were simply called agent\_1 and agent\_2 , the LLM would have no information to decide which one is appropriate for each task. If needed, you could modify the prompt to add a description of each agent, which could help the LLM in picking an agent for each query.

Now let's see how to integrate this supervisor node into a larger graph that includes two other subagents, which we will call researcher and coder. Our overall goal with this graph is to handle queries that can be answered either by the researcher by itself or the coder by itself, or even both of them in succession. This example doesn't include implementations for either the researcher or coder—the key idea is they could be any other LangGraph graph or node:

#### <span id="page-380-0"></span>*Python*

```
from typing import Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesS
model = ChatOpenAI()
class AgentState(BaseModel):
 next: Literal["researcher", "coder", "FINISH"
def researcher(state: AgentState):
 response = model.invoke(...)
 return {"messages": [response]}
def coder(state: AgentState):
 response = model.invoke(...)
```

```
 return {"messages": [response]}
builder = StateGraph(AgentState)
builder.add_node(supervisor)
builder.add_node(researcher)
builder.add_node(coder)
builder.add_edge(START, "supervisor")
# route to one of the agents or exit based on the
builder.add_conditional_edges("supervisor", lambd
builder.add_edge("researcher", "supervisor")
builder.add_edge("coder", "supervisor")
supervisor = builder.compile()
```
#### <span id="page-381-0"></span>*JavaScript*

```
import {
 StateGraph,
 Annotation,
 MessagesAnnotation,
 START,
 END,
} from "@langchain/langgraph";
import { ChatOpenAI } from "@langchain/openai";
```

```
const model = new ChatOpenAI({
 model: "gpt-4o",
});
const StateAnnotation = Annotation.Root({
 ...MessagesAnnotation.spec,
 next: Annotation(),
});
const researcher = async (state) => {
 const response = await model.invoke(...);
 return { messages: [response] };
};
const coder = async (state) => {
 const response = await model.invoke(...);
 return { messages: [response] };
};
const graph = new StateGraph(StateAnnotation)
 .addNode("supervisor", supervisor)
 .addNode("researcher", researcher)
 .addNode("coder", coder)
 .addEdge(START, "supervisor")
 // route to one of the agents or exit based on 
 .addConditionalEdges("supervisor", async (state
 state.next === 'FINISH' ? END : state.next)
 .addEdge("researcher", "supervisor")
```

```
 .addEdge("coder", "supervisor")
 .compile();
```
A few things to notice: In this example, both subagents (researcher and coder) can see each other's work, as all progress is recorded in the messages list. This isn't the only way to organize this. Each of the subagents could be more complex. For instance, a subagent could be its own graph that maintains internal state and only outputs a summary of the work it did.

After each agent executes, we route back to the supervisor node, which decides if there is more work to be done and which agent to delegate that to if so. This routing isn't a hard requirement for this architecture; we could have each subagent make a decision as to whether its output should be returned directly to the user. To do that, we'd replace the hard edge between, say, researcher and supervisor, with a conditional edge (which would read some state key updated by researcher).

## <span id="page-383-0"></span>Summary

This chapter covered two important extensions to the agent architecture: reflection and multi-agent architectures. The chapter also looked at how to work with subgraphs in

LangGraph, which are a key building block for multi-agent systems.

These extensions add more power to the LLM agent architecture, but they shouldn't be the first thing you reach for when creating a new agent. The best place to start is usually the straightforward architecture we discussed in [Chapter](#page-315-0) 6.

[Chapter](#page-385-0) 8 returns to the trade-off between reliability and agency, which is the key design decision when building LLM apps today. This is especially important when using the agent or multi-agent architectures, as their power comes at the expense of reliability if left unchecked. After diving deeper into why this trade-off exists, [Chapter](#page-385-0) 8 will cover the most important techniques at your disposal to navigate that decision, and ultimately improve your LLM applications and agents.

## <span id="page-385-0"></span>Chapter 8. Patterns to Make the Most of LLMs

LLMs today have some major limitations, but that doesn't mean your dream LLM app is impossible to build. The experience that you design for users of your application needs to work around, and ideally with, the limitations.

<span id="page-385-4"></span><span id="page-385-3"></span><span id="page-385-2"></span><span id="page-385-1"></span>[Chapter](#page-277-0) 5 touched on the key trade-off we face when building LLM apps: the trade-off between *agency* (the LLM's capacity to act autonomously) and *reliability* (the degree to which we can trust its outputs). Intuitively, any LLM application will be more useful to us if it takes more actions without our involvement, but if we let agency go too far, the application will inevitably do things we wish it hadn't.

[Figure](#page-386-0) 8-1 illustrates this trade-off.

<span id="page-386-0"></span>![](_page_386_Figure_0.jpeg)

<span id="page-386-2"></span><span id="page-386-1"></span>Figure 8-1. The agency-reliability trade-off

To borrow a concept from other fields, we can visualize the trade-off as a *frontier*—all points on the frontier's curved line are optimal LLM architectures for some application, marking different choices between agency and reliability. (Refer to [Chapter](#page-277-0) 5 for an overview of different LLM application architectures.) As an example, notice how the chain architecture has relatively low agency but higher reliability, **[1](#page-423-0)**

whereas the Agent architecture has higher agency at the expense of lower reliability.

Let's briefly touch on a number of additional (but still important) objectives that you might want your LLM application to have. Each LLM app will be designed for a different mix of one or more of these objectives:

#### *Latency*

<span id="page-387-1"></span>Minimize time to get final answer

#### *Autonomy*

<span id="page-387-0"></span>Minimize interruptions for human input

#### *Variance*

<span id="page-387-2"></span>Minimize variation between invocations

This is not meant as an exhaustive list of all possible objectives, but rather as illustrative of the trade-offs you face when building your application. Each objective is somewhat at odds with all the others (for instance, the easiest path to higher reliability requires either higher latency or lower autonomy). Each objective would nullify the others if given full weight (for instance, the minimal latency app is the one that does nothing at all). [Figure](#page-388-0) 8-2 illustrates this concept.

<span id="page-388-0"></span>![](_page_388_Figure_0.jpeg)

Figure 8-2. Shifting the frontier, or more agency, for the same reliability

What we really want as application developers is to shift the frontier outward. For the same level of reliability, we'd like to achieve higher agency; and for the same level of agency, we'd like to achieve higher reliability. This chapter covers a number of techniques you can use to achieve this:

#### *Streaming/intermediate output*

Higher latency is easier to accept if there is some communication of progress/intermediate output throughout.

#### *Structured output*

Requiring an LLM to produce output in a predefined format makes it more likely that it will conform to expectations.

#### *Human in the loop*

Higher-agency architectures benefit from human intervention while they're running: interrupting, approving, forking, or undoing.

#### *Double texting modes*

<span id="page-389-0"></span>The longer an LLM app takes to answer, the more likely it is that the user might send it new input before the previous one has finished being processed.

## Structured Output

<span id="page-389-1"></span>It is often crucial to have LLMs return structured output, either because a downstream use of that output expects a things in a specific *schema* (a definition of the names and types of the

various fields in a piece of structured output) or purely to reduce variance to what would otherwise be completely freeform text output.

<span id="page-390-1"></span>There are a few different strategies you can use for this with different LLMs:

#### *Prompting*

<span id="page-390-0"></span>This is when you ask the LLM (very nicely) to return output in the desired format (for instance, JSON, XML, or CSV). Prompting's big advantage is that it works to some extent with any LLM; the downside is that it acts more as a suggestion to the LLM and not as a guarantee that the output will come out in this format.

#### *Tool calling*

<span id="page-390-2"></span>This is available for LLMs that have been fine-tuned to pick from a list of possible output schemas, and to produce something that conforms to the chosen one. This usually involves writing, for each of the possible output schemas: a name to identify it, a description to help the LLM decide when it is the appropriate choice, and a schema for the desired output format (usually in JSONSchema notation).

*JSON mode*

<span id="page-391-0"></span>This is a mode available in some LLMs (such as recent OpenAI models) that enforces the LLM to output a valid JSON document.

Different models may support different variants of these, with slightly different parameters. To make it easy to get LLMs to return structured output, LangChain models implement a common interface, a method called

.with\_structured\_output . By invoking this method—and passing in a JSON schema or a Pydantic (in Python) or Zod (in JS) model—the model will add whatever model parameters and output parsers are necessary to produce and return the structured output. When a particular model implements more than one of the preceding strategies, you can configure which method to use.

Let's create a schema to use:

<span id="page-391-1"></span>*Python*

from pydantic import BaseModel, Field

class Joke(BaseModel):

```
 setup: str = Field(description="The setup of 
 punchline: str = Field(description="The punch
```
<span id="page-392-0"></span>*JavaScript*

c ass Jo e( ase ode )

```
import { z } from "zod";
const joke = z.object({
 setup: z.string().describe("The setup of the jo
 punchline: z.string().describe("The punchline t
});
```
Notice how we take care to add a description to each field. This is key because—together with the name of the field—this is the information the LLM will use to decide what part of the output should go in each field. We could also have defined a schema in raw JSONSchema notation, which would look like this:

```
{'properties': {'setup': {'description': 'The set
 'title': 'Setup',
 'type': 'string'},
 'punchline': {'description': 'The punchline to t
```

```
'title': 'Punchline'
```

```
 'title': 'Punchline',
 'type': 'string'}},
 'required': ['setup', 'punchline'],
 'title': 'Joke',
 'type': 'object'}
```
And now let's get an LLM to generate output that conforms to this schema:

<span id="page-393-1"></span>*Python*

```
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-3.5-turbo", tempera
model = model.with_structured_output(Joke)
model.invoke("Tell me a joke about cats")
```
<span id="page-393-0"></span>*JavaScript*

```
import { ChatOpenAI } from "@langchain/openai";
let model = new ChatOpenAI({
 model: "gpt-3.5-turbo",
```

```
 temperature: 0
});
model = model.withStructuredOutput(joke);
await structuredLlm.invoke("Tell me a joke about
```
#### *An example of output*

```
{
 setup: "Why don't cats play poker in the wild
 punchline: "Too many cheetahs."
}
```
A couple of things to notice:

- We create the instance of the model as usual, specifying the model name to use and other parameters.
- Low temperature is usually a good fit for structured output, as it reduces the chance the LLM will produce invalid output that doesn't conform to the schema.
- Afterward, we attach the schema to the model, which returns a new object, which will produce output that matches the schema provided. When you pass in a Pydantic or Zod object

for schema, this will be used for validation as well; that is, if the LLM produces output that doesn't conform, a validation error will be returned to you instead of the failed output.

Finally, we invoke the model with our (free-form) input, and receive back output that matches the structure we desired.

This pattern of using structured output can be very useful both as a standalone tool and as a part of a larger application; for instance, refer back to [Chapter](#page-277-0) 5, where we make use of this capability to implement the routing step of the router architecture.

### **Intermediate Output**

<span id="page-395-0"></span>The more complex your LLM architecture becomes, the more likely it will take longer to execute. If you think back to the architecture diagrams in Chapters [5](#page-277-0) and [6,](#page-315-0) every time you see multiple steps (or nodes) connected in sequence or in a loop, that is an indication that the time it takes for a full invocation is increasing.

<span id="page-395-1"></span>This increase in latency—if not addressed—can be a blocker to user adoption of LLM applications, with most users expecting computer applications to produce some output within seconds. There are several strategies to make the higher latency more

palatable, but they all fall under the umbrella of *streaming output*, that is, receiving output from the application while it is still running.

For this section, we'll use the last architecture described in ["Dealing](#page-342-0) with Many Tools". Refer back to [Chapter](#page-315-0) 6 for the full code snippet.

<span id="page-396-3"></span><span id="page-396-1"></span>To generate intermediate output with LangGraph, all you have to do is to invoke the graph with the stream method, which will yield the output of each node as soon as each finishes. Let's see what that looks like:

<span id="page-396-2"></span>*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
for c in graph.stream(input, stream_mode='updates
 print(c)
```
<span id="page-396-0"></span>*JavaScript*

```
const input = {
 messages: [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const output = await graph.stream(input, streamMo
for await (const c of output) {
 console.log(c)
}
```
*The output:*

```
{
 "select_tools": {
 "selected_tools": ['duckduckgo_search', 
 }
}
{
 "model": {
 "messages": AIMessage(
 content="",
 tool_calls=[
 {
 "name": "duckduckgo_search",
```

```
 "args": {
 "query": "30th president 
 },
 "id": "9ed4328dcdea4904b1b544
 "type": "tool_call",
 }
 ],
 )
 }
}
{
 "tools": {
 "messages": [
 ToolMessage(
 content="Calvin Coolidge (born Ju
 U.S.—died January 5, 1933, No
 the 30th president of the Uni
 acceded to the presidency aft
 Warren G. Harding, just as th
 to light....",
 name="duckduckgo_search",
 tool_call_id="9ed4328dcdea4904b1b
 )
 ]
 }
}
{
 "model": {
```

```
 "messages": AIMessage(
 content="Calvin Coolidge, the 30th pr
 was born on July 4, 1872, and die
 calculate his age at the time of 
 birth year from his death year. \
 Birth year\nAge at death = 1933 -
 years\n\nCalvin Coolidge was 61 y
 )
 }
}
```
Notice how each output entry is a dictionary with the name of the node that emitted as the key and the output of that node as the value. This gives you two key pieces of information:

- Where the application currently is; that is, if you think back to the architecture diagrams shown in previous chapters, where in that diagram are we currently?
- Each update to the shared state of the application, which together build up to the final output of the graph.

<span id="page-399-0"></span>In addition, LangGraph supports more stream modes:

- <span id="page-399-1"></span>updates . This is the default mode, described above.
- <span id="page-399-2"></span>values . This mode yields the current state of the graph every time it changes, that is after each set of nodes finishes

executing. This can be useful when the way you display output to your users closely tracks the shape of the graph state.

- <span id="page-400-1"></span><span id="page-400-0"></span>debug . This mode yields detailed events every time something happens in your graph, including:
	- checkpoint events, whenever a new checkpoint of the current state is saved to the database
	- task events, emitted whenever a node is about to start running
	- task\_result events, emitted whenever a node finishes running
- <span id="page-400-5"></span>Finally, you can combine these modes; for instance, requesting both updates and values by passing a list.

<span id="page-400-3"></span>You control the stream mode with the stream\_mode argument to stream() .

### **Streaming LLM Output Token-by-Token**

<span id="page-400-4"></span><span id="page-400-2"></span>Sometimes you may also want to get streaming output from each LLM call inside your larger LLM application. This can be useful for various projects, such as when building an interactive chatbot, where you want each word to be displayed as soon as it is produced by the LLM.

<span id="page-401-1"></span>You can achieve this with LangGraph as well:

#### <span id="page-401-2"></span>*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
output = app.astream_events(input, version="v2")
async for event in output:
 if event["event"] == "on_chat_model_stream":
 content = event["data"]["chunk"].content
 if content:
 print(content)
```
<span id="page-401-0"></span>*JavaScript*

```
const input = {
 messages: [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
```

```
}
const output = await agent.streamEvents(input, {v
for await (const { event, data } of output) {
 if (event === "on_chat_model_stream") {
 const msg = data.chunk as AIMessageChunk;
 if (msg.content) {
 console.log(msg.content);
 }
 }
}
```
This will emit each word (technically each token) as soon as it is received from the LLM. You can find more details on this pattern from [LangChain](https://oreil.ly/ExYll).

### **Human-in-the-Loop Modalities**

<span id="page-402-0"></span>As we walk the autonomy (or agency) ladder, we find ourselves increasingly giving up control (or oversight) in exchange for capability (or autonomy). The shared state pattern used in LangGraph (see [Chapter](#page-277-0) 5 for an introduction) makes it easier to observe, interrupt, and modify the application. This makes it possible to use many different *human-in-the-loop* modes, or

ways for the developer/end user of an application to influence what the LLM is up to.

For this section, we'll again use the last architecture described in ["Dealing](#page-342-0) with Many Tools". Refer back to [Chapter](#page-315-0) 6 for the full code snippet. For all human-in-the-loop modes, we first need to attach a [checkpointer](#page-257-0) to the graph; refer to "Adding Memory to StateGraph" for more details on this:

#### <span id="page-403-0"></span>*Python*

from langgraph.checkpoint.memory import MemorySav graph = builder.compile(checkpointer=MemorySaver(

#### *JavaScript*

```
import {MemorySaver} from '@langchain/langgraph'
graph = builder.compile({ checkpointer: new Memor
```
<span id="page-403-1"></span>This returns an instance of the graph that stores the state at the end of each step, so every invocation after the first doesn't start

from a blank slate. Any time the graph is called, it starts by using the checkpointer to fetch the most recent saved state—if any—and combines the new input with the previous state. And only then does it execute the first nodes. This is key to enabling human-in-the-loop modalities, which all rely on the graph remembering the previous state.

<span id="page-404-0"></span>The first mode, interrupt , is the simplest form of control the user is looking at streaming output of the application as it is produced, and manually interrupts it when he sees fit (see [Figure](#page-405-0) 8-3). The state is saved as of the last complete step prior to the user hitting the interrupt button. From there the user can choose to:

- Resume from that point onward, and the computation will proceed as if it hadn't been interrupted (see ["Resume"\)](#page-411-0).
- Send new input into the application (e.g., a new message in a chatbot), which will cancel any future steps that were pending and start dealing with the new input (see ["Restart"](#page-412-0)).
- Do nothing and nothing else will run.

<span id="page-405-0"></span>![](_page_405_Figure_0.jpeg)

Figure 8-3. The interrupt pattern

Let's see how to do this in LangGraph:

*Python*

import asyncio event = asyncio.Event()

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
config = {"configurable": {"thread_id": "1"}}
async with aclosing(graph.astream(input, config))
 async for chunk in stream:
 if event.is_set():
 break
 else:
 ... # do something with the output
# Somewhere else in your application
event.set()
```
#### *JavaScript*

```
const controller = new AbortController()
const input = {
  "messages": [
```

```
 messages : [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const config = {"configurable": {"thread_id": "1"
try {
 const output = await graph.stream(input, {
 ...config,
 signal: controller.signal
 });
 for await (const chunk of output) {
 console.log(chunk); // do something with the 
 }
} catch (e) {
 console.log(e);
}
// Somewhere else in your application
controller.abort()
```
This makes use of an event or signal, so that you can control interruption from outside of the running application. Notice in the Python code block the use of aclosing ; this ensures the stream is properly closed when interrupted. Notice in JS the use <span id="page-408-2"></span>of the try-catch statement, as interrupting the run will result in an abort exception being raised. Finally notice that usage of the checkpointer requires passing in an identifier for this thread, to distinguish this interaction with the graph from all others.

<span id="page-408-0"></span>![](_page_408_Figure_1.jpeg)

Figure 8-4. The authorize pattern

<span id="page-408-1"></span>A second control mode is authorize , where the user defines ahead of time that they want the application to hand off control to them every time a particular node is about to be called (see [Figure](#page-408-0) 8-4). This is usually implemented for tool confirmationbefore any tool (or particular tools) is called, the application will pause and ask for confirmation, at which point the user can, again:

- Resume computation, accepting the tool call.
- Send a new message to guide the bot in a different direction, in which case the tool will not be called.
- Do nothing.

Here's the code:

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
config = {"configurable": {"thread_id": "1"}}
output = graph.astream(input, config, interrupt_b
async for c in output:
 ... # do something with the output
```
#### *JavaScript*

```
const input = {
 "messages": [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const config = {"configurable": {"thread_id": "1"
const output = await graph.stream(input, {
 ...config,
 interruptBefore: ['tools']
});
for await (const chunk of output) {
 console.log(chunk); // do something with the ou
}
```
This will run the graph up until it is about to enter the node called tools , thus giving you the chance to inspect the current state, and decide whether to proceed or not. Notice that interrupt\_before is a list where order is not important; if

you pass multiple node names, it will interrupt before entering each of them.

#### <span id="page-411-0"></span>**Resume**

<span id="page-411-1"></span>To proceed from an interrupted graph—such as when using one of the previous two patterns—you just need to re-invoke the graph with null input (or None in Python). This is taken as a signal to continue processing the previous non-null input:

*Python*

```
config = {"configurable": {"thread_id": "1"}}
output = graph.astream(None, config, interrupt_be
async for c in output:
 ... # do something with the output
```
*JavaScript*

const config = {"configurable": {"thread\_id": "1"

```
const output = await graph.stream(null, {
 ...config,
 interruptBefore: ['tools']
});
for await (const chunk of output) {
 console.log(chunk); // do something with the ou
}
```
#### <span id="page-412-0"></span>**Restart**

<span id="page-412-1"></span>If instead you want an interrupted graph to start over from the first node, with additional new input, you just need to invoke it with new input:

*Python*

```
input = {
 "messages": [
 HumanMessage("""How old was the 30th pres
 when he died?""")
 ]
}
```

```
config = {"configurable": {"thread_id": "1"}}
output = graph.astream(input, config)
async for c in output:
 ... # do something with the output
```
#### *JavaScript*

```
const input = {
 "messages": [
 new HumanMessage(`How old was the 30th presid
 he died?`)
 ]
}
const config = {"configurable": {"thread_id": "1"
const output = await graph.stream(input, config);
for await (const chunk of output) {
 console.log(chunk); // do something with the ou
}
```
This will keep the current state of the graph, merge it with the new input, and start again from the first node.

If you want to lose the current state, just change the thread\_id , which will start a new interaction from a blank slate. Any string value is a valid thread\_id ; we'd recommend using UUIDs (or other unique identifiers) as thread IDs.

#### **Edit state**

<span id="page-414-0"></span>Sometimes you might want to update the state of the graph before resuming; this is possible with the update\_state method. You'll usually want to first inspect the current state with get\_state .

Here's what it looks like:

*Python*

```
config = {"configurable": {"thread_id": "1"}}
state = graph.get_state(config)
# something you want to add or replace
update = { }
```

```
graph.update_state(config, update)
```
*JavaScript*

```
const config = "configurable": {"thread_id": "1"}
const state = await graph.getState(config)
// something you want to add or replace
const update = { }
await graph.updateState(config, update)
```
This will create a new checkpoint containing your update. After this, you're ready to resume the graph from this new point. See ["Resume"](#page-411-0) to find out how.

#### **Fork**

<span id="page-415-0"></span>You can also browse the history of all past states the graph has passed through, and any of them can be visited again, for instance, to get an alternative answer. This can be very useful in more creative applications, where each run through the graph is expected to produce different output.

Let's see what it looks like:

#### *Python*

```
config = {"configurable": {"thread_id": "1"}}
history = [
 state for state in
 graph.get_state_history(config)
]
# replay a past state
graph.invoke(None, history[2].config)
```
*JavaScript*

```
const config = "configurable": {"thread_id": "1"}
const history = await Array.fromAsync(graph.getSt
// replay a past state
await graph.invoke(null, history[2].config)
```
Notice how we collect the history into a list/array in both languages; get\_state\_history returns an iterator of states (to allow consuming lazily). The states returned from the history method are sorted with the most recent first and the oldest last.

<span id="page-417-2"></span>The true power of the human-in-the-loop controls comes from mixing them in whatever way suits your application.

### **Multitasking LLMs**

<span id="page-417-1"></span><span id="page-417-0"></span>This section covers the problem of handling concurrent input for LLM applications. This is a particularly relevant problem given that LLMs are quite slow, much more so when producing long outputs or when chained in multistep architectures (like you can do with LangGraph). Even as LLMs become faster, dealing with concurrent inputs will continue to be a challenge, as latency improvements will also unlock the door for more and more complex use cases, in much the same way as even the most productive person still faces the need to prioritize competing demands on their time.

Let's walk through the options.

#### **Refuse concurrent inputs**

<span id="page-418-0"></span>Any input received while processing a previous one is rejected. This is the simplest strategy, but unlikely to cover all needs, as it effectively means handing off concurrency management to the caller.

### **Handle independently**

<span id="page-418-2"></span>Another simple option is to treat any new input as an independent invocation, creating a new thread (a container for remembering state) and producing output in that context. This has the obvious downside of needing to be shown to the user as two separate and unreconcilable invocations, which isn't always possible or desirable. On the other hand, it has the upside of scaling to arbitrarily large sizes, and is something you'll use to some extent in your application almost certainly. For instance, this is how you would think about the problem of getting a chatbot to "chat" with two different users concurrently.

#### **Queue concurrent inputs**

<span id="page-418-1"></span>Any input received while processing a previous one is queued up and handled when the current one is finished. This strategy has some pros:

- It supports receiving an arbitrary number of concurrent requests.
- Because we wait for current input to finish processing, it doesn't matter if the new input arrives almost immediately after we start handling the current input or immediately before we finish; the end result will be the same, as we will finish processing the current input before moving on to the next.

The strategy suffers from a few drawbacks as well:

- It may take a while to process all queued inputs; in fact, the queue may grow unbounded if inputs are produced at a rate faster than processed.
- The inputs may be stale by the time they get processed, given that they are queued before seeing the response to the previous one, and not altered afterwards. This strategy is not appropriate when new inputs depend on previous answers.

#### **Interrupt**

<span id="page-419-0"></span>When a new input is received while another is being processed, abandon processing of the current one and restart the chain

with the new input. This strategy can vary by what is kept of the interrupted run. Here are a few options:

- Keep nothing. The previous input is completely forgotten, as if it had never been sent or processed.
- Keep the last completed step. In a checkpointing app (which stores progress as it moves through the computation), keep the state produced by the last completed step, discard any pending state updates from the currently executing step, and start handling the new input in that context.
- Keep the last completed step, as well as the current inprogress step. Attempt to interrupt the current step while taking care to save any incomplete updates to state that were being produced at the time. This is likely to not generalize beyond the simplest architectures.
- Wait for the current node (but not any subsequent nodes) to finish, then save and interrupt.

This option has some pros compared to queuing concurrent inputs:

- New input is handled as soon as possible, reducing latency and the chance of producing stale outputs.
- For the "keep nothing" variant, the final output doesn't depend on when the new input was received.

But it also has drawbacks:

- Effectively, this strategy is still limited to processing one input at a time; any old input is abandoned when new input is received.
- Keeping partial state updates for the next run requires the state to be designed with that in mind; if not, then your application is likely to end up in an invalid state. For instance, OpenAI chat models require an AI message requesting tool calls to be immediately followed by tool messages with the tool outputs. If your run is interrupted in between, you either defensively clean up the intermediate state or risk being unable to progress further.
- The final outputs produced are very sensitive to when the new input is received; new input will be handled in the context of the (incomplete) progress previously made toward handling the previous input. This can result in brittle or unpredictable outcomes if you don't design accordingly.

#### **Fork and merge**

<span id="page-421-0"></span>Another option is to handle new input in parallel, forking the state of the thread as it is when the new input is received and merging the final states as inputs finish being handled. This option requires designing your state to either be mergeable

without conflicts (e.g., using conflict-free replicated data types [CRDTs] or other conflict resolution algorithms) or having the user manually resolve conflicts before you're able to make sense of the output or send new input in this thread. If either of those two requirements is met, this is likely to be the best option overall. This way, new input is handled in a timely manner, output is independent of time received, and it supports an arbitrary number of concurrent runs.

<span id="page-422-0"></span>Some of these strategies are implemented in LangGraph Platform, which will be covered in [Chapter](#page-424-0) 9.

### Summary

In this chapter, we returned to the main trade-off you face when building LLM applications: agency versus reliability. We learned that there are strategies to partially beat the odds and get more reliability without sacrificing agency, and vice versa.

We started by covering structured outputs, which can improve the predictability of LLM-generated text. Next, we discussed emitting streaming/intermediate output from your application, which can make high latency (an inevitable side effect of agency currently) applications pleasant to use.

We also walked through a variety of human-in-the-loop controls —that is, techniques to give back some oversight to the end user of your LLM application—which can often make the difference in making high-agency architectures reliable. Finally, we talked about the problem of handling concurrent input to your application, a particularly salient problem for LLM apps given their high latency.

In the next chapter, you'll learn how to deploy your AI application into production.

<span id="page-423-0"></span>In finance, the *efficient frontier* in portfolio optimization; in economics, a *productionpossibility frontier*; in engineering, the *Pareto front*. **[1](#page-386-1)**

# <span id="page-424-0"></span>Chapter 9. Deployment: Launching Your AI Application into Production

So far, we've explored the key concepts, ideas, and tools to help you build the core functionality of your AI application. You've learned how to utilize LangChain and LangGraph to generate LLM outputs, index and retrieve data, and enable memory and agency.

But your application is limited to your local environment, so external users can't access its features yet.

In this chapter, you'll learn the best practices for deploying your AI application into production. We'll also explore various tools to debug, collaborate, test, and monitor your LLM applications.

Let's get started.

## Prerequisites

<span id="page-424-1"></span>In order to effectively deploy your AI application, you need to utilize various services to host your application, store and retrieve data, and monitor your application. In the deployment example in this chapter, we will incorporate the following services:

*Vector store*

Supabase

*Monitoring and debugging*

LangSmith

*Backend API*

LangGraph Platform

We will dive deeper into each of these components and services and see how to adapt them for your use case. But first, let's install necessary dependencies and set up the environment variables.

If you'd like to follow the [example, fork](https://oreil.ly/brqVm) this LangChain template to your GitHub account. This repository contains the full logic of a retrieval agent-based AI application.

### **Install Dependencies**

<span id="page-425-0"></span>First, follow the instructions in the *[README.md](https://oreil.ly/N5eqe)* file to install the project dependencies.

If you're not using the template, you can install the dependencies individually from the respective *pyproject.toml* or *package.json* files.

Second, create a *.env* file and store the following variables:

```
OPENAI_API_KEY=
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
# for tracing
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.c
LANGCHAIN_API_KEY=
```
Next, we'll walk through the process of retrieving the values for each of these variables.

### **Large Language Model**

<span id="page-426-0"></span>The LLM is responsible for generating the output based on a given query. LangChain provides access to popular LLM providers, including OpenAI, Anthropic, Google, and Cohere. <span id="page-427-1"></span>In this deployment example, we'll utilize OpenAI by retrieving the API [keys](https://oreil.ly/MIpY5), as shown in [Figure](#page-427-0) 9-1. Once you've retrieved your API keys, input the value as OPENAI\_API\_KEY in your *.env* file.

<span id="page-427-0"></span>![](_page_427_Picture_1.jpeg)

Figure 9-1. OpenAI API keys dashboard

### **Vector Store**

<span id="page-427-2"></span>As discussed in previous chapters, a vector store is a special database responsible for storing and managing vector representations of your data—in other words, embeddings. A vector store enables similarity search and context retrieval to help the LLM generate accurate answers based on the user's query.

<span id="page-428-0"></span>For our deployment, we'll use Supabase—a PostgreSQL database—as the vector store. Supabase utilizes the pgvector extension to store embeddings and query vectors for similarity search.

If you haven't yet done it, create a [Supabase](https://oreil.ly/CXDsx) account. Once you've created an account, click "New project" on the dashboard page. Follow the steps and save the database password after creating it, as shown in [Figure](#page-429-0) 9-2.

<span id="page-429-0"></span>

| Create a new project | Your project will have its own dedicated instance and full Postgres database.<br>An API will be set up so you can easily interact with your new database. |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Organization         | MVP building DB<br>V                                                                                                                                      |
| Project name         | Project name                                                                                                                                              |
| Database Password    | Type in a strong password<br>This is the password to your postgres database, so it must be<br>strong and hard to guess. Generate a password               |
| Region               | East US (North Virginia)<br>V<br>Select the region closest to your users for the best performance.                                                        |
| SECURITY OPTIONS >   |                                                                                                                                                           |
| Cancel               | You can rename your project later Create new project                                                                                                      |

Figure 9-2. Supabase project creation dashboard

Once your Supabase project is created, navigate to the Project Settings tab and select API under Configuration. Under this new tab, you will see Project URL and Project API keys.

In your *.env* file, copy and paste the Project URL as the value to SUPABASE\_URL and the service\_role secret API key as the value to SUPABASE\_SERVICE\_ROLE\_KEY .

Navigate to the SQL editor in the Supabase menu and run the following SQL scripts. First, let's enable pgvector :

## Enable the pgvector extension to work with emb create extension vector;

Now create a table called documents to store vectors of your data:

```
## Create a table to store your documents
create table documents (
 id bigserial primary key,
 content text, -- corresponds to Document.pageCo
 metadata jsonb, -- corresponds to Document.meta
 embedding vector(1536) -- 1536 works for OpenAI
);
```
You should now see the documents table in the Supabase database.

Now you can create a script to generate the embeddings of your data, store them, and query from the database. Open the

Supabase SQL editor again and run the following script:

```
## Create a function to search for documents
create function match_documents (
 query_embedding vector(1536),
 match_count int DEFAULT null,
 filter jsonb DEFAULT '{}'
) returns table (
 id bigint,
 content text,
 metadata jsonb,
 embedding jsonb,
 similarity float
)
language plpgsql
as $$
#variable_conflict use_column
begin
 return query
 select
 id,
 content,
 metadata,
 (embedding::text)::jsonb as embedding,
 1 - (documents.embedding <=> query_embedding)
 from documents
 where metadata @> filter
```

```
 order by documents.embedding <=> query_embeddin
 limit match_count;
end;
$$;
```
The match\_documents database function takes a query\_embedding vector and compares it to embeddings in the documents table using cosine similarity. It calculates a similarity score for each document (1 -

```
( documents.embedding <=> query_embedding )), then
returns the most similar matches. The results are:
```
- 1. Filtered first by the metadata criteria specified in the filter argument (using JSON containment @>).
- 2. Ordered by similarity score (highest first).
- 3. Limited to the number of matches specified in match\_count .

Once the vector similarity function is generated, you can use Supabase as a vector store by importing the class and providing the necessary parameters. Here's an example of how it works:

*Python*

import os

```
from langchain_community.vectorstores import Supa
from langchain_openai import OpenAIEmbeddings
from supabase.client import Client, create_client
```

```
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_SERVICE_R
supabase: Client = create_client(supabase_url, su
```

```
embeddings = OpenAIEmbeddings()
```

```
## Assuming you've already generated embeddings o
```

```
vector_store = SupabaseVectorStore(
 embedding=embeddings,
 client=supabase,
 table_name="documents",
 query_name="match_documents",
)
## Test that similarity search is working
query = "What is this document about?"
```

```
matched_docs = vector_store.similarity_search(que
```

```
print(matched_docs[0].page_content)
```
#### *JavaScript*

```
import {
 SupabaseVectorStore
} from "@langchain/community/vectorstores/supabas
import { OpenAIEmbeddings } from "@langchain/open
import { createClient } from "@supabase/supabase-
const embeddings = new OpenAIEmbeddings();
const supabaseClient = createClient(
 process.env.SUPABASE_URL,
 process.env.SUPABASE_SERVICE_ROLE_KEY
);
const vectorStore = new SupabaseVectorStore(embed
 client: supabaseClient,
 tableName: "documents",
 queryName: "match_documents",
});
// Example documents structure of your data
const document1: Document = {
 pageContent: "The powerhouse of the cell is the
```

```
 metadata: { source: "https://example.com" },
};
const document2: Document = {
 pageContent: "Buildings are made out of brick",
 metadata: { source: "https://example.com" },
};
const documents = [document1, document2]
//Embed and store the data in the database
await vectorStore.addDocuments(documents, { ids:
// Query the Vector Store
const filter = { source: "https://example.com" };
const similaritySearchResults = await vectorStore
 "biology",
 2,
 filter
);
for (const doc of similaritySearchResults) {
 console.log(`* ${doc.pageContent} [${JSON.strin
}
```
*The output:*

The powerhouse of the cell is the mitochondria [{

You can review the full logic of the Supabase vector store implementation in the Github LangChain template mentioned previously.

### **Backend API**

<span id="page-436-0"></span>As discussed in previous chapters, LangGraph is a low-level open source framework used to build complex agentic systems powered by LLMs. LangGraph enables fine-grained control over the flow and state of your application, built-in persistence, and advanced human-in-the-loop and memory features. [Figure](#page-437-0) 9-3 illustrates LangGraph's control flow.

<span id="page-437-0"></span>![](_page_437_Figure_0.jpeg)

Figure 9-3. Example of LangGraph API control flow

<span id="page-437-1"></span>To deploy an AI application that utilizes LangGraph, we will use LangGraph Platform. LangGraph Platform is a managed service for deploying and hosting LangGraph agents at scale.

As your agentic use case gains traction, uneven task distribution among agents can overload the system, leading to downtime. LangGraph Platform manages horizontally scaling task queues, servers, and a robust Postgres checkpointer to handle many concurrent users and efficiently store large states and threads. This ensures fault-tolerant scalability.

LangGraph Platform is designed to support real-world interaction patterns. In addition to streaming and human-inthe-loop features, LangGraph Platform enables the following:

- Double texting to handle new user inputs on ongoing graph threads
- Asynchronous background jobs for long-running tasks
- Cron jobs for running common tasks on a schedule

LangGraph Platform also provides an integrated solution for collaborating on, deploying, and monitoring agentic AI applications. It includes [LangGraph](https://oreil.ly/2Now-) Studio—a visual playground for debugging, editing, and testing agents. LangGraph Studio also enables you to share your LangGraph agent with team members for collaborative feedback and rapid iteration, as [Figure](#page-439-0) 9-4 shows.

<span id="page-439-0"></span>![](_page_439_Figure_0.jpeg)

Figure 9-4. Snapshot of LangGraph Studio UI

Additionally, LangGraph Platform simplifies agentic deployment by enabling one-click submissions.

### **Create a LangSmith Account**

<span id="page-439-1"></span>LangSmith is an all-in-one developer platform that enables you to debug, collaborate, test, and monitor your LLM applications.

LangGraph Platform is seamlessly integrated with LangSmith and is accessible from within the LangSmith UI.

To deploy your application on LangGraph Platform, you need to create a [LangSmith](https://oreil.ly/2WVCn) account. Once you're logged in to the dashboard, navigate to the Settings page, then scroll to the API Keys section and click Create API Key. You should see a UI similar to [Figure](#page-440-0) 9-5.

<span id="page-440-0"></span>

| Create an API Key                                               | ve been converted |
|-----------------------------------------------------------------|-------------------|
| Description                                                     |                   |
| Description                                                     |                   |
| Key Type                                                        |                   |
| · Personal Access Token                                         | Created At        |
| Used for authenticating with the API as an individual           |                   |
| user.<br>Service Key                                            | 5/1/2024, 1:07 :  |
| Tied to a service principal for automation and CI<br>workflows. |                   |
| Create API Key                                                  |                   |

Figure 9-5. Create LangSmith API Key UI

Copy the API Key value as your LANGCHAIN\_API\_KEY in your *.env* file.

<span id="page-441-1"></span>Navigate to "Usage and billing" and set up your billing details. Then click the "Plans and Billings" tab and the "Upgrade to Plus" button to get instructions on transitioning to a LangSmith Plus plan, which will enable LangGraph Platform usage. If you'd prefer to use a free self-hosted deployment, you can follow the [instructions](https://oreil.ly/TBgSQ) here. Please note that this option requires management of the infrastructure, including setting up and maintaining required databases and Redis instances.

## Understanding the LangGraph Platform API

Before deploying your AI application on LangGraph Platform, it's important to understand how each component of the LangGraph API works. These components can generally be split into data models and features.

### **Data Models**

<span id="page-441-0"></span>The LangGraph Platform API consists of a few core data models:

- Assistants
- Threads
- Runs
- Cron jobs

#### **Assistants**

<span id="page-442-0"></span>An *assistant* is a configured instance of a CompiledGraph . It abstracts the cognitive architecture of the graph and contains instance-specific configuration and metadata. Multiple assistants can reference the same graph but can contain different configuration and metadata—which may differentiate the behavior of the assistants. An assistant (that is, the graph) is invoked as part of a run.

The LangGraph Platform API provides several endpoints for creating and managing assistants.

#### **Threads**

<span id="page-442-1"></span>A *thread* contains the accumulated state of a group of runs. If a run is executed on a thread, then the state of the underlying graph of the assistant will be persisted to the thread. A thread's current and historical state can be retrieved. To persist state, a thread must be created prior to executing a run. The state of a thread at a particular point in time is called a *checkpoint*.

The LangGraph Platform API provides several endpoints for creating and managing threads and thread state.

#### **Runs**

<span id="page-443-2"></span>A *run* is an invocation of an assistant. Each run may have its own input, configuration, and metadata—which may affect the execution and output of the underlying graph. A run can optionally be executed on a thread.

The LangGraph Platform API provides several endpoints for creating and managing runs.

### **Cron jobs**

<span id="page-443-0"></span>LangGraph Platform supports *cron jobs*, which enable graphs to be run on a user-defined schedule. The user specifies a schedule, an assistant, and an input. Then LangGraph Platform creates a new thread with the specified assistant and sends the specified input to that thread.

### **Features**

<span id="page-443-1"></span>The LangGraph Platform API also offers several features to support complex agent architectures, including the following:

- Streaming
- Human-in-the-loop
- Double texting
- Stateless runs
- Webhooks

#### **Streaming**

<span id="page-444-0"></span>Streaming is critical for ensuring that LLM applications feel responsive to end users. When creating a streaming run, the streaming mode determines what data is streamed back to the API client. The LangGraph Platform API supports five streaming modes:

#### *Values*

Stream the full state of the graph after each super-step is executed.

#### *Messages*

Stream complete messages (at the end of node execution) as well as tokens for any messages generated inside a node. This mode is primarily meant for powering chat applications. This is only an option if your graph contains a messages key.

#### *Updates*

Stream updates to the state of the graph after each node is executed.

#### *Events*

Stream all events (including the state of the graph) that occur during graph execution. This can be used to do token-by-token streaming for LLMs.

#### *Debug*

Stream debug events throughout graph execution.

#### **Human-in-the-loop**

<span id="page-445-0"></span>If left to run autonomously, a complex agent can take unintended actions, leading to catastrophic application outcomes. To prevent this, human intervention is recommended, especially at checkpoints where application logic involves invoking certain tools or accessing specific documents. LangGraph Platform enables you to insert this human-in-the-loop behavior to ensure your graph doesn't have undesired outcomes.

### **Double texting**

<span id="page-446-0"></span>Graph execution may take longer than expected, and often users may send one message and then, before the graph has finished running, send a second message. This is known as *double texting*. For example, a user might notice a typo in their original request and edit the prompt and resend it. In such scenarios, it's important to prevent your graphs from behaving in unexpected ways and ensure a smooth user experience. LangGraph Platform provides four different solutions to handle double texting:

#### *Reject*

This rejects any follow-up runs and does not allow double texting.

#### *Enqueue*

This option continues the first run until it completes the whole run, then sends the new input as a separate run.

#### *Interrupt*

This option interrupts the current execution but saves all the work done up until that point. It then inserts the user input and continues from there. If you enable this option, your graph should be able to handle weird edge cases that may arise.

#### *Rollback*

This option rolls back all work done up until that point. It then sends the user input in—as if it just followed the original run input.

#### **Stateless runs**

<span id="page-447-0"></span>All runs use the built-in checkpointer to store checkpoints for runs. However, it can often be useful to just kick off a run without worrying about explicitly creating a thread and keeping those checkpointers around. *Stateless* runs allow you to do this by exposing an endpoint that does these things:

- Takes in user input
- Creates a thread
- Runs the agent, but skips all checkpointing steps
- Cleans up the thread afterwards

Stateless runs are retried while keeping memory intact. However, in the case of stateless background runs, if the task worker dies halfway, the entire run will be retried from scratch.

### **Webhooks**

<span id="page-448-2"></span>LangGraph Platform also supports completion *webhooks*. A webhook URL is provided, which notifies your application whenever a run completes.

# <span id="page-448-1"></span>Deploying Your AI Application on LangGraph Platform

At this point, you have created accounts for the recommended services, filled in your *.env* file with values of all necessary environment variables, and completed the core logic for your AI application. Next, we will take the necessary steps to effectively deploy your application.

### **Create a LangGraph API Config**

<span id="page-448-0"></span>Prior to deployment, you need to configure your application with a LangGraph API configuration file called *[langgraph.json](https://oreil.ly/aVDhd)*. Here's an example of what the file looks like in a Python repository:

*Python*

```
 "dependencies": ["./my_agent"],
 "graphs": {
 "agent": "./my_agent/agent.py:graph"
 },
 "env": ".env"
}
```
And here's an example repository structure:

![](_page_449_Figure_2.jpeg)

Note that the *langgraph.json* file is placed on the same level or higher than the files that contain compiled graphs and associated dependencies.

In addition, the dependencies are specified in a *requirements.txt* file. But they can also be specified in *pyproject.toml*, *setup.py*, or *package.json* files.

Here's what each of the properties mean:

*Dependencies*

Array of dependencies for LangGraph Platform API server

*Graphs*

Mapping from graph ID to path where the compiled graph or a function that makes a graph is defined

*Env*

Path to your *.env* file or a mapping from environment variable to its value (you can learn more about configurations for the langgraph.json file [here](https://oreil.ly/bPA0W))

### **Test Your LangGraph App Locally**

<span id="page-450-0"></span>Testing your application locally ensures that there are no errors or dependency conflicts prior to deployment. To do this, we will utilize the LangGraph CLI, which includes commands to run a local development server with hot reloading and debugging capabilities.

For Python, install the Python langgraph-cli package (note: this requires Python 3.11 or higher):

pip install -U "langgraph-cli[inmem]"

Or for JavaScript, install the package as follows:

npm i @langchain/langgraph-cli

Once the CLI is installed, run the following command to start the API:

langgraph dev

This will start up the LangGraph API server locally. If this runs successfully, you should see something like this:

```
Ready!
API: http://localhost:2024
Docs: http://localhost:2024/docs
```
The LangGraph Platform API reference is available with each deployment at the */docs* URL path (*http://localhost:2024/docs*).

The easiest way to interact with your local API server is to use the auto-launched LangGraph Studio UI. Alternatively, you can interact with the local API server using cURL, as seen in this example:

```
curl --request POST \
 --url http://localhost:8123/runs/stream \
 --header 'Content-Type: application/json' \
 --data '{
 "assistant_id": "agent",
 "input": {
 "messages": [
 {
 "role": "user",
 "content": "How are you?"
 }
 ]
 },
 "metadata": {},
 "config": {
 "configurable": {}
 },
 "multitask_strategy": "reject",
```

```
 "stream_mode": [
 "values"
 ]
}'
```
If you receive a valid response, your application is functioning well. Next, we can interact with the server using the LangGraph SDK.

Here's an example both initializing the SDK client and invoking the graph:

*Python*

```
from langgraph_sdk import get_client
# only pass the url argument to get_client() if y
# when calling langgraph up
client = get_client()
# Using the graph deployed with the name "agent"
assistant_id = "agent"
thread = await client.threads.create()
input = {"messages": [{"role": "user", "content"
async for chunk in client.runs.stream(
```

```
 thread["thread_id"],
 assistant_id,
 input=input,
 stream_mode="updates",
):
 print(f"Receiving new event of type: {chunk.e
 print(chunk.data)
 print("\n\n")
```
*JavaScript*

{

```
import { Client } from "@langchain/langgraph-sdk"
// only set the apiUrl if you changed the default
const client = new Client();
// Using the graph deployed with the name "agent"
const assistantId = "agent";
const thread = await client.threads.create();
const input = {
 messages: [{ "role": "user", "content": "what's
}
const streamResponse = client.runs.stream(
 thread["thread_id"],
 assistantId,
```

```
 {
 input: input,
 streamMode: "updates",
 }
);
for await (const chunk of streamResponse) {
 console.log(`Receiving new event of type: ${chu
 console.log(chunk.data);
 console.log("\n\n");
}
```
<span id="page-455-1"></span>If your LangGraph application is working correctly, you should see your graph output displayed in the console.

### **Deploy from the LangSmith UI**

<span id="page-455-0"></span>At this point, you should have completed all prerequisite steps and your LangGraph API should be working locally. Your next step is to navigate to your LangSmith dashboard panel and click the Deployments tab. You should see a UI similar to [Figure](#page-456-0) 9-6.

<span id="page-456-0"></span>![](_page_456_Picture_0.jpeg)

Figure 9-6. LangGraph Platform deployment UI page

Next, click the New Deployment button in the top right corner of the page.

#### **NOTE**

If you don't see a page with the New Deployment button, it's likely that you haven't yet upgraded to a LangSmith Plus plan according to the instructions in the "Usage and billing" setting.

You should now see a page of three form fields to complete.

#### **Deployment details**

- 1. Select "Import with GitHub" and follow the GitHub OAuth workflow to install and authorize LangChain's hostedlangserve GitHub app to access the selected repositories. After installation is complete, return to the Create New Deployment panel and select the GitHub repository to deploy from the drop-down menu.
- 2. Specify a name for the deployment and the full path to the LangGraph API config file, including the filename. For example, if the file *langgraph.json* is in the root of the repository, simply specify *langgraph.json*.
- 3. Specify the desired git reference (branch name) of your repository to deploy.

#### **Development type**

Select Production from the dropdown. This will enable a production deployment that can serve up to 500 requests/second and is provisioned with highly available storage and automatic backups.

#### **Environment variables**

<span id="page-457-0"></span>Provide the properties and values in your *.env* here. For sensitive values, like your OPENAI\_API\_KEY , make sure to tick the Secret box before inputting the value.

Once you've completed the fields, click the button to submit the deployment and wait for a few seconds for the build to complete. You should see a new revision associated with the deployment.

Since LangGraph Platform is integrated within LangSmith, you can gain deeper visibility into your app and track and monitor usage, errors, performance, and costs in production too. [Figure](#page-458-0) 9-7 shows a visual Trace Count summary chart showing successful, pending, and error traces over a given time period. You can also view all monitoring info for your server by clicking the "All charts" button.

<span id="page-458-0"></span>![](_page_458_Figure_2.jpeg)

Figure 9-7. Deployment revisions and trace count on dashboard

To view the build and deployment logs, select the desired revision from the Revisions tab, then choose the Deploy tab to view the full deployment logs history. You can also adjust the date and time range.

To create a new deployment, click the New Revision button in the navigation bar. Fill out the necessary fields, including the LangGraph API config file path, git reference, and environment variables, as done previously.

<span id="page-459-0"></span>Finally, you can access the API documentation by clicking the API docs link, which should display a similar page to the UI shown in [Figure](#page-460-0) 9-8.

<span id="page-460-0"></span>

| ant               | GET   |                     |      |                                                                                               |       |          |        |   |
|-------------------|-------|---------------------|------|-----------------------------------------------------------------------------------------------|-------|----------|--------|---|
| istant            | DEL   | SERVER              |      |                                                                                               |       |          |        |   |
| stant             | PATCH |                     |      | https://chat-langchain-langgraph-ci-d4a7041e91b655bab3bbd4fe1472e0cd.default.us.langgraph.app |       |          |        |   |
| ant Graph         | CET   | API KEY (X-API-KEY) |      |                                                                                               |       |          |        |   |
| ant Subgraphs     | CET   | Token               |      |                                                                                               |       |          |        | @ |
| ant Subgraphs by  | GET   |                     |      |                                                                                               |       |          |        |   |
| 0                 |       | CLIENT LIBRARIES    |      |                                                                                               |       |          |        |   |
| ant Schemas       | GET   | >_ Shell            | Ruby | @ Node.js                                                                                     | @ PHP | @ Python | - More |   |
| ant Versions      | POST  | cURL Shell          |      |                                                                                               |       |          |        |   |
| Assistant Version | POST  |                     |      |                                                                                               |       |          |        |   |
|                   |       |                     |      |                                                                                               |       |          |        |   |
| 3                 |       |                     |      |                                                                                               |       |          |        |   |
| Runs              |       |                     |      |                                                                                               |       |          |        |   |
| erprise-only)     |       | Assistants          |      |                                                                                               |       |          |        |   |

|     | POST /assistants                                     |
|-----|------------------------------------------------------|
|     | POST /assistants/search                              |
| GET | /assistants/{assistant_id}                           |
|     | DELETE /assistants/{assistant_id}                    |
|     | PATCH /assistants/{assistant_id}                     |
|     | GET /assistants/{assistant_id}/graph                 |
|     | GET /assistants/{assistant_id}/subgraphs             |
|     | GET /assistants/{assistant_id}/subgraphs/{namespace} |
|     | GET /assistants/{assistant_id}/schemas               |
|     | POST /assistants/{assistant_id}/versions             |
|     | POST /assistants/{assistant_id}/latest               |
|     |                                                      |

<span id="page-460-1"></span>Figure 9-8. LangGraph API documentation

### **Launch LangGraph Studio**

LangGraph Studio provides a specialized agent IDE for visualizing, interacting with, and debugging complex agentic applications. It enables developers to modify an agent result (or the logic underlying a specific node) halfway through the agent's trajectory. This creates an iterative process by letting you interact with and manipulate the state at that point in time.

Once you've deployed your AI application, click the LangGraph Studio button at the top righthand corner of the deployment dashboard, as you can see in [Figure](#page-461-0) 9-9.

<span id="page-461-0"></span>

| 27 ht-dependable-prize=85                    |                  |            |                                                                                                                                         | + New Revision |              |
|----------------------------------------------|------------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------|--------------|
|                                              |                  |            | Read ou Languagh Cloud documentation and guick start of the combridge only of decirement is allowed per language and on increase quasa. |                |              |
| TRACING PROJECT<br>28 ht-dependable-prize-85 |                  | REPOSITORY | API UN<br>O mayoearlanggraph warmpe O https://1r/decombing/2015072030322ed.default.us.inggrach.pp 0 /occ 19/09/2024,114110              | AN DOCS        | LAST UPDATED |
| DEPLOYMENT TYPE<br>Production                | SHAREABLE<br>Yes |            |                                                                                                                                         |                |              |

Figure 9-9. LangGraph deployment UI

After clicking the button, you should see the LangGraph Studio UI (for example, see [Figure](#page-462-0) 9-10).

<span id="page-462-0"></span>![](_page_462_Figure_0.jpeg)

Figure 9-10. LangGraph Studio UI

To invoke a graph and start a new run, follow these steps:

- 1. Select a graph from the drop-down menu in the top left corner of the lefthand pane. The graph in [Figure](#page-462-0) 9-10 is called *agent*.
- 2. In the Input section, click the "+ Message" icon and input a *human* message, but the input will vary depending on your application state definitions.
- 3. Click Submit to invoke the selected graph.
- 4. View the output of the invocation in the right-hand pane.

The output of your invoked graph should look like [Figure](#page-463-0) 9-11.

<span id="page-463-0"></span>![](_page_463_Figure_3.jpeg)

Figure 9-11. LangGraph Studio invocation output

In addition to invocation, LangGraph Studio enables you to change run configurations, create and edit threads, interrupt your graphs, edit graph code, and enable human-in-the-loop intervention. You can read the full [guide](https://oreil.ly/xUU37) to learn more.

#### **NOTE**

LangGraph Studio is also available as a desktop application (for Apple silicon), which enables you to test your AI application locally.

If you've followed the installation guide in the GitHub template and successfully deployed your AI application, it's now live for production use. But before you share to external users or use the backend API in existing applications, it's important to be aware of key security considerations.

## <span id="page-464-0"></span>Security

<span id="page-464-1"></span>Although AI applications are powerful, they are vulnerable to several security risks that may lead to data corruption or loss, unauthorized access to confidential information, and compromised performance. These risks may carry adverse legal, reputational, and financial consequences.

<span id="page-464-2"></span>To mitigate these risks, it's recommended to follow general application security best practices, including the following:

#### *Limit permissions*

<span id="page-464-3"></span>Scope permissions specific to the application's need. Granting broad or excessive permissions can introduce significant security vulnerabilities. To avoid such vulnerabilities, consider using read-only credentials, disallowing access to sensitive resources, and using sandboxing techniques (such as running inside a container).

#### *Anticipate potential misuse*

<span id="page-465-1"></span>Always assume that any system access or credentials may be used in any way allowed by the permissions they are assigned. For example, if a pair of database credentials allows deleting data, it's safest to assume that any LLM able to use those credentials may in fact delete data.

#### *Defense in depth*

<span id="page-465-2"></span><span id="page-465-0"></span>It's often best to combine multiple layered security approaches rather than rely on any single layer of defense to ensure security. For example, use both read-only permissions and sandboxing to ensure that LLMs are only able to access data that is explicitly meant for them to use.

Here are three example scenarios implementing these mitigation strategies:

*File access*

<span id="page-466-3"></span><span id="page-466-2"></span>A user may ask an agent with access to the file system to delete files that should not be deleted or read the content of files that contain sensitive information. To mitigate this risk, limit the agent to only use a specific directory and only allow it to read or write files that are safe to read or write. Consider further sandboxing the agent by running it in a container.

#### *API access*

<span id="page-466-0"></span>A user may ask an agent with write access to an external API to write malicious data to the API or delete data from that API. To mitigate, give the agent read-only API keys, or limit it to only use endpoints that are already resistant to such misuse.

#### *Database access*

<span id="page-466-1"></span>A user may ask an agent with access to a database to drop a table or mutate the schema. To mitigate, scope the credentials to only the tables that the agent needs to access and consider issuing read-only credentials.

In addition to the preceding security measures, you can take further steps to mitigate abuse of your AI application. Due to the dependency of external LLM API providers (such as OpenAI), there is a direct cost associated with running your

application. To prevent abuse of your API and exponential costs, you can implement the following:

#### *Account creation verification*

<span id="page-467-0"></span>This typically includes a form of authentication login, such as email or phone number verification.

#### *Rate limiting*

<span id="page-467-2"></span>Implement a rate-limiting mechanism in the middleware of the application to prevent users from making too many requests in a short period of time. This should check the number of requests a user has made in the last X minutes and "timeout" or "ban" the user if the abuse is severe.

#### *Implement prompt injection guardrails*

<span id="page-467-1"></span>*Prompt injection* occurs when a malicious user injects a prompt in an attempt to trick the LLM to act in unintended ways. This usually includes extracting confidential data or generating unrelated outputs. To mitigate this, you should ensure the LLM has proper permission scoping and that the application's prompts are specific and strict to the desired outcomes.

## Summary

Throughout this chapter, you've learned the best practices for deploying your AI application and enabling users to interact with it. We explored recommended services to handle various key components of the application in production, including the LLM, vector store, and backend API.

We also discussed using LangGraph Platform as a managed service for deploying and hosting LangGraph agents at scale in conjunction with LangGraph Studio—to visualize, interact with, and debug your application.

Finally, we briefly explored various security best practices to mitigate data breach risks often associated with AI applications.

In [Chapter](#page-469-0) 10, you'll learn how to effectively evaluate, monitor, benchmark, and improve the performance of your AI application.

# <span id="page-469-0"></span>Chapter 10. Testing: Evaluation, Monitoring, and Continuous Improvement

In [Chapter](#page-424-0) 9, you learned how to deploy your AI application into production and utilize LangGraph Platform to host and debug your app.

<span id="page-469-1"></span>Although your app can respond to user inputs and execute complex tasks, its underlying LLM is nondeterministic and prone to hallucination. As discussed in previous chapters, LLMs can generate inaccurate and outdated outputs due to a variety of reasons including the prompt, format of user's input, and retrieved context. In addition, harmful or misleading LLM outputs can significantly damage a company's brand and customer loyalty.

To combat this tendency toward hallucination, you need to build an efficient system to test, evaluate, monitor, and continuously improve your LLM applications' performance. This robust testing process will enable you to quickly debug and fix AI-related issues before and after your app is in production.

In this chapter, you'll learn how to build an iterative testing system across the key stages of the LLM app development lifecycle and maintain high performance of your application.

# Testing Techniques Across the LLM App Development Cycle

<span id="page-470-0"></span>Before we construct the testing system, let's briefly review how testing can be applied across the three key stages of LLM app development:

#### *Design*

In this stage, LLM tests are applied directly to your application. These tests can be assertions executed at runtime that feed failures back to the LLM for selfcorrection. The purpose of testing at this stage is error handling within your app before it affects users.

#### *Preproduction*

In this stage, tests are run right before deployment into production. The purpose of testing at this stage is to catch and fix any regressions before the app is released to real users.

#### *Production*

<span id="page-471-1"></span>In this stage, tests are run while your application is in production to help monitor and catch errors affecting real users. The purpose is to identify issues and feed them back into the design or preproduction phases.

The combination of testing across these stages creates a continuous improvement cycle where these steps are repeated: design, test, deploy, monitor, fix, and redesign. See [Figure](#page-471-0) 10-1.

<span id="page-471-0"></span>![](_page_471_Figure_3.jpeg)

Figure 10-1. The three key stages of the LLM app development cycle

In essence, this cycle helps you to identify and fix production issues in an efficient and quick manner.

Let's dive deeper into testing techniques across each of these stages.

## The Design Stage: Self-Corrective RAG

<span id="page-472-0"></span>As discussed previously, your application can incorporate error handling at runtime that feeds errors to the LLM for selfcorrection. Let's explore a RAG use case using LangGraph as the framework to orchestrate error handling.

<span id="page-472-1"></span>Basic RAG-driven AI applications are prone to hallucination due to inaccurate or incomplete retrieval of relevant context to generate outputs. But you can utilize an LLM to grade retrieval relevance and fix hallucination issues.

<span id="page-472-2"></span>LangGraph enables you to effectively implement the control flow of this process, as shown in [Figure](#page-473-0) 10-2.

<span id="page-473-0"></span>![](_page_473_Figure_0.jpeg)

Figure 10-2. Self-corrective RAG control flow

The control flow steps are as follows:

- 1. In the routing step, each question is routed to the relevant retrieval method, that is, vector store and web search.
- 2. If, for example, the question is routed to a vector store for retrieval, the LLM in the control flow will retrieve and grade the documents for relevancy.
- 3. If the document is relevant, the LLM proceeds to generate an answer.
- 4. The LLM will check the answer for hallucinations and only proceed to display the answer to the user if the output is accurate and relevant.

5. As a fallback, if the retrieved document is irrelevant or the generated answer doesn't answer the user's question, the flow utilizes web search to retrieve relevant information as context.

<span id="page-474-0"></span>This process enables your app to iteratively generate answers, self-correct errors and hallucinations, and improve the quality of outputs.

Let's run through an example code implementation of this control flow. First, download the required packages and initialize relevant API keys. For these examples, you'll need to set your OpenAI and LangSmith API keys as environment variables.

First, we'll create an index of three blog posts:

*Python*

from langchain.text\_splitter import RecursiveChar from langchain\_community.document\_loaders import from langchain\_community.vectorstores import InMe from langchain\_openai import OpenAIEmbeddings from langchain\_core.prompts import ChatPromptTemp from pydantic import BaseModel, Field from langchain\_openai import ChatOpenAI

```
 
# --- Create an index of documents ---

urls = [
 "https://blog.langchain.dev/top-5-langgraph-a
 "https://blog.langchain.dev/langchain-state-o
 "https://blog.langchain.dev/introducing-ambie
]

docs = [WebBaseLoader(url).load() for url in urls
docs_list = [item for sublist in docs for item in

text_splitter = RecursiveCharacterTextSplitter.fr
 chunk_size=250, chunk_overlap=0
)
doc_splits = text_splitter.split_documents(docs_l

# Add to vectorDB
vectorstore = InMemoryVectorStore.from_documents(
 documents=doc_splits,
 embedding=OpenAIEmbeddings(),
)
retriever = vectorstore.as_retriever()

# Retrieve the relevant documents
results = retriever.invoke(
 "What are 2 LangGraph agents used in producti
```

```
print("Results: \n"
                   , results)
```
#### *JavaScript*

```
import { RecursiveCharacterTextSplitter } from '@
import {
 CheerioWebBaseLoader
} from "@langchain/community/document_loaders/web
import {
 InMemoryVectorStore
} from '@langchain/community/vectorstores/in_memo
import { OpenAIEmbeddings } from '@langchain/open
import { ChatPromptTemplate } from '@langchain/co
import { z } from 'zod';
import { ChatOpenAI } from '@langchain/openai';

const urls = [
 'https://blog.langchain.dev/top-5-langgraph-age
 'https://blog.langchain.dev/langchain-state-of-
 'https://blog.langchain.dev/introducing-ambient
];

// Load documents from URLs
const loadDocs = async (urls) => {
 const docs = [];
  for (const url of urls) {
```

```
 for (const url of urls) {
 const loader = new CheerioWebBaseLoader(url);
 const loadedDocs = await loader.load();
 docs.push(...loadedDocs);
 }
 return docs;
};

const docsList = await loadDocs(urls);

// Initialize the text splitter
const textSplitter = new RecursiveCharacterTextSp
 chunkSize: 250,
 chunkOverlap: 0,
});

// Split the documents into smaller chunks
const docSplits = textSplitter.splitDocuments(doc

// Add to vector database
const vectorstore = await InMemoryVectorStore.fro
 docSplits,
 new OpenAIEmbeddings()
);

// The `retriever` object can now be used for que
const retriever = vectorstore.asRetriever();

const question = 'What are 2 LangGraph agents use
```

```
const question = What are 2 LangGraph agents use

const docs = retriever.invoke(question);

console.log('Retrieved documents: \n', docs[0].pa
```
As discussed previously, the LLM will grade the relevancy of the retrieved documents from the index. We can construct this instruction in a system prompt:

#### *Python*

```
### Retrieval Grader
from langchain_core.prompts import ChatPromptTemp
from langchain_core.pydantic_v1 import BaseModel,
from langchain_openai import ChatOpenAI
# Data model
class GradeDocuments(BaseModel):
 """Binary score for relevance check on retrie
 binary_score: str = Field(
 description="Documents are relevant to th
 )
```

```
# LLM with function call
llm = ChatOpenAI(model="gpt-3.5-turbo"
                                    , temperatu
structured_llm_grader = llm.with_structured_outpu
# Prompt
system = """You are a grader assessing relevance 
 user question. 
 If the document contains keyword(s) or semant
 question, grade it as relevant. 
 Give a binary score 'yes' or 'no' to indicate
 relevant to the question."""
grade_prompt = ChatPromptTemplate.from_messages(
 [
 ("system"
                , system),
 ("human"
               ,
                 """Retrieved document: \n\n {do
 {question}"""),
 ]
)
retrieval_grader = grade_prompt | structured_llm_
question = "agent memory"
docs = retriever.get_relevant_documents(question)
doc_txt = docs[0].page_content # as an example
retrieval_grader.invoke({"question": question,
                                             "d
```
#### *JavaScript*

```
import { ChatPromptTemplate } from "@langchain/co
import { z } from "zod";
import { ChatOpenAI } from "@langchain/openai";
// Define the schema using Zod
const GradeDocumentsSchema = z.object({
 binary_score: z.string().describe(`Documents ar
 'yes' or 'no'`),
});
```
// Initialize LLM with structured output using Zo const llm = new ChatOpenAI({ model: "gpt-3.5-turb const structuredLLMGrader = llm.withStructuredOut

```
// System and prompt template
const systemMessage = `You are a grader assessing
 document to a user question. 
If the document contains keyword(s) or semantic m
 question, grade it as relevant.
Give a binary score 'yes' or 'no' to indicate whe
 to the question.`;
const gradePrompt = ChatPromptTemplate.fromMessag
 { role: "system", content: systemMessage },
 {
```

```
 role: "human",
 content: "Retrieved document: \n\n {document}
 User question: {question}",
 },
]);
// Combine prompt with the structured output
const retrievalGrader = gradePrompt.pipe(structur
const question = "agent memory";
const docs = await retriever.getRelevantDocuments
await retrievalGrader.invoke({
 question,
 document: docs[1].pageContent,
});
```
*The output:*

```
binary_score='yes'
```
Notice the use of Pydantic/Zod to help model the binary decision output in a format that can be used to programmatically decide which node in the control flow to move toward.

<span id="page-482-0"></span>In LangSmith, you can see a trace of the logic flow across the nodes discussed previously (see [Figure](#page-483-0) 10-3).

<span id="page-483-0"></span>![](_page_483_Figure_0.jpeg)

Figure 10-3. LangSmith trace results

Let's test to see what happens when the input question cannot be answered by the retrieved documents in the index.

First, utilize LangGraph to make it easier to construct, execute, and debug the full control flow. See the full graph definition in the book's GitHub [repository.](https://oreil.ly/v63Vr) Notice that we've added a transform\_query node to help rewrite the input query in a format that web search can use to retrieve higher-quality results.

As a final step, we set up our web search tool and execute the graph using the out-of-context question. The LangSmith trace shows that the web search tool was used as a fallback to retrieve relevant information prior to the final LLM generated answer (see [Figure](#page-485-0) 10-4).

<span id="page-485-0"></span>![](_page_485_Figure_0.jpeg)

![](_page_485_Figure_1.jpeg)

<span id="page-486-1"></span>Let's move on to the next stage in LLM app testing: preproduction.

## The Preproduction Stage

<span id="page-486-2"></span>The purpose of the preproduction stage of testing is to measure and evaluate the performance of your application prior to production. This will enable you to efficiently assess the accuracy, latency, and cost of utilizing the LLM.

### **Creating Datasets**

<span id="page-486-0"></span>Prior to testing, you need to define a set of scenarios you'd like to test and evaluate. A *dataset* is a collection of examples that provide inputs and expected outputs used to evaluate your LLM app.

These are three common methods to build datasets for valuation:

#### *Manually curated examples*

These are handwritten examples based on expected user inputs and ideal generated outputs. A small dataset consists of between 10 and 50 quality examples. Over

time, more examples can be added to the dataset based on edge cases that emerge in production.

#### *Application logs*

<span id="page-487-0"></span>Once the application is in production, you can store realtime user inputs and later add them to the dataset. This will help ensure the dataset is realistic and covers the most common user questions.

#### *Synthetic data*

<span id="page-487-2"></span>These are artificially generated examples that simulate various scenarios and edge cases. This enables you to generate new inputs by sampling existing inputs, which is useful when you don't have enough real data to test on.

<span id="page-487-1"></span>In LangSmith, you can create a new dataset by selecting Datasets and Testing in the sidebar and clicking the "+ New Dataset" button on the top right of the app, as shown in [Figure](#page-488-0) 10-5.

In the opened window, enter the relevant dataset details, including a name, description, and dataset type. If you'd like to use your own dataset, click the "Upload a CSV dataset" button.

<span id="page-488-0"></span>![](_page_488_Picture_0.jpeg)

Figure 10-5. Creating a new dataset in the LangSmith UI

LangSmith offers three different dataset types:

#### *kv (key-value) dataset*

- <span id="page-488-1"></span>*Inputs* and *outputs* are represented as arbitrary keyvalue pairs.
- The kv dataset is the most versatile, and it is the default type. The kv dataset is suitable for a wide range of evaluation scenarios.
- This dataset type is ideal for evaluating chains and agents that require multiple inputs or generate multiple outputs.

#### *llm (large language model) dataset*

- <span id="page-489-1"></span>The llm dataset is designed for evaluating completion style language models.
- The inputs dictionary contains a single input key mapped to the prompt string.
- The outputs dictionary contains a single output key mapped to the corresponding response string.
- This dataset type simplifies evaluation for LLMs by providing a standardized format for inputs and outputs.

#### *chat dataset*

- <span id="page-489-0"></span>The chat dataset is designed for evaluating LLM structured chat messages as inputs and outputs.
- The *inputs* dictionary contains a single *input* key mapped to a list of serialized chat messages.
- The *outputs* dictionary contains a single *output* key mapped to a list of serialized chat messages.
- This dataset type is useful for evaluating conversational AI systems or chatbots.

### The most flexible option is the key-value data type (see [Figure](#page-490-0) 10-6).

<span id="page-490-0"></span>

| ← New Dataset         |                                                                                                                                                                                                                                | Cancel Create |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| Create Dataset        |                                                                                                                                                                                                                                |               |
| Import CSV            | Upload CSV or drag and drop<br>0                                                                                                                                                                                               |               |
| Dataset details       | Name                                                                                                                                                                                                                           |               |
|                       | ds-artistic-pleat-46                                                                                                                                                                                                           |               |
|                       | Description                                                                                                                                                                                                                    |               |
|                       | Type description                                                                                                                                                                                                               |               |
|                       |                                                                                                                                                                                                                                |               |
| Select a Dataset Type | Key-Value<br>Key Value (KV) datasets are the default type, allowing inputs as dictionaries. Useful for custom workflows, but extra conflyuration<br>may be needed for multi-key evaluation.                                    |               |
|                       | Chat<br>Chat datasets use an "inputs" dictionary with a single "input" key for serialized chat messages and an "outputs" dictionary with a single<br>"output" key for serialized chat messages.                                |               |
|                       | LLM<br>LLM datases have an "inputs" dictionary which contains a single "input" key mapped to a single prompt string. Similarly, the "outputs"<br>dictionary contains a single "output" key mapped to a single response string. |               |

Figure 10-6. Selecting a dataset type in the LangSmith UI

Next, add examples to the dataset by clicking Add Example. Provide the input and output examples as JSON objects, as shown in [Figure](#page-491-0) 10-7.

<span id="page-491-0"></span>

| ← Add Example to Key-Value Dataset        |          |              | Cancel | Submit |
|-------------------------------------------|----------|--------------|--------|--------|
| Input<br>Edit inputs<br>Show input schema | 1        | {}           |        |        |
| Output<br>Edit outputs                    | 1        | {}           |        |        |
| Show output schema                        |          |              |        |        |
| Dataset Splits                            | base (X) | Choose split |        |        |

Figure 10-7. Add key-value dataset examples in the LangSmith UI

You can also define a schema for your dataset in the "Dataset schema" section, as shown in [Figure](#page-492-0) 10-8.

<span id="page-492-0"></span>![](_page_492_Figure_0.jpeg)

<span id="page-492-2"></span>Figure 10-8. Adding a dataset schema in the LangSmith UI

### **Defining Your Evaluation Criteria**

<span id="page-492-1"></span>After creating your dataset, you need to define evaluation metrics to assess your application's outputs before deploying into production. This batch evaluation on a predetermined test suite is often referred to as *offline evaluation***.**

<span id="page-492-3"></span>For offline evaluation, you can optionally label expected outputs (that is, ground truth references) for the data points <span id="page-493-2"></span>you are testing on. This enables you to compare your application's response with the ground truth references, as shown in [Figure](#page-493-0) 10-9.

<span id="page-493-0"></span>![](_page_493_Figure_1.jpeg)

Figure 10-9. AI evaluation diagram

<span id="page-493-1"></span>There are three main evaluators to score your LLM app performance:

#### *Human evaluators*

<span id="page-493-4"></span>If you can't express your testing requirements as code, you can use human feedback to express qualitative characteristics and label app responses with scores. LangSmith speeds up the process of collecting and incorporating human feedback with annotation queues.

#### *Heuristic evaluators*

<span id="page-493-3"></span>These are hardcoded functions and assertions that perform computations to determine a score. You can use reference-free heuristics (for example, checking whether output is valid JSON) or reference-based heuristics such as accuracy. Reference-based evaluation compares an output to a predefined ground truth, whereas reference-free evaluation assesses qualitative characteristics without a ground truth. Custom heuristic evaluators are useful for code-generation tasks such as schema checking and unit testing with hardcoded evaluation logic.

#### *LLM-as-a-judge evaluators*

<span id="page-494-1"></span>This evaluator integrates human grading rules into an LLM prompt to evaluate whether the output is correct relative to the reference answer supplied from the dataset output. As you iterate in preproduction, you'll need to audit the scores and tune the LLM-as-a-judge to produce reliable scores.

<span id="page-494-0"></span>To get started with evaluation, start simple with heuristic evaluators. Then implement human evaluators before moving on to LLM-as-a-judge to automate your human review. This enables you to add depth and scale once your criteria are welldefined.

**TIP**

When using LLM-as-a-judge evaluators, use straightforward prompts that can easily be replicated and understood by a human. For example, avoid asking an LLM to produce scores on a range of 0 to 10 with vague distinctions between scores.

[Figure](#page-495-0) 10-10 illustrates LLM-as-a-judge evaluator in the context of a RAG use case. Note that the reference answer is the ground truth.

<span id="page-495-0"></span>![](_page_495_Figure_3.jpeg)

Figure 10-10. LLM-as-a-judge evaluator used in a RAG use case

#### **Improving LLM-as-a-judge evaluators performance**

<span id="page-495-1"></span>Using an LLM-as-a-judge is an effective method to grade natural language outputs from LLM applications. This involves passing

the generated output to a separate LLM for judgment and evaluation. But how can you trust the results of LLM-as-a-judge evaluation?

<span id="page-496-1"></span><span id="page-496-0"></span>Often, rounds of prompt engineering are required to improve accuracy, which is cumbersome and time-consuming. Fortunately, LangSmith provides a *few-shot* prompt solution whereby human corrections to LLM-as-a-judge outputs are stored as few-shot examples, which are then fed back into the prompt in future iterations.

By utilizing few-shot learning, the LLM can improve accuracy and align outputs with human preferences by providing examples of correct behavior. This is especially useful when it's difficult to construct instructions on how the LLM should behave or be formatted.

The few-shot evaluator follows these steps:

- 1. The LLM evaluator provides feedback on generated outputs, assessing factors such as correctness, relevance, or other criteria.
- 2. It adds human corrections to modify or correct the LLM evaluator's feedback in LangSmith. This is where human preferences and judgment are captured.
- 3. These corrections are stored as few-shot examples in LangSmith, with an option to leave explanations for corrections.
- 4. The few-shot examples are incorporated into future prompts as subsequent evaluation runs.

Over time, the few-shot evaluator will become increasingly aligned with human preferences. This self-improving mechanism reduces the need for time-consuming prompt engineering, while improving the accuracy and relevance of LLM-as-a-judge evaluations.

Here's how to easily set up the LLM-as-a-judge evaluator in LangSmith for offline evaluation. First, navigate to the "Datasets and Testing" section in the sidebar and select the dataset you want to configure the evaluator for. Click the Add Auto-Evaluator button at the top right of the dashboard to add an evaluator to the dataset. This will open a modal you can use to configure the evaluator.

<span id="page-497-0"></span>Select the LLM-as-a-judge option and give your evaluator a name. You will now have the option to set an inline prompt or load a prompt from the prompt hub that will be used to evaluate the results of the runs in the experiment. For the sake of this example, choose the Create Few-Shot Evaluator option, as shown in [Figure](#page-499-0) 10-11.

<span id="page-499-0"></span>![](_page_499_Picture_0.jpeg)

| Auto-Evaluator Name     |   |      |          |
|-------------------------|---|------|----------|
| Apply to past runs<br>e |   |      |          |
| Judge                   |   |      |          |
| Provider                |   |      |          |
| OpenAl                  | > | Chat | Instruct |
| Model                   |   |      |          |
| gpt-40                  |   |      | V        |
| Temperature<br>C        |   |      | 0        |

| Try a suggested Evaluator Prompt<br>Use one of our customizable off-the-shelf prompts                        | RECOMMENDED |  |  |
|--------------------------------------------------------------------------------------------------------------|-------------|--|--|
| Create Few-Shot Evaluator<br>Automatically align your evaluator with human preferences via few-shot examples |             |  |  |
| Create a prompt from scratch<br>Use our template editor to write your own prompt                             |             |  |  |
| Use a prompt from the LangChain Hub<br>Use community contributed prompts                                     |             |  |  |

Figure 10-11. LangSmith UI options for the LLM-as-a-judge evaluator

This option will create a dataset that holds few-shot examples that will autopopulate when you make corrections on the evaluator feedback. The examples in this dataset will be inserted in the system prompt message.

You can also specify the scoring criteria in the Schema field and toggle between primitive types—for example, integer and Boolean (see [Figure](#page-501-0) 10-12).

<span id="page-501-0"></span>

| score = {{score}}                                                      |   |
|------------------------------------------------------------------------|---|
| Reasoning: {{few_shot_explanation}}                                    |   |
| QUERY: {{query}}<br>RESPONSE: {{response}}<br>REFERENCE: {{reference}} | D |

| Grade<br>Grade the quiz based upon the above criteria with a score. |               |           |          |   |
|---------------------------------------------------------------------|---------------|-----------|----------|---|
| score<br>Provide the score:<br>Set allowed values                   | V<br>Required | Integer V | EDITOR C | U |
| Add criteria                                                        |               |           |          |   |

<span id="page-501-1"></span>Figure 10-12. LLM-as-a-judge evaluator scoring criteria

Save the evaluator and navigate back to the dataset details page. Moving forward, each subsequent experiment run from the dataset will be evaluated by the evaluator you configured.

#### **Pairwise evaluation**

<span id="page-502-0"></span>Ranking LLM outputs by preference can be less cognitively demanding for human or LLM-as-a-judge evaluators. For example, assessing which output is more informative, specific, or safe. Pairwise evaluation compares two outputs simultaneously from different versions of an application to determine which version better meets evaluation criteria.

<span id="page-502-1"></span>LangSmith natively supports running and visualizing pairwise LLM app generations, highlighting preference for one generation over another based on guidelines set by the pairwise evaluator. LangSmith's pairwise evaluation enables you to do the following:

- Define a custom pairwise LLM-as-a-judge evaluator using any desired criteria
- Compare two LLM generations using this evaluator

As per the LangSmith [docs](https://oreil.ly/ruFvy), you can use custom pairwise evaluators in the LangSmith SDK and visualize the results of pairwise evaluations in the LangSmith UI.

After creating an evaluation experiment, you can navigate to the Pairwise Experiments tab in the Datasets & Experiments section. The UI enables you to dive into each pairwise

experiment, showing which LLM generation is preferred based upon our criteria. If you click the RANKED\_PREFERENCE score under each answer, you can dive deeper into each evaluation trace (see [Figure](#page-503-0) 10-13).

<span id="page-503-2"></span><span id="page-503-0"></span>

| Viewing Pairwise Experiment                                                                              |                                                                                                                                                                                                                                                                |                                                                                                                                                                          |  |  |  |  |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| summary-opon-21590361 vs. summary-cird-1992a55c-4ced v   compared by   compared by   @ RANKED PREFERL. v |                                                                                                                                                                                                                                                                |                                                                                                                                                                          |  |  |  |  |
| mout                                                                                                     | summary-opus-21590361 7<br>(80) (29)<br>V                                                                                                                                                                                                                      | summary-cand-r-1092x55c 7<br>(26) (89)                                                                                                                                   |  |  |  |  |
| Can Large Language Models Reason a                                                                       | Can LLMs Really Plan and Reason? Title: "OPT-4: Impressive Retrieval, but No -                                                                                                                                                                                 | "LLMs = 7 Parming ( 7 Think again! _ " = Large Language Models don't actually reason or plan, despite pop                                                                |  |  |  |  |
| Example #102f *                                                                                          | · RANKED PREFERENCE : 1 · = SUMMARY ENGAGEMENT SCORE : 8 ·                                                                                                                                                                                                     | · RANKED PREFERENCE : 0 · B BUMMARY ENGAGEMENT, SCORE : B =                                                                                                              |  |  |  |  |
| Segment Anything Alexander Kirillov                                                                      | Here is a summary Tweet for the Segment Anything paper. A Segment Anything: A                                                                                                                                                                                  | New RAI research from @MetaAlllesearch! Check out the latest innovation in computer vision the Segm                                                                      |  |  |  |  |
| Example Pladia •                                                                                         | · RANKED PREFERENCE : 1 · + 5 : SUMMARY ENGAGEMENT SCORE : 5 =                                                                                                                                                                                                 | · RANKED PREFERENCE : 0 +                                                                                                                                                |  |  |  |  |
| LangRoPE: Extending LLM Context Wi<br>Example #2b53 #                                                    | Here is a Tweet to summarize the LongRoPE paper: @ LongRoPE: Extending LLM Co<br>· RANKED PREFERENCE : 0 + = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = | New research axtends #LLM contisel window to a whopping LJ Million Tokent L. Introduction: Current<br>· RANKED PREFERENCE : 1 + ] = SUMMARY ENGAGEMENT, SCORE : 4 +<br>= |  |  |  |  |
| Empowering Large Language Model A                                                                        | Here is a potential Tweet to summarize the paper "Empowering Large Language Mod                                                                                                                                                                                | New research empowers Large Language Model Agents! @ The innovative approach, LearnAct, enable                                                                           |  |  |  |  |
| Example #4409 #                                                                                          | · RANKED PREFERENCE : 1 + = 5 SUMMAY ENGASEMENT SCORE : 5 +                                                                                                                                                                                                    | · RANKED PREFERENCE : 0 ->                                                                                                                                               |  |  |  |  |
| Jamba: A Hybrid Transformer-Mamba                                                                        | Here is a tweet summarizing the Jamba: A Powerful Hybrid Transfor                                                                                                                                                                                              | New PLLM Aiert Jambat the hybrid Transformer Mamba language model that's got it all ga Jamba                                                                             |  |  |  |  |
| Example #4424 +                                                                                          | · RANKED PREFERENCE : 0 + ] @ SUMMARY ENGASEMENT SCORE : 5 +                                                                                                                                                                                                   | B RANKED PREFERENCE : 1 + ] @ SUMMARY ENGAGEMENT SCONE : 4 +                                                                                                             |  |  |  |  |
| Swin Transformer V2: Scalling Up Cap                                                                     | Here is a suggested Tweet is summarize the "Swin Transformer VZ" paper. Title: Swi                                                                                                                                                                             | New BSwinTransformer's & to 38 parameters! @ 1536x1536 rest  Key Innovations: Resident Post                                                                              |  |  |  |  |
| Example #5681 *                                                                                          | · RANKED PREFERENCE : 1 + = SUMMARY ENGAGEMENT SCORE : 5 +                                                                                                                                                                                                     | · RANKED PREFERENCE : 0 + ] @ SUMMAY ENGAGEMENT, SCORE : 2 +                                                                                                             |  |  |  |  |
| Provided proper attribution is provide                                                                   | Here is a suggested Tweet In summarize the "All You Need" paper: ( ) Tra-                                                                                                                                                                                      | New Paper Alerti . "Attention is All You Need" . a transformative study @ Trom @GoogleAl. @ Introduc                                                                     |  |  |  |  |
| Example #c9d7 +                                                                                          | · RANKED PREFERENCE : 1 + = SUMMARY ENGAGEMENT SCORE ! S +                                                                                                                                                                                                     | · RANKED PREFERENCE : 0 + ] @ SUMMARY ENGAGEMENT, SCORE ! 6 +                                                                                                            |  |  |  |  |
| ROF ORMER: ENHANCED TRANSFOR                                                                             | Here is a suggested Tweet is summarize the RoFormer paper: [+] Rotary Position Em                                                                                                                                                                              | Introducing the "Riformer": an enhanced Transformer that rolates your position embeddings! & "What                                                                       |  |  |  |  |
| Example #d518 =                                                                                          | · RANKED PREFERENCE : 1 · = SUMMARY ENGAGEMENT SCORE : 8 ·                                                                                                                                                                                                     | · RANKED PREFERENCE : 0 · B BUMMARY ENGAGEMENT SCORE ! 4 +                                                                                                               |  |  |  |  |
| Phi-3 Technical Report: A Mighly Capa                                                                    | Here is a suggestied Tweet to summarize the phi-3 technical report: w Mighty Mini-                                                                                                                                                                             | Hene's a draft of the Tweet for the pager you provided: يل يل "Ph-3 Min' Your Phone's New Bent Friend" (j) - Trail                                                       |  |  |  |  |
| Example #e319 *                                                                                          | · RANKED PREFERENCE : 1 · · 5 SUMMARY ENGAGEMENT SCORE : 5 ·                                                                                                                                                                                                   | · RANKED PREFERENCE : 0 + ] B BUMMARY ENGAGEMENT, SCORE : B =                                                                                                            |  |  |  |  |
| Extending Llama-3's Contaxt Ten-Fold                                                                     | @ Llama-3 Leags to BOK Contaxt Overnight with QLoRA Fine-Tuning! _ Key Points -                                                                                                                                                                                | Hene's a draft of the Tweet for this paper: New Research: Extending LLM Contest & LLama-J 1 conte                                                                        |  |  |  |  |
| Example #13d5 #                                                                                          | · RANKED PREFERENCE : 1 + = 5 = 5UMMARY ENGASEMENT SCORE : 5 =                                                                                                                                                                                                 | · RANKED PREFERENCE : 0 + = = SUMMARY ENGAGEMENT, SCORE : \$ =                                                                                                           |  |  |  |  |

<span id="page-503-1"></span>Figure 10-13. Pairwise experiment UI evaluation trace

### **Regression Testing**

<span id="page-503-3"></span>In traditional software development, tests are expected to pass 100% based on functional requirements. This ensures stable behavior once the test is validated. In contrast, however, AI models' output performances can vary significantly due to model *drift* (degradation due to changes in data distribution or

updates to the model). As a result, testing AI applications may not always lead to a perfect score on the evaluation dataset.

This has several implications. First, it's important to track results and performance of your tests over time to prevent regression of your app's performance. *Regression* testing ensures that the latest updates or changes of the LLM model of your app do not *regress* (perform worse) relative to the baseline.

Second, it's crucial to compare the individual data points between two or more experimental runs to see where the model got it right or wrong.

<span id="page-504-0"></span>LangSmith's comparison view has native support for regression testing, allowing you to quickly see examples that have changed relative to the baseline. Runs that regressed or improved are highlighted differently in the LangSmith dashboard (see [Figure](#page-505-0) 10-14).

<span id="page-505-0"></span>![](_page_505_Picture_0.jpeg)

Figure 10-14. LangSmith's experiments comparison view

In LangSmith's Comparing Experiments dashboard, you can do the following:

- Compare multiple experiments and runs associated with a dataset. Aggregate stats of runs is useful for migrating models or prompts, which may result in performance improvements or regression on specific examples.
- Set a baseline run and compare it against prior app versions to detect unexpected regressions. If a regression occurs, you can isolate both the app version and the specific examples that contain performance changes.

Drill into data points that behaved differently between compared experiments and runs.

This regression testing is crucial to ensure that your application maintains high performance over time regardless of updates and LLM changes.

Now that we've covered various preproduction testing strategies, let's explore a specific use case.

### **Evaluating an Agent's End-to-End Performance**

<span id="page-506-0"></span>Although agents show a lot of promise in executing autonomous tasks and workflows, testing an agent's performance can be challenging. In previous chapters, you learned how agents use tool calling with planning and memory to generate responses. In particular, tool calling enables the model to respond to a given prompt by generating a tool to invoke and the input arguments required to execute the tool.

Since agents use an LLM to decide the control flow of the application, each agent run can have significantly different outcomes. For example, different tools might be called, agents might get stuck in a loop, or the number of steps from start to finish can vary significantly.

Ideally, agents should be tested at three different levels of granularity:

#### *Response*

<span id="page-507-0"></span>The agent's final response to focus on the end-to-end performance. The inputs are a prompt and an optional list of tools, whereas the output is the final agent response.

#### *Single step*

<span id="page-507-1"></span>Any single, important step of the agent to drill into specific tool calls or decisions. In this case, the output is a tool call.

#### *Trajectory*

<span id="page-507-2"></span>The full trajectory of the agent. In this case, the output is the list of tool calls.

[Figure](#page-508-0) 10-15 illustrates these levels:

<span id="page-508-0"></span>![](_page_508_Figure_0.jpeg)

Figure 10-15. An example of an agentic app's flow

Let's dive deeper into each of these three agent-testing granularities.

#### **Testing an agent's final response**

<span id="page-508-1"></span>In order to assess the overall performance of an agent on a task, you can treat the agent as a black box and define success based on whether or not it completes the task.

Testing for the agent's final response typically involves the following:

*Inputs*

User input and (optionally) predefined tools

*Output*

Agent's final response

*Evaluator*

LLM-as-a-judge

To implement this in a programmatic manner, first create a dataset that includes questions and expected answers from the agent:

*Python*

```
from langsmith import Client
client = Client()
# Create a dataset
examples = [
 ("Which country's customers spent the most? A
 """The country whose customers spent the 
 expenditure of $523.06"""),
 ("What was the most purchased track of 2013?"
 "The most purchased track of 2013 was Hot
 ("How many albums does the artist Led Zeppeli
```

```
 "Led Zeppelin has 14 albums"),
 ("What is the total price for the album "Big 
 "The total price for the album 'Big Ones
 ("Which sales agent made the most in sales in
 "Steve Johnson made the most sales in 200
]
dataset_name = "SQL Agent Response"
if not client.has_dataset(dataset_name=dataset_na
 dataset = client.create_dataset(dataset_name=
 inputs, outputs = zip(
 *[({"input": text}, {"output": label}) fo
 )
 client.create_examples(inputs=inputs, outputs
## chain
def predict_sql_agent_answer(example: dict):
 """Use this for answer evaluation"""
 msg = {"messages": ("user", example["input"])
 messages = graph.invoke(msg, config)
 return {"response": messages['messages'][-1]
```
*JavaScript*

import { Client } from 'langsmith';

```
const client = new Client();
```

```
// Create a dataset
const examples = [
 ["Which country's customers spent the most? And
 `The country whose customers spent the most i
 expenditure of $523.06`],
 ["What was the most purchased track of 2013?",
 "The most purchased track of 2013 was Hot Gir
 ["How many albums does the artist Led Zeppelin 
 "Led Zeppelin has 14 albums"],
 ["What is the total price for the album 'Big On
 "The total price for the album 'Big Ones' is 
 ["Which sales agent made the most in sales in 2
 "Steve Johnson made the most sales in 2009"],
];
const datasetName = "SQL Agent Response";
async function createDataset() {
 const hasDataset = await client.hasDataset({ da
 if (!hasDataset) {
 const dataset = await client.createDataset(da
 const inputs = examples.map(([text]) => ({ in
 const outputs = examples.map(([, label]) => (
 await client.createExamples({ inputs, outputs
```
}

```
 }
}
createDataset();
// Chain function
async function predictSqlAgentAnswer(example) {
 // Use this for answer evaluation
 const msg = { messages: [{ role: "user", conten
 const output = await graph.invoke(msg, config);
 return { response: output.messages[output.messa
}
```
Next, as discussed earlier, we can utilize the LLM to compare the generated answer with the reference answer:

*Python*

```
from langchain import hub
from langchain_openai import ChatOpenAI
from langsmith.evaluation import evaluate
# Grade prompt
grade_prompt_answer_accuracy = hub.pull("langchai
def answer_evaluator(run, example) -> dict:
    """
```

```
 A simple evaluator for RAG answer accuracy
 """
```

```
 # Get question, ground truth answer, RAG chai
 input_question = example.inputs["input"]
 reference = example.outputs["output"]
 prediction = run.outputs["response"]
```

```
 # LLM grader
 llm = ChatOpenAI(model="gpt-4o", temperature=
```

```
 # Structured prompt
 answer_grader = grade_prompt_answer_accuracy
```

```
 # Run evaluator
```

```
 score = answer_grader.invoke({"question": inp
 "correct_answer
                       "student_answer
```

```
 score = score["Score"]
```

```
 return {"key": "answer_v_reference_score", "s
```

```
## Run evaluation
experiment_results = evaluate(
 predict_sql_agent_answer,
 data=dataset_name,
```
evaluators=[answer evaluator]

```
 evaluators=[answer_evaluator],
 num_repetitions=3,
)
```
#### *JavaScript*

```
import { pull } from "langchain/hub";
import { ChatOpenAI } from "langchain_openai";
import { evaluate } from "langsmith/evaluation";
async function answerEvaluator(run, example) {
 /**
 * A simple evaluator for RAG answer accuracy
 */
 // Get question, ground truth answer, RAG chain
 const inputQuestion = example.inputs["input"];
 const reference = example.outputs["output"];
 const prediction = run.outputs["response"];
 // LLM grader
 const llm = new ChatOpenAI({ model: "gpt-4o", t
 // Grade prompt 
 const gradePromptAnswerAccuracy = pull(
 "langchain-ai/rag-answer-vs-reference"
 )
```

```
 // Structured prompt
 const answerGrader = gradePromptAnswerAccuracy
 // Run evaluator
 const scoreResult = await answerGrader.invoke({
 question: inputQuestion,
 correct_answer: reference,
 student_answer: prediction
 });
 const score = scoreResult["Score"];
 return { key: "answer_v_reference_score", score
}
// Run evaluation
const experimentResults = evaluate(predictSqlAgen
 data: datasetName,
 evaluators: [answerEvaluator],
 numRepetitions: 3,
});
```
**Testing a single step of an agent**

);

<span id="page-516-1"></span><span id="page-516-0"></span>Testing an agent's individual action or decision enables you to identify and analyze specifically where your application is underperforming. Testing for a single step of an agent involves the following:

#### *Inputs*

User input to a single step (for example, user prompt, set of tools). This can also include previously completed steps.

#### *Output*

LLM response from the inputs step, which often contains tool calls indicating what action the agent should take next.

#### *Evaluator*

Binary score for correct tool selection and heuristic assessment of the tool input's accuracy.

The following example checks a specific tool call using a custom evaluator:

*Python*

from langsmith.schemas import Example, Run

```
def predict_assistant(example: dict):
 """Invoke assistant for single tool call eval
 msg = [ ("user", example["input"]) ]
 result = assistant_runnable.invoke({"messages
 return {"response": result}
```

```
def check_specific_tool_call(root_run: Run, examp
 """
 Check if the first tool call in the response 
 """
 # Expected tool call
 expected_tool_call = 'sql_db_list_tables'
 # Run
 response = root_run.outputs["response"]
 # Get tool call
 try:
 tool_call = getattr(response, 'tool_calls
 except (IndexError, KeyError):
 tool_call = None
 score = 1 if tool_call == expected_tool_call
 return {"score": score, "key": "single_tool_c
```

```
experiment_results = evaluate(
```

```
 predict_assistant,
 data=dataset_name,
 evaluators=[check_specific_tool_call],
 num_repetitions=3,
 metadata={"version": metadata},
)
```
#### *JavaScript*

```
import {evaluate} from 'langsmith/evaluation';
// Predict Assistant
function predictAssistant(example) {
 /**
 * Invoke assistant for single tool call eval
 */
 const msg = [{ role: "user", content: example
 const result = assistantRunnable.invoke({ mes
 return { response: result };
}
// Check Specific Tool Call
function checkSpecificToolCall(rootRun, example)
 /**
 * Check if the first tool call in the respon
 * tool call.
```

```
 */
 // Expected tool call
 const expectedToolCall = "sql_db_list_tables"
 // Run
 const response = rootRun.outputs.response;
 // Get tool call
 let toolCall;
 try {
 toolCall = response.tool_calls?.[0]?.name
 } catch (error) {
 toolCall = null;
 }
 const score = toolCall === expectedToolCall ?
 return { score, key: "single_tool_call" };
}
// Experiment Results
const experimentResults = evaluate(predictAssista
 data: datasetName,
 evaluators: [checkSpecificToolCall],
 numRepetitions: 3,
});
```
The preceding code block implements these distinct components:

- Invoke the assistant, assistant\_runnable , with a prompt and check if the resulting tool call is as expected.
- Utilize a specialized agent where the tools are hardcoded rather than passed with the dataset input.
- <span id="page-520-0"></span>Specify the reference tool call for the step that we are evaluating for expected\_tool\_call .

#### **Testing an agent's trajectory**

<span id="page-520-1"></span>It's important to look back on the steps an agent took in order to assess whether or not the trajectory lined up with expectations of the agent—that is, the number of steps or sequence of steps taken.

Testing an agent's trajectory involves the following:

*Inputs*

User input and (optionally) predefined tools.

*Output*

Expected sequence of tool calls or a list of tool calls in any order.

#### *Evaluator*

Function over the steps taken. To test the outputs, you can look at an exact match binary score or metrics that focus on the number of incorrect steps. You'd need to evaluate the full agent's trajectory against a reference trajectory and then compile as a set of messages to pass into the LLM-as-a-judge.

The following example assesses the trajectory of tool calls using custom evaluators:

#### *Python*

```
def predict_sql_agent_messages(example: dict):
 """Use this for answer evaluation"""
 msg = {"messages": ("user", example["input"])
 messages = graph.invoke(msg, config)
 return {"response": messages}
def find_tool_calls(messages):
 """
 Find all tool calls in the messages returned
 """
 tool_calls = [
 tc['name']
```
f i [' '] f i

```
 for m in messages['messages'] for tc in g
 ]
 return tool_calls
def contains_all_tool_calls_any_order(
 root_run: Run, example: Example
) -> dict:
 """
 Check if all expected tools are called in any
 """
 expected = [
 'sql_db_list_tables',
 'sql_db_schema',
 'sql_db_query_checker',
 'sql_db_query',
 'check_result'
 ]
 messages = root_run.outputs["response"]
 tool_calls = find_tool_calls(messages)
 # Optionally, log the tool calls -
 #print("Here are my tool calls:")
 #print(tool_calls)
 if set(expected) <= set(tool_calls):
 score = 1
 else:
 score = 0
 return {"score": int(score), "key": "multi_to
```
d f i ll l ll i d (

```
def contains_all_tool_calls_in_order(root_run: Ru
 """
 Check if all expected tools are called in exa
 """
 messages = root_run.outputs["response"]
 tool_calls = find_tool_calls(messages)
 # Optionally, log the tool calls -
 #print("Here are my tool calls:")
 #print(tool_calls)
 it = iter(tool_calls)
 expected = [
 'sql_db_list_tables',
 'sql_db_schema',
 'sql_db_query_checker',
 'sql_db_query',
 'check_result'
 ]
 if all(elem in it for elem in expected):
 score = 1
 else:
 score = 0
 return {"score": int(score), "key": "multi_to
def contains_all_tool_calls_in_order_exact_match(
 root_run: Run, example: Example
) -> dict:
 """
 Check if all expected tools are called in exa
```
ddi i l l ll

```
 additional tool calls.
 """
 expected = [
 'sql_db_list_tables',
 'sql_db_schema',
 'sql_db_query_checker',
 'sql_db_query',
 'check_result'
 ]
 messages = root_run.outputs["response"]
 tool_calls = find_tool_calls(messages)
 # Optionally, log the tool calls -
 #print("Here are my tool calls:")
 #print(tool_calls)
 if tool_calls == expected:
 score = 1
 else:
 score = 0
 return {"score": int(score), "key": "multi_to
experiment_results = evaluate(
 predict_sql_agent_messages,
 data=dataset_name,
 evaluators=[
 contains_all_tool_calls_any_order,
 contains_all_tool_calls_in_order,
 contains_all_tool_calls_in_order_exact_ma
```
]

```
 ],
 num_repetitions=3,
)
```
#### *JavaScript*

```
import {evaluate} from 'langsmith/evaluation';
// Predict SQL Agent Messages
function predictSqlAgentMessages(example) {
 /**
 * Use this for answer evaluation
 */
 const msg = { messages: [{ role: "user", conten
 // Replace with your graph and config
 const messages = graph.invoke(msg, config);
 return { response: messages };
}
// Find Tool Calls
function findToolCalls({messages}) {
 /**
 * Find all tool calls in the messages returned
 */
 return messages.flatMap(m => m.tool_calls?.map(
}
```

```
// Contains All Tool Calls (Any Order)
function containsAllToolCallsAnyOrder(rootRun, ex
 /**
 * Check if all expected tools are called in an
 */
 const expected = [
 "sql_db_list_tables",
 "sql_db_schema",
 "sql_db_query_checker",
 "sql_db_query",
 "check_result"
 ];
 const messages = rootRun.outputs.response;
 const toolCalls = findToolCalls(messages);
 const score = expected.every(tool => toolCalls
 return { score, key: "multi_tool_call_any_order
}
// Contains All Tool Calls (In Order)
function containsAllToolCallsInOrder(rootRun, exa
 /**
 * Check if all expected tools are called in ex
 */
 const messages = rootRun.outputs.response;
 const toolCalls = findToolCalls(messages);
 const expected = [
```

```
 "sql_db_list_tables",
 "sql_db_schema",
 "sql_db_query_checker",
 "sql_db_query",
 "check_result"
 ];
 const score = expected.every(tool => {
 let found = false;
 for (let call of toolCalls) {
 if (call === tool) {
 found = true;
 break;
 }
 }
 return found;
 }) ? 1 : 0;
 return { score, key: "multi_tool_call_in_order"
}
// Contains All Tool Calls (Exact Order, Exact Ma
function containsAllToolCallsInOrderExactMatch(ro
 /**
 * Check if all expected tools are called in ex
 * additional tool calls.
 */
```

```
 const expected = [
```

```
 "sql_db_list_tables",
 "sql_db_schema",
 "sql_db_query_checker",
 "sql_db_query",
 "check_result"
 ];
 const messages = rootRun.outputs.response;
 const toolCalls = findToolCalls(messages);
 const score = JSON.stringify(toolCalls) === JSO
 ? 1
 : 0;
 return { score, key: "multi_tool_call_in_exact_
}
// Experiment Results
const experimentResults = evaluate(predictSqlAgen
 data: datasetName,
 evaluators: [
 containsAllToolCallsAnyOrder,
 containsAllToolCallsInOrder,
 containsAllToolCallsInOrderExactMatch
 ],
 numRepetitions: 3,
});
```
This implementation example includes the following:

- Invoking a precompiled LangGraph agent graph.invoke with a prompt
- Utilizing a specialized agent where the tools are hardcoded rather than passed with the dataset input
- Extracting of the list of tools called using the function find\_tool\_calls
- Checking if all expected tools are called in any order using the function contains\_all\_tool\_calls\_any\_order or called in order using contains\_all\_tool\_calls\_in\_order
- Checking whether all expected tools are called in the exact order using

```
contains_all_tool_calls_in_order_exact_match
```
<span id="page-529-0"></span>All three of these agent evaluation methods can be observed and debugged in LangSmith's experimentation UI (see [Figure](#page-530-0) 10-16).

<span id="page-530-0"></span>

|  | sql-agent-multi-step-tool-calling-trajecory-in-order-55bd2954 |
|--|---------------------------------------------------------------|
|  |                                                               |

| 1 experiment ▼<br>multi_tool_call_in_ V<br>showing |         |                                        |                                                           | 6 | ->       |   |  |
|----------------------------------------------------|---------|----------------------------------------|-----------------------------------------------------------|---|----------|---|--|
| Input                                              |         | Reference Output                       | sql-agent-multi-step-tool-calling-trajecory-in-order-55bd |   | 7        | p |  |
| How many albums does                               | #36ce + | Led Zeppelin has 14 albums             | 3 REPS >                                                  |   | 0.00 µ   |   |  |
| What was the most purc                             | #4210 → | The most purchased track of 2013 wa    | 3 REPS >                                                  |   | . 0.00 µ |   |  |
| Which sales agent mad                              | #7338 → | Steve Johnson made the most sales i    | 3 REPS >                                                  |   | 0.00 U   |   |  |
| Which country's custo                              | #9372 + | The country whose customers spent t    | 3 REPS >                                                  |   | = 0.00 µ |   |  |
| What is the total price fo                         | #ad01 + | The total price for the album 'Big One | 3 REPS >                                                  |   | . 0.00 µ |   |  |

<span id="page-530-1"></span>Figure 10-16. Example of an agent evaluation test in the LangSmith UI

In general, these tests are a solid starting point to help mitigate an agent's cost and unreliability due to LLM invocations and variability in tool calling.

### Production

<span id="page-530-4"></span><span id="page-530-3"></span><span id="page-530-2"></span>Although testing in the preproduction phase is useful, certain bugs and edge cases may not emerge until your LLM application interacts with live users. These issues can affect latency, as well as the relevancy and accuracy of outputs. In addition, observability and the process of *online evaluation* can help ensure that there are guardrails for LLM inputs or outputs. These guardrails can provide much-needed protection from prompt injection and toxicity.

The first step in this process is to set up LangSmith's tracing feature.

### **Tracing**

<span id="page-531-0"></span>A *trace* is a series of steps that your application takes to go from input to output. LangSmith makes it easy to visualize, debug, and test each trace generated from your app.

Once you've installed the relevant LangChain and LLM dependencies, all you need to do is configure the tracing environment variables based on your LangSmith account credentials:

```
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
# The below examples use the OpenAI API, though y
export OPENAI_API_KEY=<your-openai-api-key>
```
After the environment variables are set, no other code is required to enable tracing. Traces will be automatically logged <span id="page-532-1"></span>to their specific project in the "Tracing projects" section of the LangSmith dashboard. The metrics provided include trace volume, success and failure rates, latency, token count and cost, and more—as shown in [Figure](#page-532-0) 10-17.

<span id="page-532-0"></span>

| 1%       | LangChain Team > Projects > 88 chat-langchain-langgraph-cloud                  |   |   |      |                                          |                  |                               |          |                   |            |
|----------|--------------------------------------------------------------------------------|---|---|------|------------------------------------------|------------------|-------------------------------|----------|-------------------|------------|
| D        | 88 chat-langchain-langgraph-cloud                                              |   |   |      |                                          |                  | O ID<br>Data Retention 400d √ |          | 4 Add Rule / Edit |            |
| 중국       | Runs<br>Threads<br>Monitor<br>Setup                                            |   |   |      |                                          |                  |                               |          |                   |            |
| A        | Root Runs<br>8 Last 7 days<br>LLM Calls<br>All Runs<br>▼ 1 filter              |   |   |      |                                          |                  |                               |          | Columns           |            |
| 0        | Start comparing Select one of the below traces in the table to start comparing |   |   |      |                                          |                  |                               |          |                   | ×          |
| 20       |                                                                                | > | 0 | Name | Input                                    | Output           | Start Time                    | Latency  | Dataset           | Annotation |
| B        |                                                                                | > | 0 | chat | human: 你会说中文吗                            | 《query":"你会说     | 7/31/2024, 9:20:31            | 3 2.63s  | 0<br>0            | 0 %        |
| O        |                                                                                | > | 0 | chat | human: can you spea                      | {"query":"can yo | 7/31/2024, 9:20:15            | 3 2.865  | 00                | 0 %        |
|          |                                                                                | > | 0 | chat | human: Explain multi-  {"query":"Explain |                  | 7/31/2024, 9:06:39            | © 3.175  | 0<br>0            | 0 %        |
|          | >                                                                              | > | 0 | chat | human: I am using lan  {"query":"I am us |                  | 7/31/2024, 9:05:52            | 3 2.944  | =                 | A<br>0     |
|          | 网站 上海网站                                                                        | > | 0 | chat | human: I am using lan  {"query":"I am us |                  | 7/31/2024, 9:05:32 --         | 3 2.694  | 0<br>0            | 02         |
| ்கு<br>0 |                                                                                | > | 0 | chat | human: I am using lan  {"query":"I am us |                  | 7/31/2024, 9:05:17 ---        | © 3.084  | 0<br>0            | 0 %        |
|          |                                                                                | > | 0 | chat | human: is langchain a  {"query":"is lang |                  | 7/31/2024, 9:01-38            | 3.68€    | 0<br>0            | 0 %        |
|          |                                                                                | > | 0 | chat | human: What is the la  {"query":"What is |                  | 7/31/2024, 8:56:26            | 3 4.064  | 0<br>0            | 0 %        |
|          |                                                                                | 3 | 0 | chat | human:自己的資料(例  《"query":"自己的             |                  | 7/31/2024, 8:54:58            | @ 11.03s | 0<br>0            | 02         |
| e        |                                                                                | > | 0 | chat | human: # nDay: previ                     | {"query":"# nDay | 7/31/2024, 8:51:46            | 3 6.365  | 00                | 0 %        |
| ಡಿ       |                                                                                | > | 0 | chat | human: gemma2b을                          | {"query":"gemma  | 7/31/2024, 8:51:44            | © 4.255  | D<br>0            | 0 %        |
|          | 1                                                                              | > | 0 | chat | human: 具體作法                              | 《"query":"具體作    | 7/31/2024, 8:51:27 --         | 3 7.00s  | 0<br>D            | 0 %        |
|          | 1990                                                                           | > | 0 | chat | human: 如何鹏文件存                            | 《"query":"如何猫    | 7/31/2024, 8:51:15 P          | ® 4.99%  | 0<br>0            | 0 %        |

Figure 10-17. An example of LangSmith's trace performance metrics

You can review a variety of strategies to implement tracing based on your needs.

### **Collect Feedback in Production**

<span id="page-533-0"></span>Unlike the preproduction phase, evaluators for production testing don't have grounded reference responses for the LLM to compare against. Instead, evaluators need to score performance in real time as your application processes user inputs. This reference-free, real-time evaluation is often referred to as *online evaluation*.

There are at least two types of feedback you can collect in production to improve app performance:

#### *Feedback from users*

You can directly collect user feedback explicitly or implicitly. For example, giving users the ability to click a like and dislike button or provide detailed feedback based on the application's output is an effective way to track user satisfaction. In LangSmith, you can attach user feedback to any trace or intermediate run (that is, span) of a trace, including annotating traces inline or reviewing runs together in an annotation queue.

#### *Feedback from LLM-as-a judge evaluators*

As discussed previously, these evaluators can be implemented directly on traces to identify hallucination and toxic responses.

The earlier preproduction section already discussed how to set up LangSmith's auto evaluation in the Datasets & Experiments section of the dashboard.

### **Classification and Tagging**

<span id="page-534-1"></span>In order to implement effective guardrails against toxicity or gather insights on user sentiment analysis, we need to build an effective system for labeling user inputs and generated outputs.

This system is largely dependent on whether or not you have a dataset that contains reference labels. If you don't have preset labels, you can use the LLM-as-a-judge evaluator to assist in performing classification and tagging based upon specified criteria.

If, however, ground truth classification labels are provided, then a custom heuristic evaluator can be used to score the chain's output relative to the ground truth class labels.

### **Monitoring and Fixing Errors**

<span id="page-534-0"></span>Once your application is in production, LangSmith's tracing will catch errors and edge cases. You can add these errors into your

test dataset for offline evaluation in order to prevent recurrences of the same issues.

Another useful strategy is to release your app in phases to a small group of beta users before a larger audience can access its features. This will enable you to uncover crucial bugs, develop a solid evaluation dataset with ground truth references, and assess the general performance of the app including cost, latency, and quality of outputs.

## <span id="page-535-0"></span>Summary

As discussed in this chapter, robust testing is crucial to ensure that your LLM application is accurate, reliable, fast, toxic-free, and cost-efficient. The three key stages of LLM app development create a data cycle that helps to ensure high performance throughout the lifetime of the application.

During the design phase, in-app error handling enables selfcorrection before the error reaches the user. Preproduction testing ensures each of your app's updates avoids regression in performance metrics. Finally, production monitoring gathers real-time insights and application errors that inform the subsequent design process and the cycle repeats.

Ultimately, this process of testing, evaluation, monitoring, and continuous improvement, will help you fix issues and iterate faster, and most importantly, deliver a product that users can trust to consistently deliver their desired results.

## Chapter 11. Building with LLMs

<span id="page-537-2"></span><span id="page-537-1"></span>One of the biggest open questions in the world of LLMs today is how to best put them in the hands of end users. In some ways, LLMs are actually a more intuitive interface for computing than what came before them. They are much more forgiving of typos, slips of the tongue, and the general imprecision of humans, when compared to traditional computer applications. On the other hand, the very ability to handle inputs that are "slightly off" comes with a tendency to sometimes produce results that are also "slightly off"—which is also very much unlike any previous computing tendencies.

<span id="page-537-3"></span><span id="page-537-0"></span>In fact, computers were designed to reliably repeat the same set of instructions with the same results every time. Over the past few decades, that principle of reliability has permeated the design of human-computer interfaces (variously called HCI, UX, and UI) to the extent that a lot of the usual constructs end up being subpar for use in applications that rely heavily on LLMs.

Let's take an example: Figma is a software application used by designers to create faithful renderings of designs for websites, mobile applications, book or magazine covers—the list goes on. As is the case with pretty much all productivity software

(software for the creation of some kind of long-form content), its interface is a combination of the following:

- <span id="page-538-1"></span>A palette of tools and prebuilt *primitives* (fundamental building blocks), in this case lines, shapes, selection and paint tools, and many more
- <span id="page-538-0"></span>A canvas, where the user inserts these building blocks and organizes them into their creation: a website page, a mobile app screen, and so on

This interface is built upon the premise that the capabilities of the software are known ahead of time, which is in fact true in the case of Figma. All building blocks and tools were coded by a software engineer ahead of time. Therefore, they were known to exist at the time the interface was designed. It sounds almost silly to point that out, but the same is not strictly true of software that makes heavy use of LLMs.

Look at a word processor (e.g., Microsoft Word or Google Docs). This is a software application for the creation of long-form text content of some kind, such as a blog post, article, book chapter, and the like. The interface at our disposal here is also made up of a familiar combination:

- A palette of tools and prebuilt *primitives*: in the case of a word processor, the primitives available are tables, lists, headings, image placeholders, and so forth, and the tools are spellcheck, commenting, and so on.
- *A canvas*: in this case, it's literally a blank page, where the user types words and may include some of the elements just mentioned.

How would this situation change if we were to build an LLMnative word processor? This chapter explores three possible answers to this question, which are broadly applicable to any LLM application. For each of the patterns we explore, we'll go over what key concepts you'd need to implement it successfully. We don't mean to imply that these are the only ones, it will be a while until the dust settles on this particular question.

Let's look at each of these patterns, starting with the easiest to add to an existing app.

## Interactive Chatbots

<span id="page-539-0"></span>This is arguably the easiest lift to add to an existing software application. At its most basic conception, this idea just bolts on an AI sidekick—to bounce ideas off of—while all work still happens in the existing user interface of the application. An

<span id="page-540-3"></span><span id="page-540-1"></span>example here is GitHub Copilot Chat, which can be used in a sidebar inside the VSCode code editor.

An upgrade to this pattern is to add some communication points between the AI sidekick extension and the main application. For example, in VSCode, the assistant can "see" the content of the file currently being edited or whatever portion of that code the user has selected. And in the other direction, the assistant can insert or edit text in that open editor, arriving at some basic form of collaboration between the user and the LLM.

#### **NOTE**

<span id="page-540-2"></span>Streaming chat as we're describing here is currently the prototypical application of LLMs. It's almost always the first thing app developers learn to build on their LLM journey, and it's almost always the first thing companies reach for when adding LLMs to their existing applications. Maybe this will remain the case for years to come, but another possible outcome could be for streaming chat to become the command line of the LLM era—that is, the closest to direct programming access, becoming a niche interface, just as it did for computers.

<span id="page-540-0"></span>To build the most basic chatbot you should use these components:

*A chat model*

<span id="page-541-0"></span>Their dialogue tuning lends itself well to multiturn interactions with a user. Refer to the [Preface](#page-8-0) for more on dialogue tuning.

*Conversation history*

<span id="page-541-2"></span>A useful chatbot needs to be able to "get past hello." That is, if the chatbot can't remember the previous user inputs, it will be much harder to have meaningful conversations with it, which implicitly refer to previous messages.

To go beyond the basics, you'd probably add the following:

#### *Streaming output*

<span id="page-541-4"></span><span id="page-541-3"></span><span id="page-541-1"></span>The best chatbot experiences currently stream LLM output token by token (or in larger chunks, like sentences or paragraphs) directly to the user, which alleviates the latency inherent to LLMs today.

#### *Tool calling*

<span id="page-541-5"></span>To give the chatbot the ability to interact with the main canvas and tools of the application, you can expose them as tools the model can decide to call on—for instance, a "get selected text" tool and an "insert text at end of doc" tool.

#### *Human-in-the-loop*

<span id="page-542-1"></span>As soon as you give the chatbot tools that can change what's in the application canvas, you create the need to give back some control to the user—for example, letting the user confirm, or even edit, before new text is inserted.

## Collaborative Editing with LLMs

<span id="page-542-0"></span>Most productivity software has some form of collaborative editing built in, which we can classify into one of these buckets (or somewhere in between):

#### *Save and send*

<span id="page-542-2"></span>This is the most basic version, which only supports one user editing the document at a time, before "passing the buck" to another user (for example, sending the file over email) and repeating the process until done. The most obvious example is the Microsoft Office suite of apps: Excel, Word, PowerPoint.

#### *Version control*

<span id="page-542-3"></span>This is an evolution of save and send that supports multiple editors working simultaneously on their own (and unaware of each other's changes) by providing tools to combine their work afterward: merge strategies (how to combine unrelated changes) and conflict resolution (how to combine incompatible changes). The most popular example today is Git/GitHub, used by software engineers to collaborate on software projects.

#### *Real-time collaboration*

<span id="page-543-1"></span>This enables multiple editors to work on the same document at the same time, while seeing each other's changes. This is arguably the most natural form of software-enabled collaboration, evidenced by the popularity of Google Docs and Google Sheets among technical and nontechnical computer users.

This pattern of LLM user experience consists of employing an LLM agent as one of those "users" contributing to this shared document. This can take many forms, including the following:

- <span id="page-543-0"></span>An always-on "copilot" giving you suggestions on how to complete the next sentence
- An asynchronous "drafter," which you task with, for example, going off and researching the topic in question and returning later with a section you can incorporate in your final document

To build this, you'd likely need the following:

#### *Shared state*

<span id="page-544-1"></span>The LLM agent and the human users should be on the same footing in terms of access and understanding of the state of the document—that is, they would be able to parse the state of the document and produce edits to that state in a compatible format.

#### *Task manager*

<span id="page-544-2"></span>Producing a useful edit to the document will invariably be a multistep process, which can take time and fail halfway. This creates the need for reliable scheduling and orchestration of long-running jobs, with queueing, error recovery, and control over running tasks.

#### *Merging forks*

<span id="page-544-0"></span>Users will continue to edit the document after tasking the LLM agent, so LLM outputs will need to be merged with the users' work, either manually by the user (an experience like Git) or automatically (through conflict resolution algorithms such as CRDT and operational transformation (OT), employed by applications such as Google Docs).

#### *Concurrency*

<span id="page-545-3"></span>The fact that the human user and the LLM agent are working on the same thing at the same time requires the ability to handle interruptions, cancellations, reroutings (do this instead), and queueing (do this as well).

#### *Undo/redo stack*

<span id="page-545-5"></span>This is a ubiquitous pattern in productivity software, which inevitably is needed here too. Users change their minds and want to go back to an earlier state of the document, and the LLM application needs to be capable of following them there.

#### *Intermediate output*

<span id="page-545-4"></span><span id="page-545-2"></span>Merging user and LLM outputs is made a lot easier when those outputs are gradual and arrive piecemeal as soon as they're produced, in much the same way that a person writes a 10-paragraph page one sentence at a time.

## Ambient Computing

<span id="page-545-1"></span><span id="page-545-0"></span>A very useful UX pattern has been the always-on background software that pipes up when something "interesting" has

happened that deserves your attention. You can find this in many places today. A few examples are:

- You can set an alert in your brokerage app to notify you when some stock goes below a certain price.
- You can ask Google to notify you when new search results are found matching some search query.
- You can define alerts for your computer infrastructure to notify you when something is outside the regular pattern of behavior.

The main obstacle to deploying this pattern more widely may be coming up with a reliable definition of *interesting* ahead of time that is both of the following:

#### *Useful*

It will notify you when you think it should.

#### *Practical*

Most users won't want to spend massive amounts of time ahead precreating endless rules for alerts.

The reasoning capabilities of LLMs can unlock new applications of this pattern of *ambient computing* that are simultaneously more useful (they identify more of what you'd find interesting)

and less work to set up (their reasoning can replace a lot or all of the manual setup of rules).

The big difference between *collaborative* and *ambient* is concurrency:

#### *Collaborative*

You and the LLM are usually (or sometimes) doing work at the same time and feeding off each other's work.

#### *Ambient*

The LLM is continuously doing some kind of work in the background while you, the user, are presumably doing something else entirely.

To build this, you need:

#### *Triggers*

<span id="page-547-0"></span>The LLM agent needs to receive (or poll periodically for) new information from the environment. This is in fact what motivates ambient computing: a preexisting source of periodic or continuous new information that needs to be processed.

*Long-term memory*

<span id="page-548-1"></span>It would not be possible to detect new interesting events without consulting a database of previously received information.

#### *Reflection (or learning)*

<span id="page-548-3"></span>Understanding what is *interesting* (what deserves human input) likely requires learning from each previous interesting event after it happens. This is usually called a *reflection step*, in which the LLM produces an update to its long-term memory, possibly modifying its internal "rules" for detecting future interesting events.

#### *Summarize output*

<span id="page-548-2"></span>An agent working in the background is likely to produce much more output than the human user would like to see. This requires that the agent architecture be modified to produce summaries of the work done and surface to the user only what is new or noteworthy.

#### *Task manager*

<span id="page-548-4"></span><span id="page-548-0"></span>Having an LLM agent working continuously in the background requires employing some system for managing the work, queuing new runs, and handling and recovering from error.

## Summary

LLMs have the potential to change not only how we build [software, but](https://oreil.ly/RqnCm) also the very software we build. This new capability that we developers have at our disposal to generate new content will not only enhance many existing apps, but it can make new things possible that we haven't dreamed of yet.

There's no shortcut here. You really do need to build something (s)crappy, speak to users, and rinse and repeat until something new and unexpected comes out the other side.

With this last chapter, and the book as a whole, we have tried to give you the knowledge we think can help you build something uniquely good with LLMs. We want to thank you for coming on this journey with us and wish you the best of luck in your career and future.

## Index

### **Symbols**

{} (curly braces), Making LLM Prompts [Reusable](#page-63-0)

#### **A**

abstractions, [LangChain](#page-33-0) and Why It's Important [agency, Cognitive](#page-322-0) [Architectures](#page-278-0) with LangGraph, The Plan-Do Loop, [Patterns](#page-385-1) to Make the Most of LLMs agency-reliability trade-off, Cognitive Architectures with [LangGraph, Patterns](#page-278-1) to Make the Most of LLMs-Patterns to Make the Most of LLMs agent architecture agent abstractions, [LangChain](#page-35-0) and Why It's Important always calling tools first, [Always](#page-332-0) Calling a Tool First-[Always](#page-342-1) Calling a Tool First dealing with many tools, [Dealing](#page-342-2) with Many [Tools-Dealing](#page-352-0) with Many Tools LangGraph agent creation, Building a [LangGraph](#page-323-0) Agent-Building a [LangGraph](#page-332-1) Agent multi-agent architectures, Multi-Agent [Architectures-](#page-374-0)Supervisor [Architecture,](#page-383-0) [Multitasking](#page-417-0) LLMs plan-do loop, The [Plan-Do](#page-318-0) Loop-The [Plan-Do](#page-322-1) Loop

reflection prompting technique, [Reflection](#page-354-0)[-Reflection](#page-366-0) unique aspects of, Agent [Architecture](#page-315-1) agents, evaluating performance of final [response, Testing](#page-516-0) an agent's final [response](#page-508-1)-Testing a single step of an agent levels of [testing, Evaluating](#page-506-0) an Agent's End-to-End Performance single steps, [Testing](#page-516-1) a single step of an [agent-Testing](#page-520-0) a single step of an agent [trajectory, Testing](#page-530-1) an agent's [trajectory-](#page-520-1)Testing an agent's trajectory AI chatbots (see chatbots) AIMessage interface, Using LLMs in [LangChain](#page-57-0) alerts, Ambient [Computing](#page-545-0) algorithms, [Preface](#page-9-0) ambient computing, Ambient [Computing](#page-545-1) [Anthropic, P](#page-47-0)[refac](#page-10-0)[e, L](#page-47-0)[angChain](#page-34-0) and Why It's Important, LLM Fundamentals with LangChain API access, protecting, [Security](#page-466-0) API keys, retrieving, Large [Language](#page-427-1) Model application logs, [Creating](#page-487-0) Datasets architecture (see also agent architecture; cognitive architectures)

ReAct [architecture, L](#page-322-2)[angChain](#page-35-1) and Why It's Important, The Plan-Do Loop router [architecture, A](#page-313-0)[rchitecture](#page-298-0) #3: Router-Architecture #3: Router transformer neural network [architecture, Brief](#page-16-1) Primer on LLMs

ArcSearch, [Introducing](#page-244-0) LangGraph argument k, Retrieving Relevant [Documents](#page-173-0) assistant [role,](#page-55-0) [Dialogue-Tuned](#page-20-0) LLMs, Using LLMs in LangChain assistants (see chatbots) assistants (LangGraph Platform), [Assistants](#page-442-0) async execution, Using the [Runnable](#page-80-0) Interface authentication, [Security](#page-467-0) authorize mode, [Human-in-the-Loop](#page-408-1) Modalities [auto-evaluators, adding, Improving](#page-497-0) LLM-as-a-judge evaluators performance autonomy, Cognitive [Architectures](#page-279-0) with [LangGraph, Patterns](#page-387-0) to Make the Most of LLMs

#### **B**

bag-of-words model, [Embeddings](#page-100-0) Before LLMs Bard, [Preface](#page-10-1) batch method, Using the [Runnable](#page-77-0) Interface, [Summary](#page-91-0) BLOOM, Brief [Primer](#page-13-1) on LLMs braces, curly ({}), Making LLM Prompts [Reusable](#page-63-0)

#### **C**

canvases, [Building](#page-538-0) with LLMs

chain [architecture,](#page-298-1) [Architecture](#page-289-1) #2: Chain-Architecture #2:

Chain

chain-of-thought (CoT) prompting, [Chain-of-Thought](#page-25-1),

[LangChain](#page-35-2) and Why It's Important, Agent [Architecture](#page-316-0)

Chase, Harrison, [Preface](#page-10-2)

chat dataset, [Creating](#page-489-0) Datasets

chat models

alternative LLM providers for, LLM [Fundamentals](#page-47-1) with

LangChain

interactive chatbots, [Interactive](#page-541-0) Chatbots

message interfaces in, Using LLMs in [LangChain](#page-56-0)

roles in, Using LLMs in [LangChain](#page-54-0)

chatbots

adding memory to chatbots, Adding Memory to

[StateGraph-Adding](#page-257-1) Memory to [StateGraph](#page-262-0)

advanced components, [Interactive](#page-541-1) Chatbots

asynchronous execution of, Imperative [Composition](#page-86-0)

basic components, [Interactive](#page-540-0) Chatbots

building chatbot memory [systems, Building](#page-238-1) a Chatbot Memory System[-Building](#page-242-0) a Chatbot Memory System ChatGPT, [Preface](#page-8-1) conversation history, [Modifying](#page-262-1) Chat History-[Summary](#page-276-0), [Interactive](#page-541-2) Chatbots interactive, [Interactive](#page-539-0) Chatbots limitation of simple, RAG Part I: [Indexing](#page-93-1) Your Data memory and, [LangChain](#page-35-3) and Why It's Important modifying chat history, [Modifying](#page-262-1) Chat History[-Summary](#page-276-0) overview of creating, What to [Expect](#page-37-0) from This Book prompt and chat model example [of, Imperative](#page-81-1) Composition

streaming support with Python or [JavaScript, Imperative](#page-84-0)

Composition

ChatGPT, [Preface](#page-8-1)

ChatMessage interface, Using LLMs in [LangChain](#page-57-1)

[ChatPromptTemplate, Making](#page-71-0) LLM Prompts [Reusable-](#page-66-0)Getting Specific Formats out of LLMs

checkpoint events, [Intermediate](#page-400-0) Output

checkpointers, Adding Memory to [StateGraph](#page-257-2)[, Human-in-the-](#page-403-0)Loop Modalities

classification problems, [Embeddings](#page-100-1) Before LLMs

Claude, [Preface](#page-10-3)

code examples, obtaining and using, Using Code [Examples](#page-40-0)

cognitive architectures

chain [architecture,](#page-298-1) [Architecture](#page-289-1) #2: Chain-Architecture #2: Chain

definition of [term, Cognitive](#page-279-1) Architectures with

LangGraph

LLM call architecture, [Architecture](#page-283-0) #1: LLM Call-

[Architecture](#page-289-2) #1: LLM Call

major LLM [architectures, Cognitive](#page-280-2) Architectures with

LangGraph

router [architecture, A](#page-313-0)[rchitecture](#page-298-0) #3: Router-Architecture

#3: Router

Cohere, LLM [Fundamentals](#page-47-2) with [LangChain, Generating](#page-122-0) Text Embeddings

ColBERT model, ColBERT: Optimizing [Embeddings](#page-157-1)

collaborative editing, [Collaborative](#page-542-0) Editing with LLMs-

[Collaborative](#page-545-2) Editing with LLMs

comments and questions, How to [Contact](#page-42-0) Us

composition (see declarative composition; imperative

composition)

concurrency, [Collaborative](#page-545-3) Editing with LLMs

concurrent inputs, dealing with, Refuse [concurrent](#page-418-0) inputs-

Fork and [merge](#page-422-0)

context

accurate output with, The Goal: Picking Relevant Context for LLMs, Introducing [Retrieval-Augmented](#page-95-0) Generation dealing with complex, Multi-Agent [Architectures](#page-374-1)

definition of term, [Retrieval-Augmented](#page-27-0) Generation context windows, Converting Your [Documents](#page-113-0) into Text, [Trimming](#page-262-2) Messages

continuous [improvement](#page-471-1) cycle, Testing Techniques Across the LLM App Development Cycle (see also testing) conversation history, [Interactive](#page-541-2) Chatbots copilots, [Collaborative](#page-543-0) Editing with LLMs cosine similarity, Semantic [Embeddings](#page-106-0) Explained, Retrieving Relevant [Documents](#page-169-0) CoT prompting (see chain-of-thought prompting) [create, read, update, delete](#page-129-1) (CRUD), Storing Embeddings in a Vector Store cron jobs (LangGraph Platform), [Cron](#page-443-0) jobs CSV format, Other [Machine-Readable](#page-75-0) Formats with Output Parsers curly braces ({}), Making LLM Prompts [Reusable](#page-63-0)

current events, RAG Part I: [Indexing](#page-94-0) Your Data, Introducing [Retrieval-Augmented](#page-164-1) Generation

**D**

data indexing

converting documents into text, Converting Your Documents into [Text-Converting](#page-109-0) Your [Documents](#page-114-0) into Text embeddings, [Embeddings:](#page-97-0) Converting Text to Numbers-Converting Your [Documents](#page-109-0) into Text end-to-end example, Generating Text [Embeddings-](#page-125-0)Generating Text [Embeddings](#page-128-0) generating text embeddings, Generating Text [Embeddings-](#page-122-1)Generating Text [Embeddings](#page-125-1) limitations of LLM's knowledge [corpus, RAG](#page-93-1) Part I: Indexing Your Data optimizing, Indexing [Optimization](#page-147-0)-[Summary](#page-161-1) process of, Retrieving Relevant [Documents](#page-166-0) relevant content for LLMs, The Goal: Picking Relevant Context for [LLMs, Retrieving](#page-94-1) Relevant [Documents](#page-166-1)-Generating LLM [Predictions](#page-184-0) Using Relevant Documents splitting text into chunks, [Splitting](#page-114-1) Your Text into Chunks-[Splitting](#page-122-2) Your Text into Chunks storing embeddings in vector stores, Storing Embeddings in a Vector [Store-Working](#page-128-1) with Vector Stores tracking document changes, Tracking Changes to Your [Documents-Tracking](#page-138-1) Changes to Your [Documents](#page-147-1) data models (LangGraph Platform), Data [Models](#page-441-0) data queries

query construction, Query [Construction](#page-224-1)-[Text-to-SQL](#page-234-0)

query routing, Query [Routing](#page-211-0)[-Semantic](#page-223-0) Routing

query transformation, Query [Transformatio](#page-184-1)[n-Hypothetical](#page-211-1) Document Embeddings

database access, protecting, [Security](#page-466-1)

database description, [Text-to-SQL](#page-230-1)

datasets

[creating,](#page-492-1) [Creating](#page-486-0) Datasets-Defining Your Evaluation Criteria

dialogue datasets, [Dialogue-Tuned](#page-20-1) LLMs

task-specific datasets, [Instruction-Tuned](#page-18-0) LLMs

debug mode (LangGraph), [Intermediate](#page-400-1) Output

declarative composition, Using the [Runnable](#page-80-1) Interface,

Declarative [Composition](#page-87-0)[-Summary](#page-91-1)

defense in depth, [Security](#page-465-0)

dense embeddings, LLM-Based [Embeddings](#page-102-1)

dependencies, installing, Install [Dependencies](#page-425-0)

deployment

LangGraph API [configuration](#page-448-0) file, Create a LangGraph API Config

LangGraph [Studio, Launch](#page-464-0) [LangGraph](#page-460-1) Studio-Launch LangGraph Studio

from LangSmith UI, Deploy from the [LangSmith](#page-455-0) UI-

[Environment](#page-459-0) variables

prerequisites, [Prerequisites-](#page-424-1)Create a [LangSmith](#page-441-1) Account

security considerations, [Security](#page-464-1)

testing LangGraph app locally, Test Your LangGraph App

[Locally-Test](#page-450-0) Your [LangGraph](#page-455-1) App Locally

design stage, testing during, The Design Stage: [Self-Corrective](#page-472-0)

RAG-The Design Stage: [Self-Corrective](#page-486-1) RAG

dialogue-tuning, [Dialogue-Tuned](#page-19-0) LLMs

dimensions, LLM-Based [Embeddings](#page-102-2)

document loaders, Converting Your [Documents](#page-109-1) into Text documents

classifying, [Embeddings](#page-100-1) Before LLMs

[decoupling, M](#page-156-1)[ultiVectorRetrieve](#page-147-2)[r-RAPTOR:](#page-156-1) Recursive

Abstractive Processing for Tree-Organized Retrieval

deleting, Tracking Changes to Your [Documents](#page-139-0)

[preprocessing, The](#page-95-1) Goal: Picking Relevant Context for LLMs

reranking/reordering, [RAG-Fusion](#page-199-0)

retrieving relevant [documents, Retrieving](#page-166-2) Relevant

Documents-Retrieving Relevant [Documents](#page-174-0)

tracking document changes, Tracking Changes to Your

[Documents-Tracking](#page-138-1) Changes to Your [Documents](#page-147-1)

double texting (LangGraph Platform), [Double](#page-446-0) texting

drift, [Regression](#page-503-1) Testing

DuckDuckGo, Building a [LangGraph](#page-323-1) Agent

dynamic few-shot prompting, Few-Shot [Prompting](#page-32-0)

dynamic inputs, Making LLM Prompts [Reusable](#page-60-0)

#### **E**

edges, [Introducing](#page-248-0) LangGraph editing, collaborative, [Collaborative](#page-542-0) Editing with LLMs-[Collaborative](#page-545-2) Editing with LLMs embedding models, [LangChain](#page-35-4) and Why It's Important, LLM Fundamentals with [LangChain, LLM-Based](#page-47-3) [Embeddings](#page-102-3) embeddings bag-of-words model, [Embeddings](#page-100-0) Before LLMs benefits of, [Embeddings:](#page-97-1) Converting Text to Numbers [definition](#page-97-2) of term, The Goal: Picking Relevant Context for LLMs generating text embeddings, Generating Text [Embeddings-](#page-122-1)Generating Text [Embeddings](#page-125-1) LLM-based embeddings, LLM-Based [Embeddings](#page-101-0) optimizing, ColBERT: Optimizing [Embeddings](#page-157-1) retrieving relevant [embeddings, Retrieving](#page-172-0) Relevant Documents semantic embeddings, Semantic [Embeddings](#page-103-0) Explained-Semantic [Embeddings](#page-106-1) Explained storing embeddings in vector stores, Storing Embeddings in a Vector [Store-Working](#page-128-1) with Vector Stores

uses [for, E](#page-107-0)[mbeddings](#page-98-0) Before LLMs, Semantic Embeddings Explained

environment variables, [Environment](#page-457-0) variables error handling, The Design Stage: [Self-Corrective](#page-472-1) RAG errors, monitoring, [Monitoring](#page-534-0) and Fixing Errors evaluation metrics (see also testing)

defining, Defining Your [Evaluation](#page-492-2) Criteria getting started, Defining Your [Evaluation](#page-494-0) Criteria improving LLM-as-a-judge [performance, Improving](#page-495-1) LLMas-a-judge evaluators [performance-Improving](#page-501-1) LLM-as-ajudge evaluators performance main evaluators, Defining Your [Evaluation](#page-493-1) Criteria pairwise evaluation, Pairwise [evaluation](#page-502-0) expected output, Brief [Primer](#page-17-0) on LLMs external [data, retrieving, The](#page-95-2) Goal: Picking Relevant Context for LLMs

### **F**

[feedback, collecting](#page-533-0) in production, Collect Feedback in Production few-shot prompting, Few-Shot [Prompting](#page-32-1), [Text-to-SQL](#page-230-2), Improving [LLM-as-a-judge](#page-496-0) evaluators performance file access, protecting, [Security](#page-466-2)

final response, evaluating, Testing an agent's final [response-](#page-508-1)[Testing](#page-516-0) a single step of an agent

fine-tuning

dialogue datasets, [Dialogue-Tuned](#page-20-2) LLMs

fine-tuned LLMs, [Fine-Tuned](#page-21-0) LLMs

floating-point values, Semantic [Embeddings](#page-104-1) Explained

flow engineering, [Architecture](#page-289-3) #2: Chain

fork and merge strategy, Fork and [merge](#page-421-0)

formats

[machine-readable, Other](#page-75-0) Machine-Readable Formats with

Output Parsers

providing format [instructions, Other](#page-75-1) Machine-Readable Formats with Output Parsers

specifying from LLMs, Getting Specific Formats out of

LLMs-Other [Machine-Readable](#page-71-1) Formats with Output

Parsers

frontiers, [Patterns](#page-386-2) to Make the Most of LLMs function calls, Logical [Routing](#page-213-0)

### **G**

Gemma, Brief Primer on [Prompting](#page-22-0)[, LangChain](#page-34-1) and Why It's Important

generate-reflect loop, [Reflection](#page-363-0)

generation [stage, Generating](#page-175-1) LLM Predictions Using Relevant

Documents

generative AI

beginnings of, [Preface](#page-9-1)

LLMs versus ML algorithms, [Preface](#page-9-2)

GitHub Copilot Chat, [Interactive](#page-540-1) Chatbots

Google

Gemini, [Preface](#page-10-1)

LangChain integration [with, LangChain](#page-34-0) and Why It's

Important

graphs, [Introducing](#page-243-1) LangGraph (see also LangGraph) ground truth references, Defining Your [Evaluation](#page-493-2) Criteria

#### **H**

hallucinations, RAG Part I: [Indexing](#page-94-2) Your Data, ColBERT: Optimizing Embeddings, Query [Transformation, Trimmi](#page-158-1)ng Messages, Testing: [Evaluation, Monitoring, and](#page-262-3) Continuous Improvement heuristic evaluators, Defining Your [Evaluation](#page-493-3) Criteria Hierarchical Navigable Small World [\(HNSW\), Retrieving](#page-172-0) Relevant Documents Hugging Face, Generating Text [Embeddings](#page-122-3) human evaluators, Defining Your [Evaluation](#page-493-4) Criteria human-computer interfaces (HCI), [Building](#page-537-0) with LLMs

human-in-the-loop modalities authorize mode, [Human-in-the-Loop](#page-408-1) Modalities checkpointers, [Human-in-the-Loop](#page-403-0) Modalities edit state, Edit [state](#page-414-0) fork step, [Fork](#page-415-0) interactive chatbots and, [Interactive](#page-542-1) Chatbots interrupt mode, [Human-in-the-Loop](#page-404-0) Modalities LangGraph Platform API, [Human-in-the-loop](#page-445-0) restart step, [Restart](#page-412-1) resume step, [Resume](#page-411-1) HumanMessage interface, Using LLMs in [LangChain](#page-57-2) Hypothetical Document Embeddings (HyDE), Hypothetical Document [Embeddings-Hypothetical](#page-205-1) Document Embeddings

### **I**

imperative composition, Using the [Runnable](#page-80-2) Interface-Imperative [Composition,](#page-86-1) [Summary](#page-91-2) inaccuracies, RAG Part I: [Indexing](#page-94-3) Your Data independent agents, Multi-Agent [Architectures](#page-374-2) indexing (see data indexing; vector indexes) ingestions, The Goal: Picking [Relevant](#page-97-3) Context for LLMs input chat format and, [Dialogue-Tuned](#page-20-3) LLMs dynamic inputs, Making LLM Prompts [Reusable](#page-60-0)

handling concurrent, [Multitasking](#page-417-1) LLMs-Fork and [merge](#page-422-0) in LLMs versus machine learning, Brief [Primer](#page-17-0) on LLMs role in LLMs, Brief [Primer](#page-12-1) on LLMs instruction-tuning, [Instruction-Tuned](#page-18-1) LLMs interactive chatbots, Streaming LLM Output [Token-by-Token,](#page-400-2) [Interactive](#page-539-0) Chatbots (see also chatbots) intermediate output, [Intermediate](#page-395-0) Output-Intermediate [Output, Collaborative](#page-400-3) Editing with LLMs interrupt mode, [Human-in-the-Loop](#page-404-0) Modalities interrupt strategy, [Interrupt](#page-419-0) invoke method, Using LLMs in [LangChain](#page-53-0)[, Making](#page-63-1) LLM Prompts Reusable, Using the [Runnable](#page-77-1) Interface, [Summary](#page-91-0)

### **J**

jailbreaking, [Dialogue-Tuned](#page-20-4) LLMs JavaScript agent architecture implementing, Building a [LangGraph](#page-325-0) Agent subagents, Supervisor [Architecture](#page-381-0) supervisor, Supervisor [Architecture](#page-378-0) asynchronous execution with, Imperative [Composition](#page-86-2) chatbot conversation [configuration, Using](#page-56-1) LLMs in LangChain chatbot edges, adding, Creating a [StateGraph](#page-254-0)

chatbot memory [systems, Building](#page-240-0) a Chatbot Memory System

chatbot nodes, adding, Creating a [StateGraph](#page-252-0)

chatbot streaming support, Imperative [Composition,](#page-85-0)

Declarative [Composition](#page-90-0)

ChatPromptTemplate, Making LLM Prompts [Reusable-](#page-67-0)

Getting Specific [Formats](#page-71-0) out of LLMs

cognitive architectures

chain, [Architecture](#page-293-0) #2: Chain

LLM call, [Architecture](#page-284-0) #1: LLM Call

router, [Architecture](#page-304-0) #3: Router

composition

declarative, Declarative [Composition](#page-88-0)

imperative, Imperative [Composition](#page-82-0)

data indexing

end-to-end example, Generating Text [Embeddings](#page-127-0)

example of, Retrieving Relevant [Documents](#page-168-0)

document loaders [and, Converting](#page-112-0) Your Documents into

Text

documents, retrieving full context, [MultiVectorRetriever](#page-152-0)-

RAPTOR: Recursive [Abstractive](#page-156-1) Processing for Tree-

Organized Retrieval

dynamic inputs

constructing, Making LLM Prompts [Reusable](#page-61-0)

feeding into LLMs, Making LLM Prompts [Reusable](#page-65-0) [embeddings, retrieving](#page-172-1) relevant, Retrieving Relevant Documents

Hypothetical Document Embeddings (HyDE), Hypothetical Document [Embeddings-Hypothetical](#page-207-0) Document Embeddings

LangChain set up using, Getting Set Up with [LangChain](#page-51-0) LangGraph

installation, [Introducing](#page-248-1) LangGraph

visual representation, Creating a [StateGraph](#page-255-1)

messages

filtering, Filtering [Messages](#page-268-0)

merging, Merging [Consecutive](#page-273-0) Messages

trimming, [Trimming](#page-264-0) Messages

model predictions, invoking, Using LLMs in [LangChain,](#page-53-1)

Generating LLM [Predictions](#page-177-0) Using Relevant Documents-

Generating LLM [Predictions](#page-184-0) Using Relevant Documents

multi-query retrieval in, [Multi-Query](#page-192-0) [Retrieval-Multi-](#page-196-0)

Query Retrieval

output

intermediate, [Intermediate](#page-396-0) Output

streaming [token-by-token, Streaming](#page-401-0) LLM Output

Token-by-Token

structured, [Structured](#page-393-0) Output

output parsers in, Other [Machine-Readable](#page-76-1) Formats with Output Parsers

RAG-Fusion strategy, [RAG-Fusion](#page-198-0)-[RAG-Fusion](#page-205-2)

record [management](#page-142-0) in, Tracking Changes to Your

#### Documents

reflection prompting technique, [Reflection](#page-358-0)

Rewrite-Retrieve-Read strategy, [Rewrite-Retrieve-Read](#page-188-0) routing

logical, Logical [Routing](#page-214-0)-Logical [Routing](#page-219-1)

semantic, [Semantic](#page-221-0) Routing-[Semantic](#page-223-0) Routing runnable interface, Using the [Runnable](#page-78-0) Interface schema creation, [Structured](#page-392-0) Output state inspection and [updating, Adding](#page-261-0) Memory to StateGraph

StateGraph

creating, Creating a [StateGraph](#page-250-0)

memory addition, Adding Memory to [StateGraph](#page-258-0) subgraphs

calling directly, Calling a [Subgraph](#page-369-0) Directly

calling with [functions, Calling](#page-372-0) a Subgraph with a Function

SystemMessage instruction, Using LLMs in [LangChain](#page-58-0) text embeddings with, Generating Text [Embeddings](#page-123-0) text extraction with, Converting Your [Documents](#page-113-1) into Text

text, splitting into chunks, [Splitting](#page-116-0) Your Text into Chunks-[Splitting](#page-122-2) Your Text into Chunks text-to-metadata [filter, T](#page-230-3)[ext-to-Metadata](#page-227-0) Filter-Text-to-Metadata Filter text-to-SQL translations, [Text-to-SQL](#page-232-0) tools always calling first, [Always](#page-334-0) Calling a Tool First dealing with many, [Dealing](#page-345-0) with Many Tools vector stores and, [Working](#page-133-0) with Vector Stores JSON output, JSON [Output](#page-72-0), [Structured](#page-391-0) Output JSONSchema notation, [Structured](#page-392-1) Output

### **K**

k parameter, [RAG-Fusion](#page-202-0)

k-nearest neighbors [\(k-NN\), RAPTOR:](#page-156-2) Recursive Abstractive Processing for Tree-Organized Retrieval Kahneman, Daniel, [Reflection](#page-354-1) keyword searches, [Embeddings](#page-100-2) Before LLMs kv (key-value) dataset, [Creating](#page-488-1) Datasets

#### **L**

LangChain (see also LangGraph; large language models; LLM applications; retrieval-augmented generation)

assembling LLM applications, Assembling the Many Pieces of an LLM [Application-Summary, Cognitive](#page-77-2) Architectures with LangGraph-Cognitive [Architectures](#page-283-1) with LangGraph beginnings of, [Preface](#page-10-2)

benefits [of, P](#page-33-1)[refac](#page-8-2)[e-P](#page-33-1)[reface](#page-11-0)[, LangChain](#page-33-1) and Why It's Important, LLM [Fundamentals](#page-46-1) with [LangChain-LLM](#page-49-0) Fundamentals with LangChain

documentation for, LLM [Fundamentals](#page-47-3) with LangChain getting specific formats out of LLMs, Getting Specific Formats out of LLMs-Other [Machine-Readable](#page-71-1) Formats with Output Parsers

interfaces provided, Using LLMs in [LangChain](#page-52-0) making LLM prompts [reusable, Making](#page-59-0) LLM Prompts Reusable-Getting Specific [Formats](#page-71-0) out of LLMs setting up, Getting Set Up with [LangChain](#page-49-1) using LLMs in, Using LLMs in [LangChai](#page-52-1)[n-Using](#page-59-1) LLMs in LangChain

LangChain Expression Language (LCEL)

imperative versus declarative [composition, Using](#page-80-0) the Runnable Interface

optimized execution plan using, Declarative [Composition](#page-87-0) LangGraph (see also cognitive architectures; LangChain; LangSmith)

adding memory to chatbots, Adding Memory to [StateGraph-Adding](#page-257-1) Memory to [StateGraph](#page-262-0) basics of, [Introducing](#page-243-2) LangGraph-[Introducing](#page-249-0) LangGraph building chatbot memory [systems, Building](#page-238-1) a Chatbot Memory System[-Building](#page-242-0) a Chatbot Memory System building LangGraph agents, Building a [LangGraph](#page-323-0) Agent-Building a [LangGraph](#page-332-1) Agent configuration file, Create a [LangGraph](#page-448-0) API Config control flow illustration, [Backend](#page-436-0) API creating a [StateGraph, Creating](#page-257-3) a [StateGraph](#page-249-1)-Creating a StateGraph installing, [Introducing](#page-248-2) LangGraph intermediate output, [Intermediate](#page-396-1) Output modifying chat history, [Modifying](#page-262-1) Chat History[-Summary](#page-276-0) purpose of, [Introducing](#page-243-2) LangGraph self-corrective RAG, The Design Stage: [Self-Corrective](#page-472-2) RAG-The Design Stage: [Self-Corrective](#page-486-1) RAG stream modes supported in, [Intermediate](#page-399-0) Output streaming LLM output [token-by-token, Streaming](#page-401-1) LLM Output Token-by-Token [subgraphs, Subgraphs](#page-373-0) in [LangGraph](#page-366-1)-Calling a Subgraph with a Function LangGraph Platform API data models, Data [Models](#page-441-0)

deployment using, [Backend](#page-437-1) API

features, [Features-](#page-443-1)[Webhooks](#page-448-1)

LangGraph [Studio, Launch](#page-464-0) [LangGraph](#page-460-1) Studio-Launch LangGraph Studio

LangSmith (see also LangChain; LangGraph) account creation, Create a [LangSmith](#page-439-1) Account agent evaluation example, Testing an agent's [trajectory](#page-529-0) comparison view/regression testing, [Regression](#page-504-0) Testing dataset creation, Creating [Datasets](#page-487-1) deployment from LangSmith UI, Deploy from the LangSmith [UI-Environment](#page-455-0) variables few-shot prompting, Improving LLM-as-a-judge evaluators [performance-Improving](#page-496-1) LLM-as-a-judge evaluators performance pairwise evaluation, Pairwise [evaluation](#page-502-1) trace results in, The Design Stage: [Self-Corrective](#page-482-0) RAG tracing, [Tracing](#page-532-1) language models, Brief [Primer](#page-12-2) on LLMs large language model (llm) dataset, [Creating](#page-489-1) Datasets large language models (LLMs) (see also structured output) alternative providers for, LLM [Fundamentals](#page-47-4) with LangChain ambient computing with, Ambient [Computing](#page-545-1) benefits and drawbacks of, [Building](#page-537-1) with LLMs

brief primer on, Brief [Primer](#page-12-3) on [LLMs-Brief](#page-17-1) Primer on LLMs

building with, [Building](#page-537-2) with LLMs-Ambient [Computing](#page-548-0) Claude and Bard, [Preface](#page-10-4)

collaborative editing with, Collaborative Editing with

[LLMs-Collaborative](#page-542-0) Editing with LLMs

deployment example, Large [Language](#page-426-0) Model

getting specific formats out of LLMs, Getting Specific

Formats out of LLMs-Other [Machine-Readable](#page-71-1) Formats

with Output Parsers

limitations of knowledge [corpus, RAG](#page-93-2) Part I: Indexing Your

Data

LLM-based embeddings, LLM-Based [Embeddings](#page-101-0)

versus machine learning, [Preface](#page-9-2)

for multilingual output, Brief [Primer](#page-13-2) on LLMs

open source LLMs, Brief Primer on [Promptin](#page-22-0)[g, LangChain](#page-34-1)

and Why It's Important

OpenAI's GPT-3, Brief [Primer](#page-12-4) on LLMs

OpenAI's GPT-3.5, [Preface](#page-8-3)

relevant content for LLMs, The Goal: Picking Relevant

Context for [LLMs, Retrieving](#page-94-1) Relevant [Documents](#page-166-1)-

Generating LLM [Predictions](#page-184-0) Using Relevant Documents

types of, Brief [Primer](#page-17-2) on LLMs[-Fine-Tuned](#page-21-1) LLMs

using in [LangChain, Using](#page-59-1) LLMs in [LangChain-](#page-52-1)Using LLMs in LangChain

latency, [Patterns](#page-387-1) to Make the Most of [LLMs, Intermediate](#page-395-1) Output, [Interactive](#page-541-3) Chatbots

LCEL (see LangChain Expression Language)

Llama, Brief Primer on [Promptin](#page-22-0)[g, LangChain](#page-34-1) and Why It's Important

llm (large language model) dataset, [Creating](#page-489-1) Datasets

LLM applications (see also deployment; evaluation metrics; testing)

agentic, Agent [Architecture](#page-315-2)

assembling, Assembling the Many Pieces of an LLM

[Application-Summary, Cognitive](#page-77-2) Architectures with

LangGraph-Cognitive [Architectures](#page-283-1) with LangGraph

benefits of LangChain for building, LLM Fundamentals

with [LangChain-LLM](#page-46-1) [Fundamentals](#page-49-0) with LangChain

challenge in building good [applications, LLM](#page-44-2)

Fundamentals with LangChain

common features of, Cognitive [Architectures](#page-277-2) with

LangGraph

key stages of app [development, Testing](#page-470-0) Techniques Across the LLM App Development Cycle

major LLM [architectures, Cognitive](#page-280-2) Architectures with LangGraph

multiactor applications, [Introducing](#page-243-3) LangGraph multitasking LLMs, [Multitasking](#page-417-1) LLMs-Fork and [merge](#page-422-0) patterns and key concepts for [successful, Structured](#page-389-1) Output-Fork and [merge](#page-422-0) security considerations, [Security](#page-464-1) trade-off between agency and reliability, Cognitive Architectures with [LangGraph, Patterns](#page-278-1) to Make the Most of LLMs-[Patterns](#page-389-0) to Make the Most of LLMs LLM call [architecture,](#page-289-2) [Architecture](#page-283-0) #1: LLM Call-Architecture #1: LLM Call LLM-as-a-judge evaluators, Defining Your [Evaluation](#page-494-1) Criteria LLM-driven loop, The [Plan-Do](#page-318-1) Loop

LLMs (see large language models)

logical routing, Logical [Routing](#page-212-1)-Logical [Routing](#page-219-1)

long-term memory, Ambient [Computing](#page-548-1)

loops, The [Plan-Do](#page-318-2) Loop

#### **M**

machine learning (ML) basics of, [Preface](#page-9-3) current applications of, [Preface](#page-9-4) versus LLMs, [Preface](#page-9-2) max\_tokens parameter, Using LLMs in [LangChain](#page-54-1) memory systems

adding memory to [StateGraph, Adding](#page-257-1) Memory to StateGraph-Adding Memory to [StateGraph](#page-262-0) building chatbot memory [systems, Building](#page-238-1) a Chatbot Memory System[-Building](#page-242-0) a Chatbot Memory System long-term memory, Ambient [Computing](#page-548-1) purpose of, Using [LangGraph](#page-237-1) to Add Memory to Your Chatbot merging forks, [Collaborative](#page-544-0) Editing with LLMs messages appending, Creating a [StateGraph](#page-251-0) filtering, Filtering [Message](#page-267-0)[s-Merging](#page-272-0) Consecutive Messages merging, Merging [Consecutive](#page-272-0) Messages-[Summary](#page-276-0) trimming, [Trimming](#page-262-2) Messages[-Trimming](#page-267-1) Messages misuse, anticipating potential, [Security](#page-465-1) mitigation strategies, [Security](#page-464-2) ML (see machine learning) model drift, [Regression](#page-503-1) Testing model parameter, Using LLMs in [LangChain](#page-54-2) monitoring errors, [Monitoring](#page-534-0) and Fixing Errors (see also testing) multi-agent architectures, Multi-Agent [Architectures-](#page-374-0)Supervisor [Architecture](#page-383-0)

multi-query retrieval [strategy, M](#page-196-0)[ulti-Query](#page-190-0) Retrieval-Multi-Query Retrieval

multiactor applications, [Introducing](#page-243-3) LangGraph multilingual output, Brief [Primer](#page-13-2) on LLMs multitasking, [Multitasking](#page-417-1) LLMs-Fork and [merge](#page-422-0) [MultiVectorRetriever, M](#page-156-1)[ultiVectorRetrieve](#page-147-2)[r-RAPTOR:](#page-156-1) Recursive Abstractive Processing for Tree-Organized Retrieval

#### **N**

neural networks, Brief [Primer](#page-12-5) on LLMs nodes, [Introducing](#page-247-0) LangGraph Norvig, Peter, Agent [Architecture](#page-315-3)

#### **O**

observability, [Production](#page-530-2) offline evaluation, Defining Your [Evaluation](#page-492-3) Criteria Ollama, LLM [Fundamentals](#page-47-5) with LangChain online evaluation, [Production](#page-530-3) OpenAI API account creation, Brief Primer on [Prompting](#page-22-1)[, Getting](#page-49-2) Set Up with LangChain copying prompts to [Playground, Brief](#page-22-2) Primer on

Prompting

integration with [LangChain, LangChain](#page-34-0) and Why It's Important, Generating Text [Embeddings](#page-122-4) launch of ChatGPT and ChatGPT API, [Preface](#page-8-1) overview of models offered, Using LLMs in [LangChain](#page-54-3) pricing, [Preface](#page-8-4)

OpenSearch, LLM [Fundamentals](#page-48-0) with LangChain optimized execution plan, Declarative [Composition](#page-87-1) orchestration [capabilities, LLM](#page-48-1) Fundamentals with

LangChain

output (see also structured output) accurate, The Goal: Picking [Relevant](#page-95-3) Context for LLMs, Introducing [Retrieval-Augmented](#page-165-1) Generation expected output, Brief [Primer](#page-17-0) on LLMs JSON output, JSON [Output](#page-72-0), [Structured](#page-391-0) Output multilingual output, Brief [Primer](#page-13-2) on LLMs role in LLMs, Brief [Primer](#page-12-6) on LLMs streaming token-by-token, [Interactive](#page-541-4) Chatbots summarizing, Ambient [Computing](#page-548-2) output parsers, Other [Machine-Readable](#page-75-2) Formats with Output Parsers

#### **P**

pairwise evaluation, Pairwise [evaluation](#page-502-0) parallel execution, Using the [Runnable](#page-80-0) Interface parameters

basics of, Brief [Primer](#page-12-7) on LLMs

k parameter, [RAG-Fusion](#page-202-0)

max\_tokens, Using LLMs in [LangChain](#page-54-1)

model parameter, Using LLMs in [LangChain](#page-54-2)

temperature, Using LLMs in [LangChain](#page-54-4)

permissions, limiting, [Security](#page-464-3)

Perplexity, [Introducing](#page-244-0) LangGraph

persistence, Adding Memory to [StateGraph](#page-257-4)

PGVector, Getting Set Up with [PGVector](#page-130-1)

plan-do loop, The [Plan-Do](#page-318-0) Loop-The [Plan-Do](#page-322-1) Loop

Playground (OpenAI API), Brief Primer on [Prompting](#page-22-2)

Postgres, Getting Set Up with [PGVector](#page-130-1)

preprocessing, The Goal: Picking [Relevant](#page-95-1) Context for LLMs preproduction stage testing

dataset [creation, Creating](#page-492-1) [Datasets-](#page-486-0)Defining Your

Evaluation Criteria

defining evaluation [criteria, Defining](#page-492-1) Your Evaluation

Criteria-Pairwise [evaluation](#page-503-2)

end-to-end [performance, Evaluating](#page-506-0) an Agent's End-to-End

Performance-Testing an agent's [trajectory](#page-530-1)

purpose of, The [Preproduction](#page-486-2) Stage

regression testing, [Regression](#page-503-3) Testing

pretrained LLMs, Brief [Primer](#page-17-3) on LLMs

primitives, [Building](#page-538-1) with LLMs

private data, RAG Part I: [Indexing](#page-93-3) Your Data

production stage testing

classification and tagging, [Classification](#page-534-1) and Tagging collecting feedback, Collect Feedback in [Production](#page-533-0) monitoring and fixing [errors, Monitoring](#page-534-0) and Fixing

Errors

tracing, [Tracing](#page-531-0)

prompt [engineering,](#page-23-0) [Dialogue-Tuned](#page-20-5) LLMs-Brief Primer on Prompting

prompt injection guardrails, [Security](#page-467-1)

prompt template [abstractions, LangChain](#page-34-2) and Why It's

Important

prompts

benefits of LangChain for [prompting, LangChain](#page-33-2) and Why

It's Important

best practices for, Brief [Primer](#page-17-4) on LLMs

brief primer on prompting, Brief Primer on [Prompting](#page-22-3)-

Few-Shot [Prompting](#page-33-3)

combining prompting techniques, Tool [Callin](#page-30-0)[g, LangChain](#page-35-0) and Why It's Important

definition of term, Brief [Primer](#page-17-5) on LLMs

example of detailed, Making LLM Prompts [Reusable](#page-59-2)

purpose of, Making LLM Prompts [Reusable](#page-59-0)

reflection prompting technique, [Reflection](#page-354-0)[-Reflection](#page-366-0) [reusing, L](#page-59-0)[angChain](#page-34-2) and Why It's Important, Making LLM Prompts Reusable-Getting Specific [Formats](#page-71-0) out of LLMs structured output with, [Structured](#page-390-0) Output

Pydantic, JSON [Output](#page-74-0)

Python

agent architecture

implementing, Building a [LangGraph](#page-323-2) Agent

subagents, Supervisor [Architecture](#page-380-0)

supervisor, Supervisor [Architecture](#page-377-0)

asynchronous execution with, Imperative [Composition](#page-86-3)

chatbot conversation [configuration, Using](#page-55-1) LLMs in

LangChain

chatbot edges, adding, Creating a [StateGraph](#page-253-0)

chatbot memory [systems, Building](#page-239-1) a Chatbot Memory

System

chatbot nodes, adding, Creating a [StateGraph](#page-252-1)

chatbot streaming support, Imperative [Composition,](#page-84-0)

Declarative [Composition](#page-89-0)

ChatPromptTemplate, Making LLM Prompts [Reusable-](#page-66-1)

Getting Specific [Formats](#page-71-0) out of LLMs

cognitive architectures

chain, [Architecture](#page-290-0) #2: Chain

LLM call, [Architecture](#page-283-2) #1: LLM Call

router, [Architecture](#page-300-0) #3: Router

ColBERT model, ColBERT: Optimizing [Embeddings](#page-158-2) composition

declarative, Declarative [Composition](#page-87-2)

imperative, Imperative [Composition](#page-81-2)

data indexing

end-to-end example, Generating Text [Embeddings](#page-125-2)

example of, Retrieving Relevant [Documents](#page-168-1)

document loaders [and, Converting](#page-111-0) Your Documents into Text

document summaries, generating, [MultiVectorRetriever](#page-149-0) documents, retrieving full context, [MultiVectorRetriever](#page-152-1) dynamic inputs

constructing, Making LLM Prompts [Reusable](#page-60-1)

feeding into LLMs, Making LLM Prompts [Reusable](#page-63-2) [embeddings, retrieving](#page-172-2) relevant, Retrieving Relevant Documents

f-string syntax, Making LLM Prompts [Reusable](#page-63-3) Hypothetical Document Embeddings (HyDE), Hypothetical Document [Embeddings-Hypothetical](#page-206-1) Document Embeddings

LangChain set up using, Getting Set Up with [LangChain](#page-50-0) LangGraph

installation, [Introducing](#page-248-3) LangGraph

visual representation, Creating a [StateGraph](#page-254-1) messages

filtering, Filtering [Messages](#page-267-2)

merging, Merging [Consecutive](#page-272-1) Messages

trimming, [Trimming](#page-263-0) Messages

model predictions, invoking, Using LLMs in [LangChain,](#page-53-2)

Generating LLM [Predictions](#page-176-0) Using Relevant Documents-

Generating LLM [Predictions](#page-184-0) Using Relevant Documents

multi-query retrieval in, [Multi-Query](#page-191-1) [Retrieval-Multi-](#page-196-0)

Query Retrieval

output

intermediate, [Intermediate](#page-396-2) Output

JSON, JSON [Output](#page-72-1)

streaming [token-by-token, Streaming](#page-401-2) LLM Output

Token-by-Token

structured, [Structured](#page-393-1) Output

output parsers in, Other [Machine-Readable](#page-76-2) Formats with

Output Parsers

RAG-Fusion strategy, [RAG-Fusion](#page-197-1)-[RAG-Fusion](#page-205-2)

record [management](#page-140-0) in, Tracking Changes to Your

Documents

reflection prompting technique, [Reflection](#page-356-0)

Rewrite-Retrieve-Read strategy, [Rewrite-Retrieve-Read](#page-187-0) routing

logical, Logical [Routing](#page-213-1)-Logical [Routing](#page-219-1)

semantic, [Semantic](#page-220-0) Routing-[Semantic](#page-223-0) Routing

runnable interface, Using the [Runnable](#page-78-1) Interface

schema creation, [Structured](#page-391-1) Output

state inspection and [updating, Adding](#page-261-1) Memory to StateGraph

StateGraph

creating, Creating a [StateGraph](#page-249-2)

memory addition, Adding Memory to [StateGraph](#page-258-1) subgraphs

calling directly, Calling a [Subgraph](#page-368-0) Directly

calling with [functions, Calling](#page-371-0) a Subgraph with a

Function

SystemMessage instruction, Using LLMs in [LangChain](#page-57-3) text embeddings with, Generating Text [Embeddings](#page-123-1) text extraction with, Converting Your [Documents](#page-112-1) into Text text, splitting into chunks, [Splitting](#page-115-0) Your Text into Chunks-[Splitting](#page-122-2) Your Text into Chunks

text-to-metadata [filter, T](#page-230-3)[ext-to-Metadata](#page-225-0) Filter-Text-to-

Metadata Filter

text-to-SQL translations, [Text-to-SQL](#page-231-1)

tools

always calling first, [Always](#page-333-0) Calling a Tool First dealing with many, [Dealing](#page-343-0) with Many Tools

vector stores

storing summaries in, [MultiVectorRetriever](#page-150-0) working with, [Working](#page-132-0) with Vector Stores

### **Q**

queries (see data queries)

query construction

process of, Query [Construction](#page-224-2)

purpose of, [Summary](#page-235-3)

text-to-metadata [filter, T](#page-230-3)[ext-to-Metadata](#page-225-1) Filter-Text-to-

Metadata Filter

text-to-SQL translations, [Text-to-SQL](#page-230-4)-[Text-to-SQL](#page-234-0)

query routing strategy

logical routing, Logical [Routing](#page-212-1)-Logical [Routing](#page-219-1)

purpose of, Query [Routing](#page-212-2)

semantic routing, [Semantic](#page-219-2) Routing-[Semantic](#page-223-0) Routing

query transformation

definition of term, Query [Transformation](#page-184-3)

Hypothetical Document Embeddings (HyDE), Hypothetical

Document [Embeddings-Hypothetical](#page-205-1) Document

Embeddings

multi-query retrieval strategy, [Multi-Query](#page-190-0) Retrieval-

[Multi-Query](#page-196-0) Retrieval

purpose of, [Summary](#page-235-4)

RAG-Fusion strategy, [RAG-Fusion](#page-197-2)-[RAG-Fusion](#page-205-2) Rewrite-Retrieve-Read strategy, [Rewrite-Retrieve-Read](#page-185-2)-[Rewrite-Retrieve-Read](#page-190-1) questions and comments, How to [Contact](#page-42-0) Us

queueing, Queue [concurrent](#page-418-1) inputs

#### **R**

RAG (see retrieval-augmented generation)

RAG-Fusion strategy, [RAG-Fusion](#page-197-2)-[RAG-Fusion](#page-205-2)

RAPTOR (recursive abstractive processing for tree-organized

[retrieval\), RAPTOR:](#page-156-3) Recursive Abstractive Processing for

Tree-Organized Retrieval

rate limiting, [Security](#page-467-2)

ReAct [architecture, L](#page-322-2)[angChain](#page-35-1) and Why It's Important, The

Plan-Do Loop

real-time collaboration, [Collaborative](#page-543-1) Editing with LLMs reciprocal rank fusion (RRF) [algorithm,](#page-205-2) [RAG-Fusion](#page-197-2)[-RAG-](#page-205-2)

Fusion

record management, Tracking Changes to Your [Documents](#page-138-2)-Tracking Changes to Your [Documents](#page-147-1)

recursive abstractive processing for tree-organized retrieval

[\(RAPTOR\), RAPTOR:](#page-156-3) Recursive Abstractive Processing for

Tree-Organized Retrieval

reflection prompting technique, [Reflection](#page-354-0)[-Reflection](#page-366-0)

reflection step, Ambient [Computing](#page-548-3)

regression testing, [Regression](#page-503-3) Testing

reinforcement learning from human feedback (RLHF),

[Instruction-Tuned](#page-19-1) LLMs

reliability, Cognitive [Architectures](#page-278-2) with [LangGraph, Patterns](#page-385-4)

to Make the Most of LLMs, [Building](#page-537-3) with LLMs

reranking/reordering, [RAG-Fusion](#page-199-0)

[response, evaluating, Evaluating](#page-507-0) an Agent's End-to-End

Performance

retrieval process, Retrieving Relevant [Documents](#page-172-0)

retrieval-augmented generation (RAG)

building robust RAG [systems, Generating](#page-182-0) LLM Predictions Using Relevant Documents

core stages of, Retrieving Relevant [Documents](#page-166-3)

[definition](#page-95-4) of term, The Goal: Picking Relevant Context for

LLMs

generating LLM [predictions, Generating](#page-175-1) LLM Predictions Using Relevant [Documents-Generating](#page-184-0) LLM Predictions Using Relevant Documents

introduction to, Introducing [Retrieval-Augmented](#page-164-2)

Generation

process of, RAG Part II: [Chatting](#page-163-1) with Your Data prompting with, [Retrieval-Augmented](#page-27-1) Generation query handling

construction, Query [Construction-](#page-224-1)[Text-to-SQL](#page-234-0) routing, Query [Routing-](#page-211-0)[Semantic](#page-223-0) Routing transformation, Query [Transformatio](#page-184-1)[n-Hypothetical](#page-211-1) Document Embeddings

retrieving relevant [documents, Retrieving](#page-166-2) Relevant

Documents-Retrieving Relevant [Documents](#page-174-0)

self-corrective RAG, The Design Stage: [Self-Corrective](#page-472-0) RAG-The Design Stage: [Self-Corrective](#page-486-1) RAG

Rewrite-Retrieve-Read strategy, [Rewrite-Retrieve-Read](#page-185-2)-

[Rewrite-Retrieve-Read](#page-190-1)

RLHF (reinforcement learning from human feedback),

[Instruction-Tuned](#page-19-1) LLMs

roles, [Dialogue-Tuned](#page-20-6) LLMs, Using LLMs in [LangChain](#page-55-2)

router [architecture, A](#page-313-0)[rchitecture](#page-298-0) #3: Router-Architecture #3:

Router

routing

logical routing, Logical [Routing](#page-212-1)-Logical [Routing](#page-219-1) query routing, Query [Routing](#page-211-0)[-Semantic](#page-223-0) Routing semantic routing, [Semantic](#page-219-3) Routing-[Semantic](#page-223-0) Routing RRF (reciprocal rank fusion) algorithm, [RAG-Fusion](#page-197-2) runnable interface, Using the [Runnable](#page-77-3) Interface runs (LangGraph Platform), [Runs](#page-443-2) Russell, Stuart, Agent [Architecture](#page-315-3)

sandboxing, [Security](#page-465-2) save and send, [Collaborative](#page-542-2) Editing with LLMs security best practices, [Security](#page-464-2) self-correction, The Design Stage: [Self-Corrective](#page-474-0) RAG self-critique prompting technique, [Reflection](#page-354-2) semantic embeddings, Semantic [Embeddings](#page-103-0) Explained-Semantic [Embeddings](#page-106-1) Explained semantic relationships, [Splitting](#page-114-2) Your Text into Chunks semantic routing, [Semantic](#page-219-2) Routing-[Semantic](#page-223-0) Routing sensitive data, protecting, [Security](#page-466-3) single [steps, evaluating, Evaluating](#page-507-1) an Agent's End-to-End Performance sparse embeddings, [Embeddings](#page-100-3) Before LLMs

specialized subsystems, Multi-Agent [Architectures](#page-374-3) state, [Introducing](#page-247-1) LangGraph, Creating a [StateGraph,](#page-251-1)

[Human-in-the-Loop](#page-403-1) [Modalities, Collaborative](#page-544-1) Editing with

LLMs

statefulness, [Introducing](#page-243-4) LangGraph

StateGraph

adding memory to, Adding Memory to [StateGraph](#page-257-1)[-Adding](#page-262-0) Memory to StateGraph

creation, Creating a [StateGraph-](#page-249-1)Creating a [StateGraph](#page-257-3) stateless runs (LangGraph Platform), [Stateless](#page-447-0) runs

[statelessness, Using](#page-237-2) LangGraph to Add Memory to Your Chatbot

static few-shot prompting, Few-Shot [Prompting](#page-32-2) stream method, Using the [Runnable](#page-77-0) Interface, [Summary](#page-91-0),

[Intermediate](#page-396-3) Output

streaming (LangGraph Platform), [Streaming](#page-444-0)

streaming chat, [Interactive](#page-540-2) Chatbots

structured output

human-in-the-loop [modalities, Human-in-the-Loop](#page-402-0)

Modalities[-Fork](#page-417-2)

intermediate [output, I](#page-400-3)[ntermediate](#page-395-0) Output-Intermediate

Output

need for, [Structured](#page-389-1) Output

strategies to achieve, [Structured](#page-390-1) Output

streaming LLM output [token-by-token, Streaming](#page-400-4) LLM

Output Token-by-Token

subagents, Supervisor [Architecture](#page-379-0)

subgraphs

adding to parent graphs, Subgraphs in [LangGraph](#page-367-0)

calling subgraphs directly, Calling a [Subgraph](#page-367-1) Directly-

Calling a [Subgraph](#page-370-0) with a Function

calling subgraphs with [functions, Calling](#page-370-0) a Subgraph with

a Function

use cases for, Subgraphs in [LangGraph](#page-366-1)

subsystems, specialized, Multi-Agent [Architectures](#page-374-3) Supabase, [Vector](#page-428-0) Store supervisor architecture, Multi-Agent [Architectures-](#page-376-0)Supervisor [Architecture](#page-383-0) synthetic data, [Creating](#page-487-2) Datasets system role, [Dialogue-Tuned](#page-20-7) LLMs, Using LLMs in [LangChain](#page-55-3) SystemMessage interface, Using LLMs in [LangChain](#page-57-4)

### **T**

tables, [MultiVectorRetriever](#page-147-2) task [managers,](#page-548-4) [Collaborative](#page-544-2) Editing with LLMs, Ambient Computing task-specific datasets, [Instruction-Tuned](#page-18-0) LLMs task\_result events, [Intermediate](#page-400-5) Output temperature parameter, Using LLMs in [LangChain](#page-54-4) testing design stage, The Design Stage: [Self-Corrective](#page-472-0) RAG-The Design Stage: Self-Corrective RAG key stages of app [development, Testing](#page-470-0) Techniques Across the LLM App Development Cycle [predeployment, Test](#page-455-1) Your [LangGraph](#page-450-0) App Locally-Test Your LangGraph App Locally [preproduction](#page-530-1) stage, The [Preproduction](#page-486-2) Stage-Testing an agent's trajectory

production [stage, P](#page-535-0)[roduction](#page-530-4)[-Monitoring](#page-535-0) and Fixing Errors

text

converting documents into text, Converting Your

Documents into [Text-Converting](#page-109-0) Your [Documents](#page-114-0) into Text

converting text to [numbers, Embeddings:](#page-97-0) Converting Text

to Numbers-Semantic [Embeddings](#page-106-1) Explained

generating text embeddings, Generating Text [Embeddings-](#page-122-1)

Generating Text [Embeddings](#page-125-1)

mixed with tables, [MultiVectorRetriever](#page-147-2)

splitting text into chunks, [Splitting](#page-114-1) Your Text into Chunks-

[Splitting](#page-122-2) Your Text into Chunks

text-to-metadata [filter, T](#page-230-3)[ext-to-Metadata](#page-225-1) Filter-Text-to-

Metadata Filter

text-to-SQL translations, [Text-to-SQL](#page-230-4)-[Text-to-SQL](#page-234-0)

third-party services, [LangChain](#page-34-3) and Why It's Important

threads, Adding Memory to [StateGrap](#page-260-0)[h, Handle](#page-418-2)

independently

threads (LangGraph Platform), [Threads](#page-442-1)

token-by-token streaming [output, Streaming](#page-400-4) LLM Output

Token-by-Token

tokens, Brief [Primer](#page-15-0) on LLMs

tool-calling technique

agentic LLM applications and, Agent [Architecture](#page-316-1)

always calling tools first, [Always](#page-332-0) Calling a Tool First-[Always](#page-342-1) Calling a Tool First dealing with many tools, [Dealing](#page-342-2) with Many Tools-Dealing with Many [Tools, Multi-Agent](#page-352-0) [Architectures](#page-374-4) definition of term, Tool [Calling](#page-28-0) integrations provided [for, LangChain](#page-34-4) and Why It's Important interactive chatbots and, [Interactive](#page-541-5) Chatbots structured output with, [Structured](#page-390-2) Output tracing, [Tracing](#page-531-0) [trajectory, evaluating, Evaluating](#page-507-2) an Agent's End-to-End [Performance, Testing](#page-530-1) an agent's [trajectory-](#page-520-1)Testing an agent's trajectory transformer neural network [architecture, Brief](#page-16-2) Primer on LLMs triggers, Ambient [Computing](#page-547-0) trimming messages, [Trimming](#page-262-2) Messages[-Trimming](#page-267-1) Messages try-catch statement, [Human-in-the-Loop](#page-408-2) Modalities

### **U**

undo/redo stacks, [Collaborative](#page-545-5) Editing with LLMs Universally Unique Identifiers [\(UUIDs\), Adding](#page-260-1) Memory to StateGraph

updates mode (LangGraph), [Intermediate](#page-399-1) Output

user role, [Dialogue-Tuned](#page-20-8) LLMs, Using LLMs in [LangChain](#page-55-4)

**V**

values mode (LangGraph), [Intermediate](#page-399-2) Output variance, [Patterns](#page-387-2) to Make the Most of LLMs vector indexes, [LangChain](#page-35-5) and Why It's Important vector stores alternative providers for, LLM [Fundamentals](#page-48-2) with LangChain definition of [term, L](#page-97-4)[angChain](#page-35-6) and Why It's Important, The Goal: Picking Relevant Context for LLMs deployment example, [Vector](#page-427-2) Store storing embeddings in vector stores, Storing Embeddings in a Vector [Store-Working](#page-128-1) with Vector Stores version control, [Collaborative](#page-542-3) Editing with LLMs VSCode code editor, [Interactive](#page-540-3) Chatbots

**W**

Weaviate, LLM [Fundamentals](#page-48-3) with LangChain webhooks (LangGraph Platform), [Webhooks](#page-448-2)

**X**

XML format, Other [Machine-Readable](#page-75-3) Formats with Output Parsers

#### **Y**

Yao, Shunyu, The [Plan-Do](#page-322-3) Loop

#### **Z**

zero-shot prompting, Zero-Shot [Prompting](#page-24-0) Zod, JSON [Output](#page-74-1)

## About the Authors

**Mayo Oshin** is a tech entrepreneur, AI advisor, and angel investor. Mayo was an early developer contributor and advocate for the open source LangChain library and an early pioneer in the popular AI "chat" with data movement (5+ million people reached through his thought-leadership ideas so far).

Mayo has consulted with, advised, and trained hundreds of engineers and product managers at various leading institutions, including Amazon, LinkedIn, Evercore, Visa, and BCG.

You can learn more about him at his website, *[mayooshin.com](https://mayooshin.com/)*, and get his latest ideas on AI and technology on [X.](https://x.com/mayowaoshin)

**Nuno Campos** is a founding software engineer at LangChain, Inc. Nuno has a decade of experience as a Python and JavaScript software engineer, architect and open source maintainer. He has worked for various tech startups in software engineering and data science roles. He holds an MSc in Finance.

## Colophon

The animals on the cover of *Learning LangChain* are European tree frogs (*Hyla arborea*).

They are primarily found in mainland Europe, typically close to vegetation. Their green skin can adjust its color from green to grey or brown, depending on a variety of factors. This ability helps to camouflage them from predators. They also use their sticky tongues (for meals, i.e., insects) and the sticky pads on their feet (for movement) to navigate life in their habitat.

During mating season, European tree frogs congregate close to ponds so that they can lay eggs near water for the soon-to-be tadpoles. The males perform a mating call that is striking for its volume, particularly when many frogs are gathered in one place. The females then lay clumps of 800 to 1,000 eggs. About 10 to 14 days later, the tadpoles hatch, and the cycle of life begins anew.

Many of the animals on O'Reilly covers are endangered; all of them are important to the world.

The cover illustration is by Karen Montgomery, based on an antique line engraving from *Meyers Kleines Lexicon*. The series design is by Edie Freedman, Ellie Volckhausen, and Karen Montgomery. The cover fonts are Gilroy Semibold and Guardian Sans. The text font is Adobe Minion Pro; the heading font is Adobe Myriad Condensed; and the code font is Dalton Maag's Ubuntu Mono.

![](_page_599_Picture_1.jpeg)

*Your gateway to knowledge and culture. Accessible for everyone.* 

![](_page_599_Figure_3.jpeg)