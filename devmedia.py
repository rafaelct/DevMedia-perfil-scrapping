import mechanize
from bs4 import BeautifulSoup as bs
import http.cookiejar as cookielib
import sys

def statusPerfil(login,senha) :

    strResultado = []
    linhas = ""
    
  
    cookies = cookielib.CookieJar()  # cria um repositório de cookies
    browser = mechanize.Browser()    # inicia um browser
    browser.set_cookiejar(cookies)   # aponta para o seu repositório de cookies

    
    
    # carrega a pagina
    browser.open('https://www.devmedia.com.br/')

    browser.select_form(nr=1)      # o formulário de senha é o segundo
    browser.form['usuario'] = login     # seu e-mail de login
    browser.form['senha'] = senha  # sua senha
    browser.submit()               # submissão dos dados

    # carrega a pagina do perfil logado
    browser.open('https://www.devmedia.com.br/perfil/')
    pagina = browser.response().read()  # pega o HTML 

    # Beautiful Soup aqui
    soup = bs(pagina,'html.parser')
    codigo = soup.find_all(True,{"class":"box-numeros"})

    linhas = "Login da DevMedia: "+login+"\n"
    linhas += "-----------------"+"\n"
    linhas += "\nEstatisticas:"+"\n"

    strResultado.append(linhas)
    for item in codigo :
        titulo = item.text.split('\t')[4].split('\r')[0]
        valor = item.text.split('\t')[-3]
        linhas = titulo+" - "+ valor
        strResultado.append(linhas)

    #codigo = soup.find_all(True,{"class":"box-tecnologias"})
    codigo = soup.findAll(class_='box-tecnologias')

    #print(codigo)

    linhas = "Tecnologias:\n"
    strResultado.append(linhas)

    for item in codigo :

        listTec = item.findAll(class_='tags')
        #print(listTec)
        for tec in listTec :
            linhas =tec.text
            strResultado.append(linhas)
    return strResultado


if __name__ == '__main__' :
    
    if len(sys.argv) < 3 :
        print("Falta argumentos:")
        print("Uso: "+sys.argv[0]+" <login> <senha>")
        exit(1)

    login = sys.argv[1]
    senha = sys.argv[2]
    
    retorno = statusPerfil(login,senha)

    for linha in retorno :
        print(linha)

