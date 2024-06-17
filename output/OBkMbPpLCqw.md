# Summary

The talk presents methods to develop high-quality small language models using innovative data synthesis, distillation techniques, and efficient use of classical statistical methods without resorting to extreme scale pre-training or large-scale supervised datasets. Key points include:

1. **Challenge to Sam Altman’s Viewpoint**:
    - Sam Altman claimed it was hopeless for Indian startups to create foundational models due to compute limitations.
    - The speaker encourages not giving up and discusses creating innovative, smaller models that can compete with large ones.

2. **Innovative Distillation Approach**:
    - Begin with a small, low-quality model (e.g., GPT-2) and generate a high-quality small model.
    - This involves synthesizing innovative and novel data that OpenAI may not have, bypassing the limitations of starting with a large model.

3. **Task-Specific Symbolic Knowledge Distillation**:
    - Small models aren't necessarily outclassed by large proprietary models.
    - Evidence from various counterexamples shows efficacy in specific tasks using symbolic knowledge distillation.

4. **Learning to Abstract in Language**:
    - A practical example focused on summarizing sentences using small models without relying on extreme-scale pre-training or data.
    - Innovations in neurological decoding and aggressive filtration (using entailment classifiers) allow for generating valuable training data from poor initial outputs.

5. **Competing with GPT-3**:
    - Using a distilled approach, they were able to produce high-quality summarization data and compete favorably against GPT-3 by filtering and incremental training.
    - Proposed method competes even against ChatGPT-3.5 using a smaller model, refined data filtration, and information-theoretic distillation.

6. **Phineagram Framework**:
    - Utilizing classical statistical n-gram models (n equals infinity) to compute over trillions of tokens rapidly without GPUs.
    - Implementation highlights the use of suffix arrays to dynamically compute n-gram statistics, demonstrating fast and cost-effective processing.

7. **Real-world Implications**:
    - Innovations in synthesized data are crucial for future AI improvements.
    - Projects like Meta’s Segment Anything and Microsoft’s Textbooks are All You Need show synthesized data's potential in enhancing the quality of models.
    - Better data quality contributes significantly more than just increasing the quantity.

8. **Conclusion**:
    - Emphasizes the importance of data quality, novelty, and diversity over mere scale.
    - Future AI models will benefit from innovative data synthesis and distillation, enhancing small model capabilities.

The talk challenges prevailing assumptions about the need for scaling in AI, advocating for smarter, more innovative methods to unlock the potential of smaller models.

