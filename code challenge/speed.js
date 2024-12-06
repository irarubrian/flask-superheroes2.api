// Call prompt-sync in order to get the actual prompting function.
const prompt = require("prompt-sync")();
// Define the variable speed.
// Take the speed of a car as input.
const speed = prompt("Input speed of your car: ");
// Give the driver one demerit point for every 5 km/s above the speed limit (70).
// Print the total number of demerit points.
let points = (speed-70) /5;
// Define the function speedDetector.
// If car speed is less than 70, print out 'Ok'.
// If car speed is above the speed limit, calculate and print out points for the user.
// If customer points exceed 12, propmt out,  'License suspended'.
function speedDetector(){
    if (speed <70){
        console.log('Ok');
    } else if(points >12){
        console.log('License suspended');
    }else{
    console.log(`points: ${points}`);
}
}
// Call the function speedDetector. 
speedDetector();