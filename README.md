# pythaiwordcut - Thai Wordcut in Python

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c4cb39daa5a54ffd9c1a797072e0f6d2)](https://www.codacy.com/app/narongdejsrn/pythaiwordcut?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=narongdejsrn/pythaiwordcut&amp;utm_campaign=Badge_Grade)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pythaiwordcut.svg)
![PyPI - License](https://img.shields.io/pypi/l/pythaiwordcut.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pythaiwordcut.svg)

-----

A simple Thai wordcut written in Python, based on Maximum Matching algorithm by [S. Manabu](http://www.aclweb.org/anthology/E14-4016)
. Uses Lexitron (by [NECTEC](http://www.sansarn.com/lexto/license-lexitron.php)) dictionary as default

> Please note: This project is under development and should not be use in production , all function and interface are subject to change. If you have issue or suggestion please feel free to ask, contribution is also very welcome :)

## Installation

```bash
pip install pythaiwordcut
```

or

```bash
git clone https://github.com/zenyai/pythaiwordcut.git
python setup.py install
```

## Usage

```python
import pythaiwordcut as pwt

pt = pwt.wordcut(removeRepeat=True, stopDictionary="<full path to txt file>", removeSpaces=True, minLength=1, stopNumber=False, removeNonCharacter=False, caseSensitive=True, ngram=(1, 2), negation=False)
print "|".join(pt.segment(u'ทดสอบการตัดคำ'))
```
  * removeRepeat: remove intention insertion spelling error such as (สบายยยยยย)
  * stopDictionary: remove word that exist in this specify text file (one word one line)
  * removeSpaces: remove blank space
  * minLength: minimum length of each word
  * stopNumber: remove number if exist
  * removeNonCharacter: remove character that are not Thai or English character
  * caseSensitive: if set to false, will remove stop word without regarding the case
  * ngram: Add word ngram from (1, 2)
  * negation: If set to true, then it will add NOT_ to every word after negation word and space

