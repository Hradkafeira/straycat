# straycat
A wrapper package for easy implementation of Indonesian NLP



## Usage

```
from straycat import text_preprocessing as tp
st=tp.TextProcessing()

# Automate Text Preprocessing with default pipeline (tokenizing, case folding, remove punctuation, remove stopwords, stemming)

st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅]) #output ["ak suka mkn apel rasa enak"]

# Add more additional pipeline (normalize slang word, remove date, remove emoji, remove medianame, remove link, remove non alnum )
st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"], set_process="add_process",
                    process=["normalize_slang"]) # output ['saya suka makan apel rasa enak']

# Customize pipeline 
st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"], set_process="customize",
                    process=["emoji_removal","punctuation_removal"]) #output ['ak suka mkan apel karena rasanya enak']


# Tokenize Indonesian Language
st.tokenize("saya sedang memakan apple.")  # output ["saya", "sedang", "memakan", "apple","."]

# Stemming Indonesia Language
st.stemming("saya suka memakan apple") # output "saya suka makan apple"
st.stemming("saya suka memakan apple", return_type="tokens") # output ["saya","suka","makan","apple"]

# Case folding
st.case_folding("Proses Teks Preprocessing") #output "proses teks preprocessing"

# Stopwords Removal
st.stop_words("saya sedang memakan apple") #output "saya memakan apple"
st.stop_words("saya sedang memakan apple",return_type="tokens") #output ["saya","memakan","apple"]

# Punctuation Removal
st.remove_punc("dapat hubungi akun@google !!!"") #"dapat hubungi akun@google"
st.remove_punc("dapat hubungi akun@google !!!"", return_type="tokens") #output ["dapat","hubungi","akun@google"]

# Non Alnum Removal
st.remove_non_alnum("dapat hubungi akun@google !!!") #output "dapat hubungi"
st.remove_non_alnum("dapat hubungi akun@google !!!", return_type="tokens") #output ["dapat","hubungi"]

# Remove emoji
st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha") #output "hahaha hahaha hahaha"
st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha", return_type="tokens") #output ["hahaha","hahaha","hahaha"]

#Remove date
st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal") #output "tanggal tanggal"
st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal",return_type="tokens") #output ["tanggal", "tanggal"]


#Remove link
st.remove_link("https://www.kompas.com berita hari ini") #output "berita hari ini"
st.remove_link("https://www.kompas.com berita hari ini", return_type = "tokens") #output ["berita", "hari", "ini"]

#Remove media name
st.remove_medianame("kompas.com berita hari ini") #output "berita hari ini"
st.remove_medianame("kompas.com berita hari ini", return_type = "tokens") #output ["berita", "hari", "ini"]

#Normalize slang
st.remove_slang("ak sk mkan") #output "saya suka makan"
st.remove_slang("ak sk mkan", return_type = "tokens") #output ["saya", "suka", "makan"]

#encode text
st.encode_text("Saya \x94sedang makan apple") #output "saya sedang memakan apple"

```

## Straycat with DataFrame

```
from straycat import text_preprocessing as tp
import pandas as pd

st=tp.TextProcessing()


teks = ["tvri.com 14/08/1945 telah terjadi hari kemerdekaan","ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"]
doc=pd.DataFrame(teks,columns=["text"])

# Automate Text Preprocessing with default pipeline (tokenizing, case folding, remove punctuation, remove stopwords, stemming)
st.auto_text_prep(doc["text"]) #output ['tvri com 14 08 1945 jadi hari merdeka', 'ak suka mkn apel rasa enak']

# Add more additional pipeline (normalize slang word, remove date, remove emoji, remove medianame, remove link, remove non alnum )
st.auto_text_prep(doc["test"],set_process="add_process",process=["medianame_removal","date_removal"]) 
#output ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

# Customize pipeline 
st.auto_text_prep(doc["test"],set_process="customize",process=["medianame_removal","date_removal"])
#output ['telah terjadi hari kemerdekaan', 'ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']