module.exports = {
    // Filter
    fill: function (canvas, ctx, image, valor, imagem) {
        let { width, height } = image;

        // Selecionando a operação
        ctx.filter = `contrast(${valor[0].value}) hue-rotate(${valor[1].value}deg) brightness(${valor[2].value}%)
        sepia(${valor[3].value}%) grayscale(${valor[4].value}%) invert(${valor[5].value}%)`;

        // Exibindo a imagem
        ctx.clearRect(0, 0, width, height);
        ctx.drawImage(image, 0, 0);
        imagem.src = canvas.toDataURL();
    },

    // Revelando itens ocultos
    reveal: function (hiddens) {
        try {
            for (let i = 0; i < hiddens.length; i++) {
                hiddens[i].style.display = 'initial';
            }
        } catch (err) {
            console.log('~ Erro na hora de revelar ~\n' + err)
        }
    },
    rgb: function (ct) {
        let all, rgb = '', cores = '';

        const rgbToHex = (r, g, b) => '#' + [r, g, b].map(x => {
            const hex = x.toString(16)
            return hex.length === 1 ? '0' + hex : hex
        }).join('')

        // Cores
        let ctimg = document.getElementById('imageView');
        ctimg.addEventListener('load', function () {
            all = ct.getPalette(ctimg, 8);
            for (let i = 0; i < all.length; i++) {
                for (let k = 0; k < all[i].length; k++) {
                    rgb = rgb + ` ${all[i][k]}`;
                }
                // console.log('RGB: ' + rgb);
                // console.log('HEX: ' + rgbToHex(all[i][0], all[i][1], all[i][2]));
                cores = cores + ' ' + rgbToHex(all[i][0], all[i][1], all[i][2]);
            }

            let circles = document.getElementsByClassName('cor');
            cores = cores.split(' ');
            for (let i = 1; i < circles.length; i++) {
                circles[i].style.backgroundColor = `${cores[i]}`;
            }
        })
    },
};