import './App.css';
import Gallery from './components/Gallery';
import { useState } from 'react';

function App() {
  const [diceNumber, setDiceNumber] = useState(1);

  const rollDice = () => {
    const randomNumber = Math.floor(Math.random() * 6) + 1;
    setDiceNumber(randomNumber);
  };

  return (
    <Gallery
      images={[
        "/images/1.png",
        "/images/2.png",
        "/images/3.png",
        "/images/4.png",
        "/images/5.png",
        "/images/6.png",
      ]}
      diceNumber={diceNumber}
      onRoll={rollDice}
    />
  );
}

export default App;
