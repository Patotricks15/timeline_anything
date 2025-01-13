# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /app/requirements.txt

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação para o container
COPY . /app

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
