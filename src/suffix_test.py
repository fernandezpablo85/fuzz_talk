from suffix import remove_suffix as remove


def test_remove_suffix():
    assert "pablo" == remove(suffix="@gmail.com", string="pablo@gmail.com")
    assert "google" == remove(suffix=".com.ar", string="google.com.ar")
    assert "google.com.ar" == remove(suffix=".not. .suffix", string="google.com.ar")
