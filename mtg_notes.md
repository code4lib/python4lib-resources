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