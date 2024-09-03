#include <stdio.h>
#include <stdbool.h>

int fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

bool Validador(int num) {
    int i = 0;
    int fib;

    while ((fib = fibonacci(i)) <= num) {
        if (fib == num) {
            return true;
        }
        i++;
    }
    
    return false;
}

int main() {
    int numero;

    printf("Informe um número para verificar se ele pertence à sequência de Fibonacci: ");
    scanf("%d", &numero);

    if (Validador(numero)) {
        printf("%d pertence à sequência de Fibonacci.\n", numero);
    } else {
        printf("%d não pertence à sequência de Fibonacci.\n", numero);
    }

    return 0;
}