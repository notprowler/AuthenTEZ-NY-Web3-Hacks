import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import { TezosToolkit } from "@taquito/taquito";

function App() {
  const [inputText, setInputText] = useState("");

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const handleButtonClick = () => {
    // Do something with the inputText
    console.log(inputText);
  };

  return (
    <>
      <input type="text" value={inputText} onChange={handleInputChange} />
      <button onClick={handleButtonClick}>Submit</button>
    </>
  );
}

export default App;
