"""
    This code is very useful for match tags of html document.
"""

from ArrayStack import *


def is_matched_html(raw: str) -> object:
    """Return True if all HTML tags are properly match; False otherwise."""

    S = ArrayStack()
    j = raw.find('<')  # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)  # find next character '>'
        if k == -1:
            return False  # invalid tag
        tag = raw[j + 1:k]  # strip away <>
        if not tag.startswith('/'):  # this is opening tag
            S.push(tag)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            begin_tag = S.pop()
            if tag[1:] != begin_tag[:len(tag[1:])]:  # here's the solution
                return False  # mismatched delimiter
        j = raw.find('<', k + 1)  # find next '<' character (if any)
    return S.is_empty()  # were all opening tags matched?


def remove_DOCTYPE(html_str: str) -> str:
    return html_str.replace("<!DOCTYPE html>\n", "")


if __name__ == '__main__':
    
    html_ = """<!DOCTYPE html>
    <html>
    <head>
    	<title> Example </title>
    </head>
    <body>
        <table border="3" cellpadding="5"></table>
    	<h1>
    		<a href="/"> Header </a>
    	</h1>
    	<ul id="nav">
    		<li>
    			<a href="one/"> one </a>
    		</li>
    		<li>
    			<a href="two/"> two </a>
    		</li>
    	</ul>
    </body>
    </html>"""

    print(is_matched_html(remove_DOCTYPE(html_)))
