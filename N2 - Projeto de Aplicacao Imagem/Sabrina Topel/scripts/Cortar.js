/* <!-- ------------------------------------ COTAR IMAGEM --------------------------------------------- --> */

const photoFile = document.getElementById('photo-file')
let FotoPrevia = document.getElementById('FotoPrevia')
let image;
let photoName;
let btnRecortar = false
document.getElementById('btn_recortar')
        .onclick = function () {
                btnRecortar = true
        }
document.getElementById('btn_ajustes')
        .onclick = function () {
                selection.style.display = 'none'
                FotoPrevia.style.cursor = 'default'
                btnRecortar = false
        }


/* <!-- ------------------------------------ SELECAO E EXIBICAO --------------------------------------------- --> */
document.getElementById('select-image')
        .onclick = function () {
                photoFile.click()
        }

window.addEventListener('DOMContentLoaded', () => {
        photoFile.addEventListener('change', () => {
                let file = photoFile.files.item(0)
                photoName = file.name;

                // ler um arquivo
                let reader = new FileReader()
                reader.readAsDataURL(file)
                reader.onload = function (event) {
                        image = new Image();
                        image.src = event.target.result
                        image.onload = onLoadImage
                }
        })
})

/* <!-- ------------------------------------ SELECAO TOOL --------------------------------------------- --> */
const selection = document.getElementById('selection-tool')

let startX, startY, relativeStartX, relativeStartY,
        endX, endY, relativeEndX, relativeEndY;
let startSelection = false;

const events = {
        mouseover() {
                if (btnRecortar) this.style.cursor = 'crosshair'

        },
        mousedown() {
                if (btnRecortar) {
                        const { clientX, clientY, offsetX, offsetY } = event
                        // console.table({
                        //     'client': [clientX, clientY],
                        //     'offset': [offsetX, offsetY]
                        // })

                        startX = clientX
                        startY = clientY
                        relativeStartX = offsetX
                        relativeStartY = offsetY

                        startSelection = true
                }
        },
        mousemove() {
                if (btnRecortar) {
                        endX = event.clientX
                        endY = event.clientY

                        if (startSelection) {
                                selection.style.display = 'initial';
                                selection.style.top = startY + 'px';
                                selection.style.left = startX + 'px';
                                document.getElementById("input-largura").value = (endX - startX);
                                document.getElementById("input-altura").value = (endY - startY);
                                document.getElementById("input-x").value = (relativeStartX);
                                document.getElementById("input-y").value = (relativeStartY);
                                /*  console.log(selection.style.width)
                                 console.log(selection.style.height) */

                                selection.style.width = (endX - startX) + 'px';
                                selection.style.height = (endY - startY) + 'px';
                        }
                }

        },
        mouseup() {
                if (btnRecortar) {
                        startSelection = false;
                        relativeEndX = event.layerX;
                        relativeEndY = event.layerY;
                        // mostrar o botão de corte
                        cropButton.style.display = 'initial'
                }
        }
}

Object.keys(events)
        .forEach(eventName => {
                // addEventListener('mouseover', events.mouseover)
                FotoPrevia.addEventListener(eventName, events[eventName])
        })


/* <!-- ------------------------------------ CANVAS --------------------------------------------- --> */
let canvas = document.createElement('canvas')
let ctx = canvas.getContext('2d')

function onLoadImage() {
        const { width, height } = image
        canvas.width = width;
        canvas.height = height;

                /* LIMPAR */
        ctx.clearRect(0, 0, width, height)

        /* DESENHAR IMAGEM */
        ctx.drawImage(image, 0, 0)

        FotoPrevia.src = canvas.toDataURL()
}

/* ---------- COTAR IMAGEM -------------- */
const cropButton = document.getElementById('crop-image')
cropButton.onclick = () => {
        const { width: imgW, height: imgH } = image
        const { width: previewW, height: previewH } = FotoPrevia

        const [widthFactor, heightFactor] = [
                +(imgW / previewW),
                +(imgH / previewH)
        ]

        const [selectionWidth, selectionHeight] = [
                +selection.style.width.replace('px', ''),
                +selection.style.height.replace('px', '')
        ]

        const [croppedWidth, croppedHeight] = [
                +(selectionWidth * widthFactor),
                +(selectionHeight * heightFactor)
        ]

        const [actualX, actualY] = [
                +(relativeStartX * widthFactor),
                +(relativeStartY * heightFactor)
        ]

         /* ---- PEGAR DO CTX A IMAGEM CORTADA --------- */
        const croppedImage = ctx.getImageData(actualX, actualY, croppedWidth, croppedHeight)

        //  /* ---- LIMPAR O CTX --------- */
        ctx.clearRect(0, 0, ctx.width, ctx.height)

         /* ----AJUSTE DE PROPORÇÕES  --------- */
        image.width = canvas.width = croppedWidth;
        image.height = canvas.height = croppedHeight;
        ctx.putImageData(croppedImage, 0, 0)

        /* ----  ADICIONAR A IMAGEM CORTADA AO CTX --------- */
        selection.style.display = 'none'

          /* ----  ATUALIZAR O PREVIEW DA IMAGEM  --------- */
        FotoPrevia.src = canvas.toDataURL()
}

