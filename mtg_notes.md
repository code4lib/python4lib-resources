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
A very basic intro to Python for librarians who have little to no experience with Python but who want to get started.
The mini-workshop titled, "An Introduction to Python for Absolute Beginners":
+ What is Python and why is it useful? (5 min)
+ Hands-on practice with basic operations in Python, using Google Colaboratory (25 min)
+ Print function
+ Data types
+ Arithmetic operations
+ String concatenation
+ Variable assignment
+ Q&A/Resources (15 min)

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