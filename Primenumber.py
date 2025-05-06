class PrimeChecker:
    """
    This class provides a method to check if a given number is prime.
    """

    def is_prime(self, number):
        """
        Checks if a given number is prime.

        Args:
            number: The integer to check for primality.

        Returns:
            True if the number is prime, False otherwise.
        """
        if not isinstance(number, int):
            return "Invalid input: Please enter an integer."  # Input validation
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0 or number % 3 == 0:
            return False
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                return False
            i += 6
        return True

if __name__ == "__main__":
    """
    Main execution block:
    1. Gets a number from the user.
    2. Instantiates the PrimeChecker class.
    3. Calls the is_prime method to check the number.
    4. Prints the result.
    """
    try:
        num = int(input("Enter a number to check if it's prime: "))
        checker = PrimeChecker()  # Instantiate the class
        result = checker.is_prime(num)
        if isinstance(result, str): #check if the result is an error message
            print(result)
        elif result:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input: Please enter an integer.")
