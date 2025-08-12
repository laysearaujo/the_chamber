# Configuração do Google Sheets para The Chamber

Este guia explica como configurar a integração com Google Sheets para salvar automaticamente os dados do experimento.

## 📋 Pré-requisitos

1. Uma conta Google
2. Python 3.7+
3. Acesso à internet

## 🚀 Passo a Passo

### 1. Criar um Projeto no Google Cloud Console

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Clique em "Selecionar projeto" → "Novo projeto"
3. Digite um nome para o projeto (ex: "The Chamber Experiment")
4. Clique em "Criar"

### 2. Ativar a Google Sheets API

1. No menu lateral, vá em "APIs e serviços" → "Biblioteca"
2. Pesquise por "Google Sheets API"
3. Clique na API e depois em "Ativar"

### 3. Criar Credenciais de Conta de Serviço

1. Vá em "APIs e serviços" → "Credenciais"
2. Clique em "Criar credenciais" → "Conta de serviço"
3. Preencha:
   - **Nome da conta de serviço**: `the-chamber-sheets`
   - **Descrição**: `Conta para integração com The Chamber`
4. Clique em "Criar e continuar"
5. Em "Conceder acesso", selecione "Editor"
6. Clique em "Concluído"

### 4. Gerar e Baixar a Chave

1. Na lista de contas de serviço, clique na que você criou
2. Vá na aba "Chaves"
3. Clique em "Adicionar chave" → "Criar nova chave"
4. Selecione "JSON" e clique em "Criar"
5. O arquivo será baixado automaticamente
6. **Renomeie o arquivo para `credentials.json`**
7. **Mova o arquivo para a pasta do projeto The Chamber**

### 5. Criar a Planilha no Google Drive

1. Acesse [Google Drive](https://drive.google.com/)
2. Clique em "Novo" → "Google Sheets"
3. Dê um nome à planilha (ex: "The Chamber - Dados Experimentais")
4. **Importante**: Compartilhe a planilha com o email da conta de serviço
   - Clique em "Compartilhar" (canto superior direito)
   - Adicione o email da conta de serviço (está no arquivo `credentials.json`)
   - Dê permissão de "Editor"
   - Clique em "Enviar"

### 6. Obter o ID da Planilha

1. Na URL da planilha, copie o ID (parte entre `/d/` e `/edit`)
   - Exemplo: `https://docs.google.com/spreadsheets/d/1ABC123.../edit`
   - ID: `1ABC123...`

### 7. Configurar o Projeto

1. Abra o arquivo `google_sheets_config.py`
2. Substitua `1PcAveY4HB4sAu-alSXaGArkqErY1Xa5J2VKZlM52xHs` pelo ID da sua planilha
3. Ajuste o `RANGE_NAME` se necessário (padrão: `Sheet1!A1`)

### 8. Instalar Dependências

```bash
pip install -r requirements.txt
```

## 🔧 Estrutura da Planilha

A planilha será preenchida automaticamente com as seguintes colunas:

- ID_Sessao
- ID_Participante  
- Num_Rodada
- Idade
- Genero_Participante
- Experiencia_com_Jogos
- ID_Caso
- Tipo_de_Historia
- Genero_Suspeito
- Tempo_de_Decisao_s
- Decisao_Final
- Mudanca_de_Voto
- Resultado_Real_Caso
- Num_Jogadores_Sessao
- Versão

## ✅ Verificação

1. Execute o experimento: `python the_chamber.py`
2. Verifique se aparece a mensagem: "✅ Autenticação com Google Sheets realizada com sucesso!"
3. Após cada caso, verifique se aparece: "📊 Dados também enviados para o Google Sheets com sucesso!"
4. Abra sua planilha no Google Drive para ver os dados sendo adicionados

## 🚨 Solução de Problemas

### Erro de Autenticação
- Verifique se o arquivo `credentials.json` está na pasta correta
- Confirme se a conta de serviço tem permissão de "Editor" na planilha

### Erro de Permissão
- Verifique se a planilha foi compartilhada com o email da conta de serviço
- Confirme se as permissões estão configuradas como "Editor"

### Erro de API
- Verifique se a Google Sheets API está ativada no projeto
- Confirme se as credenciais estão corretas

## 📝 Notas Importantes

- Os dados são salvos tanto localmente quanto no Google Sheets
- Se houver falha no Google Sheets, os dados locais servem como backup
- A planilha é atualizada em tempo real durante o experimento
- Cada sessão gera uma nova linha para cada rodada de cada caso 