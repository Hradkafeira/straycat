========
STRAYCAT
========

.. image:: https://github.com/Hradkafeira/straycat/blob/straycat_dev/assets/straycat_logo.png?raw=true
  :width: 400

.. image:: https://img.shields.io/pypi/v/straycat.svg
        :target: https://pypi.python.org/pypi/straycat

.. image:: https://img.shields.io/travis/hradkafeira/straycat.svg
        :target: https://travis-ci.com/hradkafeira/straycat

.. image:: https://readthedocs.org/projects/straycat/badge/?version=latest
        :target: https://straycat.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://github.com/Hradkafeira/straycat/actions/workflows/straycat_testing.yml/badge.svg
        :target: https://github.com/Hradkafeira/straycat/actions/workflows/straycat_testing.yml

.. image:: https://codecov.io/gh/Hradkafeira/straycat/branch/main/graph/badge.svg?token=6SH3QTEU8D
        :target: https://codecov.io/gh/Hradkafeira/straycat
        
.. raw:: html

  <p align="left">
  <a href="https://github.com/difo-n8r/straycat/tree/straycat_dev">English</a> |
  <span>Bahasa</span>
    

Implementasi NLP sederhana untuk Bahasa Indonesia


* Free software: MIT license
* Documentation: https://straycat.readthedocs.io.

Fitur-fitur
--------
- Otomatisasi Text Preprocessing Pipeline
- Otomatisasi Text Preprocessing Pipeline dengan pandas
- Tokenization
- Stemming
- Stopwords 
- Menghapus Tanda baca
- Menghapus emoji
- Menghapus non alpha numeric
- Menghapus link
- Menghapus tanggal
- Menghapus Medianame
- Normalisasi kata-kata tidak baku


============
Instalasi
============

Stable release
--------------

Untuk instalasi straycat, Jalankan perintah ini di terminal:

.. code-block:: console

    $ pip install straycat

Ini adalah metode yang lebih disukai untuk menginstal straycat, karena akan selalu menginstal rilis stabil terbaru.

Penggunaan
*****
::

        from straycat.text_preprocessing import TextPreprocessing

        # Instansiasi dengan stopwords default
        st = TextPreprocessing()

        # Instansiasi dengan stopwords custom
        st = TextPreprocessing(other_stopwords=["sw1", "sw2", "etc"])

        # Instansiasi dengan menggabungkan stopwords default dan stopwords custom.
        st = TextPreprocessing.add_stopwords(["sw1", "sw2", "etc"])

        # Melihat pipelines yang tersedia.
        print(st.list_process)
        #output
        
        Berikut list untuk auto_text_prep
        Input value dengan nomor atau teks.
        1  or "case_folding"
        2  or "punctuation_removal"
        3  or "stopwords_removal"
        4  or "stemming"
        5  or "encode_text"
        6  or "medianame_removal"
        7  or "non_alnum_removal"
        8  or "link_removal"
        9  or "emoji_removal"
        10 or "normalize_slang"
        11 or "date_removal"

Otomatisasi preprocessing teks dengan metode sekali panggil.
************************************************
::

        # Otomatisasi dengan pipeline default 
        (tokenizing, case folding, remove tanda baca, remove stopwords, stemming)

        # Mengembalikan list dari Token
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"]) 
        #output [['ak', 'suka', 'mkan', 'apel', 'rasa', 'enak']]

        # Mengembalikan list dari kalimat           
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],return_types="list_of_sentences") 
        #output ['ak suka mkan apel rasa enak']

Menambahkan lagi tambahan pipeline preprocessing teks dengan metode sekali panggil
********************************************************************
::

        # Menambahkan lebih banyak pipeline (Normalisasi kata tidak baku, menghapus tanggal, menghapus emoji, menghapus medianame, menghapus link, dan menghapus non alnum)

        # Mengembalikan list dari token dengan banyak args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                        set_process="add_process",
                        process=[10])
        #output [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        # Mengembalikan list dari Tokens dengan nama args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="add_process",
                          input_proc="name",
                          process=["normalize_slang"])
        #output [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        # Mengembalikan list dari kalimat dengan beberapa args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="add_process",
                          process=[10], 
                          return_types="list_of_sentences" )
        #output ['saya suka makan apel rasa enak']

        # Mengembalikan list dari kalimat-kalimat dengan nama args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="add_process",
                          input_proc="name",
                          process=["normalize_slang"], 
                          return_types="list_of_sentences" )
        #output ['saya suka makan apel rasa enak']

