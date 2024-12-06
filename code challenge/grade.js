const readline = require( 'readline');

//create an interface for input and output

const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout,
});
function getGrade(marks) {
    if (marks > 79) return "A";
    else if (marks >= 60) return "B";
    else if (marks >= 50) return "C";
    else if (marks >= 40) return "D";
    else return "E";
}
 

// Function to prompt for student marks
function promptForMarks() {
    rl.question('Enter student marks (0 to 100): ', (input) => {
      const marks = parseInt(input, 10);
  
      if (isNaN(marks) || marks < 0 || marks > 100) {
        console.log('Invalid input. Please enter a number between 0 and 100.');
        promptForMarks(); // Retry for valid input
      } else {
        const grade = getGrade(marks);
        console.log(`The grade for marks ${marks} is: ${grade}`);
        rl.close();
      }
    });
  }
  
  // Start the prompt
  promptForMarks();


