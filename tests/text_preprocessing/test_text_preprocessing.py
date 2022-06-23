#!/usr/bin/env python

"""Tests for `straycat` package."""

import pytest
from straycat.text_preprocessing.text_preprocessing import TextPreprocessing
import pandas as pd

st = TextPreprocessing()

kalimat = [
    "tvri.com 14/08/1945 telah terjadi hari kemerdekaan",
    "ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"
    ]
doc = pd.DataFrame(kalimat, columns=["text"])

MESSAGE = "the return value of process doesn't match to expected value"


class TestTextPreprocessing(object):

    def test_auto_text_prep_value_error(self):

        with pytest.raises(ValueError) as exc_info1:
            st.auto_text_prep("tvri com 14 08 1945 jadi hari merdeka")

        with pytest.raises(ValueError) as exc_info2:
            st.auto_text_prep({"text": "tvri com 14 08 1945 jadi hari merdeka"})  # noqa:E501

        with pytest.raises(ValueError) as exc_info3:
            st.auto_text_prep(["halo nama saya arief"], process=["date_removal"])  # noqa:E501

        with pytest.raises(ValueError) as exc_info4:
            st.auto_text_prep(["halo nama saya arief"], set_process="add_process")  # noqa:E501

        with pytest.raises(ValueError) as exc_info5:
            st.auto_text_prep(["halo nama saya arief"], set_process="add_process",  # noqa:E501
                              process=[])

        with pytest.raises(ValueError) as exc_info6:
            st.auto_text_prep(["halo nama saya arief"], set_process="customize")  # noqa:E501

        with pytest.raises(ValueError) as exc_info7:
            st.auto_text_prep(["halo nama saya arief"], set_process="customize",  # noqa:E501
                              process=[])

        with pytest.raises(ValueError) as exc_info7:
            st.auto_text_prep(["halo nama saya arief"], set_process="customize",  # noqa:E501
                              process=[])

        with pytest.raises(ValueError) as exc_info8:
            st.auto_text_prep(["halo nama saya arief"], set_process="customize",  # noqa:E501
                              process=["normalize_slang"])

        with pytest.raises(ValueError) as exc_info9:
            st.auto_text_prep(["halo nama saya arief"], set_process="customize",  # noqa:E501
                              process=[10], input_proc="name")

        with pytest.raises(ValueError) as exc_info_without_match1:
            st.auto_text_prep(["halo nama saya arief"], set_process="add_process",  # noqa:E501
                              process=["remove_slang"])

        with pytest.raises(ValueError) as exc_info_without_match2:
            st.auto_text_prep(["halo nama saya arief"], set_process="custom")  # noqa:E501

        assert exc_info1.match("input type must be List or numpy array or series")  # noqa:E501
        assert exc_info2.match("input type must be List or numpy array or series")  # noqa:E501
        assert exc_info3.match("standard process no needed additional process, try 'customize' or 'add_process' argument")  # noqa:E501
        assert exc_info4.match("process must be added")
        assert exc_info5.match("process can't be empty")
        assert exc_info6.match("process must be added")
        assert exc_info7.match("process can't be empty")
        assert exc_info8.match("value process are 'name' but input_proc is 'num'")  # noqa:E501
        assert exc_info9.match("value process are 'num' but input_proc is 'name'")  # noqa:E501
        assert exc_info_without_match1
        assert exc_info_without_match2

    def test_auto_text_prep_default(self):

        actual1 = st.auto_text_prep(["tvri com 14 08 1945 jadi hari merdeka"])
        expected1 = [['tvri', 'com', '14', '08', '1945', 'jadi', 'hari', 'merdeka']]  # noqa:E501

        actual2 = st.auto_text_prep(["tvri com 14 08 1945 jadi hari merdeka"],
                                    return_types="list_of_sentences")
        expected2 = ['tvri com 14 08 1945 jadi hari merdeka']

        assert actual1 == expected1, MESSAGE
        assert actual2 == expected2, MESSAGE

    def test_auto_text_prep_add_process(self):

        actual1 = st.auto_text_prep(["tvri com 14 08 1945 jadi hari merdeka"],
                                    set_process="add_process", process=[11])  # noqa:E501
        expected1 = [['tvri', 'com', 'jadi', 'hari', 'merdeka']]

        actual2 = st.auto_text_prep(["tvri com 14 08 1945 jadi hari merdeka"],
                                    set_process="add_process", input_proc="name",  # noqa:E501
                                    process=["date_removal"])
        expected2 = [['tvri', 'com', 'jadi', 'hari', 'merdeka']]

        actual3 = st.auto_text_prep(["tvri com 14 08 1945 jadi hari merdeka"],
                                    set_process="add_process", process=[11],
                                    return_types="list_of_sentences")
        expected3 = ['tvri com jadi hari merdeka']

        actual4 = st.auto_text_prep(["tvri com 14 08 1945 jadi hari merdeka"],
                                    set_process="add_process", input_proc="name",  # noqa:E501
                                    process=["date_removal"],
                                    return_types="list_of_sentences")
        expected4 = ['tvri com jadi hari merdeka']

        assert actual1 == expected1, MESSAGE
        assert actual2 == expected2, MESSAGE
        assert actual3 == expected3, MESSAGE
        assert actual4 == expected4, MESSAGE

    def test_auto_text_prep_customize(self):

        actual1 = st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"],  # noqa:E501
                                    set_process="customize", process=[10])
        expected1 = [
                        [
                            'saya',
                            'suka',
                            'makin',
                            'apel',
                            'karena',
                            'rasanya',
                            'enak',
                            '!',
                            '!',
                            '!',
                            '😁',
                            '😆',
                            '😅'
                            ]
                    ]

        actual2 = st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"],  # noqa:E501
                                    set_process="customize", input_proc="name",
                                    process=["normalize_slang"])
        expected2 = [
                        [
                            'saya',
                            'suka',
                            'makin',
                            'apel',
                            'karena',
                            'rasanya',
                            'enak',
                            '!',
                            '!',
                            '!',
                            '😁',
                            '😆',
                            '😅'
                            ]
                    ]

        actual3 = st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"],  # noqa:E501
                                    set_process="customize", process=[10],
                                    return_types="list_of_sentences")
        expected3 = ['saya suka makin apel karena rasanya enak ! ! ! 😁 😆 😅']

        actual4 = st.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"],  # noqa:E501
                                    set_process="customize", input_proc="name",
                                    process=["normalize_slang"],
                                    return_types="list_of_sentences")
        expected4 = ['saya suka makin apel karena rasanya enak ! ! ! 😁 😆 😅']

        assert actual1 == expected1, MESSAGE
        assert actual2 == expected2, MESSAGE
        assert actual3 == expected3, MESSAGE
        assert actual4 == expected4, MESSAGE

    def test_df_auto_text_prep_default(self):

        actual1 = st.auto_text_prep(doc["text"])
        expected1 = [
            ['tvri', 'com', '14', '08', '1945', 'jadi', 'hari', 'merdeka'],
            ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']
            ]

        actual2 = st.auto_text_prep(doc["text"], return_types="list_of_sentences")  # noqa:E501
        expected2 = [
                    'tvri com 14 08 1945 jadi hari merdeka',
                    'ak suka mkn apel rasa enak'
                    ]

        assert actual1 == expected1, MESSAGE
        assert actual2 == expected2, MESSAGE

    def test_df_auto_text_prep_add_process(self):

        actual1 = st.auto_text_prep(doc["text"], set_process="add_process",
                                    process=[6, 11])  # noqa:E501
        expected1 = [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]  # noqa:E501

        actual2 = st.auto_text_prep(doc["text"], set_process="add_process",
                                    input_proc="name",
                                    process=["medianame_removal", "date_removal"])  # noqa:E501
        expected2 = [['jadi', 'hari', 'merdeka'], ['ak', 'suka', 'mkn', 'apel', 'rasa', 'enak']]  # noqa:E501

        actual3 = st.auto_text_prep(doc["text"], set_process="add_process",
                                    process=[6, 11],
                                    return_types="list_of_sentences")
        expected3 = ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

        actual4 = st.auto_text_prep(doc["text"], set_process="add_process",
                                    input_proc="name",
                                    process=["medianame_removal", "date_removal"],  # noqa:E501
                                    return_types="list_of_sentences")
        expected4 = ['jadi hari merdeka', 'ak suka mkn apel rasa enak']

        assert actual1 == expected1, MESSAGE
        assert actual2 == expected2, MESSAGE
        assert actual3 == expected3, MESSAGE
        assert actual4 == expected4, MESSAGE

    def test_df_auto_text_prep_customize(self):

        actual1 = st.auto_text_prep(doc["text"], set_process="customize",
                                    process=[6, 11])  # noqa:E501
        expected1 = [
                        ['telah', 'terjadi', 'hari', 'kemerdekaan'],
                        [
                            'ak',
                            'suka',
                            'mkn',
                            'apel',
                            'karena',
                            'rasanya',
                            'enak',
                            '!',
                            '!',
                            '!',
                            '😁',
                            '😆',
                            '😅'
                        ]
                    ]

        actual2 = st.auto_text_prep(doc["text"], set_process="customize",
                                    input_proc="name",
                                    process=["medianame_removal", "date_removal"])  # noqa:E501
        expected2 = [
                        ['telah', 'terjadi', 'hari', 'kemerdekaan'],
                        [
                            'ak',
                            'suka',
                            'mkn',
                            'apel',
                            'karena',
                            'rasanya',
                            'enak',
                            '!',
                            '!',
                            '!',
                            '😁',
                            '😆',
                            '😅'
                        ]
                    ]

        actual3 = st.auto_text_prep(doc["text"], set_process="customize",
                                    process=[6, 11],  # noqa:E501
                                    return_types="list_of_sentences")
        expected3 = [
                    'telah terjadi hari kemerdekaan',
                    'ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

        actual4 = st.auto_text_prep(doc["text"], set_process="customize",
                                    input_proc="name",
                                    process=["medianame_removal", "date_removal"],  # noqa:E501
                                    return_types="list_of_sentences")
        expected4 = [
                    'telah terjadi hari kemerdekaan',
                    'ak suka mkn apel karena rasanya enak!!! 😁 😆 😅']

        assert actual1 == expected1, MESSAGE
        assert actual2 == expected2, MESSAGE
        assert actual3 == expected3, MESSAGE
        assert actual4 == expected4, MESSAGE
