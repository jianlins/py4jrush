
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

```bash
pip install py4jrush
```

## Development and Release Process

This project uses automated workflows for building, testing, and releasing. Here's how it works:

### Automated Release Workflow

The project has an automated release workflow that:
1. **Automatically bumps version numbers** using semantic versioning
2. **Builds and tests** the package across multiple environments  
3. **Publishes to PyPI** with proper validation
4. **Creates GitHub releases** with built artifacts

### How to Release

#### Option 1: Manual Workflow Trigger (Recommended)
1. Go to the **Actions** tab in GitHub
2. Select **Build and Publish Python Package** workflow
3. Click **Run workflow** and configure:
   - **Publish to PyPI**: `true` (to actually publish)
   - **Create GitHub release**: `true` (to create a release)
   - **Version bump type**: Choose `patch`, `minor`, or `major`

#### Option 2: GitHub Release Creation
Create a new release in the GitHub UI, and the workflow will automatically trigger.

### Version Bumping Strategy
- **patch** (1.0.10 → 1.0.11): Bug fixes, small changes
- **minor** (1.0.10 → 1.1.0): New features, backwards compatible
- **major** (1.0.10 → 2.0.0): Breaking changes

### Workflow Features
- ✅ **Automatic version detection** from current VERSION file
- ✅ **Smart version bumping** prevents conflicts with existing releases
- ✅ **Multi-environment testing** (Python 3.9, 3.10, 3.11 on Ubuntu, Windows, macOS)
- ✅ **PyPI validation** with twine before publishing
- ✅ **Automatic VERSION file updates** after successful release 
- ✅ **GitHub release creation** with built artifacts

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
from spacy.lang.en import English

nlp = English()
nlp.add_pipe("medspacy_py4jrush")
doc = nlp("This is a sentence. This is another sentence.")
print('\n'.join([str(s) for s in doc.sents]))
```
