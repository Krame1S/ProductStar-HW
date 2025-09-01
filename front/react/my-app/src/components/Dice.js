import "./Dice.css";

export default function Dice({ images, diceNumber, onRoll }) {
  const currentImage = images[diceNumber - 1];

  return (
    <div className="Dice">
      <h1 className="Dice__title">Roll the Dice</h1>
      <div className="Dice__container">
        {currentImage ? (
          <img
            className="Dice__image"
            src={currentImage}
            alt={`Dice showing ${diceNumber}`}
          />
        ) : (
          <div className="Dice__image" />
        )}
      </div>

      <div className="Dice__button">
        <button onClick={onRoll}>Roll Dice</button>
      </div>
    </div>
  );
}
