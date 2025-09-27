import mpmath
import sys
sys.set_int_max_str_digits(int(10E5))
mpmath.mp.dps = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000

def main(number_start) -> None:
    power_programme: int = 1
    counter: int = 0
    while True:
        if number_start % 2 == 0:
            number_start: int = int(mpmath.floor(mpmath.mp.mpf(number_start) / mpmath.mp.power(2, power_programme)))
            counter += 1
        else:
            number_start: int = int(mpmath.mp.power(3, power_programme) * number_start + 1)
            counter += 1
        if number_start == 1 or number_start == 0:
            break
    print(f"result -> {power_programme, counter+1}")

if __name__ == '__main__':
    main(1)
