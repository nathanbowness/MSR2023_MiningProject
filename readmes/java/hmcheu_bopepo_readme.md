# JRimum: BOPEPO
> Fork por Braully Rocha


## Objetivos desse fork

- Unificado das bibliotecas do projeto JRimum (concluído)
- Atualizar dependências: Java 11 e itextpdf5 (concluído)
- Refatorar pacotes reduzindo a quantidade em unidades maiores e coesas (concluído)
- Biblioteca pra gerar boletos, arquivos de remessa e retorno  (concluído)
- Façade para facilitar o uso da biblioteca (concluído)
- Disponiblizar uma versão estável no repositorio maven central (futuro)

#### Suporte a boletos com registro dos principais bancos

- Banco do Brasil
- Bradesco
- Caixa
- Itau
- Santander
- Sicredi

### Suporte para remessa de boletos CNAB 240

- Banco do Brasil
- Bradesco
- Caixa
- Itau
- Santander
- Sicredi

###  Suporte para retorno de boletos CNAB 240

- Banco do Brasil
- Bradesco
- Caixa
- Itau
- Santander
- Sicredi

### Fusão das branches 

- 'master'
- 'helio'
- 'litio' 

### Fusão dos projetos:

- 'bopepo' 
- 'domkee' 
- 'utilix' 
- 'vallia' 
- 'texgit'
- 'texgit-febraban'

### Refatoração dos pacotes e classes
Concentrar todas as classes nos pacotes

- com.github.braully.boleto
- org.jrimum
- org.jrimum.bopepo
- org.jrimum.bopepo.campolivre
- org.jrimum.bopepo.parametro
- org.jrimum.bopepo.pdf
- org.jrimum.bopepo.view
- org.jrimum.bopepo.banco
- org.jrimum.domkee.pessoa
- org.jrimum.domkee.banco
- org.jrimum.utilix
- org.jrimum.valia

## Instalação

$ git clone https://github.com/braully/bopepo.git

$ cd bopepo

$ ./sh/compile.sh

## Exemplo


Criar um boleto simples:
```

    BoletoFacade boletoFacade = new BoletoFacade();
    boletoFacade.sacado("Sacado da Silva Sauro").sacadoCpf("1");
    boletoFacade.banco("1").agencia("1").conta("1");
    boletoFacade.cedente("Cedente da Silva Sauro").cedenteCnpj("1");
    boletoFacade.carteira("1");
    boletoFacade.numeroDocumento("1")
            .nossoNumero("1234567890")
            .valor(100.23).dataVencimento("01/01/2019");

    boletoFacade.gerarLinhaDigitavel();
    BoletoViewer create = BoletoViewer.create(boletoFacade);
    create.getPdfAsFile("./target/teste.pdf");
```


Criar um arquivo de remessa de boleto CNAB 240:
```

    RemessaFacade remessa = new RemessaFacade(LayoutsSuportados.LAYOUT_BB_CNAB240_COBRANCA_REMESSA);
            remessa.addNovoCabecalho()
                    .sequencialArquivo(1)
                    .dataGeracao(new Date()).setVal("horaGeracao", new Date())
                    .banco("0", "Banco").cedente("ACME S.A LTDA.", "1")
                    .convenio("1", "1", "1", "1")
                    .carteira("00");

    remessa.addNovoCabecalhoLote()
            .operacao("R")//Operação de remessa
            .servico(1)//Cobrança
            .forma(1)//Crédito em Conta Corrente
            .banco("0", "Banco")
            .cedente("ACME S.A LTDA.", "1")
            .convenio("1", "1", "1", "1")
            .carteira("00");;

    remessa.addNovoDetalheSegmentoP()
            .valor(1)
            .valorDesconto(0).valorAcrescimo(0)//opcionais
            .dataGeracao(new Date())
            .dataVencimento(new Date())
            .numeroDocumento(1)
            .nossoNumero(1)
            .banco("0", "Banco")
            .cedente("ACME S.A LTDA.", "1")
            .convenio("1", "1", "1", "1")
            .sequencialRegistro(1)
            .carteira("00");

    remessa.addNovoDetalheSegmentoQ()
            .sacado("Fulano de Tal", "0")
            .banco("0", "Banco")
            .cedente("ACME S.A LTDA.", "1")
            .convenio("1", "1", "1", "1")
            .sequencialRegistro(2)
            .carteira("00");;

    remessa.addNovoRodapeLote()
            .quantidadeRegistros(2)
            .valorTotalRegistros(1)
            .banco("0", "Banco")
            .cedente("ACME S.A LTDA.", "1")
            .convenio("1", "1", "1", "1")
            .carteira("00");;

    remessa.addNovoRodape()
            .quantidadeRegistros(1)
            .valorTotalRegistros(1)
            .setVal("codigoRetorno", "1")
            .banco("0", "Banco").cedente("ACME S.A LTDA.", "1")
            .convenio("1", "1", "1", "1")
            .carteira("00");

    String remessaStr = remessa.render();
    System.out.println(remessaStr);
```

Ler um arquivo de retorno de boleto CNAB 240:
```

    RetornoFacade retorno = new RetornoFacade(LayoutsSuportados.LAYOUT_FEBRABAN_CNAB240);

    String[] arrLinhas = BB_EXEMPLO_RETORNO.split("\n");

    List<String> linhas = Arrays.asList(arrLinhas);
    retorno.parse(linhas);

    System.out.println("Detalhes as Titulos: ");

    List<TituloArquivo> titulos = retorno.detalhesAsTitulos();
    for (TituloArquivo titulo : titulos) {
        String segmento = titulo.segmento();
        String numeroDocumento = titulo.numeroDocumento();
        String nossoNumero = titulo.nossoNumero();
        String valorPagamento = titulo.valorPagamento();
        String valorLiquido = titulo.valorLiquido();
        String dataOcorrencia = titulo.dataOcorrencia();
        String movimentoCodigo = titulo.movimentoCodigo();
        String rejeicoes = titulo.rejeicoes();
        String valorTarifaCustas = titulo.valorTarifaCustas();

        System.out.println("Campos: {segmento=" + segmento + " numeroDocumento=" + numeroDocumento);
        System.out.println("\tnossoNumero=" + nossoNumero + " valorPagamento=" + valorPagamento);
        System.out.println("\tvalorLiquido=" + valorLiquido + " dataOcorrencia=" + dataOcorrencia);
        System.out.println("\tmovimentoCodigo=" + movimentoCodigo + " rejeicoes=" + rejeicoes);
        System.out.println("\tvalorTarifaCustas=" + valorTarifaCustas + " rejeicoes=" + valorTarifaCustas + "}");
```