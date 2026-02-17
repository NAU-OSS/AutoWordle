# Python Wordle Solver - AutoWordle

This is an open-source Python project that solves the Wordle from the New York Times and is open to outside contributions. The program is run from the command line and provides word suggestions based on the parameters the user inputs. Currently, the user can input letters that are in the correct place, letters in the word but not in the correct spot, and letters not in the word at all. The word bank consists of 5758 different words for the program to filter from. 

## Getting Started

In order to get started with this project, clone the repository and follow the guidelines below.

### Prerequisites

Make sure you have Python downloaded on your local machine. You can verify that you have Python by running this on your command line:

```
python --version
```

If you got a Python verison return ex. `Python 3.14.2`, then you are good to go!

### Installing/Running

Enter the following command to run the program. Note: you must be in the same directory as `wordleSolver.py`

```
python wordleSolver.py
```

Enter letters in place. If you want to insert "m" in the second position, you would write the following:

```
m,1
```

Enter letters out of place. If you want to insert "t", write the following:

```
t
```

Enter letters not in the word. If you want to insert "q", write the following:

```
q
```

The program will display the remaining characters that match all of the conditions listed above. You will repeat this as many times as needed to solve the Wordle.

## Running the tests

There are currently no tests implemented in this project.

## Built With

* [Python](https://www.python.org/) - The programming language used

## Contributing

Please read [CONTRIBUTING.md](https://github.com/NAU-OSS/WordleSolver/blob/main/CONTRIBUTING.md) for details on the process for submitting pull requests to us and participating in the project.

## Code of Conduct

Please read [CODE_OF_CONDUCT.md](https://github.com/NAU-OSS/AutoWordle/blob/main/CODE_OF_CONDUCT.md) for details on community guidelines and ground rules for behavior.

## Authors

* **Aiden Seay** - *Initial work* - [aidengseay](https://github.com/aidengseay)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
