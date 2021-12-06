import './App.css';
import './functions/script';
import RangeInput from './functions/components/RangeInput/index';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <h1 id='title'>~ NotIsBeatiful ~</h1>
      <input type="file" id="preInput"></input>
      <div className='editor-zone'>
        <div className='efeitos hidden'>
          <ul id='menu-effects'>
            <h2>~ Efeitos ~</h2>
            <li><RangeInput titulo='Saturação' name='saturacao' init='1' end='3' passo='0.01'></RangeInput></li>
            <li><RangeInput titulo='Hue' name='hue' init='0' end='340' passo='1'></RangeInput></li>
            <li><RangeInput titulo='Brilho' name='brilho' init='100' end='200' passo='1'></RangeInput></li>
            <li><RangeInput titulo='Sepia' name='sepia' init='0' end='100' passo='1'></RangeInput></li>
            <li><RangeInput titulo='Escala de Cinza' name='grayscale' init='0' end='100' passo='1'></RangeInput></li>
            <li><RangeInput titulo='Inverter as cores' name='invert' init='0' end='100' passo='1'></RangeInput></li>
          </ul>
        </div>
        <div className='container'>
          <button id='select'>Selecionar uma imagem</button>
          <img alt='imagem-inicial' id='imageView' className='hidden' draggable="false"></img>
          <button id='download' className='hidden'>Baixar imagem</button>
        </div>
        <div className='funcs hidden'>
          <h4>Cores</h4>
          <div className='colors'>
            <div className='cor'></div>
            <div className='cor'></div>
            <div className='cor'></div>
            <div className='cor'></div>
            <div className='cor'></div>
            <div className='cor'></div>
            <div className='cor'></div>
            <div className='cor'></div>
          </div>
          <div className='size'>
            <h3>Selecione o tamanho da imagem</h3>
            <select className='select-size hidden'>
              <option value='normal'>Normal</option>
              <option value='small'>Pequena</option>
              <option value='media'>Média</option>
              <option value='great'>Grande</option>
            </select>
          </div>
        </div>
      </div>
      <div id='footer'>
        <h4>@NotIsBeatiful ~ by Lucas Soares</h4>
        <div>
          <div>
            <a href='https://google.com'>Termos de uso</a>
            <a href='https://google.com'>Sobre nós</a>
          </div>
          <a href='https://google.com'>Ajuda</a>
        </div>

      </div>
    </div>
  );
}

export default App;
