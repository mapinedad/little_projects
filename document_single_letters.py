document = """Strings are very important in Python. We introduced their use in Chapter 1, with
a discussion of various operator syntax's in Section 1.3. A comprehensive summary
of the named methods of the class is given in Tables A.1 through A.4 of
Appendix A. We will not formally analyze the efficiency of each of those behaviors
in this section, but we do wish to comment on some notable issues. In general,
we let n denote the length of a string. For operations that rely on a second string as
a pattern, we let m denote the length of that pattern string.
The analysis for many behaviors is quite intuitive. For example, methods that
produce a new string (e.g., capitalize, center, strip) require time that is linear in
the length of the string that is produced. Many of the behaviors that test Boolean
conditions of a string (e.g., islower) take O(n) time, examining all n characters in the
worst case, but short circuiting as soon as the answer becomes evident (e.g., islower
can immediately return False if the first character is uppercased). The comparison
operators (e.g., ==, <) fall into this category as well.
Some of the most interesting behaviors, from an algorithmic point of view, are those
that in some way depend upon finding a string pattern within a larger string; this
goal is at the heart of methods such as contains , find, index, count, replace,
and split. String algorithms will be the topic of Chapter 13, and this particular
problem known as pattern matching will be the focus of Section 13.2. A naive implementation
runs in O(mn) time case, because we consider the n−m+1 possible
starting indices for the pattern, and we spend O(m) time at each starting position,
checking if the pattern matches. However, in Section 13.2, we will develop an algorithm
for finding a pattern of length m within a longer string of length n in O(n)
time."""


def new_string_from_document(large_string: str) -> str:

    letters = ''.join((letter for letter in large_string if letter.isalpha()))
    return letters

if __name__ == '__main__':
	print(new_string_from_document(document))
