from straycat.text_preprocessing.text_preprocessing import TextPreprocessing

st = TextPreprocessing()

class TestTextPreprocessing(object):

    def test_auto_text_prep(self):
        actual = st.tokenize("saya sedang memakan apple")
        expected = ["saya", "sedang", "memakan", "apple"]
        assert actual == expected,MESSAGE