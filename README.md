# 13_cinemas

###Prerequisites:

Run in console `pip install -r requirements.txt` to install 3rd party modules.

---

This script work with `afisha.ru/msk` and `kinopoisk.ru` filter movies by rating or number of cinemas, that are currently showing this movie. 
Because `kinopoisk.ru` don't have normal api, script need some time (about ~1 minute) to fetch movie info. 

###How to use:

Script have one optional argument:

- `--movies` - determines the size of the movies list to be printed;

**Note!** By default `--movies` will set to 10, if not specified.

####INPUT

At the start, script will ask you to choose the sort method (enter `1` or `2`):
```
Sort movies by:
1. Rating
2. Cinemas

$ 1
```

####OUTPUT
```
1. Мужчины (8.163)
2. Золотая лихорадка (8.069)
3. Бал (7.97)
4. Весна, лето, осень, зима... и снова весна (7.908)
5. Москва, я терплю тебя (7.889)
6. Вторая жизнь Уве (7.88)
7. Винил (7.846)
8. Сестра его дворецкого (7.833)
9. Сияние (7.832)
10. Это всего лишь конец света (7.812)
```