# Transcription

 All right. So I'm here to share with you impossible possibilities. So last year when Sam Altman was asked, how can Indian startups create foundation models for India, he said, don't bother, it's hopeless. Whoa. First of all, I hope that Indian startups didn't give up and will not give up. Second of all, this conversation could have happened anywhere else in US, any universities, or startups, or research institute without that much of compute. So here comes impossible distillation. How to cook your small language models in an environmentally friendly manner, and it tastes as good as the real thing. So currently what we hear as the winning recipe is extreme scale pre-training followed by extreme scale post-training such as RLHF. What if I told you I'm going to start with GPT2, that small low quality model that nobody talks about, and somehow, I don't know why, but somehow we're going to create or squeeze out high quality small model and then compete against much stronger model that may be two orders of magnitude larger. Now this should really sound impossible, especially when you might have heard of a paper like this that says the false promise of imitating proprietary large language models. Although what they report is true for that particular evaluation experimental setup, they reported, please do not generalize, overgeneralize to conclude that all the small language models are completely out of league. Because there are numerous other counter example that demonstrate that task specific symbolic knowledge distillation can work across many different tasks and domains, some of which are from my own lab. Today though, let me just focus on one task which is going to be about how to learn to abstract in language. To simplify this task, let's begin with the sentence summarization as our first mission impossible. Here the goal is to achieve this without extreme scale pre-training, without LLHF at scale, and also without supervised data sets at scale because these things are not always necessarily available. But wait a minute, we have to use usually all three, at least some of them, but how are we supposed to do any good against larger model without any of this? So the key intuition is that current AI is as good as the data that it was trained on. We have to have some advantage, we cannot have zero advantage, so that advantage is going to come from data. By the way, we have to synthesize data because if already exists somewhere on the internet, open AI has already crawled it, that's not your advantage, they have it too. So you have to create something genuinely novel that's even better than what's out there. So usually distillation starts with large model, but we're going to toss that out just to show you how we may be blinded to the hidden possibilities. So I'm going to start just for demonstration purposes with GPT2, that poor low quality model, and then I'm going to do some innovations, which I'm going to sketch in a bit, to make high quality data set that can then be used to train small model that will become powerful model for a particular task. The only problem though is that GPT2 doesn't even understand your prompt, it cannot do prompt engineering using GPT2. You ask it to summarize your sentence, it generates some output, that does not make any sense. So then you try again because there's usually randomness to it, you can sample many different examples, like hundreds of examples, and we find that it's almost always no good, like less than 0.1% good. Where there's a wheel, there's can be what way. So we had multiple sequence of different ideas that included our neurologic decoding. This is plug and play inference time algorithm that can incorporate any logical constraints to your language model output. For any off the shelf models, we can plug and play this to guide the semantic space of the output. But because GPT2 is so bad, even with this, you know, the success ratio was only about 1%. But this is not 0. Now we're going somewhere. Because if you over generate a lot of samples and then filter out, you can actually gain some good examples this way. And then students, brilliant students came up with many different ideas. I'll gloss over the technical details, but we found some ways to increase the chance of success ratio to beyond the 10%. Just so that it's a little bit easier to find good examples. So then overall framework goes to something like this. You start with the poor teacher model, you over generate a lot of data points. And then because there's a lot of noise in your data, you have to do serious filtration. So here we use the three layer filtration system. The details are not very important, but let me highlight the first one, entailment to filter, which was based on off the shelf entailment classifier that can tell you whether a summary is logically entailed from the original text or not. This is off the shelf model. That's not perfect. It's maybe about 70 to 80% good. But it's good enough when you use this aggressively to filter out your data. Then we use that data to train smaller model, much smaller model, which can then become the teacher model for the next generation students. So we repeat this couple of times to make in the end high quality dim sum data and high quality model. When we evaluated this against the GPT-3, which was the best model of that time, so this actually was done before chat GPT came out, and we were able to beat that GPT-3, which was at that time the best summarization model out there. But since chat GPT came out, people are like whatever. Chat GPT can do everything, including summarization, so why should we bother? So here comes Mission Impossible 2, where we are now going to compete against chat GPT-3.5 and to make the challenge even harder for us. Now we are going to summarize documents, not just the sentences, and then we are also going to do all of this above without relying on that off the shelf entailment classifier. I mean in practice you can do that just like academically, we want it to see how much can we push the boundary against the commonly held assumption about the scale. So our new work in FOSM is information theoretic distillation method, where the key idea is instead of that off the shelf entailment filtration system, we are going to use some equations. That equation has actually only three lines of some conditional probability scores that you can compute using off the shelf language models. It's only 12 in the morning, so let's not drill into the details of the equations, but I can just tell you hand the wave that if you shuffle this around, you can interpret this as special cases of a point-wise mutual information, which you can use for the purpose of filtering your data. So we used the same overall framework as before. We now use PTH 2.8 billion parameter model because we liked it a little bit better than GPT2, and for the filtration, we are now using the three short equations that I showed you earlier. And then we do the same business. This time though, we make the model even smaller, 0.5 billion parameter model that leads to high-quality summarization data set as well as model. So how well do we do? Well, as promised, we do either as good as Chatcha PTH 3.5, at least for this task, or we do better depending on how you set up the evaluation challenges and benchmarks. You can check out more details in our paper. To summarize, I demonstrated how we can learn to summarize documents even without relying on extreme scale pre-trained models and many other things at scale. The real research question underlying these two papers though is this idea about how we can learn to abstract because right now, the recipes let's just make models super big, the bigger the better. But humans, you and I cannot really remember all the contexts, I don't know, like a million tokens. Nobody can remember a million tokens in your context. You just abstract away everything I told you instantaneously, but you still remember what I just said so far. That's really amazing human intelligence that we don't yet know how to build efficiently through AI models, and I believe that's possible. We're just not trying hard enough because we're blinded by just the magic of scale. Okay, so finally, in Phineagram is the third mission impossible. So switching the topic a little bit, now the mission is to make classical statistical Ngram language models somehow relevant to neural language models. How many of you even talk about Ngram models anymore? I don't know, do you even learn these days? Here, we're going to make N equals infinity. We're going to compute this over trillions of tokens, and the response time should be super instantaneous, and we're not even going to use a single GPU on this. Like, wow. Let me tell you how hard it is. So hypothetically, if you're going to index five trillion tokens in a classical Ngram language model with N equals infinity, then you're roughly speaking looking at two quadrillions of unique Ngram sequences that you somehow enumerate, sort, count, and store somewhere, which might take maybe 32 terabytes of disk space, maybe more, who knows, but it's too much. We cannot do that. And if you look at what other large-scale classical Ngram models other people have ever built, it was Google in 2007 due to Jeff Dean and others who only scanned two trillion tokens, I mean, it was a lot back then, up to five Ngrams, five Ngrams, which already give them about 300 billion of unique Ngram sequences that they have to enumerate, to sort, count, et cetera. So it's too many. People didn't do beyond that very much. So how on earth is it possible that we can actually blow this up to infinity? So before I reveal what we did, I invite you to go check out this online demo if you so desire, infinitygram.io slash demo. So you can look up any token you want. Here's one example highlighted, which has 48 characters. I don't know why that word even exists, but not only it exists, if you look it up, there are like more than 3,000 instances, and it shows you what millisecond it took. It's 5.5 milliseconds. And then it also shows you how you can tokenize that long word. You can also try multiple words to see which word comes next. So for example, actions speak louder than what? So it's going to show you on the web what are the other next word that comes, and again, it's a super fast. So what did we do? You'll be surprised to hear how simple this idea actually is. So there's something called the suffix array that I think not all algorithm classes teach, but some do. It's that data structure that's implemented very carefully. So we indexed the entire web corpus using this suffix array. And the truth is we don't pre-compute any of these ngram statistics. We just have this data structure ready to go. And when you call particular query, we compute this on the fly, but thanks to the data structure, we can do this super fast, especially when you do C++ implementation. I know people don't usually use that language anymore when it comes to AI research, but it's a good stuff that actually runs much faster. How chubis this? So it's only a few hundreds of dollars we spent for indexing the entire thing, and then even for servicing the APIs, you can get away with a pretty low cost. And it's really, really fast, even without GPUs, the latency for different types of API calls are just a few tens of milliseconds. You can do a lot of things with this. So one thing I can share with you right now is you can interpolate between your neural language models with our infineagram to lower the perplexity, which is the metric people often use for evaluating the quality of your language model across the board. And this is only the tip of the iceberg that I expect to see. I'm actually working on other stuff that I wish I could share, but I cannot yet. But we started serving this API and the point a few weeks ago, and already we serve the 60 million API calls, not counting our own access, so I'm really curious what people are doing with our infineagram. So concluding remarks. The TLDR of my talk is that AI, at least in the current form, is as good as the data that it was trained on. So the past and current AI usually depends primarily on human generated data, but it could really be that the future will rely on AI synthesized data. I know that there's a lot of concerns about this, that maybe the quality is not very good, there may be bias. So you cannot do this in a vanilla way. You should do it in a more innovative way, but there are many evidences piling up that this actually works. So segment anything by meta, is an example of AI synthesized annotation on images segmentations. Helped with human validation, but human alone couldn't annotate that many examples of images. Here's another example. Textbooks are all you need by Microsoft if I want to three. Again, this is a case where when you have really high quality data, textable quality data synthesized, you can actually compute against the larger counterpart across many, many different tasks. Maybe it's not as still general as larger models in some capacities, but this is amazing to serve a lot of business needs, where you may not need a general list, you may need a specialist. And also what textbook alludes to you is that quality is what matters. It's not just the brute force quantity, but it's quality. Dolly three is yet another example. Why is it better than Dolly two out of a sudden? Well, in large part because of better captions, but which better captions? The previous model used all the good captions. Well, they synthesized the captions. That's how you get high quality data. Of course, you have to do this with care, but there are many more piling examples of task-specific symbolic knowledge distillation, including the work of my own lab that demonstrate that this could really make smaller models, really unlock the hidden capabilities of small models. So it's really about quality, novelty, and diversity of your data, not just the quantity. And I'll end my talk here. Thank you.