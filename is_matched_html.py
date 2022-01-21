"""
    Function for testing if an HTML document has matching tags
"""


from ArrayStack import *


def is_matched_html(raw):

    """Return True if all HTML tags are properly match; False otherwise."""

    S = ArrayStack()
    j = raw.find('<')   # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j+1)  # find next character '>'
        if k == -1:
            return False    # invalid tag
        tag = raw[j+1:k]    # strip away <>
        if not tag.startswith('/'):     # this is opening tag
            S.push(tag)
        else:       # this closing tag
            if S.is_empty():
                return False    # nothing to match with
            if tag[1:] != S.pop():
                return False    # mismatched delimiter
        j = raw.find('<', k+1)  # find next '<' character (if any)
    return S.is_empty()     # were all opening tags matched?


html_ = """<body>
<center>
<h1> The Little Boat </h1>
</center>
<p></p>
</body>"""

print(is_matched_html(html_))