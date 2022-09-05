import json, os

print("hola")
lista_archivos = os.listdir('./pages/emisiones/audios/')
episodios = []
descripciones = []
#print(lista_archivos)
for i in lista_archivos:
    episodios.append(i.replace(".mp3","")) #tenemos que sacar el formato de archivo en el nombre, asi que los guardamos en un nuevo array
episodios.sort(reverse=True)

#print(episodios)


#las descripciones de cada capítulo se guardan en un json con el formato "fecha":["numero","descripcion"]
with open(".\pages\emisiones\descripciones.json") as json_file:
    descripciones = json.load(json_file)
    print(descripciones)

#To-Do: reemplazar tildes en el archivo json

#generamos el archivo html en función de la lista de episodios

with open(".\pages\emisiones\emisiones.html", 'w') as f:
    f.write("<!DOCTYPE html><html><head>\n<meta charset=""utf-8""><title>Faros del pasado</title>\n")

    f.write("<link rel=\"stylesheet\" href=\"../../css/styles.css\">\n\n<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.png\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    # f.write("\n<script type=\"text/javascript\">\n\t(function(c,l,a,r,i,t,y){\n\t\tc[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};\n\t\tt=l.createElement(r);t.async=1;t.src=\"https://www.clarity.ms/tag/\"+i;\n\t\ty=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);\n\t\t})(window, document, \"clarity\", \"script\", \"cfz94uis3i\");\n</script>")
    f.write("<!-- AOS -->\n<link href=\"https://unpkg.com/aos@2.3.1/dist/aos.css\" rel=\"stylesheet\">")
    f.write("<script src=\"https://unpkg.com/aos@2.3.1/dist/aos.js\"></script>")

    f.write("</head>\n<body>\n<main>\n")

    #reemplazar por header
    f.write("<a href=\"../../index.html\">Volver</a>")
    # f.write("<header><a href=\"../elfaro.html\"><img src=\"../elfarologo.jpg\"></a><h2>Faros del pasado</h2></header>\n\n")
    # f.write("<h4>Aqu&iacute; encontrar&aacute;s las grabaciones de los programas emitidos. Usando los controles del reproductor podr&aacute;s adelantar el audio, descargarlo y reproducirlo en 1.5x</h4>")
    # f.write("<a href=\"https://open.spotify.com/show/26ZvU92WzcChhUnhaSxzPw\" target=\"__blank\">\n<div class=\"spotify episodio\"><img src=\"../spotify-logo.png\"></img>")
    # f.write("<p>Escuchanos en spotify!</p></div></a>\n\n\n")

    count = 0
    for i in episodios:
        print(descripciones[i][0])
        print(descripciones[i][1])
    for i in episodios:
        if count%2 == 1:
            f.write("\t<div data-aos=\"fade-up-right\" class=\"episodio reverse\">\n")
        else:
            f.write("\t<div data-aos=\"fade-up-left\"class=\"episodio\">\n")

        f.write("\t\t<div class=\"episodio_imagen\"><img src=\"../emisiones/images/" + i + ".webp\"></div>\n")
        f.write("\t\t<div class=\"episodio_contenido\">\n")
        f.write("\t\t\t<div class=\"episodio_titulo\">Programa " +descripciones[i][0] +" - " + i +"</div>\n")
        f.write("\t\t\t<div class=\"episodio_descripcion\">\n")

        try:
            f.write("\t\t\t\t<p>"+descripciones[i][1]+"</p>\n")
        except:
            f.write("\t\t\t\t<p>Sin descripcion en JSON</p>\n")

        f.write("\t\t\t</div>\n")
        if count == 0:
            #f.write("\t\t\t<audio controls autoplay><source preload=\"true\" src=\"audios/"+ i + ".mp3\" type=\"audio/mpeg\"></audio>\n")
            f.write("\t\t<audio controls><source preload=\"true\" src=\"audios/"+ i + ".mp3\" type=\"audio/mpeg\"></audio>\n")
        else:
            f.write("\t\t\t<audio controls><source src=\"audios/"+ i + ".mp3\" type=\"audio/mpeg\"></audio>\n")

        f.write("\t\t</div>\n") #cerrar div class contenido
        f.write("\t</div>\n\n")#cerrar div class episodio
        count += 1

    f.write("</main>\n")
    f.write("<div class=\"publicidad\">\n")

    f.write("<div class=\"publicidad__item centrado\"><img src=\"../../images/publicidad/laarena.png\" alt=\"Publicidad diario La Arena\"></div>\n")
    f.write("\t<div class=\"publicidad__item centrado\"><img src=\"../../images/publicidad/unlpam.jpg\" alt=\"Publicidad Universidad de La Pampa\"></div>\n")
    f.write("\t<div class=\"publicidad__item centrado\"><div>Publicite aquí!</div></div>\n")
    f.write("\t<div class=\"publicidad__item centrado\"><img src=\"../../images/publicidad/atuel.jpg\" alt=\"Propaganda Gobierno de La Pampa\"></div>\n")
    f.write("</div>\n\n")

    f.write("<footer><a href=\"https://lu4ult.github.io\" target=\"__blank\">Desarrollado por Lautaro Tourn</a></footer>\n")
    #aos
    f.write("<script>AOS.init();</script>")
    f.write("\n\n</body>\n</html>")
    f.close()

with open(".\pages\emisiones\wa-link.html", 'w') as f:
    f.write("<!DOCTYPE html><html><head>\n<meta charset=""utf-8""><title>Faros del pasado</title>\n<link rel=\"stylesheet\" href=\"../styles.css\"> <!-- Header and footer-->\n<link rel=\"stylesheet\" href=\"styles.css\"> <!-- This file styles-->\n<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.png\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    f.write("</head>\n<body>\n")

    descripciones[episodios[0]][1] = descripciones[episodios[0]][1].replace("<br>","%0a") #reemplazamos el html break line, por el equivalente salto de línea para la url
    descripciones[episodios[0]][1] = descripciones[episodios[0]][1].replace("\"","%22")

    #print("Texto whatsapp:\n")
    #print(descripciones[episodios[0]][1])
    texto = "Ya est%C3%A1 disponible el *programa "+descripciones[episodios[0]][0]+" del "+episodios[0]+" de El Faro!*%0a%0a%0a"
    texto += descripciones[episodios[0]][1]
    texto += "%0a%0a%0aPodes esucharla en el siguiente link:%0ahttps://lu4ult.com/el-faro/emisiones/emisiones.html%0a%0a"
    texto += "O en spotify:%0ahttps://open.spotify.com/show/26ZvU92WzcChhUnhaSxzPw"

    f.write("<a target=\"__blank\" href=\"https://wa.me/542954543687?text="+texto+"\">Link Fernando</a>")
    f.write("<a target=\"__blank\" href=\"https://wa.me/542954692293?text="+texto+"\">Link Lautaro</a>")
    f.write("</body>\n</html>")
    f.close()
