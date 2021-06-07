import {Home, Login, SearchPage, SingleDateSearch, BetweenDateSearch, } from "../src/App";
import {AccessCode, RestToken} from "../src/LoginPages";
import React from 'react';
import ReactDOM from 'react-dom';
import {getByLabelText, getByDisplayValue, getByText, findByText} from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import 'regenerator-runtime/runtime';

describe("This is testing out if the components render", () => {
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
    it("Renders AccessCode component without crashing", () => {
        // testing my React Typescript components to see if they render
        let container: HTMLDivElement = document.createElement("div");
        document.body.appendChild(container);
        ReactDOM.render(<AccessCode/>, container);
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
});

describe("making the mock fetch request", () => {
    // set up a mock fetch
    global.fetch = jest.fn<any, []>(() => {
        Promise.resolve({
            json: () => Promise.resolve({BhRestToken: "Pierre2020!", restUrl: "http://aso.net"})
        })
    })
    it("Run the mock fetch test", async () => {
        let container: HTMLDivElement = document.createElement("div");
        document.body.appendChild(container);
        ReactDOM.render(<AccessCode/>, container);
        let clientId = getByLabelText(container, "Client ID");
        let clientSecret = getByLabelText(container, "Client Secret");
        let username = getByLabelText(container, "Username");
        let password = getByLabelText(container, "Password");
        clientId.textContent = "Apples";
        clientSecret.textContent = "Pears";
        username.textContent = "Oranges";
        password.textContent = "Berries";
        let submit = getByText(container, "Login");
        userEvent.click(submit);
        expect(findByText(container, "Authentication")).toBeInTheDocument;
        
        document.body.removeChild(container);
        container.remove();
    })
})