# Mediotec - Aulas de Python e Interfaces Gráficas

Bem-vindo ao repositório educativo das aulas de programação do **Mediotec**! 🎓

Este espaço foi criado para centralizar os materiais, exemplos e exercícios práticos das aulas. Nosso foco principal é o aprendizado da linguagem **Python** e a sua aplicação no desenvolvimento de Interfaces Gráficas de Usuário (GUIs), permitindo que os alunos criem seus próprios aplicativos e ferramentas interativas.

---

## Objetivo

O objetivo deste repositório é servir como um guia prático para os estudantes, mostrando como sair da programação "apenas no terminal" para a criação de programas reais com janelas, botões e interações visuais, utilizando diferentes abordagens do ecossistema Python.

---

## Tecnologias e Bibliotecas Abordadas

Durante o curso, exploramos três ferramentas principais para criação de interfaces, cada uma com seu propósito ideal:

*   **[Tkinter](https://docs.python.org/pt-br/3/library/tkinter.html)** 
    *   **O que é:** A biblioteca padrão (nativa) do Python para interfaces gráficas.
    *   **Foco:** Criação de aplicativos Desktop clássicos. Ideal para entender os conceitos de orientação a eventos, widgets, loops de janela e gerenciamento de layout (`pack`, `grid`, `place`).
*   **[ipywidgets](https://ipywidgets.readthedocs.io/en/latest/)** 
    *   **O que é:** Controles interativos em HTML para Jupyter Notebooks e Google Colab.
    *   **Foco:** Criação rápida de formulários, botões e controles deslizantes diretamente no navegador, perfeito para ciência de dados e experimentação em ambientes *headless* (como o Colab).
*   **[Flet](https://flet.dev/)** 
    *   **O que é:** Um framework moderno baseado em Flutter.
    *   **Foco:** Construir aplicativos bonitos, modernos e multiplataforma (Web, Desktop e Mobile) usando apenas Python, sem precisar aprender HTML, CSS ou JavaScript.

---

## Como Usar Este Repositório

### Pré-requisitos
Para executar os códigos locais (Tkinter e Flet), você precisará ter instalado em sua máquina:
1.  [Python 3.x](https://www.python.org/downloads/) (Lembre-se de marcar a opção "Add Python to PATH" durante a instalação).
2.  Um editor de código, recomendamos o [Visual Studio Code (VS Code)](https://code.visualstudio.com/).

### Instalações necessárias
O Tkinter já vem instalado por padrão com o Python. No entanto, para usar o Flet, você precisará instalar a biblioteca através do terminal:

```bash
pip install flet
```

Para rodar os exemplos do **ipywidgets**, recomendamos o uso direto do [Google Colab](https://colab.research.google.com/), onde o ambiente já vem configurado.

---

## 📂 Estrutura do Projeto

*(Sinta-se à vontade para organizar suas pastas desta forma)*

```text
/
├── 01_Logica_Python/       # Exercícios básicos de Python
├── 02_Interface_Tkinter/   # Códigos e projetos usando Tkinter
├── 03_Interface_Colab/     # Notebooks (.ipynb) focados em ipywidgets
└── 04_Interface_Flet/      # Aplicativos modernos utilizando o framework Flet
```

---

## Sobre o Mediotec

O Mediotec é um programa voltado para a formação técnica e profissional de estudantes. Este material é um recurso de apoio para incentivar o raciocínio lógico, a resolução de problemas e a entrada dos jovens no mundo da tecnologia e desenvolvimento de software.
