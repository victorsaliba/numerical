################################################################################
# Authors: Luiz Gustavo Mugnaini Anselmo (nUSP: 11809746)
#          Victor Manuel Saliba (nUSP: )
#          Luan Marc (nUSP: 11809090)
#
# Dekker method for finding roots of a given function.
################################################################################

def dekker(f, a, b):
    # Dekker method
    if f(a) * f(b) >= 0:
        raise Exception('The function must change sign in [a, b]')
    pass

def main():
    pass

if __name__ == "__main__":
    main()
