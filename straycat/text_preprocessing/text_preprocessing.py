""""Module for Automate Text Preprocessing"""
# from warnings import catch_warnings
from .core_text_preprocessing import CoreTextPreprocessing

class TextPreprocessing(CoreTextPreprocessing):
    """ Module for Automate Text Preprocessing"""
    def auto_text_prep(self, series, set_process="standard",process=None):
        """automate text_preprocessing steps

        Args:
          series(series): the sentences will be processing
          process: (Default value = None)
          set_process:  (Default value = "standard")

        Returns:
          List: sentences or tokens of the cleaning text

        >>> text_prep.auto_text_preprocessing(df["example_sentence"])
        ["sentence 1","sentence 2", dll]
        >>> text_prep.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅])
        ["ak suka mkn apel rasa enak"]
        >>> textp_prep.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"],
                                        set_process="add_process",process=["normalize_slang"])
        ['saya suka makan apel rasa enak']
        >>> textp_prep.auto_text_prep(["ak suka mkn apel karena rasanya enak!!! 😁 😆 😅"],
                                        set_process="customize",process=["emoji_removal","punctuation_removal"])
        ['ak suka mkan apel karena rasanya enak']

        """

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
                return steps[func](text)
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

            
        elif set_process == "customize":
            for step in process:
                series = [*map(lambda word:call_func(word, step), series)]
        
        else:
            raise ValueError("process Not Found")

        return series