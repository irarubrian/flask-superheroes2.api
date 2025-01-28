            ** BOT BATTLR

Welcome to Bot Battlr, the one-stop galactic app for building your custom bot army! This project is built using React and allows users to browse a list of bots, view their details, and enlist them into their personal army.


            **PROJECT DISCRIPTION
Bot Battlr is an interactive application that displays a collection of bots fetched from a local server. Users can:

>>Enlist bots into their personal army.

>>Release bots from their army.

>>Permanently delete bots from the collection.

This project demonstrates the use of React state management, component composition, and API interaction with JSON Server.

                **FEATURES
>>Display a list of available bots.

>>Enlist bots into your army (a bot can only be enlisted once).

>>Release bots from your army.

>>Permanently delete bots from the collection and server.

>>Sort bots by health, damage, or armor.

>>Filter bots by their class.

                **SETUP INSTRUCTION

Follow these steps to run the project locally:

 **PREREQUISITES       

.Node.js installed on your machine.

.npm (comes with Node.js).

        **INSTALLATION

(1) Clone the repository:

git clone git clone https://github.com/irarubrian/CODE-CHALLENGE-WEEK2-BOT-BATTLR.git


(2) Navigate to the project directory:

cd bot-battlr

(3) Install dependencies:

npm install

(4) Set up the JSON Server:

.Create a db.json file in the project root with the provided data.

.Start the server:

npx json-server --watch db.json --port 8001

(5) Start the React application:

npm start

(6) Open the app in your browser:


            **USAGE

(1) Browse the list of bots displayed in the BotCollection.

(2) Click a bot to enlist it in your army (YourBotArmy).

(3) Remove a bot from your army by clicking on it.

(4) Permanently delete a bot using the red "x" button.

            **ADVANCED FEATURES

(1) Bot Details View: Display detailed information about a bot when clicked.

(2) Sorting: Sort bots by health, damage, or armor.

(3) Filtering: Filter bots by class 

(4) Single Class Enlistment: Restrict enlistment to one bot per class.
