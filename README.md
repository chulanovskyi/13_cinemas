# 13_cinemas

###Prerequisites:

Run in console `pip install -r requirements.txt` to install 3rd party modules.

---

This script work with `afisha.ru/msk` and `kinopoisk.ru` filter movies by rating or number of cinemas, that are currently showing this movie. 
Because `kinopoisk.ru` don't have normal api, script need some time (about ~1 minute) to fetch movie info. 

###How to use:

You can edit in-script constants to get result as you want.

| Constant | Description |
| --- | --- |
| `MOVIES_TO_PRINT` | how many top movies need to be printed|


Что не так
> You can edit in-script constants to get result as you want.
Попробуй вынести их в args, скрипт станет удобнее в использовании

def parse_afisha_list(raw_html):
...
return movies_info
название плохо доносит смысл происходящего. Слишком общо и неконкретно

Вынеси в urls в глобальные константы

fetch_movie_info меняет входящий аргумент info. Такого быть не должно
https://devman.org/encyclopedia/decomposition/decomposition_pure_functions/

В python3 не нужна конструкция u'некий текст не на латинице'

get_sort_attr - плохое название, используй лучше input_sort_attrs - оно говорит о том что функция взаимодействует с вводом/выводом

get_sort_attr
...
exit(11)
это было неожиданно... а раз так - перепиши, код должен быть легко предсказуем, что снижает риск ошибки при его сопровождении/доработке

Магические числа – зло. Вынеси непонятную константу в переменную с говорящим названием. ('\xa0').