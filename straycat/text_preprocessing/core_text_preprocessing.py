"""Module for That contain Text Preprocessing pipeline"""
import spacy
import re
import json
import os
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.\
    StopWordRemoverFactory import StopWordRemoverFactory as swsastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from .count_decorator import counted


class _CoreTextPreprocessing:
    """
    Steps of Text Preprocessing class which contains:
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

    _CALL_SPACY = None
    _CALL_METHODCLASS_STOPWORDS = False

    @counted
    def _called_spacy(self):
        """Instantiation spacy module for bahasa Indonesia"""
        _CoreTextPreprocessing._CALL_SPACY = spacy.blank('id')

    def __init__(
            self,
            other_stopwords=None,
            token_lib="spacy"):
        """Constructor which contain set of stopwords

        Args:
        other_stopwords (list,optional): other stopwords (Default value = None)
        token_lib ("spacy","nltk"): tokenize library, (Default value = spacy)
        """
        self.token_lib = token_lib
        self.stemmer = StemmerFactory().create_stemmer()
        self.other_stopwords = other_stopwords
        # print(self._called_spacy.calls)
        if self._called_spacy.calls == 0:
            self._called_spacy()
        else:
            pass
        # print(self._called_spacy.calls)

        if self.other_stopwords is None:
            self.stopwords_lib = set(swsastrawi().get_stop_words())
        else:
            try:
                if type(other_stopwords) == str:
                    raise ValueError("type must be list")
                else:
                    self.stopwords_lib = set([word.lower() for word in other_stopwords])  # noqa:E501
            except TypeError:
                raise TypeError("type must be list")

    def __repr__(self):
        if self.other_stopwords is None and _CoreTextPreprocessing._CALL_METHODCLASS_STOPWORDS is False:  # noqa:E501
            return "Default Stopwords"
        elif self.other_stopwords is not None and _CoreTextPreprocessing._CALL_METHODCLASS_STOPWORDS is True:  # noqa:E501
            return "Add Stopwords"
        else:
            return "Use other Stopwords"

    @classmethod
    def add_stopwords(cls, add_sw=None, filenames=None, delimiter="\n"):
        """Add additional Stopwords from .txt or list

        Args:
          filenames(str, optional): filename. (Default value = None)
          add_sw(list, optional): stopwords list. (Default value = None)
          delimiter: the delimiter of .txt file. (Default value = "\n")

        Returns:
          list: list of additional stopwords

        """
        try:
            stopwords = []

            if filenames is not None and add_sw is None:
                with open(filenames) as f:
                    for word in f:
                        word = word.strip(delimiter)
                        stopwords.append(word)
            elif filenames is None and add_sw is not None:
                if type(add_sw) == str:
                    raise ValueError("type must be list")
                else:
                    for word in add_sw:
                        stopwords.append(word)
            else:
                raise ValueError("can't filled both of arguments")

            stopwords_lib = set(swsastrawi().get_stop_words() + stopwords)

            _CoreTextPreprocessing._CALL_METHODCLASS_STOPWORDS = True

            return cls(stopwords_lib)

        except TypeError:
            raise TypeError("type must be list")

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
            tokens = _CoreTextPreprocessing._CALL_SPACY(text)
            return [token.text for token in tokens]
        elif self.token_lib == "nltk":
            return word_tokenize(text)
        else:
            raise ValueError("library not found")

    def concat_token(self, token):
        """concat token into sentences

        Args:
          token(str): list of token will be concat

        Returns:
          str: the sentences formed from the sentence

        >>> st.concat_token(["saya", "sedang", "memakan", "apple"])
        "saya sedang memakan apple"
        """
        kalimat = " ".join(token)
        kalimat = re.sub("\\s+", " ", kalimat)
        if len(re.findall("\\W*quot\\W*", kalimat)) != 0:
            kalimat = re.sub("\\W*quot\\W*", " ", kalimat)
        kalimat = kalimat.strip(" ")
        return kalimat

    def normalize_slang(self, text, return_type="tokens"):
        """Remove slang words from text

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): the sentences or token without slang words.

        >>> st.normalize_slang("ak sk mkan")
        ["saya", "suka", "makan"]
        >>> st.normalize_slang("ak sk mkan", return_type = "sentences")
        "saya suka makan"
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
            return self.concat_token(tokens)
        elif return_type == "tokens":
            return tokens
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_medianame(self, text, return_type="tokens"):
        """Remove media name from text

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): the sentences or tokens without media name.

        >>> st.remove_medianame("kompas.com berita hari ini")
        ["berita", "hari", "ini"]
        >>> st.remove_medianame("kompas.com berita hari ini",
                                return_type = "sentences")
        "berita hari ini"
        """
        list_media = []
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + "/data/media.txt", 'r') as f:
            list_media = [line.rstrip('\n').lower() for line in f]

        regex = "\\w*.com|\\w*.tv|\\w*.co|\\w*.id|"
        for word in list_media:
            regex += word + "|"

        text = re.sub(regex, "", text.lower())
        text = " ".join(text.split())

        if return_type == "sentences":
            return text
        elif return_type == "tokens":
            return self.tokenize(text)
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_link(self, text, return_type="tokens"):
        """

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): the sentences or tokens without link.

        >>> st.remove_link("https://www.kompas.com berita hari ini")
        ["berita", "hari", "ini"]
        >>> st.remove_link("https://www.kompas.com berita hari ini",
                            return_type = "sentences")
        "berita hari ini"
        """

        # all link only
        regex = "(?:(?:https?|ftp|file):\\/\\/|www\\.|ftp\\.|[A-Za-z]+\\.|" + \
                "[A-Za-z]+\\d+\\.)(?:\\([-A-Z0-9+&@#\\/%=~_|$?!:,.]*\\)|" + \
                "[-A-Z0-9+&@#\\/%=~_|$?!:,.])" + \
                "*(?:\\([-A-Z0-9+&@#\\/%=~_|$?!:,.]*\\)|[A-Z0-9+&@#\\/%=~_|$])"

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

    def remove_date(self, text, return_type="tokens"):
        """Remove date from document

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens without date

        >>> st.remove_date("tanggal 03 Mei 2020 17/08/1945 10-11-1945 tanggal")
        ["tanggal", "tanggal"]
        >>> st.remove_date("tanggal 03 Mei 2020 17/08/1945 10-11-1945 tanggal",
                            return_type="sentences")
        "tanggal tanggal"
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

        text = re.sub(regex, "", text.lower())
        text = " ".join(text.split())

        if return_type == "sentences":
            return text
        elif return_type == "tokens":
            return self.tokenize(text)
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_emoji(self, text, return_type="tokens"):
        """Remove emoji from text

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens without emoji

        >>> st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha")
        ["hahaha","hahaha","hahaha"]
        >>> st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha",
                            return_type="sentences")
        "hahaha hahaha hahaha"
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
            return self.concat_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def stop_words(self, text, return_type="tokens"):
        """Remove stopwords from the documents

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens without stopwords

        >>> st.stop_words("apel yang terlihat lezat")
        ["apel","terlihat","lezat"]
        >>> st.stop_words("apel yang terlihat lezat",return_type="sentences")
        "apel terlihat lezat"
        """
        tokens = self.tokenize(text)
        for token in tokens:
            if token in self.stopwords_lib:
                index = tokens.index(token)
                tokens[index] = ''
        if return_type == "sentences":
            return self.concat_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_punc(self, text, return_type="tokens"):
        """Remove punctuation from document

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens without punctuation

        >>> st.remove_punc("dapat hubungi akun@google !!!")
        ["dapat","hubungi","akun@google"]
        >>> st.remove_punc("dapat hubungi akun@google !!!",
                            return_type="sentences")
        "dapat hubungi akun@google"
        """

        tokens = self.tokenize(text)
        for token in tokens:
            if re.match("\\W+", token) is not None:
                # if re.match("\n",token) != None:
                index = tokens.index(token)
                tokens[index] = ''
        if return_type == "sentences":
            return self.concat_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def remove_non_alnum(self, text, return_type="tokens"):
        """

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens only

        >>> st.remove_non_alnum("dapat hubungi akun@google !!!")
        ["dapat","hubungi"]
        >>> st.remove_non_alnum("dapat hubungi akun@google !!!",
                                return_type="sentences")
        "dapat hubungi"
        """

        tokens = self.tokenize(text)
        for token in tokens:
            if token.isalnum() is False:
                # if re.match("\n",token) != None:
                index = tokens.index(token)
                tokens[index] = ''

        if return_type == "sentences":
            return self.concat_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def stemming(self, text, return_type="tokens"):
        """Stemming the sentences to stem words

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens with stem words

        >>> st.stemming("saya suka memakan apple")
        ["saya","suka","makan","apple"]
        >>> st.stemming("saya suka memakan apple", return_type="sentences")
        "saya suka makan apple"
        """
        tokens = self.tokenize(text)
        for token in tokens:
            index = tokens.index(token)
            tokens[index] = self.stemmer.stem(token)

        if return_type == "sentences":
            return self.concat_token(tokens)
        elif return_type == "tokens":
            return [token for token in tokens if token.strip()]
        else:
            raise ValueError("argument "+return_type+" not found")

    def case_folding(self, text, return_type="tokens"):
        """

        Args:
          text: str
          return_type: "sentences" or "tokens" (Default value = "tokens")

        Returns:
          (str,list): The sentences or tokens with stem words

        >>> st.case_folding("saya suka memakan apple")
        ["saya","suka","memakan","apple"]
        >>> st.case_folding("saya suka memakan apple", return_type="sentences")
        "saya suka memakan apple"
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
