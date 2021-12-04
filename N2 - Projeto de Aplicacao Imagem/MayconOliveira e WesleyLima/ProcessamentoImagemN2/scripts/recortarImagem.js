const photoFile = document.getElementById('photo-file')
let photoPreview = document.getElementById('photo-preview')
let image;
let photoName;
var btnRecortar = false
document.getElementById('btn_recortar')
        .onclick = function () {
                btnRecortar = true
        }
document.getElementById('btn_ajustes')
        .onclick = function () {
                selection.style.display = 'none'
                photoPreview.style.cursor = 'default'
                btnRecortar = false
        }
// Select & Preview image
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

// Selection tool
var selection = document.getElementById('selection-tool')

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
                photoPreview.addEventListener(eventName, events[eventName])
        })


// Canvas
let canvas = document.createElement('canvas')
let ctx = canvas.getContext('2d')

function onLoadImage() {
        const { width, height } = image
        canvas.width = width;
        canvas.height = height;

        // limpar o contexto
        ctx.clearRect(0, 0, width, height)

        // desenhar a imagem no contexto
        ctx.drawImage(image, 0, 0)

        photoPreview.src = canvas.toDataURL()
}

// Cortar imagem
const cropButton = document.getElementById('crop-image')
cropButton.onclick = () => {
        const { width: imgW, height: imgH } = image
        const { width: previewW, height: previewH } = photoPreview

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

        // pegar do ctx a imagem cortada
        const croppedImage = ctx.getImageData(actualX, actualY, croppedWidth, croppedHeight)

        // limpar o ctx
        ctx.clearRect(0, 0, ctx.width, ctx.height)

        // ajuste de proporções
        image.width = canvas.width = croppedWidth;
        image.height = canvas.height = croppedHeight;

        // adicionar a imagem cortada ao ctx
        ctx.putImageData(croppedImage, 0, 0)

        // esconder a ferramenta de seleção
        selection.style.display = 'none'

        // atualizar o preview da imagem
        photoPreview.src = canvas.toDataURL()
}

