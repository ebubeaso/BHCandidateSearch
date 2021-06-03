import {Home, Login, SearchPage, SingleDateSearch, BetweenDateSearch, } from "../src/App";
import React from 'react';
import ReactDOM from 'react-dom';
import {getByLabelText, getByDisplayValue, fireEvent, render, cleanup} from '@testing-library/react';
import userEvent from '@testing-library/user-event';

it("Renders Home component without crashing", () => {
    // testing my React Typescript components to see if they render
    let container: HTMLDivElement = document.createElement("div");
    document.body.appendChild(container);
    ReactDOM.render(<Home/>, container);
    document.body.removeChild(container);
    container.remove();
})
it("Renders SearchPage component without crashing", () => {
    // testing my React Typescript components to see if they render
    let container: HTMLDivElement = document.createElement("div");
    document.body.appendChild(container);
    ReactDOM.render(<SearchPage/>, container);
    document.body.removeChild(container);
    container.remove();
})
it("Renders Login component without crashing", () => {
    // testing my React Typescript components to see if they render
    let container: HTMLDivElement = document.createElement("div");
    document.body.appendChild(container);
    ReactDOM.render(<Login/>, container);
    document.body.removeChild(container);
    container.remove();
})
it("Renders SingleDateSearch component without crashing", () => {
    // testing my React Typescript components to see if they render
    let container: HTMLDivElement = document.createElement("div");
    document.body.appendChild(container);
    ReactDOM.render(<SingleDateSearch/>, container);
    document.body.removeChild(container);
    container.remove();
})
it("Renders BetweenDateSearch component without crashing", () => {
    // testing my React Typescript components to see if they render
    let container: HTMLDivElement = document.createElement("div");
    document.body.appendChild(container);
    ReactDOM.render(<BetweenDateSearch/>, container);
    document.body.removeChild(container);
    container.remove();
})