import json, os

print("hola")
lista_archivos = os.listdir('./pages/emisiones/audios/')
episodios = []
descripciones = []

ind = "\t"  #para generar la indentación
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
    f.write("<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<meta charset=""utf-8"">\n\t\t<title>El Faro - Faros del pasado</title>\n")
    f.write("\t\t<link rel=\"icon\" type=\"image/x-icon\" href=\"../../images/favicon.png\">\n")

    f.write("\n\t\t<!-- Bootstrap -->\n\t\t<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx\" crossorigin=\"anonymous\">")
    f.write("\n\t\t<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx\" crossorigin=\"anonymous\">")
    f.write("\n\t\t<!-- AOS -->\n\t\t<link href=\"https://unpkg.com/aos@2.3.1/dist/aos.css\" rel=\"stylesheet\">")
    f.write("\n\t\t<script src=\"https://unpkg.com/aos@2.3.1/dist/aos.js\"></script>")
    f.write("\n\t\t<link rel=\"stylesheet\" href=\"../../css/styles.css\">\n\n\t\t<link rel=\"icon\" type=\"image/x-icon\" href=\"../favicon.png\">\n\t\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
    f.write("\n\t</head>\n\n\t<body>")

    #reemplazar por header
    #f.write("<a href=\"../../index.html\">Volver</a>")

    f.write("\n\t\t<header>\n\t\t\t<div class=\"logo-container centrado\">")
    f.write("\n"+ind*4+"<img src=\"../../images/logo-transparente-parcial.png\" alt=\"El Faro Isotipo\">")
    f.write("\n\t\t\t</div>\n\t\t\t<section>\n\t\t\t\t<a href=\"../../index.html\"><span id=\"titulo\">El </span><span id=\"titulo2\">Faro,</span><span id=\"titulo3\"> un programa de ciencia</span></a>\n\t\t\t</section>")
    f.write("\n\t\t\t<nav>\n"+ind*4+"<ul>")
    f.write("\n"+ind*5+"<li class=\"active\"><a href=\"#\">Emitidos</a></li>")
    f.write("\n"+ind*5+"<li><a href=\"../../pages/conductores.html\">Conduccci&oacuten</a></li>")
    f.write("\n"+ind*5+"<li><a href=\"../../pages/contacto.html\">Contacto</a></li>")
    f.write("\n"+ind*5+"<li><a href=\"../../pages/radio-online.html\">Radio Online</a></li>")
    f.write("\n"+ind*4+"</ul>\n\t\t\t</nav>\n\t\t</header>\n\n\t\t<main>\n")

    f.write(r"""
            <div class="titulo-principal">
                <h1>Faro,</h1>
                <h2>Un programa de ciencia</h2>
                <h3>Faros del pasado</h3>
            </div>
            """)

    count = 0

    for i in episodios:
        if count%2 == 1:
            f.write(ind*3+"<div data-aos=\"flip-right\" data-aos-duration=\"1000\" class=\"episodio reverse\">\n")
        else:
            f.write(ind*3+"<div data-aos=\"flip-left\" data-aos-duration=\"1000\" class=\"episodio\">\n")

        f.write(ind*4+"<div class=\"episodio_imagen\">\n"+ind*5+"<img src=\"../emisiones/images/" + i + ".jpg\" alt=\"Imagen programa "+i+"\">\n"+ind*4+"</div>\n")
        f.write(ind*4+"<div class=\"episodio_contenido\">\n")
        f.write(ind*5+"<div class=\"episodio_titulo\">Programa " +descripciones[i][0] +" - " + i +"</div>\n")
        f.write(ind*5+"<div class=\"episodio_descripcion\">\n")

        try:
            #f.write(ind*6+"<p>"+descripciones[i][1]+"</p>\n")
            f.write(ind*6+descripciones[i][1]+"\n")
        except:
            f.write(ind*6+"Sin descripcion en JSON\n")

        f.write(ind*5+"</div>\n")
        if count == 0:
            #f.write("\t\t\t<audio controls autoplay><source preload=\"true\" src=\"audios/"+ i + ".mp3\" type=\"audio/mpeg\"></audio>\n")
            f.write(ind*5+"<audio controls>\n"+ind*6+"<source preload=\"true\" src=\"audios/"+ i + ".mp3\" type=\"audio/mpeg\">\n"+ind*5+"</audio>\n")
        else:
            f.write(ind*5+"<audio controls>\n"+ind*6+"<source preload=\"true\" src=\"audios/"+ i + ".mp3\" type=\"audio/mpeg\">\n"+ind*4+"</audio>\n")

        f.write(ind*4+"</div>\n") #cerrar div class contenido
        f.write(ind*3+"</div>\n\n")#cerrar div class episodio
        count += 1

    f.write("\t\t</main>\n")
    f.write("\t\t<div class=\"publicidad\">\n")

    #  <div class="publicidad__item  publ--1 centrado"><img src="../publicidad/laarena.png" alt="Publicidad diario La Arena"></div>
    f.write(ind*3+"<div class=\"publicidad__item publ--1 centrado\"><img src=\"../../images/laarena.png\" alt=\"Publicidad diario La Arena\"></div>\n")
    f.write(ind*3+"<div class=\"publicidad__item publ--2 centrado\"><img src=\"../../images/unlpam.jpg\" alt=\"Publicidad Universidad de La Pampa\"></div>\n")
    f.write(ind*3+"<div class=\"publicidad__item publ--3 centrado\"><div>Publicite aqu&iacute!</div></div>\n")
    f.write(ind*3+"<div class=\"publicidad__item publ--4 centrado\"><img src=\"../../images/atuel.jpg\" alt=\"Propaganda Gobierno de La Pampa\"></div>\n")
    f.write("\t\t</div>\n\n")

    f.write("\t\t<footer><a href=\"https://lu4ult.github.io\" target=\"__blank\">Desarrollado por Lautaro Tourn</a></footer>\n")
    #aos
    f.write("\t\t<script>AOS.init();</script>")
    f.write("\n\n\t</body>\n</html>")
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
    texto += "%0a%0a%0aPodes esucharla en el siguiente link:%0ahttps://lu4ult.github.io/el-faro-coderhouse/pages/emisiones/emisiones.html%0a%0a"
    texto += "O en spotify:%0ahttps://open.spotify.com/show/26ZvU92WzcChhUnhaSxzPw"

    f.write("<a target=\"__blank\" href=\"https://wa.me/542954543687?text="+texto+"\">Link Fernando</a><br>")
    f.write("<a target=\"__blank\" href=\"https://wa.me/542954692293?text="+texto+"\">Link Lautaro</a>")
    f.write("</body>\n</html>")
    f.close()
