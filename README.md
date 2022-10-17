# PyTranslo
Python Client Library for Translo API. https://rapidapi.com/armangokka/api/translo

# Installing

```sh
pip install -U PyTranslo
```

# Usage

```python
from PyTranslo import PyTranslo

api = PyTranslo("<TOKEN>")

api.translate("Отличная библиотека", "en")  # "Excellent library"

api.translate("Knows many languages", "ru")  # "Знает много языков"

api.translate("没有必要指出翻译来自哪种语言。", "en")  # "There is no need to indicate which language the translation comes from."
api.translate("Но можно если нужно", "en", from_lang="ru")  # "But you can if you need"

api.detect("Что это за язык?") # "ru"
```

# What is batch translate?
If you need to translate several messages at a time, you will definitely like this

## batch_translate example

```python
from PyTranslo import PyTranslo

api = PyTranslo("<TOKEN>")

batch = [
    {
        "from": "en",
        "to": "ru",
        "text": "банан"
    },
    {
        "from": "ru",
        "to": "en",
        "text": "Картошка была очень вкусная"
    },
    {
        "from": "auto",
        "to": "bn",
        "text": "bonjour"
    }
]

api.batch_translate(batch)

# returns
# [{'from': 'en', 'to': 'ru', 'text': 'банан'}
#  {'from': 'ru', 'to': 'en', 'text': 'The potatoes were very tasty.'},)
#  {'from': 'fr', 'to': 'bn', 'text': 'হ্যালো'}])
```
