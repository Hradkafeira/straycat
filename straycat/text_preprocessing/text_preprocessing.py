""""Module for Automate Text Preprocessing"""
# from warnings import catch_warnings
from .core_text_preprocessing import CoreTextPreprocessing

class TextPreprocessing(CoreTextPreprocessing):
    """ Module for Automate Text Preprocessing"""
    def auto_text_prep(self, series, set_process="standard",process=None, return_types="list_of_tokens"):
        """automate text_preprocessing steps

        Args:
          series(series, numpy array, list): the sentences will be processing
          process:["case_folding","punctuation_removal",
                  "stopwords_removal","stemming","encode_text",
                  "medianame_removal","non_alnum_removal",
                  "link_removal","date_removal","emoji_removal",
                  "normalize_slang"] (Default value = None)
          set_process: "standard","add_process","customize" (Default value = "standard")

        Returns:
          List: sentences or tokens of the cleaning text

        >>> st.auto_text_preprocessing(df["example_sentence"])
        ["sentence 1","sentence 2", dll]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"])
        [['ak', 'suka', 'mkan', 'apel', 'rasa', 'enak']]
        
        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],return_types="list_of_sentences")
        ['ak suka mkan apel rasa enak']
        
        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"],
                                set_process="customize",process=["normalize_slang"] )
        [['saya','suka','makan','apel','karena','rasanya','enak','!','!','!','😁','😆','😅']]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!! 😁 😆 😅"],
                                set_process="customize",process=["normalize_slang"], 
                                return_types="list_of_sentences")
        ['saya suka makan apel karena rasanya enak ! ! ! 😁 😆 😅']

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                                set_process="add_process",process=["normalize_slang"] )
        [['saya', 'suka', 'makan', 'apel', 'rasa', 'enak']]

        >>> st.auto_text_prep(["ak suka mkan apel karena rasanya enak!!!"],
                                set_process="add_process",process=["normalize_slang"], 
                                return_types="list_of_sentences" )
        ['saya suka makan apel rasa enak']
        """
        if type(series) == str or type(series) == dict:
            raise ValueError("input type must be List or numpy array or series")
        # function reference: dispatcher function
        steps = {
            "case_folding": self.case_folding,
            "punctuation_removal": self.remove_punc,
            "stopwords_removal": self.stop_words,
            "stemming": self.stemming,
            "encode_text": self.encode_text,
            "medianame_removal": self.remove_medianame,
            "non_alnum_removal": self.remove_non_alnum,
            "link_removal": self.remove_link,
            "emoji_removal": self.remove_emoji,
            "normalize_slang": self.normalize_slang,
            "date_removal": self.remove_date
        }

        def call_func(text, func):
            """ Dispatcher function

            Args:
              text: the sentences that will be process
              func: the keys in steps dictionaries

            Returns:
              str: the sentences that processed from specific function

            >>> call_func(["LAPER EUY"],["lowercase"])
            "laper euy"

            """
            try:
                not_return_token=["tokenize","encode_text"]
                if func in not_return_token:
                    return steps[func](text)
                else:
                    return steps[func](text, return_type="sentences")
            except BaseException:
                raise ValueError("Process {func} Not Found".format(func=func))
        ########################################
        if set_process == "standard":

            if process != None:
                raise ValueError("standard process no needed additional process, try 'customize' or 'add_process' argument")
            else:   
                for i,step in enumerate(steps):
                    if i <= 3:
                        series = [*map(lambda word:call_func(word, step), series)]
            
        elif set_process == "add_process":

            try:

                if len(process) == 0:
                    raise ValueError("process can't be empty") 
                else:
                    temp_proc=[]

                    for i,step in enumerate(steps):
                        if i <= 3:
                            temp_proc.append(step)

                    for step in process:
                        temp_proc.append(step)
                    
                    process=temp_proc
                    del temp_proc
                    
                    for step in process:
                        series = [*map(lambda word:call_func(word, step), series)]

            except TypeError:

                raise ValueError("process must be added")

            
        elif set_process == "customize":

            try:
                if len(process) == 0:
                    raise ValueError("process can't be empty") 
                else:
                    for step in process:
                        series = [*map(lambda word:call_func(word, step), series)]

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