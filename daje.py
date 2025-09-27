import mpmath
import sys
sys.set_int_max_str_digits(int(10E5))
mpmath.mp.dps = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000

def main(number_start) -> None:
    current_number = number_start
    power_programme: int = 1
    counter: int = 0
    while True:
        if current_number % 2 == 0:
            current_number: int = int(mpmath.floor(mpmath.mp.mpf(current_number) / mpmath.mp.power(2, power_programme)))
            counter += 1
        else:
            current_number: int = int(mpmath.mp.power(3, power_programme) * current_number + 1)
            counter += 1
        if current_number == 1 or current_number == 0:
            break
    print(f"result -> {power_programme, counter+1}")

if __name__ == '__main__':
    main(1)
