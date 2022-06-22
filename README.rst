========
straycat
========

.. image:: assets/straycat_logo.png
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
    

Easy NLP implementation for Indonesian Language


* Free software: MIT license
* Documentation: https://straycat.readthedocs.io.

Features
--------
- Automate Text Preprocessing Pipeline
- Automate Text Preprocessing Pipeline With pandas
- Tokenization
- Stemming
- Stopwords 
- Remove Punctuation
- Remove emoji
- Remove non alpha numerik
- Remove link
- Remove date
- Remove Medianame
- Normalize slang words


============
Installation
============


Stable release
--------------

<<<<<<< HEAD
To install straycat, run this command in your terminal:

.. code-block:: console

    $ pip install straycat

This is the preferred method to install straycat, as it will always install the most recent stable release.

=======

Usage
*****
::

        from straycat.text_preprocessing import TextPreprocessing

        # Instatiation with default stopwords
        st = TextPreprocessing()

        # Instatiation with your own stopwords
        st = TextPreprocessing(other_stopwords=["sw1", "sw2", "etc"])

        # Instatiation with combine default stopwords and your stopwords
        st = TextPreprocessing.add_stopwords(["sw1", "sw2", "etc"])

Automate text preprocessing with single line of code
****************************************************
::

        # Automate Text Preprocessing with default pipeline (tokenizing, case folding, remove punctuation, remove stopwords, stemming)

        # Return list of Tokens
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"]) 
        #output [['ak', 'suka', 'mkan', 'apel', 'rasa', 'enak']]

        #Return list of Sentences               
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],return_types="list_of_sentences") 
        #output ['ak suka mkan apel rasa enak']


Add more additional text preprocessing pipeline with single line of code
************************************************************************
::

        # Add more additional pipeline (normalize slang word, remove date, remove emoji, remove medianame, remove link, remove non alnum )

        # Return list of Tokens
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                        set_process="add_process",process=["normalize_slang"] )
        #output [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        # Return list of Sentences
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                        set_process="add_process",process=["normalize_slang"], 
                        return_types="list_of_sentences" )
        #output ['saya suka makan apel rasa enak']


Customize text preprocessing pipeline with single line of code
**************************************************************
::

       # Customize process pipeline

        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"],
                        set_process="customize",process=["normalize_slang"] )
        #output [['saya','suka','makan','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"],
                        set_process="customize",process=["normalize_slang"], 
                        return_types="list_of_sentences")
        #output ['saya suka makan apel karena rasanya enak ! ! ! 😁 😆 😅']


Use specific text preprocessing task
************************************
::

        # Tokenize Indonesian Language

        st.tokenize("saya sedang memakan apple.")  
        #output ["saya", "sedang", "memakan", "apple","."]

        # Concatenate Tokens

        st.concat_token(["saya", "sedang", "memakan", "apple"]) 
        #output "saya sedang memakan apple"

        # Stemming Indonesia Language

        st.stemming("saya suka memakan apple") 
        #output ["saya","suka","makan","apple"]

        st.stemming("saya suka memakan apple", return_type="sentences") 
        #output "saya suka makan apple"

        # Case folding

        st.case_folding("Proses Teks Preprocessing") 
        #output ["proses", "teks", "preprocessing"]

        st.case_folding("Proses Teks Preprocessing", return_type="sentences") 
        #output "proses teks preprocessing"

        # Stopwords Removal

        st.stop_words("apel yang terlihat lezat") 
        #output ["apel","terlihat","lezat"]

        st.stop_words("apel yang terlihat lezat",return_type="sentences") 
        #output "apel terlihat lezat"

        # Punctuation Removal

        st.remove_punc("dapat hubungi akun@google !!!"") 
        #output ["dapat","hubungi","akun@google"]

        st.remove_punc("dapat hubungi akun@google !!!"", return_type="sentences") 
        #output "dapat hubungi akun@google"

        # Non Alnum Removal

        st.remove_non_alnum("dapat hubungi akun@google !!!") 
        #output ["dapat","hubungi"]

        st.remove_non_alnum("dapat hubungi akun@google !!!", return_type="sentences") 
        #output "dapat hubungi"

        # Remove emoji

        st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha") 
        #output ["hahaha","hahaha","hahaha"]

        st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha", return_type="sentences") 
        #output "hahaha hahaha hahaha"

        # Remove date

        st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal") 
        #output ["tanggal", "tanggal"]

        st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal",return_type="sentences") 
        #output "tanggal tanggal"

        # Remove link

        st.remove_link("https://www.kompas.com berita hari ini") 
        #output ["berita", "hari", "ini"]

        st.remove_link("https://www.kompas.com berita hari ini", return_type = "tokens") 
        #output "berita hari ini"

        # Remove media name

        st.remove_medianame("kompas.com berita hari ini") 
        #output ["berita", "hari", "ini"]

        st.remove_medianame("kompas.com berita hari ini", return_type = "sentences") 
        #output "berita hari ini"

        # Normalize slang

        st.remove_slang("ak sk mkan") 
        #output ["saya", "suka", "makan"]

        st.remove_slang("ak sk mkan", return_type = "sentences") 
        #output "saya suka makan"

        #encode text
        st.encode_text("Saya \x94sedang makan apple") 
        #output "saya sedang memakan apple"


WORKING WITH DATAFRAME
**********************
::

        # Straycat with DataFrame

        from straycat.text_preprocessing import TextPreprocessing
        import pandas as pd

        # Instatiation with default stopwords
        st = TextPreprocessing()

        # Instatiation with your own stopwords
        st = TextPreprocessing(other_stopwords=["sw1", "sw2", "etc"])

        # Instatiation with combine default stopwords and your stopwords
        st = TextPreprocessing.add_stopwords(["sw1", "sw2", "etc"])
        teks = ["tvri.com 14/08/1945 telah terjadi hari kemerdekaan","ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"]
        doc = pd.DataFrame(teks,columns=["text"])


Automate text preprocessing pipeline in dataframe with single line of code
**************************************************************************
::

        # Automate Text Preprocessing with default pipeline (tokenizing, case folding, remove punctuation, remove stopwords, stemming)

        st.auto_text_prep(doc["text"]) 
        #output [['tvri', 'com', '14', '08', '1945', 'jadi', 'hari', 'merdeka'],
        ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        st.auto_text_prep(doc["text"], return_types="list_of_sentences")
        #output ['tvri com 14 08 1945 jadi hari merdeka', 'ak suka mkn apel rasa enak']


Add more additional text preprocessing pipeline in dataframe with single line of code
*************************************************************************************
::

        # Add more additional pipeline (normalize slang word, remove date, remove emoji, remove medianame, remove link, remove non alnum )

        st.auto_text_prep(doc["text"], set_process="add_process", process=["medianame_removal","date_removal"])
        #output [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]


        st.auto_text_prep(doc["text"], set_process="add_process", process=["medianame_removal","date_removal"],       
                        return_types="list_of_sentences")
        #output ['jadi hari merdeka', 'ak suka mkn apel rasa enak']


Customize text preprocessing pipeline in dataframe with single line of code
***************************************************************************
::

        # Customize pipeline 

        st.auto_text_prep(doc["text"], set_process="customize", process=["medianame_removal","date_removal"])
        #output [['telah', 'terjadi', 'hari', 'kemerdekaan'],
                ['ak','suka','mkn','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        st.auto_text_prep(doc["text"], set_process="customize", process=["medianame_removal","date_removal"],
                        return_types="list_of_sentences")
        #output ['telah terjadi hari kemerdekaan','ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage