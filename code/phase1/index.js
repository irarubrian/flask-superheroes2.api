// code your solution here
// Function saturdayFun
function saturdayFun(activity = "roller-skate") {
    return `This Saturday, I want to ${activity}!`;
}

// Function mondayWork
function mondayWork(task = "go to the office") {
    return `This Monday, I will ${task}.`;
}

// Function wrapAdjective
// Function saturdayFun
function saturdayFun(activity = "roller-skate") {
    return `This Saturday, I want to ${activity}!`;
}

// Function mondayWork
function mondayWork(task = "go to the office") {
    return `This Monday, I will ${task}.`;
}

// Function wrapAdjective
function wrapAdjective(wrapper = "*") {
    return function(adjective = "special") {
        return `You are ${wrapper}${adjective}${wrapper}!`;
    };
}
