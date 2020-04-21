"""

TEST:

quote = "How can mirrors be real if our eyes aren't real"
test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")

"""

def to_jaden_case(string):
    a = string.split()
    b, c = [i[0].title() + i[1:] for i in a], " "
    return c.join(b)


if __name__ == '__main__':
	print(to_jaden_case("How can mirrors be real if our eyes aren't real"))