var blur = document.getElementById('blur'),
  brightness = document.getElementById('brightness'),
  contrast = document.getElementById('contrast'),
  grayscale = document.getElementById('grayscale'),
  hueRotate = document.getElementById('hueRotate'),
  invert = document.getElementById('invert'),
  opacity = document.getElementById('opacity'),
  saturate = document.getElementById('saturate'),
  sepia = document.getElementById('sepia'),
  photoPreview1 = document.getElementById('photo-preview')

function getValues() {
  var filterStyle = "filter: ",
    blurValue = blur.value,
    brightnessValue = brightness.value,
    contrastValue = contrast.value,
    grayscaleValue = grayscale.value,
    hueRotateValue = hueRotate.value,
    invertValue = invert.value,
    opacityValue = opacity.value,
    saturateValue = saturate.value,
    sepiaValue = sepia.value;

  filterStyle += `
  	blur(${blurValue}px) 
    brightness(${brightnessValue}%)
    contrast(${contrastValue}%) 
    grayscale(${grayscaleValue}%) 
    hue-rotate(${hueRotateValue}deg) 
    invert(${invertValue}%) 
    opacity(${opacityValue}%) 
    saturate(${saturateValue}%) 
    sepia(${sepiaValue}%)
  `;

  return filterStyle;
}

function onChangeValue() {
  var filterValue = getValues();
  photoPreview1.setAttribute('style', filterValue);
}

function reset() {
  blur.value = 0;
  brightness.value = 100;
  contrast.value = 100;
  grayscale.value = 0;
  hueRotate.value = 0;
  invert.value = 0;
  opacity.value = 100;
  saturate.value = 100;
  sepia.value = 0;
  onChangeValue();
}

var elements = document.getElementsByTagName('input');
for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener("input", onChangeValue)
}

document.getElementById('resetButton').addEventListener('click', reset);

reset();