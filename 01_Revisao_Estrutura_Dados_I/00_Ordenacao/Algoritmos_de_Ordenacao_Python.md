#include <iostream>
using namespace std;

class Pilha {
private:
    int dados[100];
    int topo;

public:
    Pilha() {
        topo = -1;
    }

    // Adiciona um elemento no topo
    void push(int valor) {
        if (topo >= 99) {
            cout << "Pilha cheia!" << endl;
            return;
        }

        dados[++topo] = valor;
    }

    // Remove o elemento do topo
    void pop() {
        if (topo == -1) {
            cout << "Pilha vazia!" << endl;
            return;
        }

        topo--;
    }

    // Retorna o elemento do topo
    int top() {
        if (topo == -1) {
            cout << "Pilha vazia!" << endl;
            return -1;
        }

        return dados[topo];
    }

    // Verifica se a pilha está vazia
    bool empty() {
        return topo == -1;
    }

    // Mostra os elementos da pilha
    void mostrar() {
        if (empty()) {
            cout << "Pilha vazia!" << endl;
            return;
        }

        cout << "Pilha: ";

        for (int i = topo; i >= 0; i--) {
            cout << dados[i] << " ";
        }

        cout << endl;
    }
};

int main() {
    Pilha pilha;

    pilha.push(10);
    pilha.push(20);
    pilha.push(30);

    pilha.mostrar();

    cout << "Elemento do topo: " << pilha.top() << endl;

    pilha.pop();

    pilha.mostrar();

    return 0;
}
