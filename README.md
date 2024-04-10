# Apresentação Comitê dia 15/04

## Requisitos funcionais:
- IDE (Visual Studio Code ou PyCharm)
- Python (compatível com todas as versões a partir da 3.11.3)
- Pytest 8.1.1

## Requisitos não funcionais:
- Lógica de programação
- Expresões Regulares
- Testes

#### Para funcionar a aplicação localmente é necessário:
-  Clone o repositório:

   ```
   git clone [https://github.com/GuilhermeMLeal/MecatronicFan.git](https://github.com/GuilhermeMLeal/Comite_Repository.git)
    ```
- Para entrar na pasta do arquivo:

    ```
    cd Comite_Repository
    ```

-   **Crie um ambiente virtual:**

    ```
    python -m venv .env 
    ```

- Utilize o seguinte comando:

    ```
    .env\Scripts\activate
    ```

-  Logo Após, utilize:

    ```
    pip install -r requirements.txt
    ```

- Para execução da aplicação, ainda no terminal da IDE entre na pasta :
  ```
    cd app
  ```
- E execute a aplicação com :
  ```
    python PersonEntity.py / python3 PersonEntity.py
  ```
- E para execução dos testes é necessário:
   ```
    pytest tests/PersonTest.py
  ```

## O que é RegEx (Regular Expression)?

Regex, ou expressões regulares, são padrões utilizados para identificar combinações de caracteres em textos. Elas são amplamente utilizadas em diversas áreas da computação, como processamento de texto, validação de dados, busca e substituição de padrões, entre outros.

### Como podemos utilizar ele no dia a dia?

- **Validação de dados**
    - **Validação de formulários**
        - Telefone
        - E-mail
        - Datas
        - CPFs
        - CNPJs
- **Busca e substituição de texto**
- **Extração de informações**
- **Manipulação de strings**



### Sites de conceitos :

https://github.com/EuCarlos/RegEx

https://github.com/odeassis/regex

### Site para testes e estudos para expressões regulares :

https://regex101.com/

### Github com expressões regulares do Brasil:

https://github.com/osintbrazuca/osint-brazuca-regex?tab=readme-ov-file

https://guilhermesteves.dev/tutoriais/regex-uteis-para-o-seu-dia-a-dia/


## O que são testes?

Testes de software são uma prática fundamental no desenvolvimento de software, que envolve a verificação e validação de um sistema para garantir que ele atenda aos requisitos especificados e funcione corretamente. Essa prática é realizada através da execução de programas ou scripts específicos que verificam diversas partes do software, desde pequenas unidades de código até o sistema como um todo.

### Como podemos utilizar ele no dia a dia?

- **Desenvolvimento de novas funcionalidades**
- **Refatoração de código**
- **Integração contínua**
- **Revisão de código**
- **Testes manuais**

## Tipo de teste utilizado no projeto:

- **Testes unitários:** São utilizados para testar unidades individuais de código, como funções ou métodos. O objetivo é verificar se cada unidade funciona corretamente de forma isolada.

## Padrões estabelecidos para criação de testes

- Para nomear uma classe é necessário a utilização do prefixo “Test”, por exemplo “TestCalculator”
- Para nomear funções:
    - Use nomes descritivos que indique qual ação está sendo, exemplo : adição, instanciação e etc
    - Prefixo : “test_”
- Para tornar o seu teste uma forma mais clara e descritiva utilize o padrão GIVEN-WHEN-THEN
    - **Given:** Nomeie a função que configura o estado inicial do teste.
    - **When:** Nomeie a função que descreve a ação que está sendo testada.
    - **Then:** Nomeie a função que verifica o resultado da ação.
- Utilizar nomes descritivos para as variáveis e não utilizar nomes genéricos.

  

```
# Classe para operações básicas de matemática
class Calculator:
    # Função de soma básica
    def add(self, valor1, valor2):
        try:
            resultado = valor1 + valor2
        except TypeError:
            return "Dados inválidos para soma"
        return resultado

    # Função de subtração básica
    def subtract(self, valor1, valor2):
        try:
            resultado = valor1 - valor2
        except TypeError:
            return "Dados inválidos para subtração"
        return resultado
```
```
import pytest
from calculator import Calculator

# Nome da classe para testes na Calculator class com o prefixo "Test"
class TestCalculator:
    # Teste para a função de adição, com prefixo "test_" 
    def test_if_is_adding_correctly(self):
        # Given
        calculator = Calculator()
        # When
        result = calculator.add(2, 3)
        # Then
        assert result == 5

    # Teste para a função de subtração
    def test_if_is_subtracting_correctly(self):
        # Given
        calculator = Calculator()
        # When
        result = calculator.subtract(5, 3)
        # Then
        assert result == 2
```
