# 🪓 Jogo da Forca em Python

### 📝 Descrição
Este é um jogo da forca interativo que roda diretamente no terminal. O diferencial deste projeto é o uso de uma **matriz dinâmica** para renderizar o desenho da forca e do boneco em tempo real conforme o jogador erra as letras.

---

### 🚀 Funcionalidades
* **Renderização por Matriz:** O boneco não é apenas um texto estático, mas sim inserido em coordenadas específicas de uma matriz.
* **Lógica de Acertos:** O jogo mascara a palavra secreta com `*` e revela as letras conforme os acertos.
* **Validação de Input:** Impede que o usuário digite mais de uma letra ou caracteres inválidos.
* **Limpeza de Tela:** Utiliza o módulo `os` para manter o terminal organizado a cada jogada.

---

### 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3
* **Módulos Nativos:** * `os`: Para limpar o console (`cls`).
* `functions` (Módulo personalizado): Contendo as funções `criar_matriz` e `desenhar_matriz`.

---

### 🎮 Como Rodar o Projeto
1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/aureliolima88/Jogo-da-Forca.git
    ```
2.  **Certifique-se de que o arquivo `functions.py` está na mesma pasta que o `main.py`.**

3.  **Execute o jogo:**
    ```bash
    python main.py
    ```

---

### 🧠 Lógica de Erros
O jogo permite até 6 erros antes do "Game Over":
1.  Cabeça (`O`)
2.  Braço Esquerdo (`/`)
3.  Tronco (`|`)
4.  Braço Direito (`\`)
5.  Perna Esquerda (`/`)
6.  Perna Direita (`\`)

---

### 🤝 Autor
Desenvolvido por Aurélio Lima - Sinta-se à vontade para sugerir melhorias!
