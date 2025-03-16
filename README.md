Você está certo! No caso deste projeto, estamos utilizando o **Amazon Comprehend** para realizar a análise de sentimentos, e não um modelo personalizado de machine learning. O **Amazon Comprehend** é um serviço da AWS especializado em processamento de linguagem natural (NLP) e oferece uma API para detectar sentimentos, entidades, categorias e outras análises linguísticas de textos.

Vamos corrigir a documentação e atualizar o foco para **Amazon Comprehend**.

---

# Análise de Sentimentos - Frontend com Integração AWS (Amazon Comprehend)

## Descrição

Este projeto realiza a análise de sentimentos de um texto fornecido pelo usuário, utilizando a **API Amazon Comprehend** da AWS para realizar o processamento do texto. O frontend é simples, construído com HTML, CSS e JavaScript, enquanto a análise de sentimentos é realizada por uma **função AWS Lambda** que faz a chamada para o serviço Amazon Comprehend.

### Funcionalidades

- **Análise de Sentimentos**: O usuário insere um texto e a aplicação envia esse texto para uma **função Lambda** que faz uma requisição para o **Amazon Comprehend**.
- **Exibição de Resultados**: A aplicação exibe o sentimento identificado (positivo, negativo, neutro ou misto) junto com a confiança associada a cada tipo de sentimento.
- **Interface Simples e Intuitiva**: Interface limpa e amigável ao usuário, com foco na usabilidade.

---

## Como Funciona

### Fluxo de Trabalho

1. **Entrada de Texto**: O usuário digita um texto na caixa de entrada e pressiona o botão "Analisar".
2. **Chamada para a API AWS**: O texto é enviado para uma **função AWS Lambda** através de uma API RESTful (gerenciada pelo **API Gateway**).
3. **Análise de Sentimentos com Amazon Comprehend**: A função Lambda usa o **Amazon Comprehend** para processar o texto e retornar o sentimento (positivo, negativo, neutro ou misto) e as respectivas porcentagens de confiança.
4. **Exibição de Resultados**: O resultado é processado no frontend e exibido na interface de usuário.

---

## Tecnologias Utilizadas

### Frontend
- **HTML5**: Estrutura da página e componentes de entrada e saída.
- **CSS3**: Design responsivo com uso de **Flexbox** e animações simples para melhorar a experiência visual.
- **JavaScript**: Lógica para enviar solicitações HTTP para a API da AWS e manipular os resultados.

### Backend
- **AWS Lambda**: Função sem servidor que processa o texto enviado e invoca o serviço **Amazon Comprehend** para realizar a análise de sentimentos.
- **API Gateway**: Expõe a função Lambda através de uma API RESTful, permitindo que o frontend envie solicitações HTTP para processar o texto.
- **IAM**: Permissões configuradas para garantir que a função Lambda tenha acesso ao **Amazon Comprehend**.
- **CloudWatch**: Usado para monitorar e registrar as atividades da Lambda, permitindo que você visualize logs e métricas de desempenho.

---

## Arquitetura AWS

1. **Frontend**: O frontend é hospedado em qualquer servidor web ou até mesmo em um bucket do **Amazon S3** configurado para servir conteúdo estático.
   
2. **API Gateway**: Configurado para expor um endpoint RESTful que permite ao frontend enviar solicitações para a Lambda.

3. **AWS Lambda**: Processa o texto enviado via API Gateway e chama o serviço **Amazon Comprehend** para determinar o sentimento do texto.
   
4. **Amazon Comprehend**: Serviço da AWS que realiza a análise de sentimentos do texto, retornando o tipo de sentimento e as respectivas porcentagens de confiança para cada categoria (positivo, negativo, neutro, misto).

5. **IAM Roles e Permissões**: A Lambda precisa de permissões adequadas para interagir com o **Amazon Comprehend** e realizar a análise de sentimentos.

6. **CloudWatch Logs**: A Lambda grava logs detalhados no CloudWatch, o que facilita o monitoramento da execução da função e depuração em caso de falhas.

---

## Como Usar

### Pré-requisitos
Antes de usar este projeto, é necessário ter uma **AWS Account** com permissões para usar os seguintes serviços:

- **AWS Lambda**: Para processar o texto e invocar o Amazon Comprehend.
- **API Gateway**: Para expor a função Lambda via API RESTful.
- **IAM**: Para configurar as permissões adequadas à função Lambda para usar o Amazon Comprehend.
- **Amazon Comprehend**: Serviço utilizado para análise de sentimentos.
- **CloudWatch**: Para monitorar logs e métricas.

### Passos para Implementação da AWS

1. **Criar a Função Lambda**
   - No Console da AWS, crie uma nova função Lambda.
   - Implemente a função que irá invocar o serviço **Amazon Comprehend** para realizar a análise de sentimentos.
   - Certifique-se de que a função tenha a permissão correta para invocar o Amazon Comprehend (via **IAM role**).

2. **Configurar o API Gateway**
   - Crie uma nova API RESTful no **API Gateway**.
   - Configure o endpoint para invocar a função Lambda que fará a análise de sentimentos.
   - Teste o endpoint para garantir que o texto seja processado corretamente.

3. **Configurar IAM**
   - Crie um papel (role) do IAM com permissões para a função Lambda acessar o **Amazon Comprehend**.
   - A função Lambda precisa da permissão `comprehend:DetectSentiment`.

4. **Monitoramento com CloudWatch**
   - Habilite o **CloudWatch** para registrar os logs da execução da função Lambda.
   - Configure alarmes no CloudWatch para alertá-lo sobre erros ou falhas no processamento.

5. **Deploy do Frontend**
   - Hospede os arquivos do frontend (HTML, CSS e JavaScript) no seu servidor ou no **Amazon S3**.
   - Conecte o frontend ao endpoint do API Gateway.

6. **Testar a Aplicação**
   - Após a configuração da AWS e o deploy do frontend, abra o arquivo `index.html` em seu navegador.
   - Insira um texto e clique em "Analisar". O resultado da análise será exibido após a interação com o **Amazon Comprehend**.

---

## Monitoramento e Logs

### AWS CloudWatch
A função Lambda grava logs detalhados no **CloudWatch**, onde você pode monitorar o comportamento da função e depurar problemas de execução. Utilize os logs do CloudWatch para verificar se a função está processando as solicitações corretamente.

---

## Possíveis Melhorias e Expansões

- **Segurança**: Adicionar autenticação à API para garantir que apenas usuários autorizados possam acessar o serviço de análise de sentimentos.
- **Escalabilidade**: Integrar com outros serviços AWS, como o **SQS** ou **SNS**, para melhorar a escalabilidade e gerenciamento de filas de requisições.
- **Análise Multilíngue**: O **Amazon Comprehend** oferece suporte a vários idiomas. Expanda a aplicação para aceitar textos em outros idiomas, utilizando a funcionalidade multilingue do Comprehend.

--
