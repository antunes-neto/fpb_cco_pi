import React from 'react';
import './style.css';

function RangeInput(props) {
    return (
        <div id='RangeInput'>
            <label htmlFor={props.name}>{props.titulo}</label>
            <input type='range' min={props.init} max={props.end} autoComplete='off' defaultValue={props.init} id={props.name + '-effect'} className={'effect ' + props.name + '-effect'} step={props.passo}></input>
        </div>
    )
}

export default RangeInput;