Memodifikasi pipeline preprocessing teks dengan memanggil satu metode
**********************************************************
::

       # Memodifikasi pipeline proses

        # Mengembalikan list dari token dengan beberapa args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                        set_process="customize",
                        process=[10])
        #output [['saya','suka','makan','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        # Mengembalikan list dari token dengan nama args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="customize",
                          input_proc="name",
                          process=["normalize_slang"])
        #output [['saya','suka','makan','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        # Mengembalikan list dari kalimat-kalimat dengan beberapa args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="customize",
                          process=[10], 
                          return_types="list_of_sentences" )
        #output ['saya suka makan apel karena rasanya enak ! ! ! 😁 😆 😅']

        # Mengembalikan list dari kalimat dengan nama args dari proses
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"],
                        set_process="customize",
                        input_proc="name",
                        process=["normalize_slang"], 
                        return_types="list_of_sentences")
        #output ['saya suka makan apel karena rasanya enak ! ! ! 😁 😆 😅']


Menggunakan penugasan preprocessing yang spesifik
************************************
::

        # Tokenisasi bahasa Indonesia

        st.tokenize("saya sedang memakan apple.")  
        #output ["saya", "sedang", "memakan", "apple","."]

        # Menggabungkan token-token

        st.concat_token(["saya", "sedang", "memakan", "apple"]) 
        #output "saya sedang memakan apple"

        # Stemming bahasa Indonesia

        st.stemming("saya suka memakan apple") 
        #output ["saya","suka","makan","apple"]

        st.stemming("saya suka memakan apple", return_type="sentences") 
        #output "saya suka makan apple"

        # Case folding

        st.case_folding("Proses Teks Preprocessing") 
        #output ["proses", "teks", "preprocessing"]

        st.case_folding("Proses Teks Preprocessing", return_type="sentences") 
        #output "proses teks preprocessing"

        # Menghapus Stopwords

        st.stop_words("apel yang terlihat lezat") 
        #output ["apel","terlihat","lezat"]

        st.stop_words("apel yang terlihat lezat",return_type="sentences") 
        #output "apel terlihat lezat"

        # Menghapus Tanda baca 

        st.remove_punc("dapat hubungi akun@google !!!"") 
        #output ["dapat","hubungi","akun@google"]

        st.remove_punc("dapat hubungi akun@google !!!"", return_type="sentences") 
        #output "dapat hubungi akun@google"

        # Menghapus Non Alnum

        st.remove_non_alnum("dapat hubungi akun@google !!!") 
        #output ["dapat","hubungi"]

        st.remove_non_alnum("dapat hubungi akun@google !!!", return_type="sentences") 
        #output "dapat hubungi"

        # Menghapus emoji

        st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha") 
        #output ["hahaha","hahaha","hahaha"]

        st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha", return_type="sentences") 
        #output "hahaha hahaha hahaha"

        # Menghapus tanggal

        st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal") 
        #output ["tanggal", "tanggal"]

        st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal",return_type="sentences") 
        #output "tanggal tanggal"

        # Menghapus link

        st.remove_link("https://www.kompas.com berita hari ini") 
        #output ["berita", "hari", "ini"]

        st.remove_link("https://www.kompas.com berita hari ini", return_type = "sentences") 
        #output "berita hari ini"

        # Menghapus nama media

        st.remove_medianame("kompas.com berita hari ini") 
        #output ["berita", "hari", "ini"]

        st.remove_medianame("kompas.com berita hari ini", return_type = "sentences") 
        #output "berita hari ini"

        # normalisasi kata tidak baku

        st.remove_slang("ak sk mkan") 
        #output ["saya", "suka", "makan"]

        st.remove_slang("ak sk mkan", return_type = "sentences") 
        #output "saya suka makan"

        #encode teks
        st.encode_text("Saya \x94sedang makan apple") 
        #output "saya sedang memakan apple"


MENGGUNAKAN DATAFRAME
**********************
::

        # Straycat dengan DataFrame

        from straycat.text_preprocessing import TextPreprocessing
        import pandas as pd

        # Instantiasi dengan stopword default
        st = TextPreprocessing()

        # Instantiasi dengan stopword custom
        st = TextPreprocessing(other_stopwords=["sw1", "sw2", "etc"])

        # Instantiasi dengan stopword default dan stopword custom
        st = TextPreprocessing.add_stopwords(["sw1", "sw2", "etc"])

        # Melihat pipeline yang tersedia
        print(st.list_process)
        #output
        
        Berikut list untuk auto_text_prep
        Input value dengan nomor atau teks
        1  or "case_folding"
        2  or "punctuation_removal"
        3  or "stopwords_removal"
        4  or "stemming"
        5  or "encode_text"
        6  or "medianame_removal"
        7  or "non_alnum_removal"
        8  or "link_removal"
        9  or "emoji_removal"
        10 or "normalize_slang"
        11 or "date_removal"

        teks = ["tvri.com 14/08/1945 telah terjadi hari kemerdekaan","ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"]
        doc = pd.DataFrame(teks,columns=["text"])

Otomatisasi pipeline preprocessing teks di dalam dataframe dengan metode sekali panggil
**********************************************************************
::

        # Otomatisasi preprocessing teks dengan pipeline default(Tokenisasi, case folding, hapus tanda baca, menghapus stopwords, stemming)

        # Mengembalikan list dari token
        st.auto_text_prep(doc["text"]) 
        #output [['tvri', 'com', '14', '08', '1945', 'jadi', 'hari', 'merdeka'],
        ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        # Mengembalikan list dari kalimat
        st.auto_text_prep(doc["text"], return_types="list_of_sentences")
        #output ['tvri com 14 08 1945 jadi hari merdeka', 'ak suka mkn apel rasa enak']


Menambahkan lagi pipeline teks preprocessing tambahan di dalam dataframe dengan metode sekali panggil
*********************************************************************************
::

        # Add more additional pipeline (normalisasi kata tidak baku, menghapus tanggal, menghapus emoji, menghapus nama media, menghapus link, menghapus non alnum )

        # Mengembalikan list dari Token dengan beberapa args dari proses
        st.auto_text_prep(doc["text"], set_process="add_process", process=[6, 11])
        #output [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        # Mengembalikan list dari token dengan nama args dari proses
        st.auto_text_prep(doc["text"], set_process="add_process",
                          input_proc="name",
                          process=["medianame_removal","date_removal"])
        #output [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        # Mengembalikan list dari kalimat dengan nama args dari proses
        st.auto_text_prep(doc["text"], set_process="add_process", 
                          process=[6, 11],       
                        return_types="list_of_sentences")
        #output ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

        # Mengembalikan list dari kalimat dengan nama args dari proses
        st.auto_text_prep(doc["text"], set_process="add_process",
                          input_proc="name",
                          process=["medianame_removal","date_removal"],       
                          return_types="list_of_sentences")
        #output ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

Memodifikasi pipeline preprocessing teks di dalam dataframe dengan metode sekali panggil
***********************************************************************
::

        # Memodifikasi pipeline 

        # Mengembalikan list dari token dengan beberapa args dari proses
        st.auto_text_prep(doc["text"], set_process="customize", process=[6, 11])
        #output [['telah', 'terjadi', 'hari', 'kemerdekaan'],
                ['ak','suka','mkn','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        # Mengembalikan list dari token dengan nama args dari proses
        st.auto_text_prep(doc["text"], set_process="customize", 
                          input_proc="name",
                          process=["medianame_removal","date_removal"])
        #output [['telah', 'terjadi', 'hari', 'kemerdekaan'],
                ['ak','suka','mkn','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]


        # Mengembalikan list dari kalimat dengan beberapa args dari proses
        st.auto_text_prep(doc["text"], set_process="customize",
                          process=[6, 11],
                        return_types="list_of_sentences")
        #output ['telah terjadi hari kemerdekaan','ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

        # Mengembalikan list dari kalimat-kalimat dengan nama args dari proses
        st.auto_text_prep(doc["text"], set_process="customize",
                          input_proc="name", 
                          process=["medianame_removal","date_removal"],
                          return_types="list_of_sentences")
        #output ['telah terjadi hari kemerdekaan','ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

Kredit
-------

Package dibuat dengan Cookiecutter_ dan template proyek `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
