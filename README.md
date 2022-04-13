# Sample Programs Template

Since early 2018, I've been managing a repository called Sample Programs.
The goal of that project was to create a repository containing as many 
code snippets in as many programming languages as possible. As the repo
grew, we added many features to it including automated testing, README
generation, and wiki generation. All of that comes together now in a
template where you can implement solutions in whatever programming 
languages you like. Feel free to use this template to track your learning
or demonstrate your knowledge. It may well serve as a solid portfolio
for you someday. If you have any questions about how to use this 
template, check out the contributing document in the 
[Sample Programs](https://github.com/TheRenegadeCoder/sample-programs) repo. 
With that said, let's talk about what this template supports.

## Programming Languages

Unlike the Sample Programs repo, the Sample Programs template repo only
supports languages with an official Docker image for testing. As a result,
here is the official list of supported programming languages:

| Language | Documentation                                                     | Image                                       | Naming Convention |
| -------- | ----------------------------------------------------------------- | ------------------------------------------- | ----------------- |
| C        | [Documentation](https://sampleprograms.io/languages/c/)           | [gcc](https://hub.docker.com/_/gcc)         | hyphen            |
| C ++     | [Documentation](https://sampleprograms.io/languages/c-plus-plus/) | [gcc](https://hub.docker.com/_/gcc)         | hyphen            |
| Go       |                                                                   | [golang](https://hub.docker.com/_/golang)   | hyphen            |
| Java     | [Documentation](https://sampleprograms.io/languages/java/)        | [openjdk](https://hub.docker.com/_/openjdk) | pascal            |
| Python   | [Documentation](https://sampleprograms.io/languages/python/)      | [python](https://hub.docker.com/_/python)   | underscore        |
| Ruby     | [Documentation](https://sampleprograms.io/languages/ruby/)        | [ruby](https://hub.docker.com/_/ruby)       | hyphen            |

In the table above, you might have noticed the naming convention column.
The terms in that column indicate the expected naming convention of the code 
files for the associated language. For example, files in Java are expected 
to be named in pascal case (e.g., HelloWorld.java). Below you'll find a list
of all the possible naming conventions with examples:

- hyphen (default): hello-world.lang
- pascal: HelloWorld.lang
- underscore: hello_world.lang

See the default naming convention column in the projects table below for
the proper naming convention for each project. 

## Projects

Like the Sample Programs repo, the Sample Programs template repo only
supports projects that have documentation and testing. As a result, 
here is the official list of supported projects:

| Project                       | Requirements                                                           | Default Naming Convention |
| ----------------------------- | ---------------------------------------------------------------------- | ------------------------- |
| Baklava                       | [Requirements](https://sampleprograms.io/projects/baklava/)            | baklava                   |
| Binary Search                 | [Requirements](https://sampleprograms.io/projects/binary-search/)      | binary-search             |
| Bubble Sort                   | [Requirements](https://sampleprograms.io/projects/bubble-sort/)        | bubble-sort               |
| Capitalize                    | [Requirements](https://sampleprograms.io/projects/capitalize/)         | capitalize                |
| Convex Hull                   | [Requirements](https://sampleprograms.io/projects/convex-hull/)        | convex-hull               |
| Even/Odd                      | [Requirements](https://sampleprograms.io/projects/even-odd/)           | even-odd                  |
| Factorial                     | [Requirements](https://sampleprograms.io/projects/factorial/)          | factorial                 |
| Fibonacci                     | [Requirements](https://sampleprograms.io/projects/fibonacci/)          | fibonacci                 |
| File IO                       | [Requirements](https://sampleprograms.io/projects/file-io/)            | file-io                   |
| Fizz Buzz                     | [Requirements](https://sampleprograms.io/projects/fizz-buzz/)          | fizz-buzz                 |
| Hello World                   | [Requirements](https://sampleprograms.io/projects/hello-world/)        | hello-world               |
| Insertion Sort                | [Requirements](https://sampleprograms.io/projects/insertion-sort/)     | insertion-sort            |
| Job Sequencing                | [Requirements](https://sampleprograms.io/projects/job-sequencing/)     | job-sequencing            |
| Longest Common Subsequence    | [Requirements](https://sampleprograms.io/projects/lcs/)                | lcs                       |
| Longest Palindromic Substring | [Requirements](https://sampleprograms.io/projects/lps/)                | lps                       |
| Linear Search                 | [Requirements](https://sampleprograms.io/projects/linear-search/)      | linear-search             |
| Merge Sort                    | [Requirements](https://sampleprograms.io/projects/merge-sort/)         | merge-sort                |
| Minimum Spanning Tree         | [Requirements](https://sampleprograms.io/projects/mst/)                | mst                       |
| Palindromic Numbers           | [Requirements](https://sampleprograms.io/projects/palindromic-number/) | palindromic-number        |
| Prime Numbers                 | [Requirements](https://sampleprograms.io/projects/prime-number/)       | prime-number              |
| Quine                         | [Requirements](https://sampleprograms.io/projects/quine/)              | quine                     |
| ROT-13                        | [Requirements](https://sampleprograms.io/projects/rot-13/)             | rot-13                    |
| Reverse a String              | [Requirements](https://sampleprograms.io/projects/reverse-string/)     | reverse-string            |
| Roman Numeral Conversion      | [Requirements](https://sampleprograms.io/projects/roman-numeral/)      | roman-numeral             |
| Selection Sort                | [Requirements](https://sampleprograms.io/projects/selection-sort/)     | selection-sort            |
| Sleep Sort                    | [Requirements](https://sampleprograms.io/projects/sleep-sort/)         | sleep-sort                |

As always, if you're interested in how this projects are tested, check
out [the official documentation](https://sampleprograms.io/projects/). 
