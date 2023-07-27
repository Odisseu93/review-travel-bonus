# Review Travel Bonus


[clique aqui para ír para a versão em português!](#portuguese_version)


### Purpose
The Review Travel Bonus project is a Python application designed to process sales data stored in CSV files and identify sellers who have achieved sales above a certain threshold. When a seller's sales exceed 55,000, the application sends an SMS notification to notify the seller about their bonus achievement.

### Inspiration
The project was inspired by a YouTube video that served as the basis for its construction. You can find the video [here](https://www.youtube.com/watch?v=GQpQha2Mfpg).

### Dependencies
Before running the project locally, make sure you have the following dependencies installed:
- pandas
- openpyxl
- twilio

### How to Run Locally
To run the project locally, follow the steps below:

1. Create a Twilio account: Before testing the project, you will need to create a Twilio account if you don't have one already. You can sign up for a free trial account at [Twilio's website](https://www.twilio.com).

2. Set up environment variables: To protect sensitive information like your Twilio account credentials and phone numbers, the project uses environment variables. Create a `.env` file in the project's root directory and add the following variables:

```
ACCOUNT_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
TWILLIO_NUMBER=your_twilio_phone_number
PHONE_NUMBER=your_phone_number_to_receive_sms
```

Replace `your_twilio_account_sid`, `your_twilio_auth_token`, `your_twilio_phone_number`, and `your_phone_number_to_receive_sms` with your Twilio account SID, authentication token, Twilio phone number, and your phone number where you want to receive the SMS notifications.

3. Install dependencies: Install the required dependencies by running the following command in your terminal or command prompt:

```
pip install pandas openpyxl twilio
```

4. Prepare the sales data: The application expects sales data in CSV files stored in the `./sales/` directory. Make sure you have CSV files for each month with the columns `seller` and `sales` containing the seller's name and sales amount, respectively.

5. Run the application: After setting up the environment variables and preparing the sales data, execute the Python script to run the application:

```
python main.py
```

The script will read the sales data from the CSV files, identify sellers with sales exceeding 55,000, and send SMS notifications to notify the sellers about their bonus achievements.

### License
This project is licensed under the MIT License. You can find the full license text in the [LICENSE](LICENSE.md) file.



## <a id="portuguese_version"></a> Português

### Propósito
O projeto Review Travel Bonus é uma aplicação em Python desenvolvida para processar dados de vendas armazenados em arquivos CSV e identificar vendedores que alcançaram um determinado valor de vendas. Quando as vendas de um vendedor ultrapassam 55.000, a aplicação envia uma notificação por SMS para informar ao vendedor sobre a conquista do bônus.

### Inspiração
O projeto foi inspirado em um vídeo do YouTube que serviu como base para sua construção. Você pode encontrar o vídeo [aqui](https://www.youtube.com/watch?v=GQpQha2Mfpg).

### Dependências
Antes de executar o projeto localmente, certifique-se de ter as seguintes dependências instaladas:
- pandas
- openpyxl
- twilio

### Como Executar Localmente
Para executar o projeto localmente, siga os passos abaixo:

1. Criar uma conta na Twilio: Antes de testar o projeto, você precisará criar uma conta na Twilio, caso ainda não possua uma. Você pode se inscrever para uma conta de avaliação gratuita no site da [Twilio](https://www.twilio.com).

2. Configurar as variáveis de ambiente: Para proteger informações sensíveis, como as credenciais da sua conta Twilio e os números de telefone, o projeto utiliza variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```
ACCOUNT_SID=sua_twilio_account_sid
AUTH_TOKEN=seu_twilio_auth_token
TWILLIO_NUMBER=seu_numero_twilio
PHONE_NUMBER=seu_numero_para_receber_sms
```

Substitua `sua_twilio_account_sid`, `seu_twilio_auth_token`, `seu_numero_twilio` e `seu_numero_para_receber_sms` pelas informações corretas da sua conta Twilio, token de autenticação, número Twilio e número de telefone para receber as notificações por SMS.

3. Instalar as dependências: Instale as dependências necessárias executando o seguinte comando no terminal ou prompt de comando:

```
pip install pandas openpyxl twilio
```

4. Preparar os dados de vendas: A aplicação espera que os dados de vendas estejam em arquivos CSV armazenados no diretório `./sales/`. Certifique-se de ter arquivos CSV para cada mês com as colunas `seller` (vendedor) e `sales` (vendas), contendo o nome do vendedor e o valor das vendas, respectivamente.

5. Executar a aplicação: Após configurar as variáveis de ambiente e preparar os dados de vendas, execute o script Python para executar a aplicação:

```
python main.py
```

O script lerá os dados de vendas dos arquivos CSV, identificará os vendedores com vendas acima de 55.000 e enviará notificações por SMS para informar aos vendedores sobre suas conquistas de bônus.

## Licença
Este projeto está licenciado sob a Licença MIT. Você pode encontrar o texto completo da licença no arquivo [LICENSE](LICENSE.md).
