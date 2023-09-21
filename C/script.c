#include <stdio.h>

int main (int argc, char *argv[]) {
    int contador;

    if (argc > 1) {
        for (contador = 0; contador <= 254; contador++) {
            printf("Atacando o IP: %s.%i\n", argv[1], contador);
        }
    } else {
        printf("./script x.x.x");
    }

    return 0;
}
