import pytest

from runner import ProjectType
from glotter import project_test, project_fixture


expected_raw = """1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz
Fizz
52
53
Fizz
Buzz
56
Fizz
58
59
FizzBuzz
61
62
Fizz
64
Buzz
Fizz
67
68
Fizz
Buzz
71
Fizz
73
74
FizzBuzz
76
77
Fizz
79
Buzz
Fizz
82
83
Fizz
Buzz
86
Fizz
88
89
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
"""


@project_fixture(ProjectType.FizzBuzz.key)
def fizz_buzz(request):
    request.param.build()
    yield request.param
    request.param.cleanup()


@project_test(ProjectType.FizzBuzz.key)
def test_fizz_buzz(fizz_buzz):
    actual = trim_whitespace(fizz_buzz.run())
    expected = trim_whitespace(expected_raw)

    assert actual == expected


@project_test(ProjectType.FizzBuzz.key)
def test_fizz_buzz_line_count(fizz_buzz):
    expected_count = len(expected_raw.split('\n'))
    actual_count = len(fizz_buzz.run().split('\n'))
    assert actual_count == expected_count


def trim_whitespace(val):
    return ''.join([v.strip() for v in val.split('\n')])
