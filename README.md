# String Calculator TDD Kata Solution
This repository contains my solution to the String Calculator Test-Driven Development (TDD) Kata, as part of the assessment process for the Software Craftsperson role at Incubyte.

## Overview
The String Calculator Kata is a programming exercise aimed at practicing TDD principles. The goal is to develop a simple string calculator that can add numbers provided as strings. The solution adheres to the principles of TDD, ensuring that the code is clean, testable, and well-refactored.

## Technologies Used
  * Programming Language: Python
  
  * Testing Framework: unittest

## Solution Components
  `StringCalculator` Class 
  
  * This class implements the core functionality of the string calculator. It contains a static method add which performs the addition of numbers represented as strings.
 
    `add(numbers: string): int` 

    * Parameters: A string containing the numbers to be added. The numbers can be separated by commas or new lines. A custom delimiter can be specified at the beginning of the string.

    * Returns: An integer representing the sum of the numbers.

      The method supports:

      * An empty string input, returning 0.
   
      * Custom delimiters specified in the format `//[delimiter]\n[numbers…]`.

   `TestStringCalculator` Class: 
   
   * This class contains unit tests for the StringCalculator class, ensuring that all functionalities adhere to the specified requirements.

     Test Methods: 
   
      * `test_empty_string_returns_zero()` : Verifies that an empty string input returns 0.

      * `test_single_number_returns_value()` : Checks that a single number returns its own value as the sum.
    
      * `test_two_numbers_comma_delimited_returns_sum()` : Ensures that two numbers separated by a comma return their sum.
    
      * `test_handle_new_lines_as_delimiters()` : Tests that new lines can be used as delimiters.
    
      * `test_support_different_delimiters()` : Verifies that custom delimiters are supported.
    
      * `test_negative_numbers_throw_exception()` : Checks that an exception is thrown when negative numbers are present.

    

   
