# taw
Translate to Arabic using Wikipedia.

Simple script to translate terminologies from English to Arabic using Wikipedia. Originally used to translate countries for [ArabicAndroidCountryPicker](https://github.com/mohabh/ArabicAndroidCountryPicker) <br>
Using urllib3, the script will navigate to the terminology page in wikipedia, look for "العربية" link, and return its corresponding terminology in Arabic.

## How to use
Right now it's configured to read terminologies from json file and write it to another json file.<br>
`python taw.py terms.json` will produce the translated terms in ar_terms.json.
