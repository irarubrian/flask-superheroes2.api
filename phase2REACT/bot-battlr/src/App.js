import React, { useState, useEffect } from "react";
import BotCollection from "./components/BotCollection";
import YourBotArmy from "./components/YourBotArmy";
import SortBar from "./components/SortBar";
import Footer from "./components/Footer"
import "./App.css";

function App() {
  const [bots, setBots] = useState([]);
  const [army, setArmy] = useState([]);
  const [error, setError] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8001/bots")
      .then((response) => response.json())
      .then((data) => {
        setBots(data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching bots:", error);
        setError(error.message);
        setIsLoading(false);
      });
  }, []);

  const addToArmy = (bot) => {
    if (!army.some((armyBot) => armyBot.id === bot.id)) {
      setArmy([...army, bot]);
    }
  };

  const removeFromArmy = (bot) => {
    setArmy(army.filter((armyBot) => armyBot.id !== bot.id));
  };

  const deleteBot = (bot) => {
    fetch(`http://localhost:8001/bots/${bot.id}`, {
      method: "DELETE",
    }).then(() => {
      setBots(bots.filter((b) => b.id !== bot.id));
      setArmy(army.filter((armyBot) => armyBot.id !== bot.id));
    });
  };

  if (isLoading) return <p>Loading bots...</p>;
  if (error) return <p>Error loading bots: {error}</p>;

  return (
    <div className="App">
      <h1>Bot Battlr</h1>
      <SortBar bots={bots} setBots={setBots} />
      <YourBotArmy army={army} removeFromArmy={removeFromArmy} deleteBot={deleteBot} />
      <BotCollection bots={bots} addToArmy={addToArmy} deleteBot={deleteBot} />
      <Footer />
    </div>
  );
}

export default App;
