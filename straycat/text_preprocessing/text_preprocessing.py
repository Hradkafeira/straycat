""""Module for Automate Text Preprocessing"""

from .core_text_preprocessing import _CoreTextPreprocessing


class TextPreprocessing(_CoreTextPreprocessing):
    """ Module for Automate Text Preprocessing"""

    def list_process(self):
        return """
                    Here the list for auto_text_prep
                    Input value with number 1 or text "case_folding"
                    1  --> "case_folding"
                    2  --> "punctuation_removal"
                    3  --> "stopwords_removal"
                    4  --> "stemming"
                    5  --> "encode_text"
                    6  --> "medianame_removal"
                    7  --> "non_alnum_removal"
                    8  --> "link_removal"
                    9  --> "emoji_removal"
                    10 --> "normalize_slang"
                    11 --> "date_removal"
                """

    def auto_text_prep(self, series,
                       set_process="standard",
                       process=None, input_proc="num",
                       return_types="list_of_tokens"):
        """automate text_preprocessing _steps

        Args:
          series(series, numpy array, list): the sentences will be processing
          process:[
                    1  --> "case_folding"
                    2  --> "punctuation_removal"
                    3  --> "stopwords_removal"
                    4  --> "stemming"
                    5  --> "encode_text"
                    6  --> "medianame_removal"
                    7  --> "non_alnum_removal"
                    8  --> "link_removal"
                    9  --> "emoji_removal"
                    10 --> "normalize_slang"
                    11 --> "date_removal"
                ]
                (Default value = None)
          set_process: "standard",
                       "add_process",
                       "customize"
                       (Default value = "standard")
          input_proc: "num", "name"

        Returns:
          List: sentences or tokens of the cleaning text

        >>> st.auto_text_preprocessing(df["example_sentence"])
        ["sentence 1","sentence 2", dll]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak! 😁 😆"])
        [['ak', 'suka', 'mkan', 'apel', 'rasa', 'enak']]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                              return_types="list_of_sentences")
        ['ak suka mkan apel rasa enak']

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak! 😆 😅"],
                                set_process="customize",input_proc="name",
                                process=["normalize_slang"])
        [['saya','suka','makan','apel','karena','rasanya','enak','!','😆','😅']]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak! 😆 😅"],
                                set_process="customize",process=[10],
                                return_types="list_of_sentences")
        ['saya suka makan apel karena rasanya enak ! ! ! 😁 😆 😅']

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                                set_process="add_process",
                                process=[10])
        [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                                set_process="add_process",
                                input_proc="str",
                                process=["normalize_slang"],
                                return_types="list_of_sentences")
        [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]
        """
        if type(series) == str or type(series) == dict:
            raise ValueError("input type must be List or numpy array or series")  # noqa:E501
        # function reference: dispatcher function

        _pipelines = {
                    1: "case_folding",
                    2: "punctuation_removal",
                    3: "stopwords_removal",
                    4: "stemming",
                    5: "encode_text",
                    6: "medianame_removal",
                    7: "non_alnum_removal",
                    8: "link_removal",
                    9: "emoji_removal",
                    10: "normalize_slang",
                    11: "date_removal"
                    }
        _functions = [
                    self.case_folding,
                    self.remove_punc,
                    self.stop_words,
                    self.stemming,
                    self.encode_text,
                    self.remove_medianame,
                    self.remove_non_alnum,
                    self.remove_link,
                    self.remove_emoji,
                    self.normalize_slang,
                    self.remove_date
                ]

        _values_funcs_dict = dict(zip(_pipelines.values(), _functions))
        _keys_funcs_dict = dict(zip(_pipelines.keys(), _functions))

        _steps = {}

        if input_proc == "num":
            for num in _keys_funcs_dict:
                _steps[num] = _keys_funcs_dict[num]
        elif input_proc == "name":
            for txt in _values_funcs_dict:
                _steps[txt] = _values_funcs_dict[txt]
        else:
            raise ValueError("input_proc must be 'num' or 'name'")

        def _call_func(text, func):
            """ Dispatcher function

            Args:
              text: the sentences that will be process
              func: the keys in _steps dictionaries

            Returns:
              str: the sentences that processed from specific function

            >>> _call_func(["LAPER EUY"],["lowercase"])
            "laper euy"

            """
            try:
                not_return_token = ["tokenize", "encode_text"]
                if func in not_return_token:
                    return _steps[func](text)
                else:
                    return _steps[func](text, return_type="sentences")
            except BaseException:
                raise ValueError("Process {func} Not Found".format(func=func))
        ########################################

        def _check_process_args():
            if type(process[0]) == str and input_proc == "num":
                raise ValueError("value process are 'name' but input_proc is 'num'")  # noqa:E501
            elif type(process[0]) == int and input_proc == "name":
                raise ValueError("value process are 'num' but input_proc is 'name'")  # noqa:E501
            else:
                pass

        if set_process == "standard":

            if process is not None:
                raise ValueError("standard process no needed additional process, try 'customize' or 'add_process' argument")  # noqa:E501
            else:
                for i, step in enumerate(_steps):
                    if i <= 3:
                        series = [*map(lambda word:_call_func(word, step), series)]  # noqa:E501

        elif set_process == "add_process":

            try:

                if len(process) == 0:
                    raise ValueError("process can't be empty")
                else:
                    temp_proc = []

                    _check_process_args()

                    for i, step in enumerate(_steps):
                        if i <= 3:
                            temp_proc.append(step)

                    for step in process:
                        temp_proc.append(step)

                    process = temp_proc
                    del temp_proc

                    for step in process:
                        series = [*map(lambda word:_call_func(word, step), series)]  # noqa:E501

            except TypeError:
                raise ValueError("process must be added")

        elif set_process == "customize":

            try:
                if len(process) == 0:
                    raise ValueError("process can't be empty")
                else:

                    _check_process_args()

                    for step in process:
                        series = [*map(lambda word:_call_func(word, step), series)]  # noqa:E501

            except TypeError:
                raise ValueError("process must be added")

        else:
            raise ValueError("process Not Found")

        if return_types == "list_of_sentences":
            return series

        elif return_types == "list_of_tokens":
            return [self.tokenize(txt) for txt in series]

        else:
            raise ValueError("Return types not found")
