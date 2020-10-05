let num = 9;
num = 0;

console.log(num);

const dontReassignMe = "Shawerma";
// dontReassignMe = "Falafel";

const constArray = [];
constArray.push("bananan");
// constArray ={};

const constObject = {name: "Ali"};
constObject.name = "Samer";
// constObject = {name: "Samer"};


// Scope
// let innerVar;
for (let i=0; i<5; i++){
    let innerVar = "Apples";
    console.log(innerVar);
}

// console.log(innerVar);

// Arrow functions

function oldSchool(a, b){
    console.log(this);
}

// oldSchool();

const newSchool = (a, b) => console.log(this);
newSchool();
