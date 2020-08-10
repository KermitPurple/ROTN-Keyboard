import sys
import string
import keyboard

def remap_on_str(s: str, n: int) -> None:
    """
    shift n places in s dataset
    :s: string of characters to shift upon
    :n: number of spaces to shift
    """
    for i in range(len(s)):
        keyboard.remap_key(s[i], s[(i + n) % len(s)])

def remap_to_ROTN(n: int, exit_key: str) -> None:
    """
    remap keyboard to work in ROTN for n
    :n: number of spaces to shift
    :exit_key: key to press to exit
    """
    remap_on_str(string.ascii_lowercase, n)
    remap_on_str(string.ascii_uppercase, n)
    print(exit_key + " to quit")
    keyboard.wait(exit_key)

def main():
    remap_to_ROTN(1 if len(sys.argv) < 2 else sys.argv[1], "shift+esc" if len(sys.argv) < 3 else sys.argv[2]) # if no args 1 is default else the second arg is taken and exit key is third arg

if __name__ == "__main__":
    main()
