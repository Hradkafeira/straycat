from straycat.text_preprocessing.core_text_preprocessing import CoreTextPreprocessing

st=CoreTextPreprocessing()

MESSAGE="the return value of process doesn't match to expected value"

class TestCoreTextPreprocessing(object):

    def test_tokenize(self):
        actual = st.tokenize("saya sedang memakan apple")
        expected = ["saya", "sedang", "memakan", "apple"]
        assert actual == expected,MESSAGE

    def test_concat_token(self):
        actual = st.concat_token(["saya", "sedang", "memakan", "apple"])
        expected = "saya sedang memakan apple"
        assert actual == expected,MESSAGE

    def test_stop_words(self):
        actual1 = st.stop_words("apel yang terlihat lezat")
        expected1 = ["apel","terlihat","lezat"]

        actual2 = st.stop_words("apel yang terlihat lezat",return_type="sentences")
        expected2 = "apel terlihat lezat"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_encode_text(self):
        actual = st.encode_text("saya \x94sedang memakan apple")
        expected = "saya sedang memakan apple"
        assert actual == expected,MESSAGE
    
    def test_normalize_slang(self):
        actual1 = st.normalize_slang("ak sk mkan")
        expected1 = ["saya", "suka", "makan"]

        actual2 = st.normalize_slang("ak sk mkan", return_type = "sentences")
        expected2 = "saya suka makan"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_remove_medianame(self):
        actual1 = st.remove_medianame("kompas.com berita hari ini")
        expected1 = ["berita", "hari", "ini"]

        actual2 = st.remove_medianame("kompas.com berita hari ini", return_type = "sentences")
        expected2 = "berita hari ini"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_remove_link(self):
        actual1 = st.remove_link("https://www.kompas.com berita hari ini")
        expected1 = ["berita", "hari", "ini"]

        actual2 = st.remove_link("https://www.kompas.com berita hari ini", return_type = "sentences")
        expected2 = "berita hari ini"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_remove_date(self):
        actual1 = st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal")
        expected1 = ["tanggal", "tanggal"]

        actual2 = st.remove_date("tanggal 03 Maret 2020 17/08/1945 10-11-1945 tanggal",return_type="sentences")
        expected2 = "tanggal tanggal"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_remove_emoji(self):
        actual1 = st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha")
        expected1 = ["hahaha","hahaha","hahaha"]

        actual2 = st.remove_emoji("hahaha 😀 😃 😄 hahaha 😁 😆 😅 hahaha", return_type="sentences")
        expected2 = "hahaha hahaha hahaha"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE
    
    def test_remove_punc(self):
        actual1 = st.remove_punc("dapat hubungi akun@google !!!")
        expected1 = ["dapat","hubungi","akun@google"]

        actual2 = st.remove_punc("dapat hubungi akun@google !!!", return_type="sentences")
        expected2 = "dapat hubungi akun@google"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_remove_non_alnum(self):
        actual1 = st.remove_non_alnum("dapat hubungi akun@google !!!")
        expected1 = ["dapat","hubungi"]

        actual2 = st.remove_non_alnum("dapat hubungi akun@google !!!", return_type="sentences")
        expected2 = "dapat hubungi"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE
    
    def test_stemming(self):
        actual1 = st.stemming("saya suka memakan apple")
        expected1 = ["saya","suka","makan","apple"]

        actual2 = st.stemming("saya suka memakan apple", return_type="sentences")
        expected2 = "saya suka makan apple"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE

    def test_case_folding(self):
        actual1 = st.case_folding("saya suka memakan apple")
        expected1 = ["saya","suka","memakan","apple"]

        actual2 = st.case_folding("saya suka memakan apple", return_type="sentences")
        expected2 = "saya suka memakan apple"

        assert actual1 == expected1,MESSAGE
        assert actual2 == expected2,MESSAGE