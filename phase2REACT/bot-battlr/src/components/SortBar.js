import React from "react";

function SortBar({ bots, setBots }) {
  const sortBots = (attribute) => {
    const sortedBots = [...bots].sort((a, b) => b[attribute] - a[attribute]);
    setBots(sortedBots);
  };

  return (
    <div className="sort-bar">
      <button onClick={() => sortBots("health")}>Sort by Health</button>
      <button onClick={() => sortBots("damage")}>Sort by Damage</button>
      <button onClick={() => sortBots("armor")}>Sort by Armor</button>
    </div>
  );
}

export default SortBar;
