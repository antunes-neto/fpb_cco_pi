const photoFile = document.getElementById('photo-file')
let photoPreview = document.getElementById('targetimage')
let image;
let photoName;

//Filtros
let myform = document.getElementById('myform');
let targetimage = document.getElementById('targetimage');
let inputrange = document.querySelectorAll('.slider');


for(let i=0; i<=inputrange.length-1; i++ ){
    inputrange[i].addEventListener('input', editimage);
}

function editimage(){
    let gs = document.getElementById('gs');
    let blur = document.getElementById('blur');
    let huerotate = document.getElementById('hue-rotate');
    let sepia = document.getElementById('sepia');
    let brightness = document.getElementById('brightness');

    

    let gsval = gs.value;
    let blurval = blur.value;
    let huerotateval = huerotate.value;
    let sepiaval = sepia.value;
    let brightval = brightness.value;

    targetimage.style.filter = 'brightness('+brightval+'%) grayscale('+gsval+'%) blur('+blurval+'px) hue-rotate('+huerotateval+'deg) sepia('+sepiaval+'%)';
}

let sliderform = document.getElementById('slider-form');
sliderform.addEventListener('reset', function(){
    sliderform.reset();
    setTimeout(function(){
        editimage();
    },0)
})



//Para carregar a imagem a partir de um arquivo
document.getElementById('select-image')
.onclick = function(){
    photoFile.click()
}

window.addEventListener('DOMContentLoaded', () =>{
    photoFile.addEventListener('change', () =>{
        let file = photoFile.files.item(0)
        let reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = function(event) {
           
            image = new Image()
            image.src = event.target.result
            image.onload= onLoadImage

        }

    })
})




//Ferramenta de seleção

const selection = document.getElementById('selection-tool')

let startX, startY, relativeStartX, relativeStartY,
endX, endY, relativeEndX, relativeEndY;
let startSelection = false;

const events = {
    mouseover(){
       this.style.cursor = 'crosshair'
    },
    mousedown(){
        const {clientX, clientY, offsetX, offsetY} = event
        // console.table({
        //     'client': [clientX, clientY],
        //     'offset': [offsetX, offsetY]
        // })

        startX = clientX
        startY = clientY
        relativeStartX = offsetX
        relativeStartY = offsetY

        startSelection = true

    },
    mousemove(){
        endX = event.clientX
        endY = event.clientY

        if(startSelection) {
            selection.style.display = 'initial';
            selection.style.top = startY + 'px';
            selection.style.left = startX + 'px';

            selection.style.width = (endX - startX) + 'px';
            selection.style.height = (endY - startY) + 'px';
        }

    },
    mouseup(){
        startSelection = false;

        relativeEndX = event.layerX;
        relativeEndY = event.layerY;

        // mostrar o botão de corte
        cropButton.style.display = 'initial'
    }
}


Object.keys(events)
.forEach(eventName =>{
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

    const [ widthFactor, heightFactor ] = [ 
        +(imgW / previewW), 
        +(imgH / previewH)
    ]

    const [ selectionWidth, selectionHeight ] = [
        +selection.style.width.replace('px', ''),
        +selection.style.height.replace('px', '')
    ]

    const [ croppedWidth, croppedHeight ] = [
        +(selectionWidth * widthFactor),
        +(selectionHeight * heightFactor)
    ]

    const [actualX, actualY] = [
        +( relativeStartX * widthFactor ),
        +( relativeStartY * heightFactor )
    ]

    // pegar do ctx a imagem cortada
    const croppedImage = ctx.getImageData(actualX, actualY, croppedWidth, croppedHeight)

    // limpar o ctx
    ctx.clearRect(0,0,ctx.width,ctx.height)

    // ajuste de proporções
    image.width = canvas.width = croppedWidth;
    image.height = canvas.height = croppedHeight;

    // adicionar a imagem cortada ao ctx
    ctx.putImageData(croppedImage, 0, 0)

    // esconder a ferramenta de seleção
    selection.style.display = 'none'

    // atualizar o preview da imagem
    photoPreview.src = canvas.toDataURL()

    // mostrar o botão de download
    downloadButton.style.display = 'initial'
}

// Download
const downloadButton = document.getElementById('download')
downloadButton.onclick = function() {
    const a = document.createElement('a')
    a.download = photoName + '-cropped.png';
    a.href = canvas.toDataURL();
    a.click()
}
