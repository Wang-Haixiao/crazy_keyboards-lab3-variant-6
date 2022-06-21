# crazy-keyboards - lab 3 - variant 6

Group Member:

- Haixiao Wang 212320012
- Yu Zhang     212320015

## Variant description

- Lambda calculus

and should check the implementation correctly works with None value.

## Project structure

- `lambda_calculus.py` -- implementation of `Lambda` immutable version.

- `lambda_calculus_test.py` -- unit tests for `Lambda`.

## Features

Unit test:

- `test_and`

- `test_or`

- `test_not`

- `test_succ`

- `test_pred`

- `test_plus`

- `test_multiply`

## Visualisation

- True & True = True

  ![](/Img/01.png)

- True & False = False

  ![](/Img/02.png)

- False & False = False

  ![](/Img/03.png)

- True or True = True

  ![](/Img/04.png)

- True or False = True

  ![](/Img/05.png)

- False or False = False

  ![](/Img/06.png)

- not True = False

  ![](/Img/07.png)

- not False = True

  ![](/Img/08.png)

- 2 + 1 = 3

  ![](/Img/09.png)

- 2 - 1  = 1

  ![](/Img/10.png)

- 2 + 3 = 5

  ![](/Img/11.png)

- 2 * 3 = 6

  ![](/Img/12.png)

## Contribution

- Haixiao Wang -- source part and upload the files to github

- Yu Zhang -- test part

## Changelog

- 21.06.2022 - 2
  - Add visualisation to readme
- 19.06.2022 - 1
  - Update README. Add formal sections.
  - Fixed some formatting issues
- 10.06.2022 - 0
  - Initial

## Design notes

- By implementing lambda calculus, we learn a set of formal systems
  developed from mathematical logic, with rules for variable binding
  and substitution, to study how functions are abstractly defined,
  how functions are applied, and recursively. Lambda calculus, by comparison,
  is the most fundamental programming language, consisting of a
  transformation rule (substitution of variables) and a way
  to define functions abstractly.
