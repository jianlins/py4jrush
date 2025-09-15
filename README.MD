# py4jrush

py4jrush is the python interface to
RuSH(https://github.com/jianlins/RuSH) (**Ru** le-based sentence **S**
egmenter using **H** ashing), which is originally developed using Java. 
This version is implemented through py4j, compared with the original PyRuSH.

RuSH is an efficient, reliable, and easy adaptable rule-based sentence
segmentation solution. It is specifically designed to handle the
telegraphic written text in clinical note. It leverages a nested hash
table to execute simultaneous rule processing, which reduces the impact
of the rule-base growth on execution time and eliminates the effect of
rule order on accuracy.

If you wish to cite RuSH in a publication, please use:

Jianlin Shi ; Danielle Mowery ; Kristina M. Doing-Harris ; John F.
Hurdle.RuSH: a Rule-based Segmentation Tool Using Hashing for Extremely
Accurate Sentence Segmentation of Clinical Text. AMIA Annu Symp Proc.
2016: 1587.

The full text can be found
[here](https://knowledge.amia.org/amia-63300-1.3360278/t005-1.3362920/f005-1.3362921/2495498-1.3363244/2495498-1.3363247?timeStamp=1479743941616).


## Installation

When you run `pip install py4jrush`, the installer will automatically check for Java JDK 8. If JDK 8 is not found, it will use the [install-jdk](https://pypi.org/project/install-jdk/) Python package to download and install JDK 8 for you. No manual Java setup is required.

> pip install py4jrush

## How to use

A standalone RuSH class is available to be directly used in your code.
From 1.0.4, pyRush adopt spaCy 3.x api to initiate an component.

```python
from py4jrush import RuSH
input_str = "The patient was admitted on 03/26/08\n and was started on IV antibiotics elevation" +\
             ", was also counseled to minimizing the cigarette smoking. The patient had edema\n\n" +\
             "\n of his bilateral lower extremities. The hospital consult was also obtained to " +\
             "address edema issue question was related to his liver hepatitis C. Hospital consult" +\
             " was obtained. This included an ultrasound of his abdomen, which showed just mild " +\
             "cirrhosis. "
rush = RuSH('../conf/rush_rules.tsv')
sentences=rush.segToSentenceSpans(input_str)
for sentence in sentences:
    print("Sentence({0}-{1}):\t>{2}<".format(sentence.begin, sentence.end, input_str[sentence.begin:sentence.end]))
```
## Spacy Componentized py4jrush

Start from version 1.0.3, py4jrush adds Spacy compatible Sentencizer
component: PyRuSHSentencizer.

```python
from py4jrush import PyRuSHSentencizer
from spacy.lang.en
import English \>\>\> nlp = English() \>\>\>
nlp.add_pipe("medspacy_py4jrush")
doc = nlp("This is a sentence. This is another sentence.")
print('n'.join(\[str(s) for s in doc.sents\]))
```
