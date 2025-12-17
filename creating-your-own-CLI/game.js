const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let wins = 0, losses = 0, ties = 0;

function mainMenu() {
  console.log('\nROCK PAPER SCISSORS');
  console.log('1. Play');
  console.log('2. Stats');
  console.log('3. Quit');
  
  rl.question('Choose: ', (choice) => {
    if (choice === '1') play();
    else if (choice === '2') showStats();
    else if (choice === '3') {
      console.log('Goodbye!');
      rl.close();
    }
    else {
      console.log('Please choose 1, 2, or 3');
      mainMenu();
    }
  });
}

function play() {
  console.log('\n1. Rock');
  console.log('2. Paper');
  console.log('3. Scissors');
  
  rl.question('Your choice: ', (playerChoice) => {
    const choices = ['rock', 'paper', 'scissors'];
    const player = choices[playerChoice - 1];
    
    if (!player) {
      console.log('Invalid choice');
      return mainMenu();
    }
    
    const computer = choices[Math.floor(Math.random() * 3)];
    
    console.log(`\nYou: ${player}`);
    console.log(`Computer: ${computer}`);
    
    if (player === computer) {
      console.log('Tie!');
      ties++;
    } else if (
      (player === 'rock' && computer === 'scissors') ||
      (player === 'paper' && computer === 'rock') ||
      (player === 'scissors' && computer === 'paper')
    ) {
      console.log('You win!');
      wins++;
    } else {
      console.log('You lose');
      losses++;
    }
    
    mainMenu();
  });
}

function showStats() {
  console.log(`\nWins: ${wins}`);
  console.log(`Losses: ${losses}`);
  console.log(`Ties: ${ties}`);

  const total = wins + losses + ties;
  if (total > 0) {
    console.log(`Win rate: ${Math.round((wins / total) * 100)}%`);
  }
  
  mainMenu();
}

mainMenu();