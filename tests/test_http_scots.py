import http
from http import HTTPMethod as StdMethod
from http import HTTPStatus as StdStatus

import pytest

from http_scots import HTTPMethod, HTTPStatus


def test_submodule_import_is_the_same_thing():
    from http_scots import http

    assert http.HTTPStatus is HTTPStatus
    assert http.HTTPMethod is HTTPMethod


def test_status_codes_are_ints():
    assert HTTPStatus.GET_TAE_FUCK == 403
    assert isinstance(HTTPStatus.NAE_BOTHER, int)


def test_status_lookup_by_code():
    assert HTTPStatus(404) is HTTPStatus.NO_FUCKIN_HERE_PAL
    assert HTTPStatus(418).phrase == "Ahm a fuckin teapot"


def test_status_codes_are_unique_and_valid():
    codes = [s.value for s in HTTPStatus]
    assert len(codes) == len(set(codes))
    assert all(100 <= c <= 599 for c in codes)


def test_every_status_has_phrase_and_description():
    for status in HTTPStatus:
        assert status.phrase
        assert status.description


def test_category_helpers():
    assert HTTPStatus.AYE_ON_YE_GO.is_informational
    assert HTTPStatus.NAE_BOTHER.is_success
    assert HTTPStatus.WEVE_FLITTED.is_redirection
    assert HTTPStatus.SLOW_DOON.is_client_error
    assert HTTPStatus.THE_COUNCIL_SAYS_NAW.is_server_error
    assert not HTTPStatus.NAE_BOTHER.is_client_error


def test_status_codes_exist_in_the_standard_library():
    """Every code we translate should be a real one, not something we made up."""
    real = {s.value for s in StdStatus}
    unknown = {s.value for s in HTTPStatus} - real
    # 508 and 510 etc. are in the stdlib too; anything left over is worth a look.
    assert not unknown, f"codes not in stdlib http.HTTPStatus: {sorted(unknown)}"


def test_methods_are_strings():
    assert HTTPMethod.GIES == "GET"
    assert HTTPMethod("POST") is HTTPMethod.HAWDES
    assert isinstance(HTTPMethod.AWAWI, str)


def test_methods_match_the_standard_library():
    assert {m.value for m in HTTPMethod} == {m.value for m in StdMethod}


def test_every_method_has_a_description():
    for method in HTTPMethod:
        assert method.description


def test_method_repr():
    assert repr(HTTPMethod.GIES) == "<HTTPMethod.GIES>"


def test_unknown_values_are_rejected():
    with pytest.raises(ValueError):
        HTTPStatus(299)
    with pytest.raises(ValueError):
        HTTPMethod("YEET")


def test_stdlib_import_is_untouched():
    assert http.HTTPStatus.NOT_FOUND == 404


def _all_strings():
    for status in HTTPStatus:
        yield status.phrase
        yield status.description
    for method in HTTPMethod:
        yield method.description


def test_no_curly_quotes():
    for text in _all_strings():
        assert "’" not in text and "‘" not in text, text


def test_space_after_punctuation():
    import re

    for text in _all_strings():
        assert not re.search(r"[?!,;][A-Za-z]", text), text
