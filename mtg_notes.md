### June 27, 2023
+ We talked about how the US PyCon (Python Conference) recently released their videos from their 2023 conference
  + [2023 sessions youtube channel](https://www.youtube.com/watch?v=eZwHvBsoPn4&list=PL2Uw4_HvXqvY2zhJ9AMUa_Z6dtMGF3gtb)
  + [PyCon YouTube home with past conference videos](https://www.youtube.com/@PyConUS)
+ Charles shared this article about “typo squatting” popular Python modules names to trick users to install malaware: https://arstechnica.com/information-technology/2023/02/451-malicious-packages-available-in-pypi-contained-crypto-stealing-malware/
+ Charles also talked about a project at the University of Miami that collects data from Twitter for research purposes. He mentioned that there is now a an API limit to only be able to check 7 days in the past. He will post the name of the Python module they are using to
+ Eric mentioned issues that he has had issues archiving older tweets in the past. Also mentioned challenges evaluating misspelled words and how to interpret emojis.
+ Talked about unit testing and test coverage with the Python project called [coverage](https://coverage.readthedocs.io/en/7.2.7/)
+ Tomasz mentioned [coveralls](https://coveralls.io/) that gives you nice visual reports on your test coverage that can be integrated with Github and be part of CI
+ we of course talked about using [Pytest](https://docs.pytest.org/en/7.3.x/) for your unit tests
+ For those that are unfamiliar with “unit tests” and “pytest” here a presentation Yamil gave this group a few months ago [“Intro to unit testing in Python”](
https://docs.google.com/presentation/d/1t1dl7SANyhp4uClRP2JsijWj05nr5AkbUJIAB66GKFQ/edit?usp=sharing)
+ We talked a bit about parallel processing in Python to finish work faster
+ We shared a link to the [free version of chapter 17 of the 2nd edition of “Automate the Boring Stuff with Python”](https://automatetheboringstuff.com/2e/chapter17/)
+ Yamil brought up a suggested approach by the author (Al Sweigart) of “Automate the Boring Stuff with Python” to download files from the internet using the python request module, but in a way that you will not be limited by the amount of free RAM on your computer ([section: Saving Downloaded Files to the Hard Drive](https://automatetheboringstuff.com/2e/chapter12/))
  + Here is the snippet that uses a loop with the iter_content() method, to prevent using up all your RAM if the file is larger than the amount of free RAM on your system...

```python
import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)
```
+ Also we mentioned [networkX](https://networkx.org/): NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
+ Tomasz ask if anyone was doing any batch work on images with Python, to find a faster way to process a larger number of images. We talked about perhaps using multiprocessing for this.
  + Again from the book ["Automating stuff with Python", Ch 19](https://automatetheboringstuff.com/2e/chapter19/) talks about using the [Pillow](https://python-pillow.org/) Python module batch change images
  + Also there should be ways to use very well known non-python library called ImageMagick, but controlled through Python, for batch making changes to images. Yamil has worked with many projects like the Drupal/PHP based Islandora project, that use ImageMagick for making changes to images

### June 13, 2023
+ Python podcasts suggestion from Tomasz: [PythonBytes](https://pythonbytes.fm/)
+ David talked about an new Python module called “Pandas AI” that did find useful if you have a paid chatGPT account
  + https://github.com/gventuri/pandas-ai
  + “Pandas AI is a Python library that integrates generative artificial intelligence capabilities into Pandas, making dataframes conversational”
  + David id also find a poorly written blog post that was claiming featured that Pandas AI does NOT have, so stay away from this article…
    + https://levelup.gitconnected.com/introducing-pandasai-the-generative-ai-python-library-568a971af014
+ We talked about when we have used chatGPT to write some Python code snippets, and what were our results.
  + The results were mostly positive, but we talked about the benefits of already knowing Python well enough to formulate request more precisely and evaluate how well the chatGPT responses were
  + Someone mentioned that chatGPT has become as an alternative to StackOverflow, specially if you are in a hurry
  + Someone mentioned Github Copilot: “Those of us who have GitHub educator accounts have free access to Copilot. Have not tried it. Very reluctant, personally.” Which uses AI to write code for you.
    + https://en.wikipedia.org/wiki/GitHub_Copilot
    + As a counter argument there is this article [“Why I don’t use Copilot”](https://inkdroid.org/2023/06/04/copilot/)
  + Will StackOverflow become obsolete with the revolution in AI? Yamil thinks that it is a good inspiration for prompts, and still has great information
  + We saw an example of sharing a snippet of object oriented Python code to ask chatGPT to explain what is missing
  + One of the participants was glad to get the explanations from chatGPT of what was missing in their object oriented code
    + Here is the link to the chat https://chat.openai.com/share/fea426fb-cb02-4b38-9f42-128f59115fc4
  + A recent Code4Lib article that talked about using AI generated code was shared [“Utilizing R and Python for Institutional Repository Daily Jobs”](https://journal.code4lib.org/articles/17134)
  + We briefly talked about the ethics of using AI written code that was trained on code that other published publicly on Github, but without their explicit consent
  + Podcast example crated by AI:
    “I’ve been listening to this series in the Planet Money podcast where they try to make an entire podcast episode made by AI:” https://www.npr.org/series/1178395718/planet-money-makes-an-episode-using-ai
  + Charles asked if anyone was using Python to automate work with the Azure cloud computing platform
    + https://en.wikipedia.org/wiki/Microsoft_Azure
    + We briefly talked about [“Azure Functions”](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp) which seem similar to [AWS Lambda](https://en.wikipedia.org/wiki/AWS_Lambda)
+ We talked about a great site and free book that many people use to get started with Python [“Python for Everyone”](https://www.py4e.com/)
+ We also talked about the well known and still very popular Python [Requests](https://requests.readthedocs.io/en/latest/) module, and but also the newer and “async compatible” [HTTPX](https://www.python-httpx.org/) module, which was also mentioned on the Python Slack channel.

### May 30, 2023
+ David shared his code utlizing `pymarc` to harvest and clean OCLC records. An older example of code: https://github.com/derlandson/PyCat
+ Demo of Match MARC toolset as well.
+ Tomasz reported his first experiences using `pymarc` v.5
+ Discussed a potential `pymarc` feature ordering subfields accoding to a particular field cataloging practice
  + challenge: no clear, outlined rules to based it on
+ Rebecca demoed a script created to have circ desk staff click a single button for simple questions (directions, tech, find a book, etc.) Creates output file and emails results as csv once per month.
 Currently doesn’t need admin permissions but various features may impact this.
  + simplified `pyinstaller` app: [auto-py-to-exe]
(https://pypi.org/project/auto-py-to-exe/) was used to help redeploy to other PCs.

### May 16, 2023
+ We had a brief discussion about [pymarc](https://pymarc.readthedocs.io/en/latest/) and [MARC authority data](https://www.loc.gov/marc/authority/ecadhome.html)
  + sparked by Benjamin's issues with using pymarc for authority records
  + Tomasz run some quick tests and they looked good: `pymarc` was able to read such data, but more tests are needed to see if manipulating and writing is done correctly. There were concerns about differences in the leader field between the bibliographic and authority data

#### Ed Summers intro to new pymarc
+ David introduced Ed
+ Ed stated pymarc is work of many people, Ed's involvement is more of the maintainer

##### Breaking changes in pymarc v.5:
+ new class `pymarc.Field.Subfield`
+ helper properties instead of methods
  + old: record.title(), new: record.title
  + old: record.publisher(), new: record.publisher
+ automatically sets UTF-8 code in record leader in the position 9
  + pymarc always converts data to unicode, but before it did not attempt to change the code in the leader to reflect that
  + most people don't want to write MARC-8, and want UTF-8 encoded data

+ Ed shows off doing live coding! Uses [Google Colab](https://colab.research.google.com/) and Jupyter notebooks (tip: you can pip install packages in Colab: `!pip install pymarc`, the exclamation mark will tell the notbook cell in not a code but a command line script)
+ Ed shows initiating new record instance, and adding fields with the new model for subfields
+ `Subfield` is a python [`namedtuple`](https://docs.python.org/3.10/library/collections.html?highlight=namedtuple#collections.namedtuple)

*New:*
```python
from pymarc import Record, Field, Subfield

record = Record()
record.add_field(
    Field(
        tag="245",
        indicators=["0", "0"],
        subfields=[
            Subfield(code="a", value="Foo :"),
            Subfield(code="b", value=" bar /"),
            Subfield(code="c", value="Spam.")
        ]
    ))
```
or simply:
```python
field = Field(
    tag="245",
    indicators=["0", "0"],
    subfields=[
        Subfield("a", "Foo :"),
        Subfield("b", "bar /"),
        Subfield("c", "Spam.")
    ])
```

*old*
```python
record.add_field(
    Field(
        tag="245",
        indicators=["0", "0"],
        subfields=["a", "Foo :", "b", "bar /", "c", "Spam."]
    ))
```

+ New model has advantages over subfiels as a list of strings:
  + matches how cataloger's think about subfields - as code-value pairs (Tomasz)
  + helps guard against errors such as missing an element to properly create a subfield


+ discussed briefly differences between pymarc and similar Pearl library [MARC::Record]https://metacpan.org/pod/MARC::Record()
+ Ed showed a tip how to avoid malformed or otherwise invalid records when looping over a file:
Ed errors looping over return None (malformed bibs, leader lenght problems, )

```python
from pymarc import MARCReader

with open("foo.mrc", "rb") as marcfile:
    reader = MARCReader(marcfile)
    for record in reader:
        if record is None:
            print(reader.current_exception)
        else:
          # do something
```

+ talked about potential new features in pymarc, for example handling of [linked 880 fields](https://www.loc.gov/marc/bibliographic/bd880.html) that include parallel data in non-Latin scripts

### May 2, 2023
+ We talked about Rebecca’s code for parsing MARCXML from Ex Libris Alma
Then we talked about our various experiences (good and bad) with parsing XML with Python’s built in ElementTree module versus LXML versus Beautiful soup. We took a moment to talk about the typical issues that can come up with web scraping when a site’s HTML changes over time.

+ We then spoke about Eric Morgan’s recent question to the Code4lib mailing list about “literary warrant.”

+ John asked if anyone had experience with Python modules for creating barcodes. We briefly also spoke about creating QR codes with Python.
John is using this Python module:
https://python-barcode.readthedocs.io/en/stable/
Jason is using:
PyQRCode==1.2.1
pyzbar==0.1.9
Emma shared a good explainer on QR codes : https://ivantay2003.medium.com/qr-code-demystify-2a5263ab136e
12:00

+ Meghan asked about what tools to use when handed Excel files or CSV files that users would like some charts created from the data in a way that is shareable. This is in addition to creating charts inside Excel and Jupiter or Colab notebooks, then sharing them with a group of people.
Here are some of the suggestions discussed...
Plotly - https://plotly.com/
Streamlit - https://streamlit.io/
This book on mixing Python to process data, but then use JS based tools for web visualization was mentioned again in this group...
Data Visualization with Python and JavaScript, 2nd Edition
https://www.oreilly.com/library/view/data-visualization-with/9781098111861/
The author’s website is also worth a look: https://www.kyrandale.com
https://www.kyrandale.com

+ We talked about creating RDFs with Python, including Python modules, visualization tool, and GML files
https://github.com/RDFLib/rdflib
https://rdflib.readthedocs.io/en/stable/
“RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.”
https://gephi.org/
“Gephi is the leading visualization and exploration software for all kinds of graphs and networks. Gephi is open-source and free.”
GML files
https://en.wikipedia.org/wiki/Graph_Modelling_Language
+ We talked briefly about the new version 5.0 of Pymarc and that we would like to go over the changes to Pymarc in thsi group in the future
https://gitlab.com/pymarc/pymarc/-/releases/v5.0.0

### April 18, 2023
At today meeting we had @michelle.janowiecki give a short presentation on Pandas, partially based on a longer Pandas presentation she has given before.
[Speedy pandas : a super brief intro to Python's pandas library (see slides)](https://docs.google.com/presentation/d/1xRdNVonTxi9-gEsQkNvbF1e47o_2cuo1iimunoFUky4/edit#slide=id.p)
Here are a couple of useful links from her presentation...

#### Pandas Official resources
+ [documentation website](https://pandas.pydata.org/pandas-docs/stable/index.html)
+ [User Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
+ [API reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

#### Pandas Additional resources
+ ["Pandas for Metadata Transformation and Cleanup" workshop by Michelle Janowiecki](https://mjanowiecki.github.io/intro-pandas-metadata/intro.html)
+ the best book: [Pandas for everyone : Python data analysis](https://www.worldcat.org/title/pandas-for-everyone-python-data-analysis/oclc/1240309883?referer=br&ht=edition)

#### Examples of the code Michelle demonstrated

```python
import pandas as pd

filename = "sampleData.csv"
df = pd.read_csv(filename)
print(df.head())

print(df.columns)

degree_department = df["degree_department"]
department_unique = degree_department.unique()
print(department_unique)
unique_list = list(department_unique)
print(unique_list)
```

```python
import pandas as pd

filename = "sampleData.csv"
df = pd.read_csv(filename)

print(df.shape)
df = df.dropna(axis=0, how="all")
df = df.dropna(axis=1, how="all")
df = df.drop_duplicates()
df["title"] = df["title"].str.strip()

print(df.head())
print(df.shape)

df.to_csv("sampleData_cleaned.csv", index=False)
```

```python
import pandas as pd

df_1 = pd.read_csv("frame_1.csv")
df_2 = pd.read_csv("frame_2.csv")

merged = pd.merge(df_1, df_2, how="left", on="subject_id")
print(merged.head())

merged.to_csv("merged_frames.csv", index=False)
```

These are some of the Pandas features @michelle.janowiecki demonstrated today
+ drop_duplicates()
+ dropna()
+ merge()

After the presentation we all exchanged pandas usage tips
+ like pd.json_normalize(a_dict)
  + “All Pandas json_normalize() you should know for flattening JSON”
  + https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd
+ and the ability of doing mathematical
+ also there was a mention of the command line JQ tool for parsing JSON
  + https://stedolan.github.io/jq/


### April 4, 2023
#### The mini-workshop "An Introduction to Python for Absolute Beginners":
A very basic intro to Python for librarians who have little to no experience with Python but who want to get started.
+ What is Python and why is it useful? (5 min)
+ Hands-on practice with basic operations in Python, using Google Colaboratory (25 min)
+ Print function
+ Data types
+ Arithmetic operations
+ String concatenation
+ Variable assignment
+ Q&A/Resources (15 min)

#### Notes
+ We got a shortened version of a Rice University Library workshop called “Mini Python Intro”
+ We used Google Colab
  + Which is a free Google service that essentially hosts Python Jupyter Notebooks that can be shared with others
  + https://colab.research.google.com/
+ For the training using the following resources
  + Pre-loaded notebook:
    + https://colab.research.google.com/drive/1m3cz4KeozooHFzjswyjgJmbfXZTfG0mP?usp=sharing
    + Exercises:
      + https://drive.google.com/file/d/1CRda_Gh3mrqpEmbnvF58-7jvYnmV-LhI/view?usp=share_link
+ We discussed the Python print() sep parameter
+ David shared an article and specifically a tip about using a “union” operator, in this special case a bar “|” character, to join multiple dictionaries together.
  + https://medium.com/techtofreedom/19-sweet-python-syntax-sugar-for-improving-your-coding-experience-37c4118fc6b1
+ Python f-strings were briefly mentioned
  + https://realpython.com/python-f-strings/
  + f-strings are available as of Python 3.6
+ Talked about copy /pasting parts of your Python error messages right into Google to help you figure out what is wrong
  + and how https://stackoverflow.com/ is a common place to look for error advice
  + Google Colab actually offers to send you to StackOverflow when you get an error on code running in Colab
+ @Yamil Suárez shared a code snippet demonstrating how to read a file stored in a Google Drive into Google Colab:
```python
from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/data.tsv', sep='\t')
```



### March 21, 2023 
+ Talked about this group’s [new repository](https://github.com/code4lib/python4lib-resources), and that we want to encourage others to contribute changes via PRs (or reach out to the group)
+ Talked about combining JS and python for web visualization
  + [Data Visualization with Python and JavaScript, 2nd Edition by Kyran Dale](https://www.oreilly.com/library/view/data-visualization-with/9781098111861/)
+ Talked about if on macOS we should currently be using homebrew for installing Python on macOS
  + https://docs.brew.sh/Homebrew-and-Python
  + consensus was that it should work fine
  + “if you use VSCode, it recommends homebrew on mac. I used home-brew to install 3.10 and I haven’t encountered any issues
  + (https://code.visualstudio.com/docs/python/python-tutorial”)
  + we talked about how Anaconda or Anaconda can be used for python installations
+ Talked about [Library Carpentry lessons](https://librarycarpentry.org/lessons/) on Python and other skills like bash, OpenRefine
+ Spoke a bit about [Google Collab](https://colab.research.google.com/), which are essentially Jupyter Notebooks in the cloud, no need for local installation
+ Pivoted to talk about interesting things seen in during Code4lib
  + the Python GUI package mentioned named [Gooey](https://pypi.org/project/Gooey/)
  + “There was a poster about updating subject headings as well. Which was something we had briefly talked about briefly a week before C4L.”
+ Touched on a suggested breaking change to [pymarc](https://gitlab.com/pymarc/pymarc), [MR details](https://gitlab.com/pymarc/pymarc/-/merge_requests/194)
  + this change uses Python “namedtuples”
  + this change is welcome by many
  + We then covered how to use pymarc with authority records, as opposed to bibliographic records - more research needs to be done
+ NOTE: this Python group in the future plans to host a pymarc “code recipe” sharing session
+ Talked about current issues in pymarc with MARC bib tag 880

### March 7, 2023
+ Introductions with a few new members
+ Move the Python{4}Lib resource page to a Code{4}Lib, thanks @klinga
+ @Rebecca Hyams working on an ELUNA Dev. Day presentation gathering specific holding data (granular) from Alma via API and parsing it via python script.
Chat about maintaining authorities when you’ve decided to change from standard language. Is/should there be a tool to check for changes for authorities you select?
+ A project for a heat map visual for circulation might be a new way of helping to weed/collection develop.
  + Perhaps there's interest to have a working group dive into different projects. Could be helpful for design ideas.
+ Dashboards and/or developing scripts that can translate one form of data to another; identifying transformation steps and when to streamline them in one script vs. multiple.
+ IPEDS data transformations. A lot of data isn’t as streamlined as we’d like every time IPEDS comes up. Still quite local though. (Changes year to year?)
