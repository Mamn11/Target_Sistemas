#include <stdio.h>

int main()
{
    // Valores de faturamento por estado
    float sp = 67836.43;
    float rj = 36678.66;
    float mg = 29229.88;
    float es = 27165.48;
    float outros = 19849.53;
 
    // Calculando o total
    float total = sp + rj + mg + es + outros;
 
    // Calculando o percentual de cada estado
    float percentual_sp = (sp / total) * 100;
    float percentual_rj = (rj / total) * 100;
    float percentual_mg = (mg / total) * 100;
    float percentual_es = (es / total) * 100;
    float percentual_outros = (outros / total) * 100;
 
    // Imprimindo os resultados
    printf("Percentual de representação por estado:\n");
    printf("SP: %.2f%%\n", percentual_sp);
    printf("RJ: %.2f%%\n", percentual_rj);
    printf("MG: %.2f%%\n", percentual_mg);
    printf("ES: %.2f%%\n", percentual_es);
    printf("Outros: %.2f%%\n", percentual_outros);
 
    return 0;
}