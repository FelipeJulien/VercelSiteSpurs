#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

double calcularNotaSemestre(double prova, double trabalho) {
    return prova + trabalho;
}

double calcularResultadoFinal(double semestre1, double semestre2) {
    return semestre1 + (semestre2 * 2);
}

string verificarSituacao(double resultado) {
    if (resultado >= 21.0) {
        return "APROVADO";
    } else {
        return "REPROVADO";
    }
}

int main() {
    string nomeAluno;
    double prova, trabalho;
    double nota1, nota2;
    double resultadoFinal;

    
    cout << "     SISTEMA DE CALCULO DE NOTAS        " << endl;
    

    cout << "Digite o nome do aluno: ";
    getline(cin, nomeAluno);

    
    cout << "\n--- 1 SEMESTRE ---" << endl;

    do {
        cout << "  Nota da prova (0 a 7): ";
        cin >> prova;
        if (prova < 0 || prova > 7)
            cout << "  Valor invalido! Digite entre 0 e 7." << endl;
    } while (prova < 0 || prova > 7);

    do {
        cout << "  Nota do trabalho (0 a 3): ";
        cin >> trabalho;
        if (trabalho < 0 || trabalho > 3)
            cout << "  Valor invalido! Digite entre 0 e 3." << endl;
    } while (trabalho < 0 || trabalho > 3);

    nota1 = calcularNotaSemestre(prova, trabalho);

  
    cout << "\n--- 2 SEMESTRE ---" << endl;

    do {
        cout << "  Nota da prova (0 a 7): ";
        cin >> prova;
        if (prova < 0 || prova > 7)
            cout << "  Valor invalido! Digite entre 0 e 7." << endl;
    } while (prova < 0 || prova > 7);

    do {
        cout << "  Nota do trabalho (0 a 3): ";
        cin >> trabalho;
        if (trabalho < 0 || trabalho > 3)
            cout << "  Valor invalido! Digite entre 0 e 3." << endl;
    } while (trabalho < 0 || trabalho > 3);

    nota2 = calcularNotaSemestre(prova, trabalho);

    resultadoFinal = calcularResultadoFinal(nota1, nota2);
    string situacao = verificarSituacao(resultadoFinal);

    cout << "\n========================================" << endl;
    cout << "  Aluno      : " << nomeAluno << endl;
    cout << "  1 Semestre : " << nota1 << "/10 (peso 1)" << endl;
    cout << "  2 Semestre : " << nota2 << "/10 (peso 2)" << endl;
    cout << "  Resultado  : " << nota1 << " + (" << nota2 << " x 2) = " << resultadoFinal << "/30 = " << fixed << setprecision(2) << resultadoFinal / 3.0 << "/10" << endl;
    cout << "  Situacao   : " << situacao << " (minimo 21)" << endl;
    cout << "========================================" << endl;

    return 0;
}
