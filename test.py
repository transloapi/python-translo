from PyTranslo import PyTranslo

api = PyTranslo("<TOKEN>")

assert api.translate("Отличная библиотека", "en") == "Excellent library"

assert api.translate("Knows many languages", "ru") == "Знает много языков"

assert api.translate("没有必要指出翻译来自哪种语言。", "en") == "There is no need to indicate which language the translation comes from."
assert api.translate("Но можно если нужно", "en",
                     from_lang="ru") == "But you can if you need"
assert api.detect("Что это за язык?") == "ru"
assert api.detect("What is this lang?") == "en"

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
assert api.batch_translate(batch) == [{'from': 'en', 'to': 'ru', 'text': 'банан'},
                                      {'from': 'ru', 'to': 'en', 'text': 'The potatoes were very tasty.'},
                                      {'from': 'fr', 'to': 'bn', 'text': 'হ্যালো'}]


print("test")
