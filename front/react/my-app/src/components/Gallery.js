import "./Gallery.css";

export default function Gallery({ images, diceNumber, onRoll }) {
  const currentImage = images[diceNumber - 1];

  return (
    <div className="Gallery">
    <h1 className="Gallery__title">Roll the Dice</h1>
      <div className="Gallery__list">
        {currentImage ? (
          <img
            className="Gallery__photo"
            src={currentImage}
            alt={`Dice showing ${diceNumber}`}
          />
        ) : (
          <div className="Gallery__photo" />
        )}
      </div>

      <div className="Gallery__buttons">
        <button onClick={onRoll}>Roll Dice</button>
      </div>
    </div>
  );
}
