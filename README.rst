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
  <span>English</span> |
  <a href="https://github.com/difo-n8r/straycat/tree/straycat_dev/lang/indonesia#straycat">Bahasa</a>

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

Testing release
--------------

To install straycat (, run this command in your terminal:

.. code-block:: console

    $ pip install -i https://test.pypi.org/simple/ straycat

This is the preferred method to install straycat in developer mode.

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

        #See available pipelines before using it
        print(st.list_process)
        #output
        
        Here the list for auto_text_prep
        Input value with number or text
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

Automate text preprocessing with call one method
************************************************
::

        # Automate Text Preprocessing with default pipelines 
        (tokenizing, case folding, remove punctuation, remove stopwords, stemming)

        # Return list of Tokens
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"]) 
        #output [['ak', 'suka', 'mkan', 'apel', 'rasa', 'enak']]

        #Return list of Sentences               
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],return_types="list_of_sentences") 
        #output ['ak suka mkan apel rasa enak']

Add more additional text preprocessing pipeline with call one method
********************************************************************
::

        # Add more additional pipeline (normalize slang word, remove date, remove emoji, remove medianame, remove link, remove non alnum )

        # Return list of Tokens with number args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                        set_process="add_process",
                        process=[10])
        #output [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        # Return list of Tokens with name args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="add_process",
                          input_proc="name",
                          process=["normalize_slang"])
        #output [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        # Return list of Sentences with number args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="add_process",
                          process=[10], 
                          return_types="list_of_sentences" )
        #output ['saya suka makan apel rasa enak']

        # Return list of Sentences with name args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="add_process",
                          input_proc="name",
                          process=["normalize_slang"], 
                          return_types="list_of_sentences" )
        #output ['saya suka makan apel rasa enak']

Customize text preprocessing pipeline with call one method
**********************************************************
::

       # Customize process pipeline

        # Return list of Tokens with number args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                        set_process="customize",
                        process=[10])
        #output [['saya','suka','makan','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        # Return list of Tokens with name args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="customize",
                          input_proc="name",
                          process=["normalize_slang"])
        #output [['saya','suka','makan','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        # Return list of Sentences with number args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                          set_process="customize",
                          process=[10], 
                          return_types="list_of_sentences" )
        #output ['saya suka makan apel karena rasanya enak ! ! ! 😁 😆 😅']

        # Return list of Sentences with name args of process
        st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"],
                        set_process="customize",
                        input_proc="name",
                        process=["normalize_slang"], 
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

        st.remove_link("https://www.kompas.com berita hari ini", return_type = "sentences") 
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

        #See available pipelines before using it
        print(st.list_process)
        #output
        
        Here the list for auto_text_prep
        Input value with number or text
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

Automate text preprocessing pipeline in dataframe with call one method
**********************************************************************
::

        # Automate Text Preprocessing with default pipeline (tokenizing, case folding, remove punctuation, remove stopwords, stemming)

        # Return list of Tokens
        st.auto_text_prep(doc["text"]) 
        #output [['tvri', 'com', '14', '08', '1945', 'jadi', 'hari', 'merdeka'],
        ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        # Return list of Sentences
        st.auto_text_prep(doc["text"], return_types="list_of_sentences")
        #output ['tvri com 14 08 1945 jadi hari merdeka', 'ak suka mkn apel rasa enak']


Add more additional text preprocessing pipeline in dataframe with call one method
*********************************************************************************
::

        # Add more additional pipeline (normalize slang word, remove date, remove emoji, remove medianame, remove link, remove non alnum )

        # Return list of Tokens with number args of process
        st.auto_text_prep(doc["text"], set_process="add_process", process=[6, 11])
        #output [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        # Return list of Tokens with name args of process
        st.auto_text_prep(doc["text"], set_process="add_process",
                          input_proc="name",
                          process=["medianame_removal","date_removal"])
        #output [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]

        # Return list of Sentences with name args of process
        st.auto_text_prep(doc["text"], set_process="add_process", 
                          process=[6, 11],       
                        return_types="list_of_sentences")
        #output ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

        # Return list of Sentences with name args of process
        st.auto_text_prep(doc["text"], set_process="add_process",
                          input_proc="name",
                          process=["medianame_removal","date_removal"],       
                          return_types="list_of_sentences")
        #output ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

Customize text preprocessing pipeline in dataframe with call one method
***********************************************************************
::

        # Customize pipeline 

        # Return list of Tokens with number args of process
        st.auto_text_prep(doc["text"], set_process="customize", process=[6, 11])
        #output [['telah', 'terjadi', 'hari', 'kemerdekaan'],
                ['ak','suka','mkn','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        # Return list of Tokens with name args of process
        st.auto_text_prep(doc["text"], set_process="customize", 
                          input_proc="name",
                          process=["medianame_removal","date_removal"])
        #output [['telah', 'terjadi', 'hari', 'kemerdekaan'],
                ['ak','suka','mkn','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]


        # Return list of Sentences with number args of process
        st.auto_text_prep(doc["text"], set_process="customize",
                          process=[6, 11],
                        return_types="list_of_sentences")
        #output ['telah terjadi hari kemerdekaan','ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

        # Return list of Sentences with name args of process
        st.auto_text_prep(doc["text"], set_process="customize",
                          input_proc="name", 
                          process=["medianame_removal","date_removal"],
                          return_types="list_of_sentences")
        #output ['telah terjadi hari kemerdekaan','ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
