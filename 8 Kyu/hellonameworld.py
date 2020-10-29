"""
Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Ex:
hello "john"   => "Hello, John!"
hello "aliCE"  => "Hello, Alice!"
hello          => "Hello, World!" # name not given
hello ''       => "Hello, World!" # name is an empty String


TEST:

test.describe("Example Tests")

tests = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

for inp, exp in tests:
    test.assert_equals(hello(inp), exp)

test.assert_equals(hello(), "Hello, World!")
"""

def hello(name=''):
    return 'Hello,' + f' {name}!'.title() if name else 'Hello, World!'