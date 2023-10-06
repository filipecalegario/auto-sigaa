# Automação de Lançamento de Notas no SIGAA

Este script Python utiliza a biblioteca Selenium para automatizar o processo de lançamento de notas no sistema SIGAA da UFPE. Ele utiliza a biblioteca pandas para ler os nomes dos estudantes e suas respectivas notas de um arquivo Excel (`template.xlsx`) e, em seguida, preenche automaticamente as notas no SIGAA.

## Requisitos

Assegure-se de ter as seguintes bibliotecas instaladas em seu ambiente:

- `pandas>=1.5.1`
- `selenium>=4.13.0`
- `openpyxl>=3.1.2`

Você pode instalar as bibliotecas necessárias com:

```
pip install pandas selenium openpyxl
```

Ou pode rodar o seguinte comando:

```
pip install -r requirements.txt
```

Além disso, este script utiliza o WebDriver do Chrome. Certifique-se de ter o [ChromeDriver](https://sites.google.com/chromium.org/driver/) instalado e no seu PATH.

## Como usar

1. Prepare um arquivo Excel chamado `template.xlsx` com, pelo menos, duas colunas: `NOME` (com os nomes dos estudantes) e `NOTA` (com a nota do estudante).

2. Execute o script:

```
python auto_sigaa.py
```

3. O navegador Chrome será aberto e você será direcionado para a página de login do SIGAA.

4. Faça o login e navegue manualmente até a página de lançamento de notas.

5. Quando estiver na página de lançamento de notas, volte para o terminal/script e pressione Enter.

6. O script agora tentará preencher automaticamente as notas dos estudantes.

7. Após o preenchimento, verifique se as notas foram lançadas corretamente.

**Nota Importante:** Este script NÃO salva as notas automaticamente. Certifique-se de pressionar o botão "SALVAR" no SIGAA após verificar as notas.

## Considerações

- O script assume que o input de notas no SIGAA já adiciona a vírgula automaticamente. Portanto, ele multiplica a nota por 10 ao enviar o valor.
- Em caso de erros ao tentar localizar um estudante na página, o script imprimirá uma mensagem de erro e continuará tentando os próximos estudantes.
- Certifique-se que os nomes dos estudantes estejam exatamente como estão escritos no SIGAA, pois a busca é realizada pela string exata.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou adicionar novos recursos. Abra um pull request ou uma issue!

⚠️ **Aviso Importante** ⚠️

Este é um script **NÃO OFICIAL** para automatização de lançamento de notas no SIGAA. Ele é uma **versão ALPHA** e foi desenvolvido com o objetivo de agilizar o processo e reduzir potenciais erros advindos de preenchimento manual, oferecendo uma alternativa automática.

No entanto, o uso deste script é de **inteira responsabilidade do usuário**. Os desenvolvedores ou contribuintes deste projeto não se responsabilizam por quaisquer problemas, imprecisões, perdas de dados ou outras questões que possam surgir durante ou após o uso.

Recomendamos fortemente que, após o uso do script, **todas as entradas sejam revisadas manualmente** para garantir a acurácia e a integridade dos dados lançados.

Use com cautela e sempre verifique o resultado final.