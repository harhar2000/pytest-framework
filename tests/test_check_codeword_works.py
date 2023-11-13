from lib.check_codeword import check_codeword



"""
If codeword is correct
Returns 'Correct! Come in.'
"""

def test_check_codeword_works():
    result = check_codeword("horse")
    assert result == "Correct! Come in."





# def check_codeword(codeword):
    if codeword == "horse":
        return "Correct! Come in."
    elif codeword[0] == "h" and codeword[-1] == "e":
        return "Close, but nope."
    else:
        return "WRONG!"