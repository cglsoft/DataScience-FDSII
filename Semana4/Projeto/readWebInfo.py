"""
#https://github.com/AlanPrado/FDSI2_subway_data/blob/master/analyzing-subway-data-ndfdsi.ipynb


Subway Data Analysis
Introduction
O sistema de ônibus e trens de Nova Iorque - o Metro Transit Authority - fornece seus dados para download através de arquivos csv. Uma das informações disponíveis são os dados das catracas do metrô que contém logs semanais de entradas cumulativas e saídas por catraca por estação de metrô em algum intervalo de tempo.

Neste projeto iremos utilizar apenas os das catraca disponíveis em: http://web.mta.info/developers/turnstile.html.

Seção 1 - Coleta de Dados
Exercicio 1.1
Mãos a obra!! Agora é sua vez de coletar os dados. Escreva abaixo um código python que acesse o link http://web.mta.info/developers/turnstile.html e baixe os arquivos do mês de junho de 2017. O arquivo deverá ser salvo com o nome turnstile_100617.txt onde 10/06/17 é a data do arquivo.

Abaixo seguem alguns comandos que poderão te ajudar:

Utilize a biblioteca urllib para abrir e resgatar uma página da web. Utilize o comando abaixo onde url será o caminho da página da web onde se encontra o arquivo:

u = urllib.urlopen(url)
html = u.read()
Utilize a biblioteca BeautifulSoup para procurar na página pelo link do arquivo que deseja baixar. Utilize o comando abaixo para criar o seu objeto soup e procurar por todas as tags 'a'no documento:

soup = BeautifulSoup(html, "html.parser")
links = soup.find_all('a')
Uma dica para baixar apenas os arquivos do mês de junho é verificar a data no nome do arquivo. Por exemplo, para baixar o arquivo do dia 17/06/2017 verifique se o link termina com "turnstile_170610.txt". Se não fizer isso você baixará todos os arquivos da página. Para fazer isso utilize o comando conforme abaixo:

if '1706' in link.get('href'):
E a dica final é utilizar o comando abaixo para fazer o download do arquivo txt:

urllib.urlretrieve(link_do_arquivo, filename)
Lembre-se, primeiro, carregue todos os pacotes e funções que você estará usando em sua análise.


"""

import os
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime as dt
import time


# Recuperar informações da Web
def getUrl(url):
    try:
        u = urllib.request.urlopen(url)
        html = u.read()
        
        return html, u     
    except Exception as e:
        raise RuntimeError("HTTP Request error %s" % str(e))    

def create_Directory(path):
    directory = os.path.abspath(path)

    if not os.path.exists(directory):
        os.makedirs(directory)

def download(links, basedir):
    try:        
        # Create directory
        create_Directory(basedir + '/')

        files = []
        total = len(links)
        count = 0        
        start = time.time()
        print('Starting download {} files'.format(total))
        
        for filename, link in links.items(): 
            count+=1                                
            path = os.path.abspath(basedir + '/%s' % filename)
            files.append(path)  
            local_filename, headers = urllib.request.urlretrieve(link,path)
            print( '{} - {} downloaded'.format( count, local_filename ) )           
        
        print('{} files download has finished successfully in {}'.format( total, time.time()-start ))
            
        return files

    except Exception as e:
        raise RuntimeError("Exception Download  %s" % str(e))
    
    
def get_turnstile_links(year, month=None):
    try:
        html, u = getUrl("http://web.mta.info/developers/turnstile.html")
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find("div", class_="last").find_all("a")

        datalinks = {}

        for link in links:
            try:
                date = dt.strptime(link.get_text(), "%A, %B %d, %Y")

                if (date.year == year and (not month or date.month == month)):
                    href = link.get("href")
                    filename = href.rsplit("/", 1)[-1]
                    datalinks[filename] = "http://web.mta.info/developers/" + href
            except ValueError as e:
                print("Invalid link %s: Reason %s" % (link.get("href"), str(e)))

        return datalinks
    except Exception as e:
        raise RuntimeError("Reason %s" % str(e))


# Global Variable defination
download_Directory = "data"
year = 2017
month = 7
links = get_turnstile_links(year, month)
fileNames = download(links, download_Directory)


"""
Exercicio 1.2
Escreva uma função que pegue a lista de nomes dos arquivos que você baixou no exercicio 1.1 e consolide-os em um único arquivo. Deve existir apenas uma linha de cabeçalho no arquivo de saida.

Por exemplo, se o arquivo_1 tiver: linha 1... linha 2...

e o outro arquivo, arquivo_2 tiver: linha 3... linha 4... linha 5...

Devemos combinar o arquivo_1 com arquivo_2 em um arquivo mestre conforme abaixo:

'C/A, UNIT, SCP, DATEn, TIMEn, DESCn, ENTRIESn, EXITSn' linha 1... linha 2... linha 3... linha 4... linha 5...
"""

def create_master_turnstile_file(filenames, output_file):
    create_Directory(output_file.rsplit("/", 1)[0])
    
    with open(output_file, 'w') as master_file:
        master_file.write('C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATEn,TIMEn,DESCn,ENTRIESn,EXITSn\n')
        for filename in filenames:
            with open(filename, 'r') as f:
                f.readline()
                master_file.write(f.read())
    
    return output_file

print("Merging files...")
output_dir = "output"
turnstile_file = create_master_turnstile_file(fileNames, output_dir + "/turnstile_1707.txt")
print("Files merged...")