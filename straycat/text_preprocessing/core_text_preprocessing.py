"""Module for That contain Text Preprocessing pipeline"""
import spacy
import nltk
import re
import json
import os
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from .count_decorator import counted


class CoreTextPreprocessing:
    """Steps of Text Preprocessing class which contains case folding,encode text, tokenizing,
    stopwords removal, punctuation removal, stemmming, date removal,
    normalize slang, link removal, medianame removal, non alnum removal, emoji removal
    """

    CALL_SPACY = None

    @counted
    def called_spacy(self):
        """Instantiation spacy module for bahasa Indonesia"""
        CoreTextPreprocessing.CALL_SPACY = spacy.blank('id')

    def __init__(
            self,
            other_stp_words=None,
            token_lib="spacy",
            set_stop_words=None):
        """Constructor which contain set of stopwords

        Args:
        other_stp_words (list,optional): list of stopwords from additional stopwords. (Default value = None)
        set_stop_words (set, optional): set of stopwords, if any additional, will be merged. (Default value = None)
        token_lib ("spacy","nltk"): library for tokenize text, (Default value = spacy)
        """
        self.token_lib = token_lib
        self.other_stp_words = other_stp_words
        stprf = StopWordRemoverFactory()
        self.stemmer = StemmerFactory().create_stemmer()

        # print(self.called_spacy.calls)
        if self.called_spacy.calls == 0:
            self.called_spacy()
        else:
            pass
        # print(self.called_spacy.calls)

        if self.other_stp_words is None:
            self.set_stop_words = set(stprf.get_stop_words())
        else:
            # merge_stp_words=stprf.get_stop_words()+other_stp_words
            # self.set_stop_words=set([word.lower() for word in merge_stp_words])
            self.set_stop_words = set([word.lower()
                                      for word in other_stp_words])

    def __repr__(self):
        if self.other_stp_words is None:
            return f"Default Stopwords"
        else:
            return f"Using other Stopwords"

    @classmethod
    def append_stop_words(cls, words=None, filenames=None, delimiter="\n"):
        """Add additional Stopwords from .txt or list

        Args:
          filenames(str, optional): str file will be process delimiter. (Default value = None)
          words(list, optional): list of stopwords. (Default value = None)
          delimiter: the delimiter of .txt file. (Default value = "\n")

        Returns:
          list: list of additional stopwords

        """

        other_stp_words = []
        if filenames is not None:
            with open(filenames) as f:
                for word in f:
                    word = word.strip(delimiter)
                    other_stp_words.append(word)
        else:
            for word in words:
                other_stp_words.append(word)

        return cls(other_stp_words)

    def encode_text(self, text):
        """Encode the text

        Args:
          text(str): The sentence or paragraph of the documents

        Returns:
          str: The sentence or paragraph of the documents with encode

        >>> st.encode_text("saya \x94sedang memakan apple")
        "saya sedang memakan apple"
        """
        return text.encode("ASCII", "ignore").decode("UTF-8")

    def tokenize(self, text):
        """Tokenize the text

        Args:
          text(str): The sentence or paragraph from the documents

        Returns:
          list: list of token

        >>> st.tokenize("saya sedang memakan apple")
        ["saya", "sedang", "memakan", "apple"]
        """
        if self.token_lib == "spacy":
            tokens = CoreTextPreprocessing.CALL_SPACY(text)
            return [token.text for token in tokens]
        elif self.token_lib == "nltk":
            return nltk.tokenize.word_tokenize(text)
        else:
            raise ValueError("library not found")

    def concate_token(self, token):
        """concate token into sentences

        Args:
          token(str): list of token will be concate

        Returns:
          str: the sentences formed from the sentence

        >>> st.concate_token(["saya", "sedang", "memakan", "apple"])
        "saya sedang memakan apple"
        """
        kalimat = " ".join(token)
        kalimat = re.sub("\\s+", " ", kalimat)
        if len(re.findall("\\W*quot\\W*", kalimat)) != 0:
            kalimat = re.sub("\\W*quot\\W*", " ", kalimat)
        kalimat = kalimat.strip(" ")
        return kalimat

    def normalize_slang(self, text,return_type="sentences"):
        """Remove slang words from text

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): the sentences or token without slang words.

        >>> st.normalize_slang("ak sk mkan")
        "saya suka makan"
        >>> st.normalize_slang("ak sk mkan", return_type = "tokens")
        ["saya", "suka", "makan"]
        """
        kamus_alay = {}
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + "/data/slangwords.json", 'r') as f:
            kamus_alay = json.load(f)
        tokens = self.tokenize(text)
        for token in tokens:
            if token in kamus_alay:
                index = tokens.index(token)
                tokens[index] = kamus_alay[token]

        if return_type == "sentences":
            return self.concate_token(tokens)
        elif return_type == "tokens":
            return tokens
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_medianame(self, text, return_type="sentences"):
        """Remove media name from text

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): the sentences or tokens without media name.

        >>> st.remove_medianame("kompas.com berita hari ini")
        "berita hari ini"
        >>> st.remove_medianame("kompas.com berita hari ini", return_type = "tokens")
        ["berita", "hari", "ini"]
        """
        list_media = []
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + "/data/media.txt", 'r') as f:
            list_media = [line.rstrip('\n').lower() for line in f]

        regex = "\\w*.com|\\w*.tv|\\w*.co|\\w*.id|"
        for word in list_media:
            regex += word + "|"
        
        text=re.sub(regex, "", text.lower())
        text=" ".join(text.split())

        if return_type == "sentences":
            return text
        elif return_type == "tokens":
            return self.tokenize(text)
        else:
            raise ValueError("argument "+return_type+" not found")


    def remove_link(self, text,return_type="sentences"):
        """

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): the sentences or tokens without link.

        >>> st.remove_link("https://www.kompas.com berita hari ini")
        "berita hari ini"
        >>> st.remove_link("https://www.kompas.com berita hari ini", return_type = "tokens")
        ["berita", "hari", "ini"]
        """

        # all link only
        regex = "(?:(?:https?|ftp|file):\\/\\/|www\\.|ftp\\.|[A-Za-z]+\\.|[A-Za-z]+\\d+\\.)(?:\\([-A-Z0-9+&@#\\/%=~_|$?!:,.]*\\)|[-A-Z0-9+&@#\\/%=~_|$?!:,.])*(?:\\([-A-Z0-9+&@#\\/%=~_|$?!:,.]*\\)|[A-Z0-9+&@#\\/%=~_|$])"

        # all link and domain like 255.255.
        # regex =
        # "([\w+]+\:\/\/)?([\w\d-]+\.)*[\w-]+[\.\:]\w+([\/\?\=\&\#.]?[\w-]+)*\/?"

        # regex="""[a-zA-Z0-9.]*\\.com|[a-zA-Z0-9.]*\\.xyz|[a-zA-Z0-9.]*\\.id|\
        # 	[a-zA-Z0-9.]*\\.online|http\S+|[a-zA-Z0-9.]*\\.org|[a-zA-Z0-9.]*\\.tv|[a-zA-Z0-9.]*\\.co"""

        text = re.sub(regex, "", text.lower(), flags=re.IGNORECASE)
        text = " ".join(text.split())

        if return_type == "sentences":
            return text 
        elif return_type == "tokens":
            return self.tokenize(text)
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_date(self, text,return_type="sentences"):
        """Remove date from document

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens without date

        >>> st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal")
        "tanggal tanggal"
        >>> st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal",return_type="tokens")
        ["tanggal", "tanggal"]
        """

        bulan = {
            "januari": "01",
            "februari": "02",
            "maret": "03",
            "april": "04",
            "mei": "05",
            "juni": "06",
            "juli": "07",
            "agustus": "08",
            "september": "09",
            "oktober": "10",
            "november": "11",
            "desember": "12",
            "jan": "01",
            "feb": "02",
            "mar": "03",
            "apr": "04",
            "may": "05",
            "jun": "06",
            "jul": "07",
            "agu": "08",
            "sep": "09",
            "okt": "10",
            "des": "12",
            "nov": "12",
            "oct": "10",
            "dec": "12",
            "aug": "08"}
        str_month = ""
        for el in bulan.keys():
            str_month += el + "|"

        regex = "\\d{2}\\W\\d{2}\\W\\d{4}|\\d+\\W(?:" + \
            str_month + ")\\W\\d{4}"

        text=re.sub(regex, "", text.lower())
        text=" ".join(text.split())

        if return_type == "sentences":
            return text
        elif return_type == "tokens":
            return self.tokenize(text)
        else:
            raise ValueError("argument "+return_type+" not found")


    def remove_emoji(self, text,return_type="sentences"):
        """

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens without emoji

        >>> st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha")
        "hahaha hahaha hahaha"
        >>> st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha", return_type="tokens")
        ["hahaha","hahaha","hahaha"]
        """
        regex = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

        tokens = self.tokenize(text)
        for token in tokens:
            if re.match(regex, token) is not None:
                index = tokens.index(token)
                tokens[index] = ''
        
        if return_type == "sentences":
            return self.concate_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")


    def stop_words(self, text,return_type="sentences"):
        """remove stopwords from the documents

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens without stopwords

        >>> st.stop_words("apel yang terlihat lezat")
        "apel terlihat lezat"
        >>> st.stop_words("apel yang terlihat lezat",return_type="tokens")
        ["apel","terlihat","lezat"]
        """
        tokens = self.tokenize(text)
        for token in tokens:
            if token in self.set_stop_words:
                index = tokens.index(token)
                tokens[index] = ''
        if return_type == "sentences":
            return self.concate_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_punc(self, text, return_type="sentences"):
        """Remove punctuation from document

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens without punctuation

        >>> st.remove_punc("dapat hubungi akun@google !!!")
        "dapat hubungi akun@google"
        >>> st.remove_punc("dapat hubungi akun@google !!!", return_type="tokens")
        ["dapat","hubungi","akun@google"]
        """

        tokens = self.tokenize(text)
        for token in tokens:
            if re.match("\\W+", token) is not None:
                # if re.match("\n",token) != None:
                index = tokens.index(token)
                tokens[index] = ''
        if return_type == "sentences":
            return self.concate_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_non_alnum(self, text, return_type="sentences"):
        """

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens only

        >>> st.remove_non_alnum("dapat hubungi akun@google !!!")
        "dapat hubungi"
        >>> st.remove_non_alnum("dapat hubungi akun@google !!!", return_type="tokens")
        ["dapat","hubungi"]
        """

        tokens = self.tokenize(text)
        for token in tokens:
            if token.isalnum() == False:
                # if re.match("\n",token) != None:
                index = tokens.index(token)
                tokens[index] = ''
        
        if return_type == "sentences":
           return self.concate_token(tokens)
        elif return_type == "tokens":
           return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")
            
    def stemming(self, text,return_type="sentences"):
        """Stemming the sentences to stem words

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens with stem words

        >>> st.stemming("saya suka memakan apple")
        "saya suka makan apple"
        >>> st.stemming("saya suka memakan apple", return_type="tokens")
        ["saya","suka","makan","apple"]
        """
        tokens = self.tokenize(text)
        for token in tokens:
            index = tokens.index(token)
            tokens[index] = self.stemmer.stem(token)
        
        if return_type == "sentences":
            return self.concate_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")
            

    def case_folding(self, text, return_type="sentences"):
        """

        Args:
          text: str
          return_type: sentences (Default value = "sentences")

        Returns:
          (str,list): The sentences or tokens with stem words

        >>> st.case_folding("saya suka memakan apple")
        "saya suka memakan apple"
        >>> st.case_folding("saya suka memakan apple", return_type="tokens")
        ["saya","suka","memakan","apple"]
        """

        if return_type == "sentences":
            if isinstance(text, str):
                return text.lower()
            else:
                return text.str.lower()

        elif return_type == "tokens":
            if isinstance(text, str):
                return self.tokenize(text.lower())
            else:
                return self.tokenize(text.str.lower())

        else:
            raise ValueError("argument "+return_type+" not found")
