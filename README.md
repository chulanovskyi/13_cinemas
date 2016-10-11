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