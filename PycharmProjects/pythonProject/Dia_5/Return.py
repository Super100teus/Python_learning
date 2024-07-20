def multiplicar(num1, num2):
    return num1 * num2


res = multiplicar(5, 67.91)
print(res)
def invertir_palabra(pal):
    j=''
    for i in pal:
        j = i + j
    return j

palabra = 'Setir'
print(invertir_palabra(palabra))
