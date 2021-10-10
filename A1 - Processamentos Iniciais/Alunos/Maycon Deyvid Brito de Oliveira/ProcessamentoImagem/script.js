let imagem = null;

function upload() {
        //Obtem a entrada da imagem
        var fileinput = document.getElementById("finput");
        //Gera uma nova imagem simples
        imagem = new SimpleImage(fileinput);
        //Exibi imagem original
        var imgOrig = document.getElementById("imgOriginal");
        imagem.drawTo(imgOrig);
}

function escalaCinza() {
        let imagemCinza = new SimpleImage(imagem);
        //Altera todos os pixels da imagem para cinza
        for (var pixel of imagemCinza.values()) {
                var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
                pixel.setRed(avg);
                pixel.setGreen(avg);
                pixel.setBlue(avg);
        }
        //Exibe o resultado
        var canvas = document.getElementById("resultadoUnico");
        imagemCinza.drawTo(canvas);
}

function coresNegativas() {
        //Altera todos os pixels da imagem para cores negativas
        let imagemNegativa = new SimpleImage(imagem);
        for (var pixel of imagemNegativa.values()) {
                pixel.setRed(255 - pixel.getRed());
                pixel.setGreen(255 - pixel.getGreen());
                pixel.setBlue(255 - pixel.getBlue());
        }
        //Exibe o resultado
        var canvas = document.getElementById("resultadoUnico");
        imagemNegativa.drawTo(canvas);
}

function vermelho() {
        let imagemVermelho = new SimpleImage(imagem);
        //Mantem pixel vermelho
        for (var pixel of imagemVermelho.values()) {
                var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
                if (pixel.getRed() > 40 & pixel.getGreen() < 80 & pixel.getBlue() < 80) {
                        pixel.setRed(pixel.getRed());
                        pixel.setGreen(pixel.getGreen());
                        pixel.setBlue(pixel.getBlue());
                } else {
                        pixel.setRed(avg);
                        pixel.setGreen(avg);
                        pixel.setBlue(avg);
                }
        }
        //Exibe o resultado
        var canvas = document.getElementById("resultadoUnico");
        imagemVermelho.drawTo(canvas);
}

function verde() {
        let imagemVerde = new SimpleImage(imagem);
        //Mantem pixel verde
        for (var pixel of imagemVerde.values()) {
                var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
                if (pixel.getGreen() > 40 & pixel.getRed() < 80 & pixel.getBlue() < 80) {
                        pixel.setRed(pixel.getRed());
                        pixel.setGreen(pixel.getGreen());
                        pixel.setBlue(pixel.getBlue());
                } else {
                        pixel.setRed(avg);
                        pixel.setGreen(avg);
                        pixel.setBlue(avg);
                }
        }
        //Exibe o resultado
        var canvas = document.getElementById("resultadoUnico");
        imagemVerde.drawTo(canvas);
}

function azul() {
        let imagemAzul = new SimpleImage(imagem);
        //Mantem pixel azul
        for (var pixel of imagemAzul.values()) {
                var avg = (pixel.getRed() + pixel.getGreen() + pixel.getBlue()) / 3;
                if (pixel.getBlue() > 40 & pixel.getRed() < 80 & pixel.getGreen() < 80) {
                        pixel.setRed(pixel.getRed());
                        pixel.setGreen(pixel.getGreen());
                        pixel.setBlue(pixel.getBlue());
                } else {
                        pixel.setRed(avg);
                        pixel.setGreen(avg);
                        pixel.setBlue(avg);
                }
        }
        //Exibe o resultado
        var canvas = document.getElementById("resultadoUnico");
        imagemAzul.drawTo(canvas);
}

/* PERMITE SALVAR FAZER O DOWNLOAD DA IMAGEM CONVERTIDA */
function downloadImg() {
        var download = document.getElementById("download");
        var image = document.getElementById("resultadoUnico").toDataURL("image/png")
                .replace("image/png", "image/octet-stream");
        download.setAttribute("href", image);
}
