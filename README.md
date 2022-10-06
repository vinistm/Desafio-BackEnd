
## Instalação

no seu terminal o seguinte comando : 
```
  git clone git@github.com:vinistm/Desafio-BackEnd.git
```
Após o clone  do arquivo, utilize os seguintes comandos:
```bash
  cd Desafio-BackEnd/

  pip install -r requirements.txt

  ./manage.py makemigrations
  ./manage.py migrate
  
```
ou : 
```bash
  cd Desafio-BackEnd/

  pip install -r requirements.txt

  python manage.py makemigrations
  python manage.py migrate
  
```
assim que efetuar esses comando é necessario rodar o servidor : 
```bash
  ./manage.py runserver
  
```
ou : 

```bash
  python manage.py runserver
  
```

## Envio de Arquivo:

Com o servidor rodando é possivel acessar algumas rotas, seriam elas :

envio de aruivo CNAB.txt

```bash
  http://127.0.0.1:8000/api/insertfile/
  
```
listagem e post de valores, ja com a leitura de um arquivo CNAB.txt


```bash
  http://127.0.0.1:8000/api/insertvalues/
  
```