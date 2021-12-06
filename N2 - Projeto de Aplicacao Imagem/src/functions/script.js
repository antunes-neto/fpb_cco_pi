import { reveal, fill, rgb } from './functions';
import cthief from '../../node_modules/colorthief/dist/color-thief.mjs';

let ct = new cthief();
window.onload = function () {

    let image, name, resize;
    const reader = new FileReader();
    const loader = document.getElementById('preInput');
    const select = document.getElementById('select');
    const hiddens = document.getElementsByClassName('hidden');
    const effects = document.getElementsByClassName('effect');
    const view = document.getElementById('imageView');
    let size = document.getElementsByClassName('select-size');

    // Ocultando o input
    select.addEventListener('click', () => {
        loader.click();
    })

    // Carregando a imagem na tela
    loader.addEventListener('change', () => {
        let file = loader.files.item(0);
        name = file.name;
        reader.readAsDataURL(file);

        reader.onload = function (event) {
            image = new Image();
            image.src = event.target.result;
            image.onload = onLoadImage;

        }
    })

    // Criando o canvas e exibindo a imagem
    let canvas = document.createElement('canvas');
    let ctx = canvas.getContext('2d');

    // Resize canvas
    let cv = document.createElement('canvas');
    let ctx2 = cv.getContext('2d');

    function onLoadImage() {

        // Pegando as medidas da imagem
        const { width, height } = image;
        canvas.width = width;
        canvas.height = height;

        size[0].addEventListener('change', () => {
            if (size[0].value === 'small') resize = 640;
            if (size[0].value === 'media') resize = 1200;
            if (size[0].value === 'great') resize = 1600;


            let fator_de_escala = resize / width;

            let width_2 = resize;
            let height_2 = height * fator_de_escala;
            ctx2.drawImage(image, 0, 0, width_2, height_2);

            let b = ctx2.canvas.toDataURL(image, 'image/jpeg', 0);

            view.src = cv.toDataURL();


        })

        // Desenhando a imagem
        ctx.clearRect(0, 0, width, height);
        ctx.drawImage(image, 0, 0);
        view.src = canvas.toDataURL();
        let img_pass = image;

        // Revelando os botões ocultos
        reveal(hiddens);
        rgb(ct);

        // Carregando a espera da funções
        for (let i = 0; i < effects.length; i++) {
            effects[i].addEventListener('change', () => {
                fill(canvas, ctx, img_pass, effects, view);
            });
        }

    }
    document.getElementById('download').onclick = () => {
        const a = document.createElement('a');
        a.download = (name.split('.')[0]) + '-edited.png';
        if (size[0].value !== 'normal') {
            a.href = cv.toDataURL();
            a.click()
        } else {
            a.href = canvas.toDataURL();
            a.click();
        }
    }
}
