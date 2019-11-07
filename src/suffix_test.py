from suffix import remove_suffix


def test_remove_suffix():
    assert "pablo.fernandez" == remove_suffix("@gmail.com", "pablo.fernandez@gmail.com")
    assert "google" == remove_suffix(".com.ar", "google.com.ar")
    assert "google.com.ar" == remove_suffix(".not.a.suffix", "google.com.ar")
