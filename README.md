# WikiQA
This is a PyTorch implementation of the WikiQA system described in the ACL 2017 paper [Reading Wikipedia to Answer Open-Domain Questions](https://arxiv.org/abs/1704.00051).

## Quick Links

- [About](#machine-reading-at-scale)

## Machine Reading at Scale

<p align="center"><img width="70%" src="img/WikiQA.png" /></p>

WikiQA is a system for reading comprehension applied to open-domain question answering. In particular, WikiQA is targeted at the task of "machine reading at scale" (MRS). In this setting, we are searching for an answer to a question in a potentially very large corpus of unstructured documents (that may not be redundant). Thus the system has to combine the challenges of document retrieval (finding the relevant documents) with that of machine comprehension of text (identifying the answers from those documents).

Our experiments with WikiQA focus on answering factoid questions while using Wikipedia as the unique knowledge source for documents. Wikipedia is a well-suited source of large-scale, rich, detailed information. In order to answer any question, one must first retrieve the few potentially relevant articles among more than 5 million, and then scan them carefully to identify the answer.

Note that WikiQA treats Wikipedia as a generic collection of articles and does not rely on its internal graph structure. As a result, **_WikiQA can be straightforwardly applied to any collection of documents_**, as described in the retriever [README](scripts/retriever/README.md).

This repository includes code, data, and pre-trained models for processing and querying Wikipedia as described in the paper -- see [Trained Models and Data](#trained-models-and-data). We also list several different datasets for evaluation, see [QA Datasets](#qa-datasets). Note that this work is a refactored and more efficient version of the original code. Reproduction numbers are very similar but not exact.

## Quick Start: Demo

[Install](#installing-WikiQA) WikiQA and [download](#trained-models-and-data) our models to start asking open-domain questions!

Run `python scripts/pipeline/interactive.py` to drop into an interactive session. For each question, the top span and the Wikipedia paragraph it came from are returned.

```
>>> process('What is question answering?')

Top Predictions:
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
| Rank |                                                  Answer                                                  |        Doc         | Answer Score | Doc Score |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+
|  1   | a computer science discipline within the fields of information retrieval and natural language processing | Question answering |    1917.8    |   327.89  |
+------+----------------------------------------------------------------------------------------------------------+--------------------+--------------+-----------+

Contexts:
[ Doc = Question answering ]
Question Answering (QA) is a computer science discipline within the fields of
information retrieval and natural language processing (NLP), which is
concerned with building systems that automatically answer questions posed by
humans in a natural language.
```

```
>>> process('What is the answer to life, the universe, and everything?')

Top Predictions:
+------+--------+---------------------------------------------------+--------------+-----------+
| Rank | Answer |                        Doc                        | Answer Score | Doc Score |
+------+--------+---------------------------------------------------+--------------+-----------+
|  1   |   42   | Phrases from The Hitchhiker's Guide to the Galaxy |    47242     |   141.26  |
+------+--------+---------------------------------------------------+--------------+-----------+

Contexts:
[ Doc = Phrases from The Hitchhiker's Guide to the Galaxy ]
The number 42 and the phrase, "Life, the universe, and everything" have
attained cult status on the Internet. "Life, the universe, and everything" is
a common name for the off-topic section of an Internet forum and the phrase is
invoked in similar ways to mean "anything at all". Many chatbots, when asked
about the meaning of life, will answer "42". Several online calculators are
also programmed with the Question. Google Calculator will give the result to
"the answer to life the universe and everything" as 42, as will Wolfram's
Computational Knowledge Engine. Similarly, DuckDuckGo also gives the result of
"the answer to the ultimate question of life, the universe and everything" as
42. In the online community Second Life, there is a section on a sim called
43. "42nd Life." It is devoted to this concept in the book series, and several
attempts at recreating Milliways, the Restaurant at the End of the Universe, were made.
```

```
>>> process('Who was the winning pitcher in the 1956 World Series?')

Top Predictions:
+------+------------+------------------+--------------+-----------+
| Rank |   Answer   |       Doc        | Answer Score | Doc Score |
+------+------------+------------------+--------------+-----------+
|  1   | Don Larsen | New York Yankees |  4.5059e+06  |   278.06  |
+------+------------+------------------+--------------+-----------+

Contexts:
[ Doc = New York Yankees ]
In 1954, the Yankees won over 100 games, but the Indians took the pennant with
an AL record 111 wins; 1954 was famously referred to as "The Year the Yankees
Lost the Pennant". In , the Dodgers finally beat the Yankees in the World
Series, after five previous Series losses to them, but the Yankees came back
strong the next year. On October 8, 1956, in Game Five of the 1956 World
Series against the Dodgers, pitcher Don Larsen threw the only perfect game in
World Series history, which remains the only perfect game in postseason play
and was the only no-hitter of any kind to be pitched in postseason play until
Roy Halladay pitched a no-hitter on October 6, 2010.
```

Try some of your own! Of course, WikiQA might provide alternative facts, so enjoy the ride.


Default model paths for the different modules can also be modified programmatically in the code, e.g.:


#### Document Retriever

TF-IDF model using Wikipedia (unigrams and bigrams, 2^24 bins, simple tokenization), evaluated on multiple datasets (test sets, dev set for SQuAD):

| Model | SQuAD P@5 | CuratedTREC P@5 | WebQuestions P@5 | WikiMovies P@5 | Size |
| :---: | :-------: | :-------------: | :--------------: | :------------: | :---: |
| [TF-IDF model](https://dl.fbaipublicfiles.com/WikiQA/docs-tfidf-ngram%3D2-hash%3D16777216-tokenizer%3Dsimple.npz.gz) | 78.0 | 87.6 | 75.0 | 69.8 | ~13GB |

_P@5 here is defined as the % of questions for which the answer segment appears in one of the top 5 documents_.

#### Document Reader

Model trained only on SQuAD, evaluated in the SQuAD setting:

| Model | SQuAD Dev EM | SQuAD Dev F1 | Size |
| :---: | :-----------:| :----------: | :--: |
| [Single model](https://dl.fbaipublicfiles.com/WikiQA/single.mdl) | 69.4 | 78.9 | ~130MB |

Model trained with distant supervision without NER/POS/lemma features, evaluated on multiple datasets (test sets, dev set for SQuAD) in the full Wikipedia setting:

| Model | SQuAD EM | CuratedTREC EM | WebQuestions EM | WikiMovies EM | Size |
| :---: | :------: | :------------: | :-------------: | :-----------: | :--:
| [Multitask model](https://dl.fbaipublicfiles.com/WikiQA/multitask.mdl) | 29.5 | 27.2 | 18.5 | 36.9 | ~270MB |

#### Wikipedia

Our full-scale experiments were conducted on the 2016-12-21 dump of English Wikipedia. The dump was processed with the [WikiExtractor](https://github.com/attardi/wikiextractor) and filtered for internal disambiguation, list, index, and outline pages (pages that are typically just links). We store the documents in an sqlite database for which `WikiQA.retriever.DocDB` provides an interface.

| Database | Num. Documents | Size |
| :------: | :------------: | :-----------------: |
| [Wikipedia](https://dl.fbaipublicfiles.com/WikiQA/docs.db.gz) | 5,075,182 | ~13GB |
