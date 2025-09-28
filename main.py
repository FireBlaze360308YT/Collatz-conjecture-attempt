#Imports
import csv
import mpmath

#Float precision
mpmath.mp.dps = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000

#Collatz Function
def function1(number_start: int = 1, power_programme: int = 1) -> None:

    with open("result_int_division.csv", "a", newline="") as csvfile:
        while True:
            counter: int = 0
            current_number: int = number_start
            while True:
                if current_number % 2 == 0:
                    current_number: int = int(mpmath.floor(mpmath.mp.mpf(current_number) / mpmath.mp.power(2, power_programme)))

                else:
                    current_number: int = mpmath.mp.power(3, power_programme) * current_number + 1

                counter += 1

                if current_number == 1 or current_number == 0:
                    break

            writer = csv.DictWriter(csvfile, fieldnames=["power", "steps"])
            writer.writerows([{"power": power_programme, "steps": counter+1}])

            power_programme += 1

#Main Function
def main() -> None:
    function1(1, 1)

#Start
if __name__ == '__main__':
    main()